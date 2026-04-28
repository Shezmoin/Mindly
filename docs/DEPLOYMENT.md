## **Deployment - Mindly Application**

This document provides comprehensive deployment instructions for running Mindly locally and in production environments.

---

## Table of Contents

- [Deployment Platform](#deployment-platform)
- [Local Development Deployment](#local-development-deployment)
- [Production Deployment (Heroku)](#production-deployment-heroku)
- [Environment Variables Reference](#environment-variables-reference)
- [Database Setup](#database-setup)
- [Stripe Setup](#stripe-setup)
- [Troubleshooting](#troubleshooting)
- [Deployment Checklist (Heroku)](#deployment-checklist-heroku)
- [Deployment Notes](#deployment-notes)

---

## **Deployment Platform**

Mindly is deployed on **Heroku** — a cloud platform that supports Django applications with managed PostgreSQL, environment config vars, and automatic HTTPS.

[**[Screenshot: Heroku Dashboard - Mindly App]**](#)

---

## **Local Development Deployment**

### **Prerequisites**

Before deploying locally, ensure these are installed:

- **Python 3.13+** - Download from [python.org](https://www.python.org/)
- **Git** - Download from [git-scm.com](https://git-scm.com/)
- **pip** - Comes with Python
- **Virtual Environment Tool** - `venv` (built-in to Python)

### **Step 1: Clone Repository**

```bash
git clone https://github.com/Shezmoin/Mindly.git
cd Mindly
```

### **Step 2: Create and Activate Virtual Environment**

**Windows (CMD):**
```bash
python -m venv venv
venv\Scripts\activate
```

**Windows (PowerShell):**
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

Verify activation - you should see `(venv)` prefix in terminal.

### **Step 3: Install Dependencies**

```bash
pip install -r requirements.txt
```

This installs all required packages:
- Django 4.2
- stripe 11.3.0
- python-decouple
- Bootstrap 5 (via CDN)
- Other dependencies

### **Step 4: Prepare Environment Variables**

```bash
copy .env.example .env
```

Edit `.env` and set required values:

```
SECRET_KEY=your-django-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

STRIPE_PUBLIC_KEY=pk_test_51234...
STRIPE_SECRET_KEY=sk_test_51234...
STRIPE_PRICE_ID=price_1234...
STRIPE_WEBHOOK_SECRET=whsec_test_1234...
```

### **Step 5: Apply Database Migrations**

```bash
python manage.py migrate
```

This creates the SQLite database and applies all migrations:
- Users (CustomUser, UserProfile)
- Journal (JournalEntry)
- Assessments (MoodEntry)
- Payments (minimal setup)

### **Step 6: Create Superuser (Admin Account)**

```bash
python manage.py createsuperuser
```

Follow prompts to create admin credentials:
```
Username: admin
Email: admin@example.com
Password: [enter secure password]
```

### **Step 7: Collect Static Files (Optional for Development)**

```bash
python manage.py collectstatic --noinput
```

### **Step 8: Run Development Server**

```bash
python manage.py runserver
```

Server starts at `http://127.0.0.1:8000/`

### **Step 9: Verify Installation**

1. Open `http://localhost:8000` in browser
2. Navigate through key pages:
   - Home page (/)
   - Register (/users/register/)
   - Pricing (/payments/pricing/)
   - Admin (/admin/)

3. Log in with superuser credentials to verify authentication

### **Windows Quick Launch**

On Windows, run all steps in one command:

```bash
launch_safe.bat
```

This script runs system checks and launches the server.

---

## **Production Deployment (Heroku)**

### **Prerequisites**

- [Heroku account](https://heroku.com) (free tier available)
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) installed
- Git repository pushed to GitHub

### **Step 1: Install Heroku CLI and Login**

```bash
heroku login
```

This opens a browser window for authentication.

### **Step 2: Create Heroku App**

```bash
heroku create mindly-app
```

Or choose your own app name. Heroku provides a URL: `https://mindly-app.herokuapp.com`

### **Step 3: Add PostgreSQL Database**

```bash
heroku addons:create heroku-postgresql:essential-0
```

Heroku automatically sets `DATABASE_URL` as a config var.

### **Step 4: Add Required Files**

Ensure these files exist in the project root:

**`Procfile`** (no extension):
```
web: gunicorn mindly.wsgi
```

**`runtime.txt`**:
```
python-3.13.0
```

Install `gunicorn` and `whitenoise` for static files if not already present:
```bash
pip install gunicorn whitenoise
pip freeze > requirements.txt
```

Add `whitenoise` to `MIDDLEWARE` in `settings.py` (after `SecurityMiddleware`):
```python
'whitenoise.middleware.WhiteNoiseMiddleware',
```

Add to `settings.py` for static file serving:
```python
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

### **Step 5: Set Config Vars (Environment Variables)**

```bash
heroku config:set SECRET_KEY=your-strong-secret-key
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS=mindly-app.herokuapp.com
heroku config:set STRIPE_PUBLIC_KEY=pk_live_...
heroku config:set STRIPE_SECRET_KEY=sk_live_...
heroku config:set STRIPE_PRICE_ID=price_...
heroku config:set STRIPE_WEBHOOK_SECRET=whsec_...
```

Generate a strong secret key:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Verify all config vars are set:
```bash
heroku config
```

### **Step 6: Deploy to Heroku**

```bash
git push heroku main
```

Heroku detects Django automatically, installs dependencies from `requirements.txt`, and starts the `web` dyno.

### **Step 7: Apply Database Migrations**

```bash
heroku run python manage.py migrate
```

### **Step 8: Create Superuser**

```bash
heroku run python manage.py createsuperuser
```

### **Step 9: Collect Static Files**

```bash
heroku run python manage.py collectstatic --noinput
```

### **Step 10: Configure Stripe Webhook**

In Stripe Dashboard:

1. Go to **Developers → Webhooks**
2. Create new endpoint: `https://mindly-app.herokuapp.com/payments/webhook/`
3. Events to subscribe: `checkout.session.completed`
4. Copy webhook signing secret
5. Update Heroku config var:
```bash
heroku config:set STRIPE_WEBHOOK_SECRET=whsec_...
```

### **Step 11: Verify Deployment**

```bash
heroku open
```

Or visit `https://mindly-app.herokuapp.com` in your browser.

Check logs if there are any errors:
```bash
heroku logs --tail
```

---

## **Environment Variables Reference**

### **Django Settings**

| Variable | Value | Purpose |
|----------|-------|---------|
| `SECRET_KEY` | Random 50+ char string | Django session/CSRF security |
| `DEBUG` | False | Disable debug mode in production |
| `ALLOWED_HOSTS` | mindly-app.herokuapp.com | Prevent Host header attacks |
| `DATABASE_URL` | Set automatically by Heroku | Database connection string |

### **Database Configuration**

| Variable | Example | Purpose |
|----------|---------|---------|
| `DATABASE_URL` | postgresql://user:pass@localhost/db | Production database |

### **Stripe Credentials**

| Variable | Example | Purpose |
|----------|---------|---------|
| `STRIPE_PUBLIC_KEY` | pk_live_... | Client-side Stripe.js key |
| `STRIPE_SECRET_KEY` | sk_live_... | Server-side API key |
| `STRIPE_PRICE_ID` | price_1234... | Product price ID for checkout |
| `STRIPE_WEBHOOK_SECRET` | whsec_... | Webhook signature verification |

### **Optional Variables**

| Variable | Default | Purpose |
|----------|---------|---------|
| `SECURE_HSTS_SECONDS` | 31536000 | HTTPS security header |
| `SECURE_SSL_REDIRECT` | True | Redirect HTTP to HTTPS |
| `SESSION_COOKIE_SECURE` | True | Send cookies only over HTTPS |

---

## **Database Setup**

### **Development (SQLite)**

Automatically created when migrations run:

```bash
python manage.py migrate
```

Creates `db.sqlite3` in project root.

### **Production (PostgreSQL on Heroku)**

Heroku automatically provisions a PostgreSQL database when you run:

```bash
heroku addons:create heroku-postgresql:essential-0
```

`DATABASE_URL` is set automatically as a Heroku config var — no manual configuration needed.

Run migrations on Heroku:
```bash
heroku run python manage.py migrate
```

### **Creating Admin User**

```bash
heroku run python manage.py createsuperuser
```

Access admin at `https://mindly-app.herokuapp.com/admin`

---

## **Stripe Setup**

### **Stripe Test Mode**

1. Create free Stripe account at [stripe.com](https://stripe.com)
2. Go to **Developers → API Keys**
3. Copy test keys (starts with `pk_test_` and `sk_test_`)
4. Add to `.env`
5. Create test product and price at Prices tab
6. Copy Price ID (starts with `price_`)

### **Stripe Production Mode**

1. In Stripe dashboard, go to **Settings → Account**
2. Click **Activate Production**
3. Complete business verification
4. Go to **Developers → API Keys**
5. Copy live keys (starts with `pk_live_` and `sk_live_`)
6. Update `.env` with live keys
7. Create production product/price
8. Update `STRIPE_PRICE_ID`

### **Webhook Configuration**

**Test Webhook (Local Development):**

```bash
stripe login
stripe listen --forward-to 127.0.0.1:8000/payments/webhook/
```

Copy printed webhook secret to `.env`.

**Production Webhook (Heroku):**

1. Stripe dashboard → **Developers → Webhooks**
2. Create endpoint
3. URL: `https://mindly-app.herokuapp.com/payments/webhook/`
4. Events: `checkout.session.completed`
5. Copy signing secret
6. Run: `heroku config:set STRIPE_WEBHOOK_SECRET=whsec_...`

---

## **Troubleshooting**

### **Problem: Migration Errors**

**Symptom:** `django.db.utils.OperationalError` when running migrations

**Solution:**
```bash
heroku run python manage.py migrate --run-syncdb
heroku run python manage.py migrate
```

### **Problem: Static Files Missing**

**Symptom:** CSS/JS/images not loading (404 errors)

**Solution:**
```bash
heroku run python manage.py collectstatic --clear --noinput
```

Also ensure `whitenoise` is installed and configured (see Step 4 above).

### **Problem: Secret Key Issues**

**Symptom:** `ImproperlyConfigured: The SECRET_KEY setting must not be empty`

**Solution:**
```bash
# Generate new key
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# Set on Heroku
heroku config:set SECRET_KEY=<output_from_above>
```

### **Problem: DEBUG Mode Exposed**

**Symptom:** Stack traces showing in browser

**Solution:**
```bash
heroku config:set DEBUG=False
```

### **Problem: Webhook Failing (400 Errors)**

**Symptom:** Webhook returns [400] responses

**Solution:**
1. Verify `STRIPE_WEBHOOK_SECRET` config var is correct on Heroku
2. Confirm webhook URL matches Heroku app URL exactly
3. Check `heroku logs --tail` for error details
4. Verify signature verification code in `payments/views.py`

### **Problem: Database Connection Failed**

**Symptom:** `django.db.utils.OperationalError: could not connect to server`

**Solution:**
1. Verify PostgreSQL addon is provisioned: `heroku addons`
2. Check `DATABASE_URL` is set: `heroku config | grep DATABASE_URL`
3. Re-run migrations: `heroku run python manage.py migrate`

### **Problem: H10 App Crashed (Heroku)**

**Symptom:** H10 error, app not starting

**Solution:**
1. Check `Procfile` exists with `web: gunicorn mindly.wsgi`
2. Check `requirements.txt` includes `gunicorn`
3. Check logs: `heroku logs --tail`
4. Verify all required config vars are set: `heroku config`

### **Problem: Static Files Not Loading**

**Symptom:** CSS/JS missing on Heroku

**Solution:**
1. Ensure `whitenoise` is in `requirements.txt` and `MIDDLEWARE`
2. Run: `heroku run python manage.py collectstatic --noinput`
3. Verify `STATICFILES_STORAGE` is set to WhiteNoise in `settings.py`

---

## **Deployment Checklist (Heroku)**

Before going live, verify:

- [ ] Heroku app created and CLI authenticated
- [ ] `Procfile` present with `web: gunicorn mindly.wsgi`
- [ ] `runtime.txt` specifies Python version
- [ ] `gunicorn` and `whitenoise` in `requirements.txt`
- [ ] `DEBUG = False` set via `heroku config:set`
- [ ] `ALLOWED_HOSTS` set to Heroku app domain
- [ ] `SECRET_KEY` is strong and set via `heroku config:set`
- [ ] PostgreSQL addon provisioned
- [ ] Database migrations applied (`heroku run python manage.py migrate`)
- [ ] Static files collected (`heroku run python manage.py collectstatic`)
- [ ] HTTPS enabled (automatic on Heroku)
- [ ] Stripe keys are production (pk_live_, sk_live_)
- [ ] Stripe webhook endpoint configured with Heroku URL
- [ ] Admin user created (`heroku run python manage.py createsuperuser`)
- [ ] Database backups enabled
- [ ] Error logging configured
- [ ] Uptime monitoring enabled
- [ ] Security headers set (HSTS, X-Frame-Options, etc.)

---

## **Deployment Notes**

- Always backup the database before deploying: `heroku pg:backups:capture`
- Use Heroku config vars for all secrets (never hardcode or commit)
- Keep dependency versions updated for security patches
- Monitor logs with `heroku logs --tail`
- Use Heroku Postgres automatic daily backups (paid plans)
- Scale dynos if needed: `heroku ps:scale web=2`
- Heroku provides automatic HTTPS — no manual SSL setup required
- Use `heroku run` for any management commands on production

---

**Shehzad Moin, 2026**
