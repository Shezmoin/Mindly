# 💙 mindly

> Your mental wellbeing, supported every day

A Django-based mental health and wellbeing platform providing mood tracking, mental health assessments, journaling, and premium support services. Built with Bootstrap 5 for a responsive, accessible experience.

## 🌟 Features

- **Mood Tracking** - Monitor your emotional wellbeing over time
- **Mental Health Assessments** - Evidence-based psychological assessments
- **Private Journaling** - Secure space for personal reflections
- **Resources Library** - Curated mental health information and guides
- **Premium Subscriptions** - Advanced features and priority support
- **Donation System** - Support mental health services with one-time donations
- **User Authentication** - Secure account management

## 💷 Payment Features

Mindly includes two Stripe payment integrations with **British Pounds (GBP)**:

1. **One-Time Donations** - Support the platform with £5, £10, £25, £50, or custom amounts
2. **Premium Subscriptions** - £9.99/month recurring subscription with:
   - Unlimited assessments and mood tracking
   - Advanced analytics and insights
   - Priority email support
   - Ad-free experience
   - Premium resources library

## 🚀 Quick Start

### Prerequisites

- Python 3.8+ (tested with Python 3.13.9)
- pip and virtualenv
- Git
- Stripe account (for payment features)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Shezmoin/Mindly.git
   cd Mindly
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   # Copy the example environment file
   cp .env.example .env

   # Edit .env and add your Stripe keys (see Stripe Setup below)
   ```

5. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

6. **Collect static files**
   ```bash
   python manage.py collectstatic --noinput
   ```

7. **Create a superuser** (optional)
   ```bash
   python manage.py createsuperuser
   ```

8. **Run the development server**
   ```bash
   python manage.py runserver
   ```

9. **Open in browser**
   ```
   http://localhost:8000
   ```

## 💳 Stripe Setup

To enable payment features, you'll need to configure Stripe:

### 1. Get Stripe API Keys

1. Sign up at [https://stripe.com](https://stripe.com)
2. Navigate to **Developers > API keys**
3. Copy your **Publishable key** and **Secret key** (use test keys for development)

### 2. Create Premium Product in Stripe

1. Go to **Products** in Stripe Dashboard
2. Click **+ Add product**
3. Set:
   - Name: "Premium Subscription"
   - Description: "Monthly premium subscription"
   - Pricing: £9.99 GBP, Recurring (monthly)
4. Copy the **Price ID** (starts with `price_`)

### 3. Configure Webhook (for production)

1. Go to **Developers > Webhooks**
2. Click **+ Add endpoint**
3. Set URL: `https://yourdomain.com/payments/webhook/`
4. Select events: `payment_intent.succeeded`, `checkout.session.completed`, `customer.subscription.deleted`
5. Copy the **Signing secret** (starts with `whsec_`)

### 4. Update .env File

Edit `.env` with your Stripe credentials:

```env
STRIPE_PUBLIC_KEY=pk_test_your_key_here
STRIPE_SECRET_KEY=sk_test_your_key_here
STRIPE_WEBHOOK_SECRET=whsec_your_secret_here
STRIPE_PREMIUM_PRICE_ID=price_your_price_id_here
```

### 5. Uncomment Stripe Code

In `payments/views.py`, uncomment the Stripe API calls:
- Line 2: `stripe.api_key = settings.STRIPE_SECRET_KEY`
- Checkout session creation code in `donate_view()` and `subscribe_view()`
- Webhook verification in `webhook_handler()`

## 📁 Project Structure

```
Mindly/
├── mindly/                 # Main project settings
│   ├── settings.py         # Django configuration + Stripe settings
│   ├── urls.py             # Root URL routing
│   └── wsgi.py
├── users/                  # User authentication app
├── assessments/            # Mental health assessments
├── journal/                # Private journaling
├── payments/               # Stripe payment integration
│   ├── views.py            # Donation & subscription views
│   ├── urls.py             # Payment routes
│   └── templates/
│       └── payments/
│           ├── index.html       # Support page
│           ├── donate.html      # Donation form
│           ├── subscribe.html   # Subscription page
│           ├── success.html     # Payment success
│           └── cancel.html      # Payment cancelled
├── pages/                  # Static pages (home, about)
├── templates/              # Project-level templates
│   ├── base.html           # Base template with navbar
│   └── pages/
│       ├── home.html       # Homepage
│       └── about.html      # About page
├── static/                 # CSS, JS, images
│   └── css/
│       └── style.css       # Custom styles
├── requirements.txt        # Python dependencies
├── .env.example            # Environment variables template
└── manage.py
```

## 🎨 Tech Stack

- **Backend**: Django 4.2
- **Frontend**: Bootstrap 5.3.0, Font Awesome 6.4.0
- **Database**: SQLite (development), PostgreSQL (production)
- **Payments**: Stripe API v11.3.0
- **Deployment**: Heroku (planned)

## 🔐 Security Notes

- Never commit `.env` file to version control
- Use test Stripe keys in development
- Enable HTTPS in production
- Set `DEBUG = False` in production
- Configure `ALLOWED_HOSTS` for production

## 🧪 Testing Payments

Use Stripe test cards:

- **Success**: `4242 4242 4242 4242`
- **Requires authentication**: `4000 0025 0000 3155`
- **Declined**: `4000 0000 0000 9995`

Use any future expiry date, any 3-digit CVC, and any postal code.

## 🌍 Deployment to Heroku

1. **Install Heroku CLI**
   ```bash
   # Download from: https://devcenter.heroku.com/articles/heroku-cli
   ```

2. **Create Heroku app**
   ```bash
   heroku create mindly-app
   ```

3. **Set environment variables**
   ```bash
   heroku config:set SECRET_KEY=your-secret-key
   heroku config:set DEBUG=False
   heroku config:set STRIPE_PUBLIC_KEY=pk_live_...
   heroku config:set STRIPE_SECRET_KEY=sk_live_...
   heroku config:set STRIPE_WEBHOOK_SECRET=whsec_...
   heroku config:set STRIPE_PREMIUM_PRICE_ID=price_...
   ```

4. **Add Procfile** (create in project root)
   ```
   web: gunicorn mindly.wsgi --log-file -
   ```

5. **Install gunicorn**
   ```bash
   pip install gunicorn
   pip freeze > requirements.txt
   ```

6. **Deploy**
   ```bash
   git push heroku main
   heroku run python manage.py migrate
   heroku run python manage.py createsuperuser
   ```

## 📝 License

This project was created for academic purposes.

## 📧 Contact

For questions or support: support@mindly.com

## 🙏 Acknowledgments

- Mental health resources provided by NHS UK
- Crisis support information from Samaritans
- UI design inspired by modern mental health platforms

---

**⚠️ Disclaimer**: Mindly is not a substitute for professional mental health care. If you're experiencing a crisis, please contact emergency services or call Samaritans at 116 123 (UK).
