import unittest
from app import app


class TestCalculationsIntegration(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_calculation_integration(self):
        response = self.client.post("/", data={"a": "8", "b": "2"})
        html = response.data.decode("utf-8")

        self.assertIn("Sum: 10.0", html)
        self.assertIn("Difference: 6.0", html)
        self.assertIn("Product: 16.0", html)
        self.assertIn("Quotient: 4.0", html)


if __name__ == "__main__":
    unittest.main()
