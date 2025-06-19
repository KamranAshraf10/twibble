
# Twibble - A Twitter-like Django App

Twibble is a social media application built using Django, allowing users to post tweets, view others' posts, and manage their profiles. This project implements CRUD functionality for tweets, user authentication, and uses Django templating, forms, and the Django admin panel for management.

## Features

- **User Authentication**: Register, login, logout, and profile management.
- **CRUD for Tweets**: Create, read, update, and delete tweets.
- **Django Admin Panel**: Manage tweets, users, and other data easily.
- **Django Forms**: Create forms for user input (creating and editing tweets).

## Setup

### Prerequisites
- Python 3.x
- Django 4.x
- A virtual environment (recommended)

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/KamranAshraf10/twibble.git
   ```

2. Navigate to the project folder:

   ```bash
   cd twibble
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Run migrations to set up the database:

   ```bash
   python manage.py migrate
   ```

6. Run the development server:

   ```bash
   python manage.py runserver
   ```

7. Visit http://127.0.0.1:8000/ in your browser to see the app in action!

## Contributing

- Fork this repository.
- Create a new branch (`git checkout -b feature-name`).
- Make your changes and commit them (`git commit -am 'Add new feature'`).
- Push to your fork (`git push origin feature-name`).
- Create a pull request.

## License

This project is open-source and available under the MIT License.
