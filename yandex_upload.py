
import requests
import json
from open_file import read_my_token
from exceptions import YandexErrors


class YaUploader:
    def __init__(self, current_file_path : str, remote_file_path : str, photoes_to_upload : int):
        self.current_file_path = current_file_path
        self.remote_file_path = remote_file_path
        self.photoes_to_upload = photoes_to_upload
        self.__token = read_my_token("yandex")
        self.URL = 'https://cloud-api.yandex.net/v1/disk/resources'
        self.headers = {
            'Content-Type': 'application/json', 
            'Accept': 'application/json', 
            'Authorization': f'OAuth {self.__token}',
        }


    def _check_yandex_directory(self, folder) :
        response = requests.put(f"{self.URL}?path=%2F{folder.split('/')[1]}%2F{folder.split('/')[2]}", headers=self.headers)
        if response.status_code == 409 :
            raise YandexErrors(f"Please specify another folder. {folder} is exist")
        elif response.status_code == 201 :
            print(f"Folder {folder} has been creted")
            return True
        else :
            raise YandexErrors(f"yandex error - response - {response.content.decode('utf-8')}")


    def _get_files_list(self, current_file_path, photoes_to_upload) :
        with open("photoes_info.json", "r") as json_file :
            files_list = json.load(json_file)["result"]

        sort_func = lambda x : int(x.get("size").split("x")[0]) + int(x.get("size").split("x")[1])
        files_list.sort(key=sort_func, reverse=True)
        return_list = [i.get('file_name') for i in files_list]
        return return_list[: self.photoes_to_upload]


    def _get_temp_link(self, current_file_path, remote_file_path) :
        self._folder = remote_file_path + current_file_path.split("/")[-1]
        try :
            responce = requests.get(f'{self.URL}/upload?path={self._folder}&overwrite=True', headers=self.headers).json()
            return responce
        except :
            print(f"Error during getting temp link {self.responce}")
            

    def upload(self) :
        if self._check_yandex_directory(self.remote_file_path) :
            for file in self._get_files_list(self.current_file_path, self.photoes_to_upload) :
                with open(f"{self.current_file_path}{file}", 'rb') as f:
                    try:
                        requests.put(self._get_temp_link(f"{self.current_file_path}{file}", self.remote_file_path)['href'], files={'file':f})
                    except :
                        print("Error in upload")
                print(f"File {self.current_file_path}{file} has been sucessfully uploaded to yandex:{self.remote_file_path}")


if __name__ == '__main__':
    ya = YaUploader("/var/tmp/vk_temp/", "/api_test_upload/dowload_vk/", 3)
    # ya.upload()
    print(ya._get_files_list("photoes_info.json", 3))

