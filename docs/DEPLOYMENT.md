## **Deployment - Mindly Application**

This document provides comprehensive deployment instructions for running Mindly locally and in production environments.

---

## **Deployment Platform**

Mindly is designed to be deployed on modern cloud platforms supporting Django applications.

**Recommended Deployment Platforms:**
- Railway
- Render
- Heroku
- PythonAnywhere
- AWS/DigitalOcean

[**[Screenshot: Deployment Platform Overview]**](#)

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

## **Production Deployment**

### **Step 1: Set Production Environment Variables**

Create `.env` on production server with production values:

```bash
SECRET_KEY=generate-strong-random-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

STRIPE_PUBLIC_KEY=pk_live_[your-live-public-key]
STRIPE_SECRET_KEY=sk_live_[your-live-secret-key]
STRIPE_PRICE_ID=price_[your-production-price-id]
STRIPE_WEBHOOK_SECRET=whsec_[your-production-webhook-secret]

DATABASE_URL=postgresql://user:pass@localhost/mindly_prod
```

### **Step 2: Generate Strong SECRET_KEY**

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copy output and set as `SECRET_KEY` in `.env`.

### **Step 3: Configure Production Database**

**Option A: PostgreSQL (Recommended)**

Create PostgreSQL database on production server:

```bash
createdb mindly_prod
```

Update `DATABASE_URL` in `.env`:

```
DATABASE_URL=postgresql://username:password@localhost:5432/mindly_prod
```

### **Step 4: Ensure All Dependencies Installed**

```bash
pip install -r requirements.txt
```

### **Step 5: Apply Migrations on Production**

```bash
python manage.py migrate
```

### **Step 6: Collect Static Files**

```bash
python manage.py collectstatic --noinput
```

This collects all CSS/JS/images into a single directory for web server serving.

### **Step 7: Configure Web Server**

**Option A: Using Gunicorn + Nginx**

Install Gunicorn:
```bash
pip install gunicorn
```

Create systemd service file `/etc/systemd/system/mindly.service`:

```ini
[Unit]
Description=Mindly Django Application
After=network.target

[Service]
Type=notify
User=www-data
Group=www-data
WorkingDirectory=/path/to/mindly
ExecStart=/path/to/mindly/venv/bin/gunicorn \
    --workers 3 \
    --bind unix:/path/to/mindly/mindly.sock \
    mindly.wsgi:application

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl enable mindly
sudo systemctl start mindly
```

Configure Nginx as reverse proxy (`/etc/nginx/sites-available/mindly`):

```nginx
server {
    listen 80;
    server_name yourdomain.com;
    
    location /static/ {
        alias /path/to/mindly/static/;
    }
    
    location / {
        proxy_pass http://unix:/path/to/mindly/mindly.sock;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

Enable site:
```bash
sudo ln -s /etc/nginx/sites-available/mindly /etc/nginx/sites-enabled/
sudo nginx -s reload
```

### **Step 8: Set Up HTTPS**

Install Certbot for SSL:
```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d yourdomain.com
```

Auto-renewal:
```bash
sudo systemctl enable certbot.timer
```

### **Step 9: Configure Stripe Webhooks**

In Stripe Dashboard:

1. Go to **Developers → Webhooks**
2. Create new endpoint: `https://yourdomain.com/payments/webhook/`
3. Events to subscribe:
   - `checkout.session.completed`
4. Copy webhook secret and add to `.env` as `STRIPE_WEBHOOK_SECRET`
5. Restart application

### **Step 10: Verify Productions Deployment**

```bash
curl https://yourdomain.com/
```

Should return HTML response (not error).

---

## **Environment Variables Reference**

### **Django Settings**

| Variable | Value | Purpose |
|----------|-------|---------|
| `SECRET_KEY` | Random 50+ char string | Django session/CSRF security |
| `DEBUG` | False | Disable debug mode in production |
| `ALLOWED_HOSTS` | yourdomain.com,www.yourdomain.com | Prevent Host header attacks |
| `DATABASE_URL` | See below | Database connection string |

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

### **Production (PostgreSQL)**

1. Install PostgreSQL on server
2. Create database user and database
3. Set `DATABASE_URL` in `.env`
4. Run migrations:

```bash
python manage.py migrate
```

### **Creating Admin User**

```bash
python manage.py createsuperuser
```

Access admin at `https://yourdomain.com/admin`

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

**Production Webhook:**

1. Stripe dashboard → **Developers → Webhooks**
2. Create endpoint
3. URL: `https://yourdomain.com/payments/webhook/`
4. Events: `checkout.session.completed`
5. Copy secret to `.env`
6. Restart application

---

## **Troubleshooting**

### **Problem: Migration Errors**

**Symptom:** `django.db.utils.OperationalError` when running migrations

**Solution:**
```bash
python manage.py migrate --run-syncdb
python manage.py migrate
```

### **Problem: Static Files Missing**

**Symptom:** CSS/JS/images not loading (404 errors)

**Solution:**
```bash
python manage.py collectstatic --clear --noinput
```

### **Problem: Secret Key Issues**

**Symptom:** `ImproperlyConfigured: The SECRET_KEY setting must not be empty`

**Solution:**
```bash
# Generate new key
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# Add to .env
SECRET_KEY=<output_from_above>
```

### **Problem: DEBUG Mode Exposed**

**Symptom:** Stack traces showing in browser

**Solution:** Ensure `.env` has `DEBUG=False` in production, restart server

### **Problem: Webhook Failing (400 Errors)**

**Symptom:** Webhook returns [400] responses

**Solution:**
1. Verify `STRIPE_WEBHOOK_SECRET` is correct (no spaces/truncation)
2. Ensure webhook endpoint allows POST requests
3. Check Django DEBUG mode settings
4. Verify signature verification code in `payments/views.py`

### **Problem: Database Connection Failed**

**Symptom:** `django.db.utils.OperationalError: could not connect to server`

**Solution:**
1. Verify PostgreSQL is running
2. Check `DATABASE_URL` format
3. Verify database user has permissions
4. Test with: `psql <DATABASE_URL>`

---

## **Deployment Checklist**

Before going live, verify:

- [ ] DEBUG = False
- [ ] ALLOWED_HOSTS configured
- [ ] SECRET_KEY is strong and random
- [ ] Database migrations applied
- [ ] Static files collected
- [ ] HTTPS/SSL certificate installed
- [ ] Stripe keys are production (pk_live_, sk_live_)
- [ ] Webhook endpoint configured
- [ ] Admin user created
- [ ] Email configuration (if applicable)
- [ ] Database backups enabled
- [ ] Error logging configured
- [ ] Uptime monitoring enabled
- [ ] Security headers set (HSTS, X-Frame-Options, etc.)

---

## **Deployment Notes**

- Always backup database before deploying
- Use environment variables for all secrets
- Keep dependency versions updated (security patches)
- Monitor application logs regularly
- Set up uptime monitoring and alerts
- Implement rate limiting for API endpoints
- Regularly test disaster recovery/restore procedures
- Use strong passwords for admin and database users
- Consider CDN for static file delivery in production

---

**Shehzad Moin, 2026**
