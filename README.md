# mindly

A Django-based mental health and wellbeing platform that helps users track their mood, complete assessments, journal their thoughts, and access premium support services. Built with Django 4.2, Bootstrap 5, and Stripe payments in GBP.

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
