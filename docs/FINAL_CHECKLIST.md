# Master Final Checklist

This is the single source of truth for end-stage actions.
All final steps, on-hold items, evidence capture tasks, and release actions live here.

## A) Active Finalization Actions
- [x] Review and clean up all documentation (`README.md`, `docs/TESTING.md`, `docs/DEPLOYMENT.md`, etc.)
- [x] Ensure all links in README and docs are valid and non-placeholder
- [x] Remove test/debug data from the database
- [x] Run full automated validation one final time (`flake8 .`, `python manage.py check`, `python manage.py test`)
- [x] Run final manual smoke pass across core user journeys
- [x] Push all final commits to remote repository
- [x] Tag final release in Git
- [x] Archive/backup repository if required

## B) On-Hold Items (to complete at the end)
- [x] Add README Stripe "Error Handling & Recovery" subsection (checkout error page, 404/500 pages, subscription recovery notes)
- [x] Replace README screenshot placeholder links with real assets from `docs/screenshots/`
- [x] Capture and store required UI screenshots in `docs/screenshots/` (home, dashboard, journal, mood form, pricing)
- [x] Embed captured screenshots in README sections and verify links render correctly
- [x] Manual check: custom `404.html` rendering with `DEBUG=False` and valid `ALLOWED_HOSTS`
- [x] Manual check: custom `500.html` rendering with `DEBUG=False`
- [x] Manual check: Stripe checkout failure UX shows `templates/payments/checkout_error.html`
- [x] Manual check: subscription recovery path for user without email
- [x] Manual check: premium cancellation flow end-to-end
- [x] Final-stage verification: Heroku deployment checks
- [x] Final-stage verification: Stripe production-mode checks
- [x] Final-stage verification: PostgreSQL checks
- [x] Final visual consistency sweep (subtitle area) across support/resources/assessments/pricing/profile/journal in light and dark mode
- [x] Final visual robustness sweep at 320/375 widths and high zoom (including 200%) for subtitle wrapping/cropping and contrast

## C) Evidence, Snipping Tool, and AI Trace/Chat Records
- [x] Confirm which screenshots are required for final submission
- [x] Initialize screenshot folder structure (`docs/screenshots/readme`, `docs/screenshots/test`, `docs/screenshots/error`, `docs/screenshots/audit`)
- [x] Capture required screenshots using Snipping Tool (or equivalent) and store in agreed docs folder
- [x] Verify image filenames follow a consistent convention by purpose (`readme-`, `test-`, `error-`, `audit-`) and are mapped to checklist/test IDs
- [x] Confirm whether AI trace/chat records must be retained or removed before submission
- [x] If retained: move required summaries into approved documentation only
- [x] If removed: delete `docs/CHAT_HISTORY.md` and any unnecessary transcript artifacts before final commit
- [x] Final requirement: remove Project Chat History and any AI input traces before final submission
- [x] Final requirement: remove `docs/FINAL_CHECKLIST.md` itself at end of project cleanup, together with all remaining AI/chat trace artifacts

## D) Cleanup and Delivery Gate
- [x] Remove unused files/screenshots/error artifacts that are not part of final deliverables
- [x] Confirm sensitive content is not committed (keys, secrets, private traces)
- [x] Re-run final checks after cleanup changes
- [x] Final docs update: when all work is complete, update accessibility status line `Last Updated: April 1, 2026 Status: All accessibility improvements complete and tested` to the final completion date/status
- [x] Confirm working tree clean and release-ready

## E) Detailed Future Action Plan

### README / Final Screenshot Capture Order
- [x] Capture README screenshot: home page and save as `docs/screenshots/readme-02-home-page.png`
- [x] Capture README screenshot: dashboard page and save as `docs/screenshots/readme-03-dashboard-page.png`
- [x] Capture README screenshot: journal page and save as `docs/screenshots/readme-04-journal-page.png`
- [x] Capture README screenshot: mood form page and save as `docs/screenshots/readme-05-mood-form-page.png`
- [x] Capture README screenshot: pricing page and save as `docs/screenshots/readme-06-pricing-page.png`
- [x] Capture README screenshot: design overview and save as `docs/screenshots/readme-07-design-overview.png`
- [x] Capture README screenshot: colour scheme chart and save as `docs/screenshots/readme-08-colour-scheme-chart.png`
- [x] Capture README screenshot: typography examples and save as `docs/screenshots/readme-09-typography-examples.png`
- [x] Capture README screenshot: premium-only resource/content page and save as `docs/screenshots/readme-10-premium-content-page.png`
- [x] Capture README screenshot: payment success page and save as `docs/screenshots/readme-11-payment-success-page.png`
- [x] Replace each README screenshot placeholder with the correct embedded image path

### Manual User Journey Evidence
- [x] Capture test evidence: registration success screen as `docs/screenshots/test-01-register-success.png`
- [x] Capture test evidence: login success/dashboard load as `docs/screenshots/test-02-login-success.png`
- [x] Capture test evidence: mood entry creation as `docs/screenshots/test-03-mood-create.png`
- [x] Capture test evidence: journal entry creation as `docs/screenshots/test-04-journal-create.png`
- [x] Capture test evidence: pricing page before subscription as `docs/screenshots/test-05-pricing-free-user.png`
- [x] Capture test evidence: Stripe checkout page as `docs/screenshots/test-06-stripe-checkout.png`
- [x] Capture test evidence: payment success page as `docs/screenshots/test-07-payment-success.png`
- [x] Capture test evidence: premium badge/subscriber UI as `docs/screenshots/test-08-premium-upgrade.png`
- [x] Capture test evidence: premium-only page access after upgrade as `docs/screenshots/test-09-premium-resource-access.png`
- [x] Capture test evidence: cancellation flow outcome as `docs/screenshots/test-10-premium-cancellation.png`

### Django Functional Verification
- [x] Verify registration works with valid inputs
- [x] Verify login works with valid username/password
- [x] Verify invalid login shows correct error handling
- [x] Verify logout works and returns expected page/state
- [x] Verify profile page loads for authenticated user only
- [x] Verify profile edit updates persisted data correctly
- [x] Verify mood CRUD is owner-scoped and works end-to-end
- [x] Verify journal CRUD is owner-scoped and works end-to-end
- [x] Verify assessment pages load and return supportive results
- [x] Verify premium-only views deny free users and allow premium users
- [x] Verify donation flow does not incorrectly upgrade subscription tier
- [x] Verify subscription flow upgrades premium tier via webhook
- [x] Verify premium cancellation returns user to free state if expected by current app logic
- [x] Verify admin root loads for the deployed superuser
- [x] Verify any previously failing deeper admin routes behave as expected

### Django / Python Code Verification
- [x] Run `flake8 .` and record result
- [x] Run `python manage.py check` and record result
- [x] Run `python manage.py test` and record result
- [x] Verify no unresolved template warnings or missing static references remain
- [x] Verify README descriptions still match current implemented views, models, and routes

### HTML Verification
- [x] Validate key rendered HTML pages for structural issues
- [x] Check home page HTML output
- [x] Check dashboard page HTML output
- [x] Check journal page HTML output
- [x] Check mood form HTML output
- [x] Check pricing page HTML output
- [x] Note any unavoidable framework-generated warnings separately from real issues

### CSS Verification
- [x] Validate project CSS for syntax issues
- [x] Verify navbar alignment in logged-in and logged-out states
- [x] Verify dark mode styles on home, dashboard, journal, pricing, profile, and premium pages
- [x] Verify responsive layout at 320px, 375px, 768px, and desktop widths
- [x] Verify contrast and readability for buttons, badges, alerts, and premium chip styles

### JavaScript Verification
- [x] Verify dark mode toggle works and persists correctly
- [x] Verify no console errors appear during core page interactions
- [x] Verify Stripe-related client-side redirects/buttons behave correctly

### Stripe Verification
- [x] Verify Stripe test-mode checkout still works after latest code/docs changes
- [x] Verify `checkout.session.completed` webhook delivery shows `200 OK`
- [x] Verify Stripe webhook secret on Heroku matches current Stripe destination secret
- [x] Verify payment success route behavior for subscription mode
- [x] Verify payment success route behavior for one-time payment/donation mode
- [x] Verify failed checkout / cancellation UX matches documented behavior
- [x] Capture Stripe delivery evidence screenshots if required

### Heroku Verification
- [x] Verify current Heroku app loads publicly over HTTPS
- [x] Verify dyno state is up
- [x] Verify config vars remain present and correct
- [x] Verify Postgres addon is attached as `DATABASE`
- [x] Verify no duplicate add-ons or obsolete config remain
- [x] Verify latest required local commits are deployed to Heroku
- [x] Verify `python manage.py check --deploy` passes on Heroku

### Database / PostgreSQL Verification
- [x] Verify no pending migrations locally
- [x] Verify no pending migrations on Heroku
- [x] Verify production data reflects premium subscription upgrade after Stripe payment
- [x] Verify local SQLite fallback still works for local development

### Lighthouse / Performance / Accessibility Evidence
- [x] Run Lighthouse on home page (desktop)
- [x] Run Lighthouse on home page (mobile)
- [x] Run Lighthouse on dashboard page (desktop if authenticated run is available)
- [x] Capture Lighthouse screenshots/reports as evidence if required
- [x] Record performance, accessibility, best practices, and SEO scores
- [x] Note any non-critical third-party or environment-related warnings separately

### Error and Edge-Case Evidence
- [x] Capture custom 404 page as `docs/screenshots/error-01-404-page.png`
- [x] Capture custom 500 page if reproducible/safe as `docs/screenshots/error-02-500-page.png`
- [x] Capture checkout error or failure state as `docs/screenshots/error-03-checkout-error.png`
- [x] Capture unauthorized premium access behavior as `docs/screenshots/error-04-premium-access-denied.png`

### Responsive / Visual Audit Evidence
- [x] Capture mobile home page at 320px as `docs/screenshots/audit-01-home-320px.png`
- [x] Capture mobile dashboard at 375px as `docs/screenshots/audit-02-dashboard-375px.png`
- [x] Capture dark mode dashboard as `docs/screenshots/audit-03-dashboard-dark.png`
- [x] Capture pricing page at high zoom as `docs/screenshots/audit-04-pricing-200zoom.png`
- [x] Capture premium content page in dark mode as `docs/screenshots/audit-05-premium-dark.png`

---

Master checklist owner note:
- Do not maintain parallel checklists elsewhere.
- When new "last minute" actions appear, append them here only.

## F) Distinction Gap Action Plan (Assessor-Focused)

### Project Rationale and Development Plan
- [x] Add a short "Why this app solves a real-world problem" rationale section in `README.md` with target users, pain points, and measurable outcomes
- [x] Add a short "Development strategy" section in `README.md` that explains architecture choices (Django apps, Stripe, deployment) and why they were selected

### Data Modelling Depth and Domain Fitness
- [x] Add an `AssessmentResult` model (or equivalent persisted model) to store completed self-check runs per user with timestamp and score breakdown
- [x] Document model relationships in README with a simple ER-style explanation (users, profile, mood entries, journal entries, payments/subscription state, assessment results)
- [x] Confirm each persisted model has clear CRUD operations or justify read-only/reference-only entities in docs

### Full CRUD Coverage Evidence
- [x] Add a CRUD mapping table in `docs/TESTING.md` listing each model and where Create/Read/Update/Delete is implemented and tested
- [x] Add/expand automated tests for edit/delete flows where currently under-covered, especially premium/payment edge paths

### Backend-Frontend Integration Clarity
- [x] Add a concise "request-to-response" flow section in README for two journeys: journal CRUD and premium upgrade via Stripe webhook
- [x] Include one diagram or sequence description showing how forms/views/models/templates interact

### Publishable Professional Quality Checks
- [x] Run and record `python manage.py test`, `flake8 .`, and `python manage.py check --deploy` outputs in `docs/TESTING.md`
- [x] Complete final accessibility and responsive evidence capture for 320px/375px/768px and dark mode
- [x] Resolve remaining inline style hotspots by moving reusable styling into `static/css/style.css` where practical

### App Boundary and Reuse Review
- [x] Add an "App structure justification" section in README explaining why each Django app exists and what domain boundary it owns
- [x] Verify shared user subscription state remains centralized in `users.UserProfile` and is referenced, not duplicated, across apps

### Originality and Craftsmanship Evidence
- [x] Add a short originality statement in README describing unique project choices and how this differs from walkthrough/tutorial builds
- [x] Add a brief code craftsmanship note in README highlighting naming, owner-scoped queries, validation, and error handling patterns

---

## G) Pre-Submission Cleanup Gate (DO LAST — in this exact order)

These steps must be done **after all other work is complete and screenshots are embedded**. Do not do these early.

### Step 1 — Remove development/tooling files not needed in submission
- [ ] Delete `capture_errors.py` from the project root (Playwright error-capture automation script — not part of the app)
- [ ] Delete `launch_safe.bat` from the project root if it contains local dev paths or secrets
- [ ] Delete `validation_test.html` from the project root if it was created during HTML validation testing
- [ ] Delete any other one-off scripts in the root (e.g. `scan_emoji.py`, `clean_emoji.py`) if not already gone

### Step 2 — Remove AI trace and chat history artifacts
- [ ] Confirm whether `docs/CHAT_HISTORY.md` exists — if so, delete it
- [ ] Confirm whether any other AI conversation transcripts or Copilot session logs are tracked in git — delete them
- [ ] Remove all GitHub Copilot chat session artifacts from `docs/` if present

### Step 3 — Remove this checklist itself
- [ ] Delete `docs/FINAL_CHECKLIST.md` (this file) — it is a working document, not a submission deliverable

### Step 4 — Final commit after cleanup
- [ ] Run `git status` to confirm only expected deletions are staged
- [ ] Run `git add -A && git commit -m "chore: pre-submission cleanup — remove dev tools and AI trace artifacts"`
- [ ] Run `git push origin main && git push heroku main`
- [ ] Run `python manage.py test` one final time to confirm nothing was broken by file removals
- [ ] Confirm working tree is clean: `git status --short`
