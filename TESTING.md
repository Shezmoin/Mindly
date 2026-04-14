## Manual Test Cases (MT-21 to MT-30)

| Test ID | Feature                        | Test Steps                                                                 | Expected Result                                      |
|---------|--------------------------------|----------------------------------------------------------------------------|------------------------------------------------------|
| MT-21   | View Pricing Page (Free User)  | Log in as free user, go to Pricing                                         | Pricing page is visible                              |
| MT-22   | Checkout Redirect (Subscribe)  | On Pricing page, click Subscribe                                           | Redirected to Stripe Checkout                        |
| MT-23   | Test Card Payment              | In Stripe, use 4242 4242 4242 4242, any date/CVC, complete payment         | Payment succeeds, redirected to success page          |
| MT-24   | Premium Badge After Payment    | After payment, go to dashboard                                             | Premium badge/status is visible                      |
| MT-25   | Premium Gating (Free User)     | As free user, try to access premium page                                   | Redirected to pricing page                           |
| MT-26   | Premium Access (Premium User)  | As premium user, access premium page                                       | Premium content is visible                           |
| MT-27   | Responsive @ 375px             | Resize browser to 375px width, view main pages                             | Layout is mobile-friendly, no horizontal scroll       |
| MT-28   | Responsive @ 768px             | Resize browser to 768px width, view main pages                             | Layout adapts to tablet size, all content accessible  |
| MT-29   | Responsive @ 1280px            | Resize browser to 1280px width, view main pages                            | Layout is desktop-optimized, no layout issues         |
| MT-30   | Keyboard Navigation            | Use Tab key to navigate all interactive elements                           | All controls accessible, visible focus indicators     |

## Bug Log Template

| Bug ID | Description | Steps to Reproduce | Root Cause | Fix Applied | Status |
|--------|-------------|--------------------|------------|-------------|--------|

## Manual Test Cases (MT-21 to MT-30)

| Test ID | Feature                        | Test Steps                                                                 | Expected Result                                      | Result |
|---------|--------------------------------|----------------------------------------------------------------------------|------------------------------------------------------|--------|
| MT-21   | View Pricing Page (Free User)  | Log in as free user, go to Pricing                                         | Pricing page is visible                              | Pass   |
| MT-22   | Click Subscribe (Stripe)       | On Pricing page, click Subscribe                                           | Redirected to Stripe Checkout                        | Pass   |
| MT-23   | Complete Payment (Test Card)   | In Stripe, use 4242 4242 4242 4242, any date/CVC, complete payment         | Payment succeeds, redirected to success page          | Pass   |
| MT-24   | Premium Badge After Payment    | After payment, go to dashboard                                             | Premium badge/status is visible                      | Pass   |
| MT-25   | Access Premium (Free User)     | As free user, try to access premium page                                   | Redirected to pricing page                           | Pass   |
| MT-26   | Access Premium (Premium User)  | As premium user, access premium page                                       | Premium content is visible                           | Pass   |
| MT-27   | Responsive @ 375px             | Resize browser to 375px width, view main pages                             | Layout is mobile-friendly, no horizontal scroll       | Pass   |
| MT-28   | Responsive @ 768px             | Resize browser to 768px width, view main pages                             | Layout adapts to tablet size, all content accessible  | Pass   |
| MT-29   | Responsive @ 1280px            | Resize browser to 1280px width, view main pages                            | Layout is desktop-optimized, no layout issues         | Pass   |
| MT-30   | Keyboard Navigation            | Use Tab key to navigate all interactive elements                           | All controls accessible, visible focus indicators     | Pass   |

## Bug Log

| Bug ID | Description                                      | Steps to Reproduce                | Root Cause                                   | Fix                                              | Status |
|--------|--------------------------------------------------|-----------------------------------|-----------------------------------------------|---------------------------------------------------|--------|
| 2026-04-13-1 | Premium message after donation (premium user) | Donate as premium user, see message| Success page did not check payment type       | Pass payment type, show message only for subscription | Fixed  |
| 2026-04-13-2 | Donation grants premium (any user)            | Donate as any user, become premium | Webhook did not check session mode            | Webhook checks mode, only upgrades for subscription | Fixed  |
## Manual Test Cases (MT-11 to MT-20)

| Test ID | Feature                | Test Steps                                                                 | Expected Result                                      |
|---------|------------------------|----------------------------------------------------------------------------|------------------------------------------------------|
| MT-11   | Create Mood Entry      | Go to mood log, select score, (optionally) add note, submit                | Mood entry is saved and appears in mood list         |
| MT-12   | Mood Empty Note        | Go to mood log, select score, leave note empty, submit                     | Mood entry is saved with empty note                  |
| MT-13   | Create Journal Entry   | Go to journal, enter title and content, submit                             | Journal entry is saved and appears in journal list   |
| MT-14   | Edit Journal Entry     | Open existing journal entry, click edit, change content, save               | Changes are saved and visible in journal list        |
| MT-15   | Cancel Delete Entry    | Click delete on journal/mood entry, click Cancel on confirm dialog          | Entry is NOT deleted, remains in list                |
| MT-16   | Confirm Delete Entry   | Click delete on journal/mood entry, click Confirm on confirm dialog         | Entry is deleted and removed from list               |
| MT-17   | Search Match           | Use search on journal/mood list with matching keyword                       | Matching entries are shown in results                |
| MT-18   | Search No Match        | Use search on journal/mood list with non-matching keyword                   | No entries found, empty state message shown          |
| MT-19   | Access Another's Entry | Manually enter URL for another user's journal/mood entry                    | 404 Not Found error page is displayed                |
| MT-20   | Empty Form Submission  | Submit journal form with empty title/content or mood form with no score     | Validation error shown, entry is NOT saved           |
## 4. Manual Test Matrix (MT-11 to MT-20)

| Test ID | Description                                                                 | Result | Notes |
|---------|-----------------------------------------------------------------------------|--------|-------|
| MT-11   | Create mood entry and verify it appears in mood list                        | Pass   |       |
| MT-12   | Submit mood form with empty note (should still save mood record)            | Pass   |       |
| MT-13   | Create journal entry and verify it appears in journal list                  | Pass   |       |
| MT-14   | Edit journal entry and save changes                                         | Pass   |       |
| MT-15   | Delete journal or mood entry — click Cancel (entry stays)                   | Pass   |       |
| MT-16   | Delete journal or mood entry — click Confirm (entry gone)                   | Pass   |       |
| MT-17   | Search journal or mood entries — matching result appears                    | Pass   |       |
| MT-18   | Search journal or mood entries — no match (shows empty state)               | Pass   |       |
| MT-19   | Try to access another user's journal or mood entry URL — expect 404         | Pass   |       |
| MT-20   | Submit journal or mood form with empty title/score — expect validation error| Pass   | Journal: title & content required. Mood: score required, note optional. |

# TESTING.md

## Manual and Automated Test Log

This file documents all manual and automated tests for Mindly, including payment, subscription, and CRUD features.

---

## 1. Premium Subscription (Stripe)

- [ ] User can subscribe to premium via Stripe Checkout
- [ ] Stripe session is created and user is redirected
- [ ] Success and cancel URLs work as expected
- [ ] Webhook updates user profile on payment success
- [ ] Error handling for failed/abandoned payments
- [ ] UI feedback for subscription status

## 2. Journal & Mood Entry Deletion

- [ ] User can delete journal entry (confirmation required)
- [ ] User can delete mood entry (confirmation required)
- [ ] Entry is removed from list after deletion
- [ ] Success message is shown
- [ ] Permission checks (user can only delete their own entries)

## 3. Donation (Stripe One-Time)

- [ ] User can select preset or custom donation amount
- [ ] Stripe Checkout session is created for donation
- [ ] User is redirected to Stripe payment page
- [ ] Success and cancel URLs work as expected
- [ ] Webhook records donation on payment success
- [ ] Error handling for invalid/failed payments
- [ ] UI feedback for donation status

---

Add test results and notes below each section as features are tested.
