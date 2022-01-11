
import unittest

from unittest import mock
from unittest.mock import MagicMock, patch

from simple_espn_fantasy_football import EspnFantasyFootball


class EspnFantasyFootballTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_espn_ff = EspnFantasyFootball(swid='test', espn_s2='test', league_id=123456)

    def test_get_new_url_view_data(self):
        with patch('requests.get') as mock_get:
            mock_request = MagicMock()
            mock_request.json.return_value = {'gameDetails': True}
            mock_get.return_value = mock_request
            test_new_url_data = self.test_espn_ff.get_view_data(year=2021, param='test')
            self.assertTrue(test_new_url_data['gameDetails'])

    @mock.patch('requests.get', side_effect=MagicMock())
    def test_get_old_url_view_data(self, mock_get):
        with patch('requests.get') as mock_get:
            mock_request = MagicMock()
            mock_request.json.return_value = [{'gameDetails': True}]
            mock_get.return_value = mock_request
            test_new_url_data = self.test_espn_ff.get_view_data(year=2013, param='test')
            self.assertTrue(test_new_url_data['gameDetails'])

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()
