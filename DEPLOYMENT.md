# Deployment Guide - Mindly Mental Health Platform

## Overview
This document covers deployment configuration for the Mindly platform on Heroku, including environment variables, email setup, and database configuration.

---

## Environment Variables

Create a `.env` file in the project root with the following variables:

```bash
# Django Settings
DEBUG=False
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=mindly-shez-9ca695ee4969.herokuapp.com

# Database
DATABASE_URL=your-database-url-here

# Stripe Payment Processing
STRIPE_PUBLIC_KEY=pk_live_your_key
STRIPE_SECRET_KEY=sk_live_your_key
STRIPE_WEBHOOK_SECRET=whsec_your_webhook_secret

# Email Configuration (Password Reset & Notifications)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-specific-password
DEFAULT_FROM_EMAIL=noreply@mindly.app
```

---

## Email Configuration for Password Reset

### Gmail (Recommended for Quick Setup)

1. **Enable 2-Step Verification** on your Gmail account
2. **Generate an App Password:**
   - Go to [Google Account Security](https://myaccount.google.com/security)
   - Select "2-Step Verification"
   - At the bottom, select "App passwords"
   - Choose "Mail" and "Windows Computer"
   - Generate and copy the 16-character password

3. **Set environment variables:**
   ```bash
   EMAIL_HOST=smtp.gmail.com
   EMAIL_PORT=587
   EMAIL_USE_TLS=True
   EMAIL_HOST_USER=your-email@gmail.com
   EMAIL_HOST_PASSWORD=xxxx xxxx xxxx xxxx  # (16-char app password)
   DEFAULT_FROM_EMAIL=your-email@gmail.com
   ```

### SendGrid (Enterprise Alternative)

1. **Create SendGrid Account** at [sendgrid.com](https://sendgrid.com)
2. **Generate API Key:**
   - Go to Settings → API Keys
   - Create a new API key
   
3. **Set environment variables:**
   ```bash
   EMAIL_HOST=smtp.sendgrid.net
   EMAIL_PORT=587
   EMAIL_USE_TLS=True
   EMAIL_HOST_USER=apikey
   EMAIL_HOST_PASSWORD=SG.your-api-key-here
   DEFAULT_FROM_EMAIL=noreply@mindly.app
   ```

### Mailgun (Popular Alternative)

1. **Create Mailgun Account** at [mailgun.com](https://mailgun.com)
2. **Get SMTP Credentials:**
   - Go to Sending → Domain Settings
   - Copy SMTP Host and credentials

3. **Set environment variables:**
   ```bash
   EMAIL_HOST=smtp.mailgun.org
   EMAIL_PORT=587
   EMAIL_USE_TLS=True
   EMAIL_HOST_USER=postmaster@your-domain.mailgun.org
   EMAIL_HOST_PASSWORD=your-mailgun-password
   DEFAULT_FROM_EMAIL=noreply@mindly.app
   ```

---

## Heroku Deployment

### 1. Install Heroku CLI
```bash
npm install -g heroku
heroku login
```

### 2. Create Heroku App
```bash
heroku create mindly-shez
heroku addons:create heroku-postgresql:hobby-dev  # Add database
```

### 3. Set Environment Variables
```bash
heroku config:set DEBUG=False
heroku config:set SECRET_KEY=your-secret-key-here
heroku config:set STRIPE_PUBLIC_KEY=pk_live_...
heroku config:set STRIPE_SECRET_KEY=sk_live_...
heroku config:set STRIPE_WEBHOOK_SECRET=whsec_...
heroku config:set EMAIL_HOST=smtp.gmail.com
heroku config:set EMAIL_PORT=587
heroku config:set EMAIL_USE_TLS=True
heroku config:set EMAIL_HOST_USER=your-email@gmail.com
heroku config:set EMAIL_HOST_PASSWORD=xxxx-xxxx-xxxx-xxxx
heroku config:set DEFAULT_FROM_EMAIL=noreply@mindly.app
```

### 4. Deploy
```bash
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py collectstatic --noinput
heroku restart
```

### 5. Verify Deployment
```bash
heroku logs --tail
heroku open
```

---

## Password Reset Configuration

### How It Works
1. **Request Reset**: User enters email on `/users/password-reset/`
2. **Email Sent**: Django sends email with unique token (expires in 1 hour)
3. **Confirmation Page**: User sees `/users/password-reset/done/` with Mindly styling
4. **Token Validation**: User clicks email link → `/users/password-reset/<uidb64>/<token>/`
5. **Password Reset Form**: User enters new password on custom form
6. **Success Page**: User sees `/users/password-reset/complete/` with success message

### Settings (mindly/settings.py)
```python
# Email Configuration
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = config('EMAIL_HOST', default='smtp.gmail.com')
    EMAIL_PORT = config('EMAIL_PORT', default=587, cast=int)
    EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=True, cast=bool)
    EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
    EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
    DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default='noreply@mindly.app')

# Password reset token timeout (1 hour)
PASSWORD_RESET_TIMEOUT = 3600
```

---

## Testing Email Configuration

### Development (Console Backend)
Emails print to terminal instead of sending:
```bash
python manage.py shell
from django.core.mail import send_mail
send_mail('Test', 'Body', 'noreply@mindly.app', ['test@example.com'])
# Output appears in terminal
```

### Production (SMTP)
Check Heroku logs for email sending:
```bash
heroku logs --tail | grep -i "email\|mail"
```

---

## Database Setup

### PostgreSQL on Heroku
```bash
# Automatic via heroku addons:create heroku-postgresql:hobby-dev
# URL available as DATABASE_URL environment variable
# Django automatically uses it if DATABASE_URL is set
```

### Local Development
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## SSL/HTTPS Configuration

Heroku automatically provides SSL certificates. Ensure `settings.py` includes:
```python
SECURE_SSL_REDIRECT = not DEBUG
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG
SECURE_HSTS_SECONDS = 31536000 if not DEBUG else 0
```

---

## Troubleshooting

### Password Reset Emails Not Sending
```bash
# Check email configuration
heroku config | grep EMAIL

# Check logs
heroku logs --tail

# Test SMTP credentials manually
heroku run python manage.py shell
from django.core.mail import send_mail
send_mail('Test', 'Test body', 'your-email@gmail.com', ['recipient@example.com'])
```

### Dyno Restart Required
```bash
heroku restart
# Clear template cache by restarting
```

### Static Files Not Loading
```bash
python manage.py collectstatic --noinput
git push heroku main
```

---

## Security Best Practices

1. **Never commit `.env`** - Use `.gitignore`
2. **Rotate SECRET_KEY** periodically
3. **Use app-specific passwords** for Gmail (not your main password)
4. **Enable 2FA** on all service accounts
5. **Monitor logs** for authentication errors
6. **Test email sending** after deployment

---

## Support

For issues, check:
- Heroku logs: `heroku logs --tail`
- Django error logs in stderr
- Email provider's bounce/complaint messages
