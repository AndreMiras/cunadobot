import json
from unittest import mock
import gspread

import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_main(self):
        m_settings = mock.Mock()
        m_settings.CREDENTIALS_FILE = "/tmp/credentials.json"
        json_content = {
            'type': 'service_account',
            'client_email': 'foo@bar.com',
            'private_key': '',
            'private_key_id': '',
            'client_id': '',
        }
        with open(m_settings.CREDENTIALS_FILE, 'w') as f:
            f.write(json.dumps(json_content))
        with \
                mock.patch.dict('sys.modules', settings=m_settings), \
                self.assertRaises(gspread.exceptions.APIError) as e:
            import cunao
        self.assertTrue('insufficientPermissions' in str(e.exception))
        self.assertFalse('Foo'.isupper())

if __name__ == '__main__':
    unittest.main()
