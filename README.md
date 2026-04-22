# **Mindly - Mental Health and Wellbeing Platform**

### Milestone Project 4

Mindly is a full-stack web application that empowers users to track their mental wellbeing, journal their thoughts, and access premium support services. The platform combines mood tracking, journaling, and optional premium content behind a secure Stripe subscription system.

This project demonstrates professional backend development, full-stack integration, relational database design, payment processing, and industry-standard security practices using Django 4.2, Bootstrap 5, SQLite, and Stripe.

Screenshot placeholder pending upload: `docs/screenshots/readme-01-dashboard-overview.png`

---

## **Table of Contents**

<ol>
  <li><a href="#project-goals">Project Goals</a></li>
  <li><a href="#real-world-rationale">Real-World Rationale</a></li>
  <li><a href="#development-strategy">Development Strategy</a></li>
  <li><a href="#live-project">Live Project</a></li>
  <li><a href="#repository">Repository</a></li>
  <li><a href="#badges">Badges</a></li>
  <li><a href="#user-experience">User Experience</a>
    <ul style="list-style-type: disc;">
      <li><a href="#user-stories">User Stories</a></li>
      <li><a href="#first-time-users">First-time Users</a></li>
      <li><a href="#returning-premium-users">Returning Premium Users</a></li>
    </ul>
  </li>
  <li><a href="#design">Design</a>
    <ul style="list-style-type: disc;">
      <li><a href="#overview">Overview</a></li>
      <li><a href="#colour-scheme">Colour Scheme</a></li>
      <li><a href="#typography">Typography</a></li>
      <li><a href="#accessibility">Accessibility</a></li>
    </ul>
  </li>
  <li><a href="#features">Features</a>
    <ul style="list-style-type: disc;">
      <li><a href="#all-pages-features">All Pages Features</a></li>
      <li><a href="#authentication-features">Authentication Features</a></li>
      <li><a href="#mood-tracking-features">Mood Tracking Features</a></li>
      <li><a href="#journal-features">Journal Features</a></li>
      <li><a href="#premium-features">Premium Features</a></li>
      <li><a href="#payment-features">Payment Features</a></li>
    </ul>
  </li>
  <li><a href="#future-features">Future Features</a></li>
  <li><a href="#data-model--schema">Data Model / Schema</a></li>
  <li><a href="#backend-frontend-flow-examples">Backend-Frontend Flow Examples</a></li>
  <li><a href="#mindly-project-structure">Project Structure</a></li>
  <li><a href="#technologies-used">Technologies Used</a></li>
  <li><a href="#testing">Testing</a></li>
  <li><a href="#errors">Errors</a></li>
  <li><a href="#deployment">Deployment</a></li>
  <li><a href="#security">Security</a></li>
  <li><a href="#stripe-integration">Stripe Integration</a></li>
  <li><a href="#credits--acknowledgements">Credits & Acknowledgements</a></li>
  <li><a href="#known-bugs">Known Bugs</a></li>
</ol>

---

## **Project Goals**

The goal of this project was to design and build a full-stack mental health and wellbeing application that demonstrates:
- Advanced backend development with Django framework
- Secure user authentication and authorization
- Relational database design and management
- Payment processing integration with Stripe
- Responsive, accessible frontend design
- Professional security practices (environment variables, secret management, DEBUG disabled)
- Comprehensive testing and validation
- Industry-standard deployment practices

## **Real-World Rationale**

Mindly addresses a practical real-world problem: many users need a private, low-friction place to monitor mental wellbeing, reflect consistently, and access supportive resources without switching between multiple tools.

The app is designed for two clear user groups:
- **Free users** who need reliable daily support (mood tracking, journaling, and core resources)
- **Premium users** who need deeper guidance and expanded content access

This domain focus justified building secure authentication, user-owned records, and subscription-aware access controls instead of a static content site.

## **Development Strategy**

Mindly was developed using a domain-driven multi-app Django structure so each app maps to a natural product boundary:
- `users`: identity, profile, subscription state
- `journal`: mood/journal CRUD operations
- `assessments`: interactive self-check tools and persisted result records
- `payments`: Stripe checkout, webhook processing, and premium upgrade flow
- `pages`: static and premium resource views

Key architecture decisions:
- Use Django ORM for safe relational data handling and owner-scoped query patterns
- Use Stripe Checkout + webhook verification for secure payment lifecycle handling
- Use Bootstrap + custom CSS for responsive UI consistency across mobile/desktop
- Deploy on Heroku with environment-variable based secrets and production hardening

---

### **Live Project**

Mindly is deployed and accessible for public testing.

The live application is available here: [**Mindly on Heroku**](https://mindly-shez-9ca695ee4969.herokuapp.com/)

### **Screenshot Placeholders (Pending Upload)**

The following screenshots are still pending capture/upload and should be added under `docs/screenshots/`:

* Home page: `docs/screenshots/readme-02-home-page.png`
* Dashboard page: `docs/screenshots/readme-03-dashboard-page.png`
* Journal index/page: `docs/screenshots/readme-04-journal-page.png`
* Mood form page: `docs/screenshots/readme-05-mood-form-page.png`
* Pricing page: `docs/screenshots/readme-06-pricing-page.png`

---

### **Repository**

[**GitHub Repository**](https://github.com/Shezmoin/Mindly)

---

### **Badges**

* **Django 4.2:** Backend framework
* **Python 3.13:** Core language
* **Bootstrap 5:** Responsive frontend
* **Stripe:** Payment processing
* **SQLite/PostgreSQL:** Relational database
* **Git & GitHub:** Version control
* **Deployed:** Ready for production

---

## **User Experience**

### **User Stories**

#### **Free User Story: Daily Mood Tracking**
* As a free user, I want to record my daily mood score (1-10) and write a short note, so that I can track my emotional wellbeing over time.

#### **Free User Story: Journal Writing**
* As a free user, I want to create and edit private journal entries, so that I can reflect on my thoughts and experiences.

#### **Free User Story: View History**
* As a free user, I want to view my past mood entries and journal entries, so that I can observe patterns and track my progress.

#### **Premium User Story: Premium Resources**
* As a premium subscriber, I want to access exclusive premium resources, so that I can benefit from advanced wellbeing tools and content.

---

### **First-time Users**

* As a first-time user, I want to understand the purpose of Mindly immediately upon landing.
* As a first-time user, I want a clear registration process that is simple and secure.
* As a first-time user, I want to navigate the application intuitively without confusion.
* As a first-time user, I want to see the application work seamlessly on mobile, tablet, and desktop.
* As a first-time user, I want clear information about the pricing model and premium tier benefits.

---

### **Returning Premium Users**

* As a returning user, I want to log in securely and access my personal data immediately.
* As a returning user, I want to create, edit, and delete my mood entries and journal entries.
* As a returning user, I want my data to remain private and accessible only to me.
* As a premium subscriber, I want to receive immediate access to premium features upon successful payment.
* As a premium subscriber, I want to manage my subscription and see my current tier status.

---

## **Design**

### **Overview**

Mindly is designed to be calm, supportive, and user-friendly. The interface prioritises clarity, accessibility, and ease of use to encourage consistent wellbeing tracking and journaling without overwhelming the user.

Screenshot placeholder pending upload: `docs/screenshots/readme-07-design-overview.png`

---

### **Colour Scheme**

A warm, supportive colour palette is chosen to create a positive, welcoming environment that encourages mental health reflection and action.

Screenshot placeholder pending upload: `docs/screenshots/readme-08-colour-scheme-chart.png`

#### **Primary Colours:**

* Background: `#f5f3ef` (Warm Cream) - Calming page background
* Container: `#fffdf9` (Soft Ivory) - Card/content background
* Primary Action: `#6c9b7f` (Wellness Green) - Buttons, CTAs
* Secondary: `#4a5d54` (Deep Teal) - Navigation, text emphasis

#### **Accent Colours:**

* Success: `#5fa97f` (Success Green) - Positive feedback
* Warning: `#e8a538` (Warm Amber) - Alerts, warnings
* Error: `#d96a6a` (Calm Red) - Error states
* Text: `#2e2f31` (Dark Charcoal) - Main readable text
* Hover: `#e6efe9` (Light Mint) - Interactive hover states

---

### **Typography**

* **Headings:** Clear, distinct hierarchy for easy navigation and readability.
* **Body Text:** Soft, approachable sans-serif for calm reading experience.
* **Font Family:** System fonts optimized for accessibility and performance.

Screenshot placeholder pending upload: `docs/screenshots/readme-09-typography-examples.png`

---

### **Accessibility**

Mindly follows WCAG accessibility best practices:

* Semantic HTML used throughout for screen reader compatibility
* Labels associated with all form inputs for clarity
* Keyboard navigation supported for all interactive elements
* Sufficient colour contrast maintained (WCAG AA standard)
* Responsive design ensures usability on all device sizes
* Alt text provided for all non-decorative images
* Form validation provides clear error messages

---

## **Features**

### **All Pages Features**

* Responsive navigation bar with user status indicator
* Bootstrap-based responsive grid layout
* Clear visual hierarchy and consistent branding
* Mobile-optimized interface for all screen sizes
* Accessible form controls and labels
* User authentication status visible throughout
* Dark mode / Light mode toggle (persisted via localStorage)

### **Authentication Features**

* Secure user registration with username and email
* Username-based login with password verification
* Secure logout functionality
* Profile page for logged-in users with editable email and bio
* Premium users can cancel subscription from the profile page
* @login_required decorators on protected views
* CSRF protection on all forms

### **Mood Tracking Features**

* Create mood entries with score (1-10) and optional note
* View all past mood entries in reverse chronological order
* Edit mood entries to update score or note
* Delete mood entries with confirmation
* Mood entry metadata (date/time created)
* Monthly journal limit for free users is enforced and clearly communicated
* Responsive mood entry display across devices

### **Journal Features**

* Create full journal entries with title and body content
* Mark entries as private for personal use
* Edit journal entries to update content
* Delete journal entries with confirmation
* View all journal entries with summaries
* Search journal entries by title
* Timestamp tracking for entry creation/modification

### **Assessment Features**

* Dedicated assessment hub with interactive self-check tools
* Includes a Mood Self-Check, Stress Self-Check, and Sleep Habits Check
* Supportive results are displayed instantly after submission
* Assessment content is informational and not intended as a diagnosis

### **Premium Features**

### **Resource Library**

* Six professionally presented mental wellbeing resource pages are available in the platform.
* Free users can access Anxiety, Depression, and Stress guides.
* Premium users can additionally access Mindfulness, Sleep, and Self-Care guides.
* Each resource page includes structured wellbeing guidance and a reference section linking to reputable sources such as NHS, Mind, Sleep Foundation, and the Mental Health Foundation.

* Premium resources page (gated by subscription)
* Subscription tier stored securely in UserProfile
* @premium_required decorator enforces access control
* Premium users see subscription status on dashboard
* Automatic tier upgrade on successful payment

### **Payment Features**

* Stripe Checkout integration for secure payments
* Monthly recurring subscription at £9.99
* Subscription pricing page with Free/Premium comparison
* Payment success confirmation page
* Payment cancellation handling
* Webhook integration to auto-upgrade users
* Secure environment variable management for API keys

---

## **Future Features**
* Expand the resource library with clinician-reviewed articles and downloadable worksheets.
* Add searchable categories and saved favourites for premium users.
### **User Experience Improvements**

* Mood analytics with charts and trends
* Export entries as PDF or text files
* Email reminders for daily journaling
* Shareable mood statistics (with privacy controls)
* Notification system for premium content updates
* Social features (optional shared mood insights with consent)
* Profile editing (update bio and profile picture)

### **Premium Content Expansion**

* Video meditation guides
* Wellness articles and resources
* Guided reflection prompts
* Expert-authored wellbeing content
* Monthly wellness newsletter for premium users

### **Technical Enhancements**

* Advanced search and filtering
* Data backup and recovery features
* Two-factor authentication (2FA)
* API for mobile app development
* Payment method management for subscribers

---

## **Data Model / Schema**

Mindly's data model supports secure user account management, mood tracking, journaling, and subscription management.

### **CustomUser Table**

Custom user model extending Django's AbstractUser.

| Column          | Type            | Description                    |
| --------------- | --------------- | ------------------------------ |
| id              | INTEGER (PK)    | Unique user ID                 |
| username        | VARCHAR(150)    | Unique username                |
| email           | VARCHAR(254)    | User email address             |
| password        | VARCHAR(128)    | Hashed password                |
| first_name      | VARCHAR(150)    | User's first name              |
| last_name       | VARCHAR(150)    | User's last name               |
| bio             | TEXT            | Optional short bio             |
| profile_picture | IMAGE           | Optional profile picture       |
| is_active       | BOOLEAN         | Account activation status      |
| date_joined     | DATETIME        | Account creation timestamp     |

### **UserProfile Table**

Extended user profile for subscription and wellbeing tracking.

| Column           | Type            | Description                    |
| ---------------- | --------------- | ------------------------------ |
| id               | INTEGER (PK)    | Unique profile ID              |
| user_id          | INTEGER (FK)    | Link to CustomUser             |
| subscription_tier| VARCHAR(10)     | 'free' or 'premium'            |
| joined_date      | DATE            | Profile creation date          |
| reminder_time    | TIME (Optional) | Optional reminder time         |

**Subscription Tiers:**
- `free`: Free tier user (default)
- `premium`: Premium subscriber (set via Stripe webhook)

### **MoodEntry Table**

Daily mood tracking records.

| Column      | Type            | Description                    |
| ----------- | --------------- | ------------------------------ |
| id          | INTEGER (PK)    | Unique entry ID                |
| user_id     | INTEGER (FK)    | Link to CustomUser             |
| mood_score  | INTEGER         | Mood rating 1-10               |
| note        | TEXT (Optional) | Optional mood note             |
| created_at  | DATETIME        | Entry creation timestamp       |

### **JournalEntry Table**

Longer-form reflection and journaling.

| Column      | Type            | Description                    |
| ----------- | --------------- | ------------------------------ |
| id          | INTEGER (PK)    | Unique entry ID                |
| user_id     | INTEGER (FK)    | Link to CustomUser             |
| title       | VARCHAR(200)    | Entry title                    |
| content     | TEXT            | Full journal content           |
| is_private  | BOOLEAN         | Privacy flag (default: True)   |
| created_at  | DATETIME        | Entry creation timestamp       |
| updated_at  | DATETIME        | Entry modification timestamp   |

### **AssessmentResult Table**

Persisted self-check submissions for authenticated users.

| Column          | Type            | Description                                 |
| --------------- | --------------- | ------------------------------------------- |
| id              | INTEGER (PK)    | Unique result ID                            |
| user_id         | INTEGER (FK)    | Link to CustomUser                          |
| assessment_type | VARCHAR(20)     | Tool key (`mood`, `stress`, `sleep`)        |
| q1_score        | INTEGER         | Question 1 score (0-3)                      |
| q2_score        | INTEGER         | Question 2 score (0-3)                      |
| q3_score        | INTEGER         | Question 3 score (0-3)                      |
| q4_score        | INTEGER         | Question 4 score (0-3)                      |
| total_score     | INTEGER         | Sum of all question scores (0-12)           |
| level           | VARCHAR(20)     | Result level (`Low/Moderate/Higher concern`)|
| created_at      | DATETIME        | Submission timestamp                         |

**Note:** `MoodEntry` and `JournalEntry` are both defined in the `journal` app (`journal/models.py`).

### **Relationships**

- `CustomUser` → `UserProfile` (1-to-1)
- `CustomUser` → `MoodEntry` (1-to-many)
- `CustomUser` → `JournalEntry` (1-to-many)
- `CustomUser` → `AssessmentResult` (1-to-many)

### **ERD (ASCII)**

```text
┌──────────────────────┐
│      CustomUser      │
│ id (PK)              │
│ username             │
│ email                │
│ ...                  │
└─────────┬────────────┘
          │ 1
          │
          │ 1
┌─────────▼────────────┐
│      UserProfile     │
│ id (PK)              │
│ user_id (FK, unique) │
│ subscription_tier    │
│ joined_date          │
└──────────────────────┘

┌──────────────────────┐
│      CustomUser      │
└─────────┬────────────┘
          │ 1
          │
          │ N
┌─────────▼────────────┐
│       MoodEntry      │
│ id (PK)              │
│ user_id (FK)         │
│ mood_score           │
│ note                 │
└──────────────────────┘

┌──────────────────────┐
│      CustomUser      │
└─────────┬────────────┘
          │ 1
          │
          │ N
┌─────────▼────────────┐
│     JournalEntry     │
│ id (PK)              │
│ user_id (FK)         │
│ title                │
│ content              │
│ is_private           │
└──────────────────────┘

┌──────────────────────┐
│      CustomUser      │
└─────────┬────────────┘
          │ 1
          │
          │ N
┌─────────▼────────────┐
│   AssessmentResult   │
│ id (PK)              │
│ user_id (FK)         │
│ assessment_type      │
│ q1_score ... q4_score│
│ total_score          │
│ level                │
└──────────────────────┘
```

All entries are scoped to logged-in user via `request.user` for data privacy.

## **Backend-Frontend Flow Examples**

### **Flow 1: Journal CRUD (Create example)**

1. User submits the journal form in the template (`templates/journal/journal_form.html`)
2. POST request is handled by `journal_create_view` in `journal/views.py`
3. Django form validates inputs and binds the entry to `request.user`
4. ORM saves `JournalEntry` into the database
5. User is redirected to journal list with a success message
6. Template renders updated list using query results for that logged-in user only

### **Flow 2: Premium Upgrade via Stripe Webhook**

1. User starts checkout from pricing/support page
2. `payments/checkout_view` creates Stripe Checkout Session
3. Stripe sends `checkout.session.completed` event to `payments/webhook/`
4. Webhook verifies signature with `STRIPE_WEBHOOK_SECRET`
5. Matching user is identified from metadata/email
6. `UserProfile.subscription_tier` is updated to `premium`
7. Premium-protected views become accessible through the `@premium_required` gate

---

## **Mindly Project Structure**

```
mindly/
├── manage.py                           # Django management script
├── db.sqlite3                          # Development database
├── requirements.txt                    # Python dependencies
├── README.md                           # Project documentation
├── launch_safe.bat                     # Safe launch script (Windows)
├── .env                                # Environment variables (local, not committed)
├── .env.example                        # Environment variable template
├── .gitignore                          # Git ignore file
├── .git/                               # Git repository
├── mindly/                             # Project settings
│   ├── settings.py                     # Django configuration
│   ├── urls.py                         # Root URL router
│   ├── wsgi.py                         # WSGI application
│   └── asgi.py                         # ASGI application
├── users/                              # Authentication & profile app
│   ├── models.py                       # CustomUser, UserProfile models
│   ├── views.py                        # Auth views (register/login/logout), profile edit, premium cancellation
│   ├── urls.py                         # User URLs
│   ├── decorators.py                   # @premium_required decorator
│   ├── tests.py                        # User model tests
│   ├── forms.py                        # Auth forms
│   └── templates/users/                # User templates
├── journal/                            # Journal app
│   ├── models.py                       # JournalEntry and MoodEntry models
│   ├── views.py                        # Journal and mood CRUD views
│   ├── urls.py                         # Journal URLs
│   ├── tests.py                        # Journal tests
│   └── templates/journal/              # Journal templates
├── assessments/                        # Assessment self-check tools
│   ├── models.py                       # AssessmentResult model for persisted self-check submissions
│   ├── views.py                        # Mood/stress/sleep self-check logic
│   ├── urls.py                         # Assessment URLs
│   └── tests.py                        # Assessment tests
├── payments/                           # Payments & subscription
│   ├── models.py                       # Payment models (minimal)
│   ├── views.py                        # Stripe checkout, success recovery, webhook
│   ├── urls.py                         # Payment URLs
│   ├── tests.py                        # Payment tests
│   └── templates/payments/             # Pricing, checkout, success/cancel/error pages
├── pages/                              # Static pages & premium resources
│   ├── views.py                        # Home/about/dashboard, resources, premium resources
│   ├── urls.py                         # Static page URLs
│   ├── tests.py                        # Page tests
│   └── templates/pages/                # Page templates
├── templates/                          # Project-level templates
│   ├── base.html                       # Base template & navbar
│   ├── pages/                          # Home, dashboard, resources
│   ├── journal/                        # Journal & mood entry templates
│   ├── payments/                       # Pricing, checkout, success pages
│   └── users/                          # Register, login, profile templates
├── static/                             # Static files
│   └── css/
│       └── style.css                   # Custom styles
├── docs/                               # Documentation
│   ├── TESTING.md                      # Testing documentation
│   ├── DEPLOYMENT.md                   # Deployment guide
│   └── ERROR_LOG.md                    # Error log with fixes
├── errors/                             # Error capture logs and session records
│   └── README.md                       # Error notes
└── venv/                               # Python virtual environment
```

---

## **Technologies Used**

### **Languages Used**

* Python 3.13
* HTML5
* CSS3
* JavaScript

### **Frameworks, Libraries & Tools**

* **Django 4.2** - Backend web framework
* **django-crispy-forms** - Cleaner and consistent Django form rendering
* **crispy-bootstrap5** - Bootstrap 5 template pack for crispy forms
* **Bootstrap 5** - Responsive CSS framework
* **SQLite** - Development database
* **PostgreSQL (Heroku)** - Production relational database
* **dj-database-url** - Database URL parsing for environment-based config
* **psycopg2-binary** - PostgreSQL adapter used by Django on Heroku
* **Stripe** - Payment processing
* **Python Decouple** - Environment variable management
* **WhiteNoise** - Static file serving in production
* **Gunicorn** - Production WSGI HTTP server for Django
* **Pillow** - Image processing support for profile image uploads
* **Git & GitHub** - Version control
* **Windows/CMD** - Development environment
* **VS Code** - Code editor

### **Current Status Note**

Core application functionality is implemented and actively tested. Heroku deployment, PostgreSQL setup, Stripe webhook delivery, and production verification checks have been completed.

---

## **Testing**

Comprehensive testing has been carried out to ensure functionality, security, usability, and reliability across all features.

Automated Django test modules are maintained across the main apps (`users`, `journal`, `payments`, `pages`, `assessments`) and are run with `python manage.py test` as part of routine verification.

See [**TESTING.md**](./docs/TESTING.md) for full testing documentation including:

* Automated test coverage summary
* Manual test matrix (MT-01 to MT-10): [Jump to manual test table](./docs/TESTING.md#manual-test-matrix-mt-01-to-mt-10)

* Testing strategy and methodology
* User story validation
* Feature testing (CRUD, payments, authentication)
* Form validation testing
* Browser compatibility testing
* Responsiveness testing
* Accessibility testing (WCAG compliance)
* Security testing
* Lighthouse performance scores
* Code validation (PEP8, HTML, CSS, JavaScript)
* Known issues (if any)

---

## **Errors**

All errors encountered during development have been documented with investigations and solutions.

See [**ERROR_LOG.md**](./docs/ERROR_LOG.md) for complete error documentation including:

* Error description and symptoms
* Investigation methodology
* Solution applied
* Screenshots/evidence
* Current status (resolved/workaround)

---

## **Deployment**

Mindly is deployed following professional security and deployment practices.

See [**DEPLOYMENT.md**](docs/DEPLOYMENT.md) for comprehensive deployment documentation including:

* Local development setup
* Production deployment on Heroku (step-by-step)
* Environment variable configuration (Heroku config vars)
* Database setup and migrations
* Debug mode management
* Secret key management
* Stripe keys configuration
* Deployment verification steps
* Troubleshooting guide

For Heroku setup from scratch, follow the numbered production steps in [**DEPLOYMENT.md - Production Deployment (Heroku)**](./docs/DEPLOYMENT.md#production-deployment-heroku).

---

## **Security**

Security controls are implemented in both code and deployment configuration:

* **Environment variables**: Sensitive values are loaded from environment variables (`SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, Stripe keys, webhook secret)
* **Production debug policy**: `DEBUG=False` is required for production deployments
* **CSRF protection**: Django CSRF middleware is enabled and form submissions use CSRF tokens
* **Stripe webhook verification**: Webhook signatures are verified with `STRIPE_WEBHOOK_SECRET` before processing events
* **Transport/session hardening**: HTTPS redirect, secure cookies, and HSTS are enabled when `DEBUG=False`

---

## **Stripe Integration**

### **Payment Architecture**

1. **Checkout Flow:** User clicks "Subscribe Now" → Django creates Stripe Checkout Session → Stripe hosts secure payment page
2. **Payment Processing:** Stripe processes card securely
3. **Webhook Flow:** Stripe sends checkout.session.completed event → Webhook view verifies signature → User profile upgraded to premium tier
4. **Access Control:** @premium_required decorator gates premium views

### **Security Features**

* API keys stored in environment variables (never hardcoded)
* Webhook signature verification with STRIPE_WEBHOOK_SECRET
* CSRF protection on all forms
* @login_required on sensitive endpoints
* Custom @premium_required decorator for tier verification
* Debug mode disabled in production

### **Local Webhook Testing**

```bash
stripe login
stripe listen --forward-to 127.0.0.1:8000/payments/webhook/
```

See [**DEPLOYMENT.md**](./docs/DEPLOYMENT.md) for complete Stripe setup and testing instructions.

---

## **Accessibility**

Mindly adheres to WCAG 2.1 AA accessibility standards:

* **Semantic HTML** - Proper heading hierarchy, nav landmarks, section organization
* **Form Accessibility** - Labels linked to inputs, error messages clear and associated
* **Keyboard Navigation** - All interactive elements accessible via Tab/Enter/Spacebar
* **Colour Contrast** - Text meets WCAG AA minimum (4.5:1 for body text)
* **Responsive Design** - Works at all viewport sizes from 320px upward
* **Screen Reader Compatibility** - Semantic markup ensures screen reader usability
* **Focus Management** - Visible focus indicators on all interactive elements

---

## **Credits & Acknowledgements**

### **Code**

Python documentation, Django official documentation, Stripe API documentation, Bootstrap documentation, and Django best practices from community sources.

### **Media**

All images are placeholders or placeholder sources. Final images to be sourced from royalty-free repositories.

### **Acknowledgements**

Developed as a professional portfolio project demonstrating full-stack development capabilities.

---

## **Known Bugs**

No confirmed functional bugs are currently open in production-critical flows.

Current known non-functional gaps:

* README and testing/deployment screenshots are still placeholders pending capture/upload
* Final visual evidence capture (validation and Lighthouse screenshots) is still pending documentation completion

---

**Shehzad Moin, 2026**
