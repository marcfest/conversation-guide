# Conversation.Guide — Web App Build Spec (Minimalist Version, Version 2)

A build-ready specification for Claude Code. This supersedes the V1 spec (the single-scrolling-page version Claude Code previously implemented). The guiding principle is **radical simplicity**: the app is a reference card, not a tutorial or a worksheet.

> **Build instruction: rebuild fresh from this spec.** Do NOT try to preserve, adapt, or surgically edit the V1 build. Version 2 removes most of V1's structure (the scrolling page, the worksheet, the mental-movie field, the orientation passage, the modals), and adapting the old code would leave dead scaffolding behind. Start clean. The only V1-era code worth reading is the persuasion.guide reference codebase for visual identity and viewport-stability measures (see that section below) — not the V1 conversation.guide build.

**What changed from V1 (read this first):**
- **No more scrolling page.** V1 was a single long scrolling page (card → orientation → Prepare worksheet → mental-movie field → copy-all → footer). Version 2 is **one self-contained card with no scroll on any surface.** Depth is reached by toggling a lens, not by scrolling down a page.
- **Modals cut entirely.** No hidden tap-to-expand, no Easter egg, no per-question modal content. The four questions are not tappable. (V1 §3.1 / §4.)
- **The Prepare worksheet is cut entirely.** No input fields, no text areas, no autosave, no localStorage for answers, no evidence-specificity coaching in the app. (V1 §3.3.) The tool relies on people answering the four questions honestly, in the moment.
- **The "mental movie" field is cut.** (V1 §3.4.) The mnemonic is a session artifact; users keep it however they like, not in the app.
- **The orientation passage is cut.** (V1 §3.2.) Its spirit ("go in order, don't rush, ask a follow-up") now lives in the Listen header, in one line.
- **The print stylesheet is dropped.** (V1 §6, nice-to-have.) Nothing to print once the worksheet is gone.
- **Question 2 reworded.** "What has been your experience?" → **"What has led you to think that?"** — broadened so it works when the person has no firsthand *experience* but holds a view based on evidence, reading, or reasoning.
- **The two lenses now work by shrink-plus-header.** Tapping `Listen` or `Respond` shrinks the four questions to a supporting size and raises a **dominant header** above them carrying that mode's guidance. The header becomes the hero in each lens; the questions recede to a legible supporting role. (V1 had no lens concept; it had three "modes" described in text — Prepare/Listen/Respond — but no interactive toggle.)
- **conversation.guide is no longer framed as a persuasion tool.** It is a genuine two-way conversation tool. Persuasion rigor (concrete-evidence coaching, prep worksheets, the Claim→Evidence→Meaning→Ask scaffolding as user-facing content) is left to persuasion.guide and to live training. This is a deliberate identity decision, not an omission.

> **Net effect:** Version 2 is dramatically smaller than what Claude Code built for V1. Most of V1's screen real estate (orientation, worksheet, mental movie, modals) is gone. If you are editing the existing V1 build rather than rebuilding, expect to *remove* a lot.

---

## Overview & context

**What this is.** Conversation.Guide is a phone-first web app (a PWA — "add to home screen") built around **four questions** for better conversations. It is published at **conversation.guide** and is owned by Marc Fest as part of his EST work. It is the two-way companion to **persuasion.guide**: where persuasion.guide helps a person make a one-way case, conversation.guide helps two people genuinely understand each other.

**Who it's for, and the design consequence.** This is a **reference card for people who have already been trained** (in a live or Zoom EST session) — not a self-teaching tutorial for cold strangers. That assumption is freeing: the app does not explain the method from scratch, which is what lets it stay radically simple. The standard it must meet is "makes sense to someone who was trained a month ago and is now glancing at it before a hard conversation" — not "teaches a newcomer everything."

**The commercial logic.** The app is deliberately *not* self-sufficient. The depth — the live demo, the practice, the dwelling, the "aha" — lives in the EST workshop, which is what people pay for. But the app must still be **genuinely excellent as a reference card** (like a periodic table: complete and useful for someone who knows the domain, not artificially crippled). A great artifact sells the training better than a thin teaser does.

**The core idea.** Before you make your point, help the other person make theirs.

**The crucial UX decision.** This must feel like **an app, not a long scrolling web page.** The home screen is **one self-contained card** (the four questions) with **no scrolling**. With the worksheet, mental movie, orientation, and modals all cut, there is now *no surface in the app that scrolls.* Depth is reached by toggling a lens, not by scrolling or tapping into pages. This is what creates the "sacred simplicity" feeling and makes it worth keeping on a home screen.

---

## The four questions (canonical — exact wording, do not alter)

1. **What do you think?**
2. **What has led you to think that?**
3. **What does that mean to you?**
4. **What would help?**

> **Change from V1:** Question 2 was "What has been your experience?" It is now **"What has led you to think that?"** — broadened so it works when the person has no firsthand *experience* but holds a view based on evidence, reading, or reasoning. The old phrasing presumed lived experience and stalled when there was none.

Notes on intent (for the builder's understanding — **not** surfaced as UI text):
- These map to a hidden underlying structure (never shown to the user): Claim → Evidence → Meaning → Ask.
- **They are "steps," in order.** Keep the sequence. (Do NOT call them "depths" or imply they're order-free.)
- The order is fixed, but the user should **dwell** — go in order, don't rush, stay on a step before moving on. This is taught live; the app only lightly gestures at it (via the Listen header).

---

## Screen architecture

### Launch splash (provisional)
A brief branded splash on launch that **auto-dismisses in under one second** — just the "Conversation Guide" wordmark on the brand background, no tap required. Keep it isolated/easily-removable; provisional, may be pulled after testing. (Unchanged from V1 §3.0.)

### Home screen — THE CARD (single screen, NO scrolling, ever)
The whole product at a glance. Must fit one phone screen with no scroll. Spare, generous spacing, calm. Contents:

- **Title:** Conversation Guide
- **A one-line orienting subtitle.** Something like: *"Four questions for any conversation."* (One line. Cheap insurance that keeps the minimalism legible rather than cryptic. Final copy TBD — see open items. Note: V1's subtitle "Four questions to prepare, listen, and respond" is now stale, since Prepare is gone.)
- **The four questions**, displayed large and beautifully spaced — the visual heart of the default screen:
  1. What do you think?
  2. What has led you to think that?
  3. What does that mean to you?
  4. What would help?
- **Two buttons: `Listen` and `Respond`.** These are *lenses* on the same four questions, not separate destinations.

**Default state = the bare four-question card** (neither lens active). The four questions are the hero, no header. This is the signature first impression and the app's resting state. Do NOT open in a lens by default — the bare card greets the user; lenses are reached for.

The four questions are **not tappable.** No modals, no chevrons, no affordances. The card reads as pure. (This removes V1's hidden tap-to-expand Easter egg entirely.)

---

## The two lenses (shrink-plus-header)

Tapping `Listen` or `Respond` reframes the same four questions **in place** — no navigation, no scrolling. In each lens:

1. The four questions **shrink** to a supporting size.
2. A **dominant header** appears above them, carrying that mode's guidance. The header is the largest, first-thing-your-eye-lands-on element — not a caption, not fine print.

The two lenses are **visual equals**: each is a dominant header over four shrunk questions. Neither has input fields. Both headers state a posture.

### `Listen` lens
The most important posture in the tool. Header carries the **two moves** that make the difference:
- **Reflect back** what you heard (paraphrase to confirm understanding — not parroting the exact words).
- **Ask one more** follow-up question, out of genuine curiosity (not challenge).

Draft header copy (Claude's words — Marc to review/test aloud):
> *"Listen first. Say back what you heard, then ask one more — out of real curiosity."*

The four questions shrink beneath this header to a **legible floor and no further.** If the dominant header and four legible questions cannot both fit at the smallest width, the **header wins** and the questions sit at their legible minimum. The questions must still *read as the four questions*, not as captioned fine print.

### `Respond` lens
You answer the same four questions yourself — **informed by what you just heard.** The header's whole job is to give permission to be changed by the conversation: not to reload and fire your pre-formed answer, but to let the listening genuinely inform (or revise) what you say, while still holding honest disagreement where you have it.

Draft header copy (Claude's words — Marc to review/test aloud; note the deliberate choice of "informed by" over "changed by," to protect honest conviction while killing the reload-and-fire reflex):
> *"Now answer these yourself — honestly, informed by what you just heard."*

No input fields. No worksheet. The user answers out loud, in the moment.

> **Note on conversation close ("Land"):** Marc raised wanting guidance on continuing the conversation after responding — finding common ground, acknowledging differences, agreeing a next step (meet again, find something out together). This is real and good, but it is a *third beat* ("Land"), not part of Respond, and forcing it into the Respond header would bloat it into a paragraph. **Deliberately not built in Version 2.** If, in testing, this guidance keeps wanting room, that is the signal to consider a light third treatment — *then*, not pre-emptively. Flagged as an open item, not a feature.

> **The governing rule:** Nothing in this app scrolls. Every surface is one phone screen. If something needs more room than a screen, it is too much content for this tool.

---

## Footer (kept minimal; does not break the no-scroll card)

Place so it does not force the card to scroll — a compact footer bar or small menu. Items:

- **Copy everything** — copies a clean, readable, formatted document to the clipboard (the four questions and the two lens headers), so the user can email it to themselves for reference. Format with headings and line breaks, not a wall of text. **Sharing is with yourself** (save/email for your own reference) — *not* a mechanism to hand your answers to your conversation partner. (V1's copy-all also included the user's prepared answers and mental movie; with those fields cut, this just copies the questions + guidance.)
- **QR code** linking to `https://conversation.guide` — for person-to-person sharing (show your screen, someone scans). Size for showing to others; responsive (may hide at smallest widths). Mirror persuasion.guide's behavior. (Unchanged from V1 §3.6.)
- **"Add to Home Screen"** link → a short, illustrated platform-by-platform instructions page (iOS/Safari: Share → Add to Home Screen; Android/Chrome: menu → Add to Home screen/Install; Desktop: install icon in address bar). (Unchanged from V1 §5.)

---

## What we cut (deliberately — do not re-add)

To protect the minimalism and the tool's identity as a *conversation* tool, not a persuasion tool. Each of these existed in the V1 build and should be **removed**:
- **The single scrolling page itself.** (V1 §3.) Replaced by the no-scroll card + lenses.
- **Modals / hidden tap-to-expand / alternate phrasings / "strong answer" notes in-app.** (V1 §3.1, §4.) Taught live.
- **The Prepare worksheet** — input fields, text areas, autosave, "Saved on this device," two-tap Clear. (V1 §3.3.) The tool relies on honest, in-the-moment answers, which is more present and vulnerable than arriving with pre-written ones.
- **Evidence-concreteness coaching** (time / place / numbers-with-context / name / quote / visual). (V1 §3.3, Modal 2.) That is persuasion.guide and live training.
- **The mental-movie field.** (V1 §3.4.) A session artifact; not in the app.
- **The orientation passage.** (V1 §3.2.) Its spirit lives in the Listen header now.
- **The print stylesheet.** (V1 §6.) Nothing to print once the worksheet is gone.
- **A separate "Prepare" mode.** Gone with the worksheet.
- **A "Land"/conversation-close section.** Noted as a possible future third beat; not built (see Respond lens note).

> **Discipline reminder for the builder:** every time space is freed, the pull is to fill it. The four questions, breathing, *are* the product. Headers are seasoning. Leave freed space empty.

---

## Reference the existing persuasion.guide code

The persuasion.guide codebase lives at `../persuasion.guide`. **Read it before building**, for two reasons:

1. **Visual identity / family look** — match its accent color (EST blue, `#0972bc`), system font, white space, rounded cards, gentle shadows, calm professional feel. conversation.guide should feel like a sibling.
2. **Viewport stability — replicate its anti-"wiggle" measures.** conversation.guide must sit *stably* in the mobile viewport: swiping sideways on static elements (the card, the question rows, the title, the headers) must NOT shift, bounce, or horizontally scroll the page. Replicate persuasion.guide's hardening — typically lock horizontal overflow (`overflow-x: hidden`, no element wider than the viewport, `max-width`/`width` discipline), prevent horizontal overscroll (`overscroll-behavior-x: none`), and set `touch-action` so static elements don't capture horizontal pan gestures. Match the real code rather than re-inventing it.

---

## Phone-first technical notes

- **Portrait, single column.** PWA manifest: `display: standalone`, `orientation: portrait-primary`, theme color `#0972bc`, `viewport-fit=cover`. Opens chromeless from the home screen.
- **No backend, no account, no login, no database, no input persistence.** With input fields cut, there is no user data to store. (If you keep any state at all, it is only which lens is active — and that can reset on reload; no need to persist.)
- **No analytics, no cookies, no data collection.** Minimal reassuring Privacy page, like persuasion.guide.
- **Touch targets** ≥44px (the two lens buttons; footer items).
- **No text areas** anywhere (fields are cut).
- **Shrink animation** between bare card and lens should be smooth and quick; avoid layout jank when the header appears and questions resize.

> **localStorage note:** With the worksheet and mental-movie fields cut, there is no longer any reason to use `localStorage` at all. (V1 used it heavily for the prepared answers; Version 2 does not.) If you preview inside a Claude artifact sandbox, this is now moot — there is no persisted state to substitute.

---

## Build order

1. The home **card** (title, one-line subtitle, four questions) — get the spare, no-scroll default screen right first.
2. The **`Listen` / `Respond` lens toggle** — shrink the questions, raise the dominant header, return to bare card. Get the shrink-plus-header behavior and the legible-floor rule right.
3. **Header copy** wired in (drafts above; flagged for Marc's review).
4. **Footer**: Copy everything (questions + headers), QR, Add to Home Screen + instructions page.
5. **Splash** last (provisional).

---

## Open items to confirm (Marc)

- **Subtitle copy.** *"Four questions for any conversation."* is a placeholder — confirm/replace; test aloud. (V1's "prepare, listen, and respond" is stale now that Prepare is gone.)
- **Listen header copy.** Draft above — review and test aloud. Watch that "say back what you heard" reads as *paraphrase to confirm*, not mechanical echo.
- **Respond header copy.** Draft above — review and test aloud. Confirm "informed by" (vs. "changed by") strikes the right balance between being genuinely moved and keeping honest disagreement.
- **The "Land" question.** Decide in testing whether conversation-close guidance (common ground, differences, next step) needs a home. Do not pre-build.
- **Splash:** provisional; keep isolated for easy removal.
- **Exact brand tokens:** pull from the real `../persuasion.guide` source rather than guessing.
