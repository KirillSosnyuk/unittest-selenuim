import unittest
import requests
from parameterized import parameterized
TOKEN = ''


class TestYandexAPI(unittest.TestCase):
    def setUp(self):
        self.headers = {'Authorization': TOKEN}
        self.url = 'https://cloud-api.yandex.net'
        self.resource = '/v1/disk/resources'
        self.response = requests.get(self.url + self.resource, headers=self.headers, params={'path': '/'}).text

    @parameterized.expand(
        [
            'test_dir_1',
            'test_dir_2',
            'test_dir_3'
        ]
    )
    def test_create_folder(self, folder_name):
        result = requests.put(self.url + self.resource, headers=self.headers, params={'path': folder_name})
        etalon = 201
        self.assertEqual(result.status_code, etalon)

    
    @parameterized.expand(
        [
            'test_dir_1',
            'test_dir_2',
            'test_dir_3'
        ]
    )
    @unittest.expectedFailure
    def test_folder_exists(self, folder_name):
        result = [file['name'] for file in self.response["_embedded"]['items']]
        self.assertNotIn(folder_name, result)
