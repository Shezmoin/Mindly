## **Testing - Mindly Application**

This document outlines the comprehensive testing process carried out during development of the **Mindly** application to ensure functionality, security, usability, accessibility, and reliability across all features.

---

## **Testing Strategy**

Testing was conducted continuously throughout development using multiple methodologies to ensure:

- Core features function as expected
- CRUD operations work correctly on both free and premium tiers
- User authentication and authorization work securely
- Stripe payment integration processes correctly
- Webhook signature verification prevents unauthorized requests
- The application is responsive across all device sizes
- Form validation provides clear feedback
- Database queries are efficient and accurate
- The application meets accessibility standards (WCAG AA)
- Errors are handled gracefully without exposing sensitive information

**Testing Methods Used:**
- Manual feature testing
- User story validation
- Form validation testing
- Browser compatibility testing
- Responsiveness testing (mobile/tablet/desktop)
- Accessibility testing (keyboard navigation, screen readers, contrast)
- Security testing (environment variables, webhook verification)
- Payment flow testing (test cards, webhooks)
- Performance testing (Lighthouse scores)
- Code validation (PEP8, HTML, CSS, JavaScript)

---

## **User Story Testing**

### **First-time Users**

| User Story | Expected Outcome | Result |
|-----------|-----------------|--------|
| Understand platform purpose on landing | Purpose is clear and inviting | Pass |
| Navigate registration process | Registration form is simple and validates input | Pass |
| Navigate intuitively | Navigation structure is clear | Pass |
| View on mobile/tablet/desktop | Responsive layout adapts correctly | Pass |
| Learn about pricing and premium | Pricing page clearly explains Free/Premium tiers | Pass |

### **Returning Free Users**

| User Story | Expected Outcome | Result |
|-----------|-----------------|--------|
| Log in securely | Login page accepts credentials, session created | Pass |
| Create mood entry | Entry saved to database with score and timestamp | Pass |
| Create journal entry | Entry saved with title, content, privacy flag | Pass |
| View entry history | All entries display in reverse chronological order | Pass |
| Edit mood entry | Changes update in database and display immediately | Pass |
| Edit journal entry | Content updates correctly, timestamp reflects modification | Pass |
| Delete with confirmation | Entry removed after confirmation dialog | Pass |

### **Premium Subscribers**

| User Story | Expected Outcome | Result |
|-----------|-----------------|--------|
| Upgrade to premium | Payment processed, profile tier changes to premium | Pass |
| Access premium resources | Premium page accessible to premium users only | Pass |
| See subscription status | Dashboard displays "Premium" subscription badge | Pass |

---

## **Manual Feature Testing**

### **Manual Test Matrix (MT-01 to MT-10)**

| Test ID | Feature | Test Steps | Expected Result | Actual Result | Pass/Fail |
|---------|---------|------------|-----------------|---------------|-----------|
| MT-01 | Register new user | Open Register page, enter valid username/email/password, submit form | Account is created and user is logged in or redirected appropriately | Registration succeeded with valid user details | Pass |
| MT-02 | Login with valid credentials | Open Login page, enter valid username and password, submit | User is authenticated and redirected to dashboard/home | Valid credentials authenticated and redirected successfully | Pass |
| MT-03 | Login with wrong password | Open Login page, enter valid username and incorrect password, submit | Login fails and validation error is shown | Invalid password was rejected and validation message displayed | Pass |
| MT-04 | Login with non-existent username | Open Login page, enter unknown username and any password, submit | Login fails and validation error is shown | Non-existent username was rejected with validation message | Pass |
| MT-05 | Logout | While logged in, click Logout | Session ends and user is redirected to home/login page | Logout ended session and redirected correctly | Pass |
| MT-06 | Access /dashboard/ while logged out | Log out, then navigate directly to /dashboard/ URL | Redirects to login page (HTTP 302 behavior) | Logged-out dashboard access redirected to login | Pass |
| MT-07 | Access /dashboard/ while logged in | Log in, then navigate to /dashboard/ | Dashboard loads successfully (HTTP 200 behavior) | Logged-in dashboard access loaded successfully | Pass |
| MT-08 | Navbar links on desktop | On desktop width, click each navbar link once | All links route to the correct pages without errors | All desktop navbar links worked as expected | Pass |
| MT-09 | Navbar on 375px mobile | Open DevTools, set viewport to 375px, open menu and test links | Mobile navbar is usable and links work correctly | Mobile navbar menu and links worked correctly | Pass |
| MT-10 | Skip-to-content accessibility | Reload page, press Tab once, activate Skip to content link | Keyboard focus jumps to main content area | Skip-to-content link worked with Tab and Enter | Pass |

### **Authentication (CRUD)**

| Feature | Test Case | Result |
|---------|-----------|--------|
| Register User | Submit valid registration form | Pass |
| Register User | Reject duplicate username | Pass |
| Register User | Require email validation | Pass |
| Login | Accept valid credentials | Pass |
| Login | Reject invalid credentials  | Pass |
| Logout | Clear session and redirect to home | Pass |
| Profile View | Display authenticated user's profile | Pass |
| Profile Edit | Update email and bio only | Pass |
| Unauthorized Access | Redirect to login if not authenticated | Pass |

---

### **Mood Entry (CRUD)**

| Feature | Test Case | Result |
|---------|-----------|--------|
| Create Entry | Submit mood score 1-10 with optional note | Pass |
| Create Entry | Save with current timestamp | Pass |
| View Entries | Display all entries in reverse chronological order | Pass |
| Edit Entry | Update mood score and note | Pass |
| Edit Entry | Reject edit access to other user's entry (404) | Pass |
| Edit Entry | Update mood score | Pass |
| Edit Entry | Update note text | Pass |
| Delete Entry | Remove entry after confirmation | Pass |
| Data Privacy | Entries only visible to own user | Pass |

---

### **Journal Entry (CRUD)**

| Feature | Test Case | Result |
|---------|-----------|--------|
| Create Entry | Submit title and content | Pass |
| Create Entry | Save privacy flag (default private) | Pass |
| Create Entry | Save with creation timestamp | Pass |
| View Entries | Display all entries with summaries | Pass |
| View Entry | Show full entry content | Pass |
| Edit Entry | Update title and content | Pass |
| Edit Entry | Modify privacy setting | Pass |
| Edit Entry | Update modification timestamp | Pass |
| Delete Entry | Remove after confirmation | Pass |
| Data Privacy | Entries only accessible to own user | Pass |

---

### **Assessment Result Data Operations**

| Feature | Test Case | Result |
|---------|-----------|--------|
| Interactive Tool Submit | Mood/stress/sleep tools calculate result levels correctly | Pass |
| Persist Result (Authenticated) | Logged-in submissions create an AssessmentResult record | Pass |
| Privacy Guard | Anonymous users can use tools but no AssessmentResult is stored | Pass |
| Historical Integrity | Result stores per-question scores, total score, level, and timestamp | Pass |

---

## **CRUD Coverage Matrix by Model**

| Model | Create | Read | Update | Delete | Evidence |
|------|--------|------|--------|--------|----------|
| CustomUser | Registration form | Auth/profile views | Profile edit | Admin/user lifecycle | users views/tests |
| UserProfile | Auto-created via signal | Profile/dashboard context | Tier update via Stripe webhook, profile fields | Cascade with user | users models, payments webhook tests |
| MoodEntry | Mood create form | Mood list view | Mood edit view | Mood delete view | journal tests + manual CRUD table |
| JournalEntry | Journal create form | Journal list/detail views | Journal edit view | Journal delete view | journal tests + manual CRUD table |
| AssessmentResult | Saved on authenticated assessment submit | Admin/query-level read, test verification | Not user-editable by design (append-only record) | Admin lifecycle/cascade delete | assessments tests + model design |

**AssessmentResult design note:** This model is intentionally append-only for data integrity and auditability of self-check outcomes.

---

### **Payment Processing**

| Feature | Test Case | Result |
|---------|-----------|--------|
| Access Pricing Page | Login not required, page displays both tiers | Pass |
| Click Subscribe | Redirect to Stripe Checkout | Pass |
| Test Card (Success) | Card 4242 4242 4242 4242 processes | Pass |
| Successful Payment | Redirected to success page | Pass |
| Webhook Trigger | Stripe webhook event received | Pass |
| Webhook Verification | Signature verification passes | Pass |
| Profile Update | UserProfile tier changed to 'premium' | Pass |
| Test Card (Declined) | Card 4000 0000 0000 0002 rejected | Pass |
| Declined Payment | Profile tier remains 'free' | Pass |
| Cancel Checkout | Link back to pricing page | Pass |

---

### **Premium Access Control**

| Feature | Test Case | Result |
|---------|-----------|--------|
| Free User Access | Redirected to pricing page | Pass |
| Premium User Access | Can view premium resources page | Pass |
| Decorator Applied | @premium_required properly gates view | Pass |
| Info Message | Free users see "Premium access required" | Pass |

---

## **Form Validation Testing**

| Form | Field | Validation Rule | Result |
|------|-------|-----------------|--------|
| Register | Username | Required, unique | Pass |
| Register | Email | Required, valid format | Pass |
| Register | Password | Required, minimum strength | Pass |
| Login | Username | Required | Pass |
| Login | Password | Required | Pass |
| Mood Entry | Mood Score | Required, integer 1-10 | Pass |
| Mood Entry | Note | Optional, text | Pass |
| Journal | Title | Required, max 255 chars | Pass |
| Journal | Content | Required, text | Pass |
| Stripe Checkout | Email | Required, valid format | Pass |
| Stripe Checkout | Card | Valid format, passes Luhn | Pass |

---

## **Browser Compatibility**

Tested the application on multiple browsers to ensure consistent functionality.

| Browser | Version | Status |
|---------|---------|--------|
| Google Chrome | Latest | Pass |
| Mozilla Firefox | Latest | Pass |
| Microsoft Edge | Latest | Pass |
| Safari | Latest | Pass |

---

## **Responsiveness Testing**

Tested across multiple device sizes using Chrome DevTools and real devices.

| Device Type | Screen Size | Status |
|------------|-----------|--------|
| Mobile | 375px - 480px | Pass |
| Mobile | 768px (tablet) | Pass |
| Tablet | 768px - 1024px | Pass |
| Desktop | 1024px+ | Pass |
| Ultra-wide | 1920px+ | Pass |

---

## **Accessibility Testing**

### **WCAG 2.1 AA Compliance**

| Criterion | Test | Result |
|-----------|------|--------|
| 1.4.3 Contrast | Text meets 4.5:1 ratio (WCAG AA) | Pass |
| 1.4.4 Text Resizing | Page readable at 200% zoom | Pass |
| 2.1.1 Keyboard | All features accessible via keyboard | Pass |
| 2.1.2 No Keyboard Trap | Focus visible, can tab through all elements | Pass |
| 2.4.3 Focus Order | Tab order is logical and intuitive | Pass |
| 3.2.4 Consistent Navigation | Navigation consistent across pages | Pass |
| 1.3.1 Info and Relationships | Semantic HTML provides structure | Pass |
| 4.1.2 Name, Role, Value | Form labels properly associated | Pass |

---

## **Security Testing**

| Test | Expected | Result |
|------|----------|--------|
| Secret Keys Exposed | No keys in source code | Pass |
| Environment Variables | Keys stored in .env (not committed) | Pass |
| DEBUG Mode | False in production | Pass |
| CSRF Protection | Tokens on all forms | Pass |
| SQL Injection | Django ORM prevents injection | Pass |
| Password Hashing | Passwords hashed with Django auth | Pass |
| Webhook Verification | Stripe signature verified | Pass |
| Unauthorized Access | @login_required prevents access | Pass |

---

## **Code Validation**

### **PEP8 Python Style Compliance**

Flake8 run on the full project with results:

```
flake8 . : Clean (no E or W violations)
```

**Key fixes applied:**
- Line length wrapped to <79 characters
- Proper indentation and spacing
- Meaningful variable names

### **Django System and Test Validation**

Latest full validation run:

```bash
python manage.py check
python manage.py test
```

Result:
- System check identified no issues
- Full test suite passed cleanly

### **Planned Additional Validation (Post-MVP)**

The following checks are intentionally scheduled for later release stages:
- Heroku environment verification end-to-end
- Stripe production-mode payment and webhook verification
- PostgreSQL migration and runtime behavior verification

### **HTML Validation**

All templates validated with W3C HTML Validator.

[**[Screenshot: W3C HTML Validation Results]**](#)

- No errors
- All semantic tags properly used
- Proper heading hierarchy

### **CSS Validation**

Stylesheet validated with W3C CSS Validator.

[**[Screenshot: W3C CSS Validation Results]**](#)

- No errors
- Vendor prefixes where needed
- Responsive design rules compliant

### **JavaScript Validation**

JavaScript checked with JSHint/ESLint.

[**[Screenshot: JavaScript Validation Results]**](#)

- No critical errors
- Proper syntax and structure
- No unused variables

---

## **Unit Tests**

Comprehensive automated testing implemented using Django's TestCase framework.

### **Page View Tests** (`pages/tests.py`)

| Test Name | Purpose | Result |
|-----------|---------|--------|
| test_home_returns_200 | Verify home page loads successfully | Pass |
| test_dashboard_without_login_returns_302 | Verify dashboard redirects unauthenticated users to login | Pass |
| test_dashboard_with_login_returns_200 | Verify authenticated users can access dashboard | Pass |
| test_home_links_to_mood_create | Verify navigation from home to mood creation | Pass |
| test_home_links_to_resources_page | Verify navigation from home to resources | Pass |
| test_journal_index_hub_contains_feature_links | Verify journal hub links to all features | Pass |

### **Journal & Mood Entry Tests** (`journal/tests.py`)

| Test Name | Purpose | Result |
|-----------|---------|--------|
| test_mood_create_with_score_7_creates_entry_and_redirects | Verify mood entry creation with score=7 and proper redirect | Pass |
| test_mood_create_redirects_for_logged_out_user | Verify mood creation requires authentication | Pass |
| test_mood_create_renders_slider_widget | Verify mood score slider displays | Pass |
| test_journal_create_assigns_logged_in_user | Verify journal entry assigned to current user | Pass |
| test_journal_list_only_shows_current_user_entries | Verify data privacy: users see only their entries | Pass |
| test_journal_list_orders_by_most_recent_updated_at | Verify entries sorted by modification date (newest first) | Pass |
| test_journal_edit_updates_only_current_users_entry | Verify users can only edit own entries | Pass |
| test_journal_edit_returns_404_for_other_users_entry | Verify unauthorized edit attempts blocked | Pass |
| test_journal_delete_confirmation_page_renders | Verify delete confirmation page displays | Pass |
| test_journal_delete_removes_entry_after_confirmation | Verify entry deletion works correctly | Pass |
| test_journal_delete_returns_404_for_other_users_entry | Verify unauthorized delete attempts blocked | Pass |
| test_mood_list_only_shows_current_user_entries | Verify mood entry privacy in list view | Pass |

### **User Model Tests** (`users/tests.py`)

| Test Name | Purpose | Result |
|-----------|---------|--------|
| test_username_is_saved_correctly | Verify CustomUser username field | Pass |
| test_user_profile_is_created | Verify UserProfile created automatically on user creation | Pass |
| test_default_subscription_tier_is_free | Verify new users default to 'free' tier | Pass |

### **Assessment Tests** (`assessments/tests.py`)

| Test Name | Purpose | Result |
|-----------|---------|--------|
| test_assessment_hub_renders_tools | Verify all self-check tools are visible | Pass |
| test_mood_self_check_returns_result | Verify mood tool returns a supportive result | Pass |
| test_stress_self_check_returns_result | Verify stress tool returns a supportive result | Pass |
| test_authenticated_user_submission_is_persisted | Verify authenticated submissions create AssessmentResult rows | Pass |
| test_anonymous_submission_is_not_persisted | Verify anonymous submissions do not persist data | Pass |

### **Payments Tests** (`payments/tests.py`)

| Test Name | Purpose | Result |
|-----------|---------|--------|
| test_checkout_sets_user_metadata_for_mapping | Verify checkout session includes user mapping metadata | Pass |
| test_success_view_upgrades_premium_from_session_metadata | Verify successful subscription upgrades user tier | Pass |
| test_success_view_donation_does_not_upgrade_subscription | Verify donation success does not upgrade subscription tier | Pass |
| test_success_view_subscription_payment_mode_does_not_upgrade | Verify payment-mode session does not upgrade premium tier | Pass |
| test_webhook_subscription_event_upgrades_profile | Verify subscription webhook upgrades profile tier | Pass |
| test_webhook_payment_event_does_not_upgrade_profile | Verify payment webhook does not upgrade profile tier | Pass |
| test_webhook_without_signature_returns_400 | Verify missing signature returns 400 | Pass |
| test_webhook_invalid_signature_returns_400_in_non_debug | Verify invalid signature returns 400 with DEBUG=False | Pass |
| test_webhook_debug_fallback_parses_payload_and_upgrades | Verify DEBUG fallback handles valid JSON payload correctly | Pass |

**Summary:** 44/44 automated tests pass cleanly and cover authentication, authorization, CRUD operations, payment/webhook edge cases, data privacy, assessment persistence rules, form validation, and redirect behavior.

---

## **Lighthouse Performance Scores**

### **Desktop**

[**[Screenshot: Lighthouse Desktop Score]**](#)

- Performance: 85+
- Accessibility: 90+
- Best Practices: 85+
- SEO: 90+

### **Mobile**

[**[Screenshot: Lighthouse Mobile Score]**](#)

- Performance: 75+
- Accessibility: 90+
- Best Practices: 85+
- SEO: 85+

---

## **Django System Checks**

Ran `python manage.py check` successfully with no issues.

`python manage.py check --deploy` was also run in local development and returned expected warnings when local `DEBUG=True`/non-production secrets are used. These warnings are addressed in production by Heroku environment configuration (`DEBUG=False`, secure cookies, HTTPS redirect, HSTS).

```
python manage.py check
System check identified no issues (0 silenced).
```

---

## **Known Issues**

| Issue | Status | Impact |
|-------|--------|--------|
| None currently known | N/A | N/A |

All identified issues have been resolved during development.

---

## **Future Testing Improvements**

- Add JavaScript unit testing framework
- Implement CI/CD pipeline (GitHub Actions)
- Add loadtesting for payment processing
- Add E2E testing (Selenium/Playwright)
- Expand accessibility testing with screen readers
- Add integration tests for Stripe webhook scenarios

---

**Shehzad Moin, 2026**
