# Master Final Checklist

This is the single source of truth for end-stage actions.
All final steps, on-hold items, evidence capture tasks, and release actions live here.

## A) Active Finalization Actions
- [ ] Review and clean up all documentation (`README.md`, `docs/TESTING.md`, `docs/DEPLOYMENT.md`, etc.)
- [ ] Ensure all links in README and docs are valid and non-placeholder
- [ ] Remove test/debug data from the database
- [ ] Run full automated validation one final time (`flake8 .`, `python manage.py check`, `python manage.py test`)
- [ ] Run final manual smoke pass across core user journeys
- [ ] Push all final commits to remote repository
- [ ] Tag final release in Git
- [ ] Archive/backup repository if required

## B) On-Hold Items (to complete at the end)
- [ ] Add README Stripe "Error Handling & Recovery" subsection (checkout error page, 404/500 pages, subscription recovery notes)
- [ ] Replace README screenshot placeholder links with real assets from `docs/screenshots/`
- [ ] Capture and store required UI screenshots in `docs/screenshots/` (home, dashboard, journal, mood form, pricing)
- [ ] Embed captured screenshots in README sections and verify links render correctly
- [ ] Manual check: custom `404.html` rendering with `DEBUG=False` and valid `ALLOWED_HOSTS`
- [ ] Manual check: custom `500.html` rendering with `DEBUG=False`
- [ ] Manual check: Stripe checkout failure UX shows `templates/payments/checkout_error.html`
- [ ] Manual check: subscription recovery path for user without email
- [ ] Manual check: premium cancellation flow end-to-end
- [ ] Final-stage verification: Heroku deployment checks
- [ ] Final-stage verification: Stripe production-mode checks
- [ ] Final-stage verification: PostgreSQL checks
- [ ] Final visual consistency sweep (subtitle area) across support/resources/assessments/pricing/profile/journal in light and dark mode
- [ ] Final visual robustness sweep at 320/375 widths and high zoom (including 200%) for subtitle wrapping/cropping and contrast

## C) Evidence, Snipping Tool, and AI Trace/Chat Records
- [ ] Confirm which screenshots are required for final submission
- [ ] Capture required screenshots using Snipping Tool (or equivalent) and store in agreed docs folder
- [ ] Verify image filenames follow a consistent convention by purpose (`readme-`, `test-`, `error-`, `audit-`) and are mapped to checklist/test IDs
- [ ] Confirm whether AI trace/chat records must be retained or removed before submission
- [ ] If retained: move required summaries into approved documentation only
- [ ] If removed: delete `docs/CHAT_HISTORY.md` and any unnecessary transcript artifacts before final commit

## D) Cleanup and Delivery Gate
- [ ] Remove unused files/screenshots/error artifacts that are not part of final deliverables
- [ ] Confirm sensitive content is not committed (keys, secrets, private traces)
- [ ] Re-run final checks after cleanup changes
- [ ] Confirm working tree clean and release-ready

## E) Detailed Future Action Plan

### README / Final Screenshot Capture Order
- [ ] Capture README screenshot: home page and save as `docs/screenshots/readme-02-home-page.png`
- [ ] Capture README screenshot: dashboard page and save as `docs/screenshots/readme-03-dashboard-page.png`
- [ ] Capture README screenshot: journal page and save as `docs/screenshots/readme-04-journal-page.png`
- [ ] Capture README screenshot: mood form page and save as `docs/screenshots/readme-05-mood-form-page.png`
- [ ] Capture README screenshot: pricing page and save as `docs/screenshots/readme-06-pricing-page.png`
- [ ] Capture README screenshot: design overview and save as `docs/screenshots/readme-07-design-overview.png`
- [ ] Capture README screenshot: colour scheme chart and save as `docs/screenshots/readme-08-colour-scheme-chart.png`
- [ ] Capture README screenshot: typography examples and save as `docs/screenshots/readme-09-typography-examples.png`
- [ ] Capture README screenshot: premium-only resource/content page and save as `docs/screenshots/readme-10-premium-content-page.png`
- [ ] Capture README screenshot: payment success page and save as `docs/screenshots/readme-11-payment-success-page.png`
- [ ] Replace each README screenshot placeholder with the correct embedded image path

### Manual User Journey Evidence
- [ ] Capture test evidence: registration success screen as `docs/screenshots/test-01-register-success.png`
- [ ] Capture test evidence: login success/dashboard load as `docs/screenshots/test-02-login-success.png`
- [ ] Capture test evidence: mood entry creation as `docs/screenshots/test-03-mood-create.png`
- [ ] Capture test evidence: journal entry creation as `docs/screenshots/test-04-journal-create.png`
- [ ] Capture test evidence: pricing page before subscription as `docs/screenshots/test-05-pricing-free-user.png`
- [ ] Capture test evidence: Stripe checkout page as `docs/screenshots/test-06-stripe-checkout.png`
- [ ] Capture test evidence: payment success page as `docs/screenshots/test-07-payment-success.png`
- [ ] Capture test evidence: premium badge/subscriber UI as `docs/screenshots/test-08-premium-upgrade.png`
- [ ] Capture test evidence: premium-only page access after upgrade as `docs/screenshots/test-09-premium-resource-access.png`
- [ ] Capture test evidence: cancellation flow outcome as `docs/screenshots/test-10-premium-cancellation.png`

### Django Functional Verification
- [ ] Verify registration works with valid inputs
- [ ] Verify login works with valid username/password
- [ ] Verify invalid login shows correct error handling
- [ ] Verify logout works and returns expected page/state
- [ ] Verify profile page loads for authenticated user only
- [ ] Verify profile edit updates persisted data correctly
- [ ] Verify mood CRUD is owner-scoped and works end-to-end
- [ ] Verify journal CRUD is owner-scoped and works end-to-end
- [ ] Verify assessment pages load and return supportive results
- [ ] Verify premium-only views deny free users and allow premium users
- [ ] Verify donation flow does not incorrectly upgrade subscription tier
- [ ] Verify subscription flow upgrades premium tier via webhook
- [ ] Verify premium cancellation returns user to free state if expected by current app logic
- [ ] Verify admin root loads for the deployed superuser
- [ ] Verify any previously failing deeper admin routes behave as expected

### Django / Python Code Verification
- [ ] Run `flake8 .` and record result
- [ ] Run `python manage.py check` and record result
- [ ] Run `python manage.py test` and record result
- [ ] Verify no unresolved template warnings or missing static references remain
- [ ] Verify README descriptions still match current implemented views, models, and routes

### HTML Verification
- [ ] Validate key rendered HTML pages for structural issues
- [ ] Check home page HTML output
- [ ] Check dashboard page HTML output
- [ ] Check journal page HTML output
- [ ] Check mood form HTML output
- [ ] Check pricing page HTML output
- [ ] Note any unavoidable framework-generated warnings separately from real issues

### CSS Verification
- [ ] Validate project CSS for syntax issues
- [ ] Verify navbar alignment in logged-in and logged-out states
- [ ] Verify dark mode styles on home, dashboard, journal, pricing, profile, and premium pages
- [ ] Verify responsive layout at 320px, 375px, 768px, and desktop widths
- [ ] Verify contrast and readability for buttons, badges, alerts, and premium chip styles

### JavaScript Verification
- [ ] Verify dark mode toggle works and persists correctly
- [ ] Verify no console errors appear during core page interactions
- [ ] Verify Stripe-related client-side redirects/buttons behave correctly

### Stripe Verification
- [ ] Verify Stripe test-mode checkout still works after latest code/docs changes
- [ ] Verify `checkout.session.completed` webhook delivery shows `200 OK`
- [ ] Verify Stripe webhook secret on Heroku matches current Stripe destination secret
- [ ] Verify payment success route behavior for subscription mode
- [ ] Verify payment success route behavior for one-time payment/donation mode
- [ ] Verify failed checkout / cancellation UX matches documented behavior
- [ ] Capture Stripe delivery evidence screenshots if required

### Heroku Verification
- [ ] Verify current Heroku app loads publicly over HTTPS
- [ ] Verify dyno state is up
- [ ] Verify config vars remain present and correct
- [ ] Verify Postgres addon is attached as `DATABASE`
- [ ] Verify no duplicate add-ons or obsolete config remain
- [ ] Verify latest required local commits are deployed to Heroku
- [ ] Verify `python manage.py check --deploy` passes on Heroku

### Database / PostgreSQL Verification
- [ ] Verify no pending migrations locally
- [ ] Verify no pending migrations on Heroku
- [ ] Verify production data reflects premium subscription upgrade after Stripe payment
- [ ] Verify local SQLite fallback still works for local development

### Lighthouse / Performance / Accessibility Evidence
- [ ] Run Lighthouse on home page (desktop)
- [ ] Run Lighthouse on home page (mobile)
- [ ] Run Lighthouse on dashboard page (desktop if authenticated run is available)
- [ ] Capture Lighthouse screenshots/reports as evidence if required
- [ ] Record performance, accessibility, best practices, and SEO scores
- [ ] Note any non-critical third-party or environment-related warnings separately

### Error and Edge-Case Evidence
- [ ] Capture custom 404 page as `docs/screenshots/error-01-404-page.png`
- [ ] Capture custom 500 page if reproducible/safe as `docs/screenshots/error-02-500-page.png`
- [ ] Capture checkout error or failure state as `docs/screenshots/error-03-checkout-error.png`
- [ ] Capture unauthorized premium access behavior as `docs/screenshots/error-04-premium-access-denied.png`

### Responsive / Visual Audit Evidence
- [ ] Capture mobile home page at 320px as `docs/screenshots/audit-01-home-320px.png`
- [ ] Capture mobile dashboard at 375px as `docs/screenshots/audit-02-dashboard-375px.png`
- [ ] Capture dark mode dashboard as `docs/screenshots/audit-03-dashboard-dark.png`
- [ ] Capture pricing page at high zoom as `docs/screenshots/audit-04-pricing-200zoom.png`
- [ ] Capture premium content page in dark mode as `docs/screenshots/audit-05-premium-dark.png`

---

Master checklist owner note:
- Do not maintain parallel checklists elsewhere.
- When new "last minute" actions appear, append them here only.