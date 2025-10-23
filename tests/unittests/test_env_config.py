import os
import unittest
from importlib import reload
from unittest.mock import patch

from pydantic import ValidationError

# Set the environment to 'test' before importing the config module.
# This ensures that the Settings object is configured to
# use the .env.test file.
os.environ["ENVIRONMENT"] = "test"
from src.config import config  # noqa: E402


class TestEnvironmentConfig(unittest.TestCase):
    """
    Test suite for environment configuration settings.

    This class tests the behavior of the Settings class and the get_settings
    function, ensuring that configuration is loaded, validated, and served
    correctly.
    """

    def setUp(self):
        """
        Set up a controlled environment for each test.

        This method patches the environment variables and reloads the config
        module to ensure that each test runs with a fresh configuration.
        """
        self.valid_settings = {
            "APP_NAME": "Test App",
            "PORT": "8080",
            "DEBUG": "True",
            "DATABASE_URI": "postgresql://test:test@localhost:5432/testdb",
            "JWT_SECRET": "a" * 32,
            "JWT_EXPIRY_SECONDS": "60",
            "ENVIRONMENT": "test",
        }
        self.patcher = patch.dict(os.environ, self.valid_settings, clear=True)
        self.patcher.start()
        reload(config)

    def tearDown(self):
        """
        Clean up the environment after each test.

        This method stops the patcher and resets the cached settings instance.
        """
        self.patcher.stop()
        config._settings = None

    def test_singleton_pattern(self):
        """
        Verify that get_settings() always returns the same Settings instance.

        This test confirms that the configuration is loaded only once, adhering
        to the singleton pattern.
        """
        settings_instance_1 = config.get_settings()
        settings_instance_2 = config.get_settings()
        self.assertIs(settings_instance_1, settings_instance_2)

    def test_dependency_injection(self):
        """
        Test the get_settings() function as a dependency injector.

        This test ensures that get_settings() successfully creates and returns
        a valid Settings object based on the patched environment.
        """
        settings = config.get_settings()
        self.assertIsInstance(settings, config.Settings)
        self.assertEqual(settings.APP_NAME, self.valid_settings["APP_NAME"])

    def test_jwt_secret_key_validation(self):
        """
        Test that a short JWT_SECRET_KEY raises a validation error.

        Pydantic should enforce the minimum length constraint defined in the
        Settings model.
        """
        invalid_settings = self.valid_settings.copy()
        invalid_settings["JWT_SECRET"] = "short-secret"
        with patch.dict(os.environ, invalid_settings, clear=True):
            with self.assertRaises(ValidationError):
                config.Settings()

    def test_jwt_expiry_validation(self):
        """
        Test that a non-positive JWT_EXPIRY_SECONDS raises a validation error.

        Pydantic should enforce that the value is greater than zero.
        """
        invalid_settings = self.valid_settings.copy()
        invalid_settings["JWT_EXPIRY_SECONDS"] = "0"
        with patch.dict(os.environ, invalid_settings, clear=True):
            with self.assertRaises(ValidationError):
                config.Settings()

    def test_port_validation(self):
        """
        Test that an out-of-range port number raises a validation error.

        Pydantic should enforce that the port is within the valid range
        (1-65535).
        """
        invalid_settings = self.valid_settings.copy()
        invalid_settings["PORT"] = "70000"
        with patch.dict(os.environ, invalid_settings, clear=True):
            with self.assertRaises(ValidationError):
                config.Settings()


if __name__ == "__main__":
    unittest.main()
