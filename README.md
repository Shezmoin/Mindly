# **Mindly - Mental Health and Wellbeing Platform**

### Milestone Project 4

Mindly is a full-stack web application that empowers users to track their mental wellbeing, journal their thoughts, and access premium support services. The platform combines mood tracking, journaling, and optional premium content behind a secure Stripe subscription system.

This project demonstrates professional backend development, full-stack integration, relational database design, payment processing, and industry-standard security practices using Django 4.2, Bootstrap 5, SQLite, and Stripe payment processing.

[**[Screenshot: Dashboard Overview]**](#)

---

## **Table of Contents**

<ol>
  <li><a href="#project-goals">Project Goals</a></li>
  <li><a href="#live-project">Live Project</a></li>
  <li><a href="#repository">Repository</a></li>
  <li><a href="#badges">Badges</a></li>
  <li><a href="#user-experience">User Experience</a>
    <ul style="list-style-type: disc;">
      <li><a href="#user-stories">User Stories</a></li>
      <li><a href="#first-time-users">First-time Users</a></li>
      <li><a href="#returning-premium-users">Returning & Premium Users</a></li>
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
  <li><a href="#mindly-project-structure">Project Structure</a></li>
  <li><a href="#technologies-used">Technologies Used</a></li>
  <li><a href="#testing">Testing</a></li>
  <li><a href="#errors">Errors</a></li>
  <li><a href="#deployment">Deployment</a></li>
  <li><a href="#stripe-integration">Stripe Integration</a></li>
  <li><a href="#credits">Credits</a></li>
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

---

### **Live Project**

Mindly is deployed and accessible for public testing.

The live application is available here: [**[Deployed Application Link]**](#)

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

### **Returning & Premium Users**

* As a returning user, I want to log in securely and access my personal data immediately.
* As a returning user, I want to create, edit, and delete my mood entries and journal entries.
* As a returning user, I want my data to remain private and accessible only to me.
* As a premium subscriber, I want to receive immediate access to premium features upon successful payment.
* As a premium subscriber, I want to manage my subscription and see my current tier status.

---

## **Design**

### **Overview**

Mindly is designed to be calm, supportive, and user-friendly. The interface prioritises clarity, accessibility, and ease of use to encourage consistent wellbeing tracking and journaling without overwhelming the user.

[**[Screenshot: Design Overview - Dashboard & Features]**](#)

---

### **Colour Scheme**

A warm, supportive colour palette is chosen to create a positive, welcoming environment that encourages mental health reflection and action.

[**[Screenshot: Colour Scheme Chart]**](#)

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

[**[Screenshot: Typography Examples]**](#)

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
* Profile page for logged-in users (view only)
* @login_required decorators on protected views
* CSRF protection on all forms

### **Mood Tracking Features**

* Create mood entries with score (1-10) and optional note
* View all past mood entries in reverse chronological order
* Edit mood entries to update score or note
* Delete mood entries with confirmation
* Mood entry metadata (date/time created and updated)
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

**Note:** `MoodEntry` and `JournalEntry` are both defined in the `journal` app (`journal/models.py`).

### **Relationships**

- `CustomUser` → `UserProfile` (1-to-1)
- `CustomUser` → `MoodEntry` (1-to-many)
- `CustomUser` → `JournalEntry` (1-to-many)

All entries are scoped to logged-in user via `request.user` for data privacy.

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
│   ├── views.py                        # Auth views (register, login, profile)
│   ├── urls.py                         # User URLs
│   ├── decorators.py                   # @premium_required decorator
│   ├── tests.py                        # User model tests
│   ├── forms.py                        # Auth forms
│   └── templates/users/                # User templates
├── journal/                            # Journal app
│   ├── models.py                       # JournalEntry model
│   ├── views.py                        # Journal CRUD views
│   ├── urls.py                         # Journal URLs
│   ├── tests.py                        # Journal tests
│   └── templates/journal/              # Journal templates
├── assessments/                        # Mood tracking app
│   ├── models.py                       # (MoodEntry defined in journal/models.py)
│   ├── views.py                        # Mood entry views
│   ├── urls.py                         # Assessment URLs
│   └── tests.py                        # Mood tracking tests
├── payments/                           # Payments & subscription
│   ├── models.py                       # Payment models (minimal)
│   ├── views.py                        # Stripe checkout, webhook
│   ├── urls.py                         # Payment URLs
│   ├── tests.py                        # Payment tests
│   └── templates/payments/             # Pricing, success pages
├── pages/                              # Static pages & premium resources
│   ├── views.py                        # Home, pricing, premium resources
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
* **Django ORM** - Object-relational mapping for database
* **Django Template Language (DTL)** - Template engine
* **Bootstrap 5** - Responsive CSS framework
* **SQLite** - Development database
* **Stripe** - Payment processing
* **Python Decouple** - Environment variable management
* **Git & GitHub** - Version control
* **Windows/CMD** - Development environment
* **VS Code** - Code editor

---

## **Testing**

Comprehensive testing has been carried out to ensure functionality, security, usability, and reliability across all features.

See [**TESTING.md**](./docs/TESTING.md) for full testing documentation including:

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

See DEPLOYMENT.md for complete Stripe setup and testing instructions.

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

## **Credits**

### **Code**

Python documentation, Django official documentation, Stripe API documentation, Bootstrap documentation, and Django best practices from community sources.

### **Media**

All images are placeholders or placeholder sources. Final images to be sourced from royalty-free repositories.

### **Acknowledgements**

Developed as a professional portfolio project demonstrating full-stack development capabilities.

---

**Shehzad Moin, 2026**
