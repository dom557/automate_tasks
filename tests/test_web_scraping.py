import unittest
from unittest.mock import MagicMock
from automate_tasks.web_scraping import fetch_html, parse_html

class TestWebScraping(unittest.TestCase):

    def test_fetch_html(self):
        # Mocking the response object
        mock_response = MagicMock()
        mock_response.text = "<html><body><h1>Hello, World!</h1></body></html>"
        with unittest.mock.patch('requests.get', return_value=mock_response):
            html = fetch_html("https://example.com")
            self.assertEqual(html, "<html><body><h1>Hello, World!</h1></body></html>")

    def test_parse_html(self):
        # Example HTML content
        html = """
            <html>
                <body>
                    <div class="article">
                        <h2>Title 1</h2>
                        <p>Content 1</p>
                    </div>
                    <div class="article">
                        <h2>Title 2</h2>
                        <p>Content 2</p>
                    </div>
                </body>
            </html>
        """
        # Test parsing HTML
        parsed_content = parse_html(html, 'div', 'article')
        self.assertEqual(len(parsed_content), 2)
        self.assertEqual(parsed_content[0].find('h2').text, 'Title 1')
        self.assertEqual(parsed_content[1].find('p').text, 'Content 2')

if __name__ == '__main__':
    unittest.main()
