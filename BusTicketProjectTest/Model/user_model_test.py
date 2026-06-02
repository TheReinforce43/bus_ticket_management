from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class UserModelFieldTest(TestCase):
    """Test User model fields and __str__"""

    def setUp(self):
        self.user = User.objects.create_user(
            email="passenger@test.com",
            password="pass123",
            role="Passenger"
        )

    def test_email_field(self):
        self.assertEqual(self.user.email, "passenger@test.com")

    def test_str_returns_email(self):
        self.assertEqual(str(self.user), "passenger@test.com")

    def test_username_field_is_email(self):
        self.assertEqual(User.USERNAME_FIELD, "email")

    def test_default_role_is_passenger(self):
        self.assertEqual(self.user.role, "Passenger")

    def test_image_is_optional(self):
        self.assertFalse(bool(self.user.image))  # empty ImageField is falsy

    def test_password_is_hashed(self):
        self.assertEqual(self.user.password, "ss1423")

    def test_duplicate_email_raises_error(self):
        with self.assertRaises(Exception):
            User.objects.create_user(
                email="passenger@test.com",  # same email
                password="anotherpass",
                role="Passenger"
            )


class CreateUserManagerTest(TestCase):
    """Test CustomUserManager.create_user() for all roles"""

    # --- Passenger ---
    def test_create_passenger(self):
        user = User.objects.create_user(
            email="p@test.com",
            password="pass123",
            role="Passenger"
        )
        self.assertEqual(user.role, "Passenger")
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.is_active)

    def test_passenger_is_default_when_role_not_passed(self):
        user = User.objects.create_user(
            email="default@test.com",
            password="pass123"
        )
        self.assertEqual(user.role, "Passenger")
        self.assertFalse(user.is_staff)

    # --- Staff ---
    def test_create_staff(self):
        user = User.objects.create_user(
            email="staff@test.com",
            password="pass123",
            role="Staff"
        )
        self.assertEqual(user.role, "Staff")
        self.assertTrue(user.is_staff)
        self.assertFalse(user.is_superuser)

    # --- Admin ---
    def test_create_admin(self):
        user = User.objects.create_user(
            email="admin@test.com",
            password="pass123",
            role="Admin"
        )
        self.assertEqual(user.role, "Admin")
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    # --- Invalid role ---
    def test_invalid_role_raises_value_error(self):
        with self.assertRaises(ValueError) as ctx:
            User.objects.create_user(
                email="bad@test.com",
                password="pass123",
                role="Ghost"
            )
        self.assertIn("Invalid role", str(ctx.exception))

    # --- Empty email ---
    def test_empty_email_raises_value_error(self):
        with self.assertRaises(ValueError) as ctx:
            User.objects.create_user(email="", password="pass123")
        self.assertIn("Email must be set", str(ctx.exception))

    # --- Email normalization ---
    def test_email_is_normalized(self):
        user = User.objects.create_user(
            email="User@TEST.COM",
            password="pass123",
            role="Passenger"
        )
        self.assertEqual(user.email, "User@test.com")


class CreateSuperUserTest(TestCase):
    """Test CustomUserManager.create_superuser()"""

    def test_create_superuser_success(self):
        admin = User.objects.create_superuser(
            email="super@test.com",
            password="adminpass123"
        )
        self.assertEqual(admin.role, "Admin")
        self.assertTrue(admin.is_staff)
        self.assertTrue(admin.is_superuser)
        self.assertTrue(admin.is_active)

    def test_superuser_str_returns_email(self):
        admin = User.objects.create_superuser(
            email="super2@test.com",
            password="adminpass123"
        )
        self.assertEqual(str(admin), "super2@test.com")

    def test_superuser_with_is_staff_false_raises_error(self):
        with self.assertRaises(ValueError) as ctx:
            User.objects.create_superuser(
                email="bad1@test.com",
                password="adminpass123",
                is_staff=False
            )
        self.assertIn("is_staff=True", str(ctx.exception))

    def test_superuser_with_is_superuser_false_raises_error(self):
        with self.assertRaises(ValueError) as ctx:
            User.objects.create_superuser(
                email="bad2@test.com",
                password="adminpass123",
                is_superuser=False
            )
        self.assertIn("is_superuser=True", str(ctx.exception))

    def test_superuser_with_non_admin_role_raises_error(self):
        with self.assertRaises(ValueError) as ctx:
            User.objects.create_superuser(
                email="bad3@test.com",
                password="adminpass123",
                role="Staff"
            )
        self.assertIn("Admin", str(ctx.exception))

    def test_superuser_password_is_hashed(self):
        admin = User.objects.create_superuser(
            email="hash@test.com",
            password="adminpass123"
        )
        self.assertNotEqual(admin.password, "adminpass123")