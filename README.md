# Django Movie Web

## Installation

### Prerequisites
- Python 3.12+
- Django 5.1+
- A virtual environment (recommended)

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd movie-web
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Mac
   source venv/bin/activate
   
   # On Windows
   venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Load sample data:
   ```bash
   python manage.py shell
   >>> from movies.load_movies import load_movies
   >>> load_movies()
   >>> exit()
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

