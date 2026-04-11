# Error Documentation - Development Phase

This document records errors encountered during development with visual evidence.

---

## Error 1: Users App - Page Not Found (404)

**URL**: `http://localhost:8000/users/`

**Status**: 404 Not Found

**Date Identified**: April 1, 2026

**Visual Evidence**:

![Users App 404 Error](users_app_error.png)

**Brief Description**:
Accessing `/users/` returns a 404 because the users app does not define a root route.

**Fix**:
Add a root users route or redirect `/users/` to a valid page such as login, register, or dashboard.

---

## Error 2: Assessments App - Template Does Not Exist (500)

**URL**: `http://localhost:8000/assessments/`

**Status**: 500 Internal Server Error

**Date Identified**: April 1, 2026

**Visual Evidence**:

![Assessments Template Error](assessments_template_error.png)

**Brief Description**:
Accessing `/assessments/` raises `TemplateDoesNotExist` because Django cannot find `assessments/index.html`.

**Fix**:
Create `templates/assessments/index.html` and ensure the assessments index view renders that template correctly.

---

## Error 3: Journal App - Template Does Not Exist (500)

**URL**: `http://localhost:8000/journal/`

**Status**: 500 Internal Server Error

**Date Identified**: April 1, 2026

**Visual Evidence**:

![Journal Template Error](journal_template_error.png)

**Brief Description**:
Accessing `/journal/` raises `TemplateDoesNotExist` because Django cannot find `journal/index.html`.

**Fix**:
Create `templates/journal/index.html` and ensure the journal index view renders that template correctly.

---

## Error 4: Assessments App - Detailed Trace Capture (500)

**URL**: `http://localhost:8000/assessments/`

**Status**: 500 Internal Server Error

**Date Identified**: April 4, 2026

**Visual Evidence**:

![Assessments Template Error (Detailed)](assessments_template_error.png)

**Brief Description**:
Accessing `/assessments/` shows the full template-loader traceback, confirming the missing `assessments/index.html` template.

**Fix**:
Create `templates/assessments/index.html` and ensure the assessments index view points to that template.

---

## Error 5: Journal App - Detailed Trace Capture (500)

**URL**: `http://localhost:8000/journal/`

**Status**: 500 Internal Server Error

**Date Identified**: April 4, 2026

**Visual Evidence**:

![Journal Template Error (Detailed)](journal_template_error.png)

**Brief Description**:
Accessing `/journal/` shows the full template-loader traceback, confirming the missing `journal/index.html` template.

**Fix**:
Create `templates/journal/index.html` and ensure the journal index view points to that template.

---

## Error 6: Subscription Flow Reverted To Placeholder Message

**URL**: `http://127.0.0.1:8000/payments/subscribe/`

**Status**: Functional Misroute (legacy placeholder path)

**Date Identified**: April 11, 2026

**Visual Evidence**:

![Stripe Subscription Placeholder Popup](stripe_subscription_placeholder_popup_apr11_2026.png)

Image reference: user-provided screenshot from the April 11, 2026 chat session.

**Brief Description**:
Clicking subscription from the old `/payments/subscribe/` path showed the temporary popup message:
"Stripe integration pending. Would create £9.99/month subscription"
and returned users to the initial subscription page instead of Stripe Checkout.

**Fix**:
1. Updated `subscribe_view` to remove placeholder behavior.
2. Set `GET /payments/subscribe/` to redirect to `/payments/pricing/`.
3. Set `POST /payments/subscribe/` to redirect to `/payments/checkout/`.
4. Kept `checkout_view` as the only Stripe Checkout Session creator.

**Result**:
Legacy path no longer displays the temporary integration message and now forwards users into the live checkout flow.

---

## Summary

Recorded errors represent incomplete features, template gaps, and payment-flow routing issues captured during development:

1. **Users app**: URL routing incomplete
2. **Assessments app**: Template files not created (plus detailed traceback capture)
3. **Journal app**: Template files not created (plus detailed traceback capture)
4. **Payments app**: Legacy subscription endpoint displayed placeholder messaging instead of forwarding users to checkout

These errors are expected during incremental development and will be resolved as each feature is implemented.

**Status**: All errors documented and awaiting implementation of respective features.

---

*Last Updated: April 11, 2026*
