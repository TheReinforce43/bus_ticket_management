

import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def passenger(db):
    return User.objects.create_user(
        email="passenger@test.com",
        password="pass123",
        role="Passenger",
    )


# ---------------------------------------------------------------------------
# UserModelFieldTest
# ---------------------------------------------------------------------------

@pytest.mark.django_db
class TestUserModelFields:
    """Test User model fields and __str__."""

    def test_email_field(self, passenger):
        assert passenger.email == "passenger@test.com"

    def test_str_returns_email(self, passenger):
        assert str(passenger) == "passenger@test.com"

    def test_username_field_is_email(self):
        assert User.USERNAME_FIELD == "email"

    def test_default_role_is_passenger(self, passenger):
        assert passenger.role == "Passenger"

    def test_image_is_optional(self, passenger):
        assert not bool(passenger.image)  # empty ImageField is falsy

    def test_password_is_hashed(self, passenger):
        # Passwords must never be stored in plain text.
        assert passenger.password != "pass123"

    def test_duplicate_email_raises_error(self, passenger):
        with pytest.raises(Exception):
            User.objects.create_user(
                email="passenger@test.com",  # same email
                password="anotherpass",
                role="Passenger",
            )


# ---------------------------------------------------------------------------
# CreateUserManagerTest
# ---------------------------------------------------------------------------

@pytest.mark.django_db
class TestCreateUserManager:
    """Test CustomUserManager.create_user() for all roles."""

    # --- Passenger ---

    def test_create_passenger(self):
        user = User.objects.create_user(
            email="p@test.com",
            password="pass123",
            role="Passenger",
        )
        assert user.role == "Passenger"
        assert not user.is_staff
        assert not user.is_superuser
        assert user.is_active

    def test_passenger_is_default_when_role_not_passed(self):
        user = User.objects.create_user(
            email="default@test.com",
            password="pass123",
        )
        assert user.role == "Passenger"
        assert not user.is_staff

    # --- Staff ---

    def test_create_staff(self):
        user = User.objects.create_user(
            email="staff@test.com",
            password="pass123",
            role="Staff",
        )
        assert user.role == "Staff"
        assert user.is_staff
        assert not user.is_superuser

    # --- Admin ---

    def test_create_admin(self):
        user = User.objects.create_user(
            email="admin@test.com",
            password="pass123",
            role="Admin",
        )
        assert user.role == "Admin"
        assert user.is_staff
        assert user.is_superuser

    # --- Invalid role ---

    def test_invalid_role_raises_value_error(self):
        with pytest.raises(ValueError, match="Invalid role"):
            User.objects.create_user(
                email="bad@test.com",
                password="pass123",
                role="Ghost",
            )

    # --- Empty email ---

    def test_empty_email_raises_value_error(self):
        with pytest.raises(ValueError, match="Email must be set"):
            User.objects.create_user(email="", password="pass123")

    # --- Email normalization ---

    def test_email_is_normalized(self):
        user = User.objects.create_user(
            email="User@TEST.COM",
            password="pass123",
            role="Passenger",
        )
        assert user.email == "User@test.com"


# ---------------------------------------------------------------------------
# CreateSuperUserTest
# ---------------------------------------------------------------------------

@pytest.mark.django_db
class TestCreateSuperUser:
    """Test CustomUserManager.create_superuser()."""

    def test_create_superuser_success(self):
        admin = User.objects.create_superuser(
            email="super@test.com",
            password="adminpass123",
        )
        assert admin.role == "Admin"
        assert admin.is_staff
        assert admin.is_superuser
        assert admin.is_active

    def test_superuser_str_returns_email(self):
        admin = User.objects.create_superuser(
            email="super2@test.com",
            password="adminpass123",
        )
        assert str(admin) == "super2@test.com"

    def test_superuser_with_is_staff_false_raises_error(self):
        with pytest.raises(ValueError, match="is_staff=True"):
            User.objects.create_superuser(
                email="bad1@test.com",
                password="adminpass123",
                is_staff=False,
            )

    def test_superuser_with_is_superuser_false_raises_error(self):
        with pytest.raises(ValueError, match="is_superuser=True"):
            User.objects.create_superuser(
                email="bad2@test.com",
                password="adminpass123",
                is_superuser=False,
            )

    def test_superuser_with_non_admin_role_raises_error(self):
        with pytest.raises(ValueError, match="Admin"):
            User.objects.create_superuser(
                email="bad3@test.com",
                password="adminpass123",
                role="Staff",
            )

    def test_superuser_password_is_hashed(self):
        admin = User.objects.create_superuser(
            email="hash@test.com",
            password="adminpass123",
        )
        assert admin.password != "adminpass123"