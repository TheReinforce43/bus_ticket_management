# Quick Start: Running Tests

## 1. Setup Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

## 2. Install Dependencies

```bash
pip install -r bus_ticket_project/requirements.txt
```

## 3. Setup Database (for local testing)

```bash
cd bus_ticket_project
python manage.py migrate
```

## 4. Run Tests

### All tests:
```bash
pytest
```

### With coverage:
```bash
pytest --cov=. --cov-report=html --cov-report=term-missing
```

### Specific app:
```bash
pytest user/
pytest location/
pytest notification/
```

### Watch for changes (requires pytest-watch):
```bash
pip install pytest-watch
ptw
```

## 5. View Coverage Report

```bash
# Open the HTML report in your browser
# Windows:
start htmlcov/index.html

# macOS:
open htmlcov/index.html

# Linux:
firefox htmlcov/index.html
```

---

## GitHub Actions Status

Once you push to GitHub, your CI/CD pipeline will automatically:
✅ Run all tests  
✅ Generate coverage reports  
✅ Validate Docker build  
✅ Check code quality  

View results in your GitHub repository's **Actions** tab.

---

## Useful pytest Commands

```bash
# Verbose output
pytest -v

# Show print statements
pytest -s

# Stop on first failure
pytest -x

# Only run failed tests from last run
pytest --lf

# Run with specific marker
pytest -m "django_db"

# Show slowest tests
pytest --durations=10
```

