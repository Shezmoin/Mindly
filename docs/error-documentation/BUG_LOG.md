# BUG LOG

## [2026-04-14]

### 0. Resource cards had no linked detail content
- Description: The resource cards originally displayed summaries only, with no actual detail pages or guidance content behind them.
- Expected: Each resource card should lead to a professional content page with appropriate information and references.
- Status: Fixed
- Steps to Reproduce:
  1. Open the Resources page.
  2. Click a resource card.
  3. Observe that the relevant content page now opens correctly.
- Fix: Six detailed resource pages were created and linked with referenced content

### 1. Free user can create more than 5 journal entries per month
- Description: Free tier users were able to create unlimited journal entries, which was against the advertised limit of 5 entries per month.
- Expected: Free users should be limited to 5 journal entries per month. On attempting a 6th entry, they should see a message encouraging them to subscribe to Premium.
- Status: Fixed
- Steps to Reproduce:
  1. Log in as a free user.
  2. Create more than 5 journal entries in the same month.
  3. Observe that the 6th entry is now blocked.
- Fix: Monthly limit added and verified with automated tests

### 2. Free user can access premium resource content
- Description: Free tier users were able to access premium resource detail pages directly via URL, which was against the intended access control.
- Expected: Free users should be blocked from accessing premium resource detail pages and shown an upgrade invitation instead.
- Status: Fixed
- Steps to Reproduce:
  1. Log in as a free user.
  2. Visit a premium resource detail page.
  3. Observe that access is now restricted correctly.
- Fix: Premium protection added and verified with automated tests

### 3. Assessment tools are not built yet
- Description: The assessments section was present, but it only contained a placeholder page with no real tools, questions, scoring, or results.
- Expected: Users should be able to complete a working assessment, or the feature should remain hidden until it is ready.
- Status: Fixed
- Steps to Reproduce:
  1. Open the Assessments page.
  2. Observe that interactive self-check tools are now available.
  3. Submit responses and receive a supportive result.
- Fix: Assessment hub built with working Mood Self-Check, Stress Self-Check, and Sleep Habits Check

### 4. Dark mode text contrast was too low across the site
- Description: In dark mode, several pages showed very low-contrast text on cards, forms, and result panels, making content difficult to read.
- Expected: Text should remain clearly readable in both light mode and dark mode across the whole website.
- Status: Fixed
- Steps to Reproduce:
  1. Enable dark mode.
  2. Visit pages with forms, cards, or result panels.
  3. Observe that text contrast is now readable and consistent.
- Fix: Global dark mode contrast styles added for cards, forms, tables, links, and assessment panels

### 5. Footer layout felt too high on lighter-content pages
- Description: On pages such as Resources, Journal, Pricing, and Profile, the footer was sitting too high and making the page feel visually congested.
- Expected: The footer should stay pinned to the bottom of the viewport when page content is short, creating a lighter and more balanced layout.
- Status: Fixed
- Steps to Reproduce:
  1. Open a shorter content page.
  2. Scroll to the lower section of the screen.
  3. Observe that the footer now remains at the bottom of the viewport.
- Fix: A global flex layout rule was added to the shared site template styling
