import unittest
from unittest.mock import MagicMock
from automate_tasks.email_handling import send_email

class TestEmailHandling(unittest.TestCase):

    def test_send_email(self):
        # Mocking the SMTP server
        mock_server = MagicMock()
        with unittest.mock.patch('smtplib.SMTP') as mock_smtp:
            mock_smtp.return_value = mock_server
            # Test sending email
            send_email(
                sender='sender@example.com',
                recipient='recipient@example.com',
                subject='Test Email',
                body='This is a test email.',
                smtp_server='smtp.example.com',
                smtp_port=587,
                login='user@example.com',
                password='password'
            )
            mock_server.starttls.assert_called()
            mock_server.login.assert_called_with('user@example.com', 'password')
            mock_server.sendmail.assert_called_with(
                'sender@example.com',
                'recipient@example.com',
                unittest.mock.ANY  # We don't need to assert the email content
            )

if __name__ == '__main__':
    unittest.main()
