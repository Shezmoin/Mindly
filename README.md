# mindly

A Django-based mental health and wellbeing platform that helps users track their mood, complete assessments, journal their thoughts, and access premium support services. Built with Django 4.2, Bootstrap 5, and Stripe payments in GBP.

## Data Models

- `CustomUser`: The main user account for the site. It stores standard login details plus a short bio and optional profile picture.
- `UserProfile`: Extra account information linked to each user. It stores the user's subscription tier, the date they joined, and an optional reminder time.
- `MoodEntry`: A simple mood tracking record linked to a user. It stores a mood score from 1 to 10, an optional note, and when the entry was created.
- `JournalEntry`: A longer written reflection linked to a user. It stores a title, the journal content, whether the entry is private, and created/updated timestamps.

## How to Run Locally

1. Clone the repository and create a virtual environment:
   ```bash
   git clone https://github.com/Shezmoin/Mindly.git
   cd Mindly
   python -m venv venv
   venv\Scripts\activate   # Windows
   ```

2. Install dependencies and configure environment variables:
   ```bash
   pip install -r requirements.txt
   cp .env.example .env
   ```

3. Run migrations and start the server:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

4. Open http://localhost:8000 in your browser.

## Stripe Integration

### Payment Flow (Subscription)

1. User opens `/payments/pricing/` and clicks **Subscribe Now**.
2. Django view `checkout_view` creates a Stripe Checkout Session in
    subscription mode using `STRIPE_PRICE_ID`.
3. Stripe hosts the card entry page and processes payment.
4. On success, Stripe redirects the user to `/payments/success/`.
5. Stripe also sends webhook events to `/payments/webhook/`.
6. `webhook_view` handles `checkout.session.completed` and upgrades the
    matching user's `subscription_tier` to `premium`.

### Secrets and Keys

- Stripe keys are loaded from environment variables in `.env` and read in
   `mindly/settings.py` using `python-decouple`.
- Required variables:
   - `STRIPE_PUBLIC_KEY`
   - `STRIPE_SECRET_KEY`
   - `STRIPE_PRICE_ID`
   - `STRIPE_WEBHOOK_SECRET`
- Real secrets should never be hardcoded in source files.
- `.env` is local-only and should not be committed. Use `.env.example` for
   placeholders.

### Local Webhook Testing (Stripe CLI)

```bash
stripe login
stripe listen --forward-to 127.0.0.1:8000/payments/webhook/
```

Copy the printed `whsec_...` value into `.env` as `STRIPE_WEBHOOK_SECRET`,
then restart Django.

## Pre-Launch Verification (Run Every Time)

Before launching, run this command to catch routing/UI regressions early:

```bash
python manage.py check && python manage.py test pages journal
```

If this passes, then launch:

```bash
python manage.py runserver
```

On Windows, you can run one command that verifies then launches:

```bash
launch_safe.bat
```
