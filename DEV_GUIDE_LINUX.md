# ClearInsure Developer Guide (Linux)

## Prerequisites
- Python 3.10+
- Podman & Podman Compose
- Git
- (Recommended) Virtualenv

## Setup Steps
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Mosethespu/clearviewins2.git
   cd clearviewins2
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install django
   ```
4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```
5. **Create a superuser (optional):**
   ```bash
   python manage.py createsuperuser
   ```
6. **Start the development server:**
   ```bash
   python manage.py runserver
   ```
   Access the app at `http://127.0.0.1:8000`

## Containerized Development
1. **Build and run with Podman Compose:**
   ```bash
   podman-compose up --build
   ```
2. **Stop containers:**
   ```bash
   podman-compose down
   ```
3. **Clean up unused images/containers:**
   ```bash
   podman system prune -f
   ```

## Useful Tips & Tricks
- Use `rebuild.sh` to automate cleanup and rebuild:
  ```bash
  ./rebuild.sh
  ```
- Use `git pull` before pushing to avoid conflicts.
- Use `python manage.py test` to run tests.
- Use `python manage.py collectstatic` for static files in production.
- Use `git branch` and `git checkout -b <branch>` for feature development.
- For merge conflicts, use `git status` and resolve files as needed.

## Troubleshooting
- If you get permission errors, run:
  ```bash
  chmod +x rebuild.sh
  ```
- If Podman can't find the Dockerfile, ensure it's named `Dockerfile`.
- For database issues, delete `db.sqlite3` and rerun migrations.

## Project Structure
- `manage.py` - Django management script
- `clearviewins2/` - Main Django app
- `static/` - Static files (CSS, images)
- `templates/` - HTML templates
- `rebuild.sh` - Podman cleanup and rebuild script

---
For more help, see the README or open an issue on GitHub.
