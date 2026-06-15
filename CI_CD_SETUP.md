# CI/CD Pipeline Setup

This project includes comprehensive CI/CD pipelines using GitHub Actions for automated testing, code quality checks, and Docker builds.

## Workflows Overview

### 1. Tests Workflow (`tests.yml`)
Runs on every push to `main` or `develop` branches, and on all pull requests.

**What it does:**
- Sets up Python 3.10 environment
- Spins up PostgreSQL and Redis services for integration tests
- Installs all project dependencies
- Runs Django migrations
- Executes pytest with coverage reporting
- Generates HTML coverage report
- Uploads coverage metrics to Codecov (optional)

**Key Features:**
- Parallel services (PostgreSQL + Redis)
- Coverage reporting with XML, HTML, and terminal output
- Artifact preservation (coverage reports kept for 30 days)
- Fast dependency caching

### 2. Docker Build Workflow (`docker-build.yml`)
Validates that the Docker image builds successfully.

**What it does:**
- Builds Docker image using the Dockerfile
- Uses GitHub's build cache for faster builds
- Runs on every push and pull request

### 3. Code Quality Workflow (`code-quality.yml`)
Checks code formatting and linting standards.

**What it does:**
- Checks code formatting with Black
- Validates import sorting with isort
- Runs flake8 linting checks

---

## Running Tests Locally

### Prerequisites
```bash
# Create virtual environment (if not already done)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r bus_ticket_project/requirements.txt
```

### Run All Tests
```bash
cd bus_ticket_project
pytest
```

### Run Tests with Coverage Report
```bash
cd bus_ticket_project
pytest --cov=. --cov-report=html --cov-report=term-missing
```

### Run Specific Test File
```bash
pytest user/tests/test_views.py
```

### Run Specific Test Class or Function
```bash
pytest user/tests/test_views.py::TestUserViews::test_user_creation
```

---

## Configuration Files

### `pytest.ini`
Configures pytest behavior:
- Django settings module
- Test file patterns: `*_test.py` and `test_*.py`
- Test class pattern: `*Test`
- Test function pattern: `test_*`
- Auto-reuse of test database
- Database setup mode

### `.github/workflows/`
Contains all GitHub Actions workflow definitions

---

## Coverage Reports

After running tests locally with coverage, view the HTML report:
```bash
# Open in browser (Windows)
start htmlcov/index.html

# Open in browser (macOS)
open htmlcov/index.html

# Open in browser (Linux)
firefox htmlcov/index.html
```

---

## Environment Variables for CI

The CI pipeline uses these environment variables:
- `DATABASE_URL`: PostgreSQL connection string
- `REDIS_URL`: Redis connection string
- `DEBUG`: Set to `False` in CI environment

---

## Codecov Integration

Coverage reports are automatically uploaded to Codecov. To enable this:

1. Visit https://codecov.io
2. Connect your GitHub repository
3. Add the CODECOV_TOKEN to your repository secrets (if private repo)

The workflow will fail gracefully if Codecov is unavailable.

---

## Best Practices

1. **Write Tests Early**: Write tests when creating new features
2. **Maintain Coverage**: Aim for >80% code coverage
3. **Run Tests Before Pushing**: Always run tests locally first
4. **Review Coverage Reports**: Check which lines aren't covered
5. **Keep Tests Fast**: Optimize database queries in tests

---

## Troubleshooting

### Tests fail in CI but pass locally
- Check environment variables are set correctly
- Ensure database migrations run successfully
- Verify Redis is accessible (if using Celery)

### Coverage is missing for some files
- Check pytest configuration in `pytest.ini`
- Ensure test files follow naming conventions
- Consider using `# pragma: no cover` for untestable code

### Docker build fails
- Check Dockerfile syntax
- Ensure requirements.txt is valid
- Verify all files referenced in COPY commands exist

---

## Adding New Tests

Create test files in your app directories:
```
app_name/
├── tests.py (or tests/ package)
│   ├── __init__.py
│   ├── test_models.py
│   ├── test_views.py
│   ├── test_serializers.py
│   └── test_urls.py
```

## Next Steps

1. Commit these workflow files to your repository
2. Push to GitHub to trigger the first CI run
3. Monitor the "Actions" tab in your GitHub repository
4. Address any failures reported by the workflows
5. Improve test coverage based on reports

