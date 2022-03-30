import os
import requests
from pprint import pprint

#Задача №1

class Hero:

    def __init__(self, name):
        self.name = name

    def search_intelligence(self):
        url = f"https://superheroapi.com/api/2619421814940190/search/{self.name}"
        data = requests.get(url)
        return data.json()

    def intelligence_hero(self):
        self.intelligence = int(self.search_intelligence()['results'][0]['powerstats']['intelligence'])
        return self.intelligence

def intelligencest_hero (name_1, name_2, name_3):
    max_intelligence = max(name_1.intelligence_hero(), name_2.intelligence_hero(), name_3.intelligence_hero())
    for i in name_1, name_2, name_3:
        if i.intelligence_hero() == max_intelligence:
            name_intelligencest = i.name
    return f'''Самый умный супергерой {name_intelligencest} = {max_intelligence}'''

Thanos = Hero('Thanos')
Hulk = Hero('Hulk')
Captain_America = Hero('Captain America')

print ('Задача №1')
print(intelligencest_hero(Thanos, Hulk, Captain_America))
print ('-------------')
print ('Задача №2')

#Задача №2

class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    file_name = 'File.txt'
    file_dir = 'Files'
    base_path = os.getcwd()
    path_to_file = os.path.join(base_path,file_dir,file_name)
    token = 
    uploader = YaUploader(token=token)
    result = uploader.upload_file_to_disk(f'{file_name}', path_to_file)
