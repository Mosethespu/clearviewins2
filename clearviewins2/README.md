# ClearInsure Project

ClearInsure is a Django-based web application for insurance transparency, supporting three user types: Customers, Insurers, and Regulators. The project uses SQLite, Bootstrap for UI, Podman/Podman Compose for containerization, and GitHub for version control.

## Features
- Landing page with animated UI
- Features page with user-type toggles and cards
- Contact, Blog, Login, and Sign Up pages
- Responsive design with Bootstrap
- Containerized with Podman/Podman Compose

## Quick Start

### Prerequisites
- Python 3.10+
- Podman & Podman Compose
- Git
- (Optional) Virtualenv

### Local Development
1. Clone the repo:
   ```bash
   git clone https://github.com/Mosethespu/clearviewins2.git
   cd clearviewins2
   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux
   venv\Scripts\activate    # Windows
   ```
3. Install dependencies:
   ```bash
   pip install django
   ```
4. Run migrations and start server:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```
5. Access the app at `http://127.0.0.1:8000`

### Containerized Development
1. Build and run with Podman Compose:
   ```bash
   podman-compose up --build
   ```
2. Access the app at `http://localhost:8000`

### Useful Commands
- Create superuser: `python manage.py createsuperuser`
- Collect static files: `python manage.py collectstatic`
- Run tests: `python manage.py test`
- Clean up Podman: `podman system prune -f`

## Tips & Tricks
- Use `rebuild.sh` to clean and rebuild containers automatically.
- Use Git branches for feature development.
- For static/media files, use the `static/` and `media/` folders.
- For troubleshooting, check logs in the terminal and Django admin.

## Contributing
Pull requests are welcome. For major changes, open an issue first to discuss what you would like to change.

## License
MIT
