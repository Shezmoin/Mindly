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
- [ ] Verify image filenames are clear and mapped to checklist/test IDs
- [ ] Confirm whether AI trace/chat records must be retained or removed before submission
- [ ] If retained: move required summaries into approved documentation only
- [ ] If removed: delete `docs/CHAT_HISTORY.md` and any unnecessary transcript artifacts before final commit

## D) Cleanup and Delivery Gate
- [ ] Remove unused files/screenshots/error artifacts that are not part of final deliverables
- [ ] Confirm sensitive content is not committed (keys, secrets, private traces)
- [ ] Re-run final checks after cleanup changes
- [ ] Confirm working tree clean and release-ready

---

Master checklist owner note:
- Do not maintain parallel checklists elsewhere.
- When new "last minute" actions appear, append them here only.