import os
import re
from datetime import datetime, timedelta
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import sendgrid
from sendgrid.helpers.mail import Mail

load_dotenv()

app = Flask(__name__)

# Rate limit tracking (in-memory; clears on restart)
submission_log = {}

def get_visitor_hash(ip):
    """Simple hash of visitor IP for rate limiting."""
    return hash(ip) % (10 ** 8)

def get_client_ip():
    """Get client IP from request, accounting for Cloudflare proxy."""
    if 'CF-Connecting-IP' in request.headers:
        return request.headers.get('CF-Connecting-IP')
    if 'X-Forwarded-For' in request.headers:
        return request.headers.get('X-Forwarded-For').split(',')[0]
    return request.remote_addr

def is_valid_email(email):
    """Basic email validation."""
    return re.match(r'^[^\s@]+@[^\s@]+\.[^\s@]+$', email) is not None

def send_contact_email(name, email, message):
    """Send contact message to admin via SendGrid."""
    sg = sendgrid.SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))

    html_content = f"""
    <div style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
                max-width:560px;color:#1a1a1a;font-size:16px;line-height:1.5;">
      <h2 style="color:#BF6A4A;margin:0 0 0.8rem;">💬 New contact message from Conversation Guide</h2>
      <p><strong>From:</strong> {name} &lt;{email}&gt;</p>
      <hr style="border:none;border-top:1px solid #eee;margin:1rem 0;">
      <p style="margin:1rem 0;white-space:pre-wrap;word-wrap:break-word;">
        {message}
      </p>
      <hr style="border:none;border-top:1px solid #eee;margin:1rem 0;">
      <p style="margin-top:0.8rem;">
        <a href="mailto:{email}"
           style="display:inline-block;padding:8px 16px;background:#BF6A4A;color:#fff;
                  border-radius:8px;text-decoration:none;font-weight:700;">
          Reply to {name}
        </a>
      </p>
    </div>
    """

    message = Mail(
        from_email=os.environ.get('SENDGRID_FROM_EMAIL', 'noreply@conversation.guide'),
        to_emails='marc@est.io',
        subject=f'💬 Contact message from {name}',
        html_content=html_content,
    )

    sg.send(message)

@app.route('/contact/submit', methods=['POST'])
def contact_submit():
    """Handle contact form submission."""
    name = (request.form.get('name') or '').strip()
    email = (request.form.get('email') or '').strip().lower()
    message = (request.form.get('message') or '').strip()
    honeypot = request.form.get('website', '').strip()

    ip_hash = get_visitor_hash(get_client_ip())

    # Honeypot: silently succeed if the hidden field is filled
    if honeypot:
        app.logger.info('Contact: honeypot triggered ip_hash=%s', ip_hash)
        return jsonify({'success': True}), 200

    # Validate fields
    if not name or not email or not message:
        return jsonify({'success': False, 'error': 'All fields are required'}), 400

    if not is_valid_email(email):
        return jsonify({'success': False, 'error': 'Invalid email address'}), 400

    # Rate limiting: max 3 submissions per IP per hour
    now = datetime.now()
    cutoff = now - timedelta(hours=1)

    if ip_hash not in submission_log:
        submission_log[ip_hash] = []

    # Clean old entries
    submission_log[ip_hash] = [ts for ts in submission_log[ip_hash] if ts > cutoff]

    if len(submission_log[ip_hash]) >= 3:
        app.logger.info('Contact: rate-limited ip_hash=%s', ip_hash)
        return jsonify({'success': True}), 200  # Silent fail to prevent enumeration

    # Send email
    try:
        send_contact_email(name, email, message)
        submission_log[ip_hash].append(now)
        app.logger.info('Contact: message sent from %s', email)
        return jsonify({'success': True}), 200
    except Exception as e:
        app.logger.exception('Contact: unexpected error for %s from %s', email, name)
        return jsonify({'success': False, 'error': 'Failed to send message'}), 500

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint."""
    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5700, debug=False)
