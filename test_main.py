from app import app
import unittest

class BasicTest(unittest.TestCase):

    def root_test(self):
        response = self.app.get("/", follow_redirects=True)
        self.assertEqual(response.status_code, 200)

breakpoint()
if __name__ == "__main__":
    unittest.main()
