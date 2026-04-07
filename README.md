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
