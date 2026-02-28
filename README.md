# TweetApp
A minimal Twitter-style app built with Django. Users can create an account, post tweets, edit or delete them, and attach images.

<img width="1887" height="728" alt="Screenshot 2026-02-28 192131" src="https://github.com/user-attachments/assets/b6fdd6a2-ad96-4163-bb08-fe2acc4a50cf" />

## Features

- User sign up, login, and logout
- Create, edit, delete, and view tweets
- Image support for tweets

## Getting Started

### Prerequisites

- Python 3.x
- Django 3.x or later

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/PatelMeet-31/tweet-app.git
   ```
2. Navigate to the project directory:

   ```bash
   cd tweet
   ```
3. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/Scripts/activate
   ```
4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```
5. Apply the migrations:

   ```bash
   python manage.py migrate
   ```
6. Create a superuser to access the admin panel:

   ```bash
   python manage.py createsuperuser
   ```
7. Start the development server:

   ```bash
   python manage.py runserver
   ```
8. Open your web browser and go to [http://127.0.0.1:8000/tweet/](http://127.0.0.1:8000/tweet/) to see the application in action.
