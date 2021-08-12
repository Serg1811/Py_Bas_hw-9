from pprint import pprint
import requests

class YaUploader:
     API_BASE_URL = 'https://cloud-api.yandex.net/'
     def __init__(self, token: str):
          self.token = token
          self.headers = {'Accept': 'application/json', 'Authorization': f'OAuth {self.token}'}
     def upload(self, file_path: str):
          """Метод загружает файл 'file_path' на яндекс диск"""
          resp = requests.get(self.API_BASE_URL + 'v1/disk/resources/upload', params={'path': file_path}, headers=self.headers)
          print(resp)
          upload_url = resp.json()['href']
          resp = requests.put(upload_url, headers=self.headers, files={"file": open(file_path, 'rb')})
          return print(resp.status_code)



if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = '1.jpeg'
    # TOKEN = 'Ваш токен'
    with open('token.txt', encoding='utf-8') as f:
         TOKEN = f.read()
    uploader = YaUploader(TOKEN)
    result = uploader.upload(path_to_file)


