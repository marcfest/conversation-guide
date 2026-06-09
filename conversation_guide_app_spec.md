# Conversation.Guide — Web App Build Spec

A build-ready specification for a prototype. Hand this to Claude Code to generate the app.

---

## 1. What this is

A mobile-first web app (a PWA — "add to home screen") that serves as a **reference card** for a four-question conversation framework. It is published at **conversation.guide**.

It is a **sibling to persuasion.guide** and should feel like part of the same family: calm, clean, professional, lots of white space, single accent color, system font, rounded cards, gentle shadows. Single scrolling page. No backend, no account, no login, no database. Any data the user enters is stored only in their own browser's `localStorage` on their own device.

> **Reference the persuasion.guide source code directly.** The existing persuasion.guide codebase lives at `../persuasion.guide`. Read it before building — not only for visual style, colors, fonts, and the family look, but also for the **viewport-stability measures** it already implements. An early version of persuasion.guide would "wiggle" (the page or elements would shift/bounce) when the user swiped sideways on elements that should be static; persuasion.guide was hardened to prevent this. Carry over those same fixes so conversation.guide sits *stably* inside the mobile viewport from the start. See §6 for specifics.

**Design role:** This is a *reference card for people who have been trained*, not a self-teaching tutorial. It assumes the user has been through a live or Zoom session on the method. It should be genuinely excellent and complete *as a reference* — not artificially thin — but it does not try to teach the method from scratch to a cold stranger. The standard it must meet: "makes complete sense to someone who sat through the training a month ago and is now staring at it before a hard conversation."

**Distinction from persuasion.guide:** persuasion.guide *builds a pitch* (linear: fill blanks, assemble a script, deliver). conversation.guide is a *reference card for a live, two-way exchange* — four questions you can prepare with, ask, and answer. It sparks a conversation; it is not the whole conversation, and it is **not** meant to be used live during a conversation.

---

## 2. The four questions (canonical — exact wording, do not alter)

1. **What do you think?**
2. **What has been your experience?**
3. **What does that mean to you?**
4. **What would help?**

These map to a hidden underlying structure (not shown to the user): Claim → Evidence → Meaning → Ask. The user-facing language is the four plain questions only. Never surface the hidden labels in the interface.

**The three modes** (the core insight — same four questions, three uses, in this temporal order):
- **Prepare** — before the conversation, answer the four yourself.
- **Listen** — in the conversation, ask the other person the four to understand them.
- **Respond** — then answer the same four yourself to make your point.

Frame these temporally so they aren't misread as three steps *of* the conversation: prepare beforehand, then listen, then respond.

---

## 3. Page structure (single scrolling page, top to bottom)

### 3.0 Launch splash (provisional)
A brief branded splash on launch that **auto-dismisses in under one second**. Just the wordmark "Conversation Guide" on the brand background. No tap required, no action. This is provisional and easy to remove — keep it as a separate, easily-disabled component.

### 3.1 The card — first screen, must fit above the fold on a phone
The sacred, spare first impression. This is the keepsake. If a user never scrolls, they still have the entire method.

- **Title:** Conversation Guide
- **One-line header (the use):** "Four questions to prepare, listen, and respond."
- **The four questions**, displayed large, generously spaced, visually the heart of the screen:
  1. What do you think?
  2. What has been your experience?
  3. What does that mean to you?
  4. What would help?

**Hidden tap-to-expand (Easter egg):** Each of the four questions is tappable and opens a **modal** with deeper guidance (content in §4). BUT there must be **no visual affordance** indicating tappability — no chevrons, no "tap for more," no icons. The card must read as a pure, clean card. The tap is a hidden bonus that trained users learn about during the session.

> **Load-bearing rule:** Because hidden interactions get forgotten, **nothing essential may live only inside the modals.** The modals are bonus depth and reinforcement. All genuinely important content (especially the evidence-specificity guidance) must *also* appear visibly in the Prepare section (§3.3), where users actively work and will reliably encounter it.

### 3.2 Short orientation (one scroll below the card)
One calm, short passage (a few sentences, NOT a section with sub-parts). Reminds the trained user of the move. Suggested copy:

> These four questions spark a conversation — they don't script the whole thing. Ask them to understand the other person. Then answer the same four to make your own point. Go in order, and don't rush: stay with each question, and ask a follow-up before moving on.

Do **not** add separate sub-sections on dwelling, acknowledging, or intertwining. That nuance is taught live, not in the app.

### 3.3 Prepare — the worksheet
Fill-in-the-blank fields for the user to prepare **their own** four answers, before a conversation. Framed as *readiness, not a script* — light preparation they'll draw on flexibly, not lines to recite.

Four text areas (auto-growing), one per question, each with a short helper line:

- **What do you think?** — *Your main point, in one clear sentence.*
- **What has been your experience?** — **(richest guidance — weight this one heaviest)** *Get concrete. Specifics let the other person "see" what you mean. Reach for: a time ("last Tuesday," not "recently"), a place ("our downtown clinic," not "our location"), a number with context ("374 families," not "hundreds"), a name, a quote, or a visual detail. Drop two or three of these concrete "nuggets" rather than telling a long story.*
- **What does that mean to you?** — *Why it matters to you — the significance behind your point.*
- **What would help?** — *What you'd suggest, or what you hope happens next. Keep it open, not a demand.*

Auto-save to `localStorage` ~1s after the user stops typing, with a quiet "Saved on this device" status that fades in. Two-tap confirm "Clear" button (turns red, says "Confirm?" before wiping), matching persuasion.guide behavior.

> **Important:** The evidence-specificity guidance above (time / place / number with context / name / quote / visual) must be **visible here**, not hidden only behind the question-tap modal — per the load-bearing rule in §3.1.

### 3.4 Your mental movie — personal storage
A single text area where the user writes down the mnemonic "mental movie" they invented (during the session) to remember the four questions, so they can revisit it.

- **Field label:** Your mental movie
- **One-line hint (required, so it makes sense out of context):** *The scene you invented to remember the four questions.*
- Auto-saves to `localStorage` like the prepare fields.

### 3.5 Copy all
A "Copy everything" button that copies a **clean, readable, formatted document** to the clipboard (button flips to "Copied!"). The output is meant to be emailed to oneself or shared, making the app self-documenting and shareable. It should include, as headed sections:

1. The four questions
2. The deeper guidance for each question (the modal content from §4) — so even a user who never discovered the tap-to-expand gets it in their copy
3. The user's own prepared answers (from §3.3)
4. The user's mental movie (from §3.4)

Format it as a readable document with section headings and line breaks — NOT a wall of concatenated text.

### 3.6 Footer
- **QR code** linking to `https://conversation.guide`. Its purpose is **person-to-person sharing in the room** (show your screen, someone else scans it). Size and place it for *showing to another person*. Make it responsive — it may hide at the smallest widths (if you're on a narrow phone, you're the holder, not the scanner), mirroring persuasion.guide.
- **"Add to Home Screen"** link → a separate instructions page (§5).
- Standard footer items: copyright, an About/Privacy link if desired.

---

## 4. Modal content (behind the hidden tap on each question)

Each modal is **one phone screen, no more**. Bonus depth — reward for the curious, reinforcement for the trained. Weight question 2 heaviest; keep the others lighter. Each modal contains: the essence of the question, a couple of alternate phrasings (to show it flexes — not a long menu), and what a strong answer sounds like.

### Modal 1 — What do you think?
- **Essence:** You're looking for the other person's main point — or clarifying your own.
- **Alternate phrasings:** "Where do you land on this?" · "How do you see it?"
- **A strong answer:** one clear point, not five hedged ones.

### Modal 2 — What has been your experience? (richest)
- **Essence:** You're after the concrete experience behind the view — what they've actually seen, lived, or been told. This is the heart of the method.
- **Alternate phrasings:** "Has there been a moment that stuck with you?" · "When did you first notice this?"
- **What a strong answer sounds like:** specifics that let you *see* it — a time ("last Tuesday," not "recently"), a place ("our downtown clinic," not "our location"), a number with context ("374 families," not "hundreds"), a name, a quote, a visual detail. Two or three concrete "nuggets" beat a long story.
- **The dwell move:** this is the question to slow down on. If the first answer is general, follow up warmly — "Tell me more about that," "What happened?" — to draw out the specific. Don't ask for "evidence" or "proof"; that sounds like a challenge. Ask out of interest.

### Modal 3 — What does that mean to you?
- **Essence:** You're listening for why it matters — the significance underneath the point.
- **Alternate phrasings:** "Why does that matter to you?" · "What's at stake for you there?"
- **A strong answer:** connects the experience to something the person cares about.

### Modal 4 — What would help?
- **Essence:** You're after the underlying need or hoped-for next step — not a demand for action. "What would help?" stays open even when people still disagree; it surfaces common ground without forcing it.
- **Alternate phrasings:** "What would make this better?" · "What are you hoping for?"
- **A strong answer:** names a need or a small next step, not an ultimatum.

---

## 5. "Add to Home Screen" instructions page

A separate, simple page reached from the footer link. Brief, illustrated instructions for installing the app to the home screen on the major platforms:

- **iOS / Safari:** tap Share → Add to Home Screen.
- **Android / Chrome:** tap the menu (⋮) → Add to Home screen / Install app.
- **Desktop (Chrome/Edge):** install icon in the address bar, or menu → Install.

Keep it short and visual.

---

## 6. Phone-first technical notes

- **Portrait, single column.** PWA manifest: `display: standalone`, `orientation: portrait-primary`. Opens chromeless from the home screen like a native app.
- **Brand:** mirror persuasion.guide's visual identity (same accent color / "family" look). [Confirm exact hex against current branding guidelines before build.]
- **Viewport stability — carry over from persuasion.guide.** Read the persuasion.guide source at `../persuasion.guide` and replicate the measures that keep the app from "wiggling." The app must sit *stably* inside the mobile viewport: swiping sideways on static elements (the card, the question rows, headings, anything not meant to be a horizontal carousel) must NOT shift, bounce, or scroll the page horizontally. An early persuasion.guide version had this wiggle bug and was hardened against it. Typical measures to replicate: lock horizontal overflow (`overflow-x: hidden` / `max-width: 100vw` / `width: 100%` discipline on containers, no element wider than the viewport), prevent horizontal overscroll/rubber-banding (`overscroll-behavior-x: none`, and `touch-action` set appropriately so static elements don't capture horizontal pan gestures), and confine any intentional swipe handling strictly to elements that are genuinely meant to swipe. Match whatever persuasion.guide does here rather than re-inventing it.
- **Text areas auto-grow** as the user types, with iOS-Safari handling so nothing hides behind a scrollbar.
- **Auto-save** ~1s after typing stops; quiet "Saved on this device" status.
- **No analytics, no cookies, no data collection.** Only storage is the user's own draft in `localStorage`. (A reassuring minimal Privacy page, like persuasion.guide.)
- **Works offline-ish and privately** — no network round-trips needed to use the tool.
- **Touch targets** ≥44px; modals are thumb-friendly with a 44px close target.
- **Print stylesheet** (optional, nice-to-have): clean letter-size handout of the card + filled answers, matching persuasion.guide.

> **NOTE — no localStorage in Claude.ai artifacts:** If this prototype is first rendered inside a Claude artifact, browser storage APIs (localStorage/sessionStorage) will NOT work there and will fail. For an artifact preview, hold state in memory (JS variables / React state) instead. The `localStorage` persistence described above is for the real deployed app at conversation.guide, not the artifact sandbox.

---

## 7. Build order suggestion

1. The card (§3.1) with the four questions and hidden tap-to-modal — get the spare first screen right first.
2. Modals (§4).
3. Orientation passage (§3.2).
4. Prepare worksheet (§3.3) with visible evidence guidance + autosave.
5. Mental movie field (§3.4).
6. Copy-all (§3.5) with clean formatted output.
7. Footer: QR + Add to Home Screen link (§3.6), instructions page (§5).
8. Splash (§3.0) last — provisional.

---

## 8. Open items to confirm before/during build

- **Exact brand hex / wordmark** — confirm against current branding guidelines (the persuasion.guide accent color and family styling).
- **Splash screen** — provisional; keep isolated so it can be pulled easily after testing.
- **Mental-movie prominence** — currently placed below Prepare; it is the most novel element (persuasion.guide has no equivalent), so revisit whether it deserves to sit higher after seeing it in context.
