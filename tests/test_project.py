import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "index.html",
    "login.html",
    "register.html",
    "admin/dashboard.html",
    "admin/products.html",
    "admin/users.html",
    "admin/categories.html",
    "admin/reports.html",
    "user/dashboard.html",
    "user/products.html",
    "user/add-product.html",
    "user/product-details.html",
    "user/service-history.html",
    "user/documents.html",
    "user/analytics.html",
    "user/expiring.html",
    "user/settings.html",
    "css/style.css",
    "js/script.js",
]


class TestWarrantyVault(unittest.TestCase):

    def test_required_files_exist(self):
        for relative_path in REQUIRED_FILES:
            with self.subTest(relative_path=relative_path):
                self.assertTrue((ROOT / relative_path).is_file())

    def test_stylesheet_is_nonempty(self):
        css = ROOT / "css/style.css"
        self.assertGreater(css.stat().st_size, 0)

    def test_javascript_is_nonempty(self):
        js = ROOT / "js/script.js"
        self.assertGreater(js.stat().st_size, 0)

    def test_index_has_html_structure(self):
        content = (ROOT / "index.html").read_text(encoding="utf-8").lower()
        self.assertIn("<html", content)
        self.assertIn("<body", content)
        self.assertIn("</html>", content)


    def test_html_pages_have_body(self):
        html_files = list(ROOT.rglob("*.html"))
        for html_file in html_files:
            with self.subTest(html_file=html_file):
                content = html_file.read_text(encoding="utf-8").lower()
                self.assertIn("<body", content)

    def test_html_pages_have_title(self):
        html_files = list(ROOT.rglob("*.html"))
        for html_file in html_files:
            with self.subTest(html_file=html_file):
                content = html_file.read_text(encoding="utf-8").lower()
                self.assertIn("<title", content)


if __name__ == "__main__":
    unittest.main(verbosity=2)
