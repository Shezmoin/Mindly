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
