import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def ya_headers(self):
        return {
            'Content-type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def create_folder(self, path):
        return requests.put(f'{"https://cloud-api.yandex.net/v1/disk/resources/"}?path={path}', headers=self.ya_headers())
    def get_link_ya(self,adres_disk_file):
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.ya_headers()
        params = {"path":adres_disk_file, "overwrite": "true"}
        response = requests.get(url, headers=headers, params=params)
        return response.json()

    def upload(self, file_name):
        href = self.get_link_ya(adres_disk_file="test/"+file_name).get("href", "")
        print(href)
        response = requests.put(href, data=open(file_name, 'rb'))
        response.raise_for_status()
        return response.status_code

if __name__ == '__main__':
    token = "TOKEN"
    uploader = YaUploader(token)
    result = uploader.create_folder("ZXC")
    print(str(result))
