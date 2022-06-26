import requests
import json
from open_file import read_my_token
import os

class VkDownloader :
    """
    Class VkDownloader dowloads profile photoes to local folder (/var/tmp/vk_temp by default)
    You can delete file after dowloading by initializing class object with is_saved=False
    """
    def __init__(self, user_id, directory, is_saved=True) :
        self.user_id = user_id
        self.is_saved = is_saved
        self.directory = directory
    

    def _check_local_directory(self, folder) :
        try :
            if not os.path.exists(folder) :
                os.mkdir(folder)
                print(f"Temporaly directory {folder} has been created")
        except Exception as ex :
            print(ex)
            return

    def _get_photo(self) :
        self.__token = read_my_token("vk")
        url = "https://api.vk.com/method/photos.get"
        params = {
            "user_ids" : self.user_id,
            "album_id" : "profile",
            "extended" : "1",
            "access_token" : self.__token,
            "v" : "5.131"
        }
        try :
            response = requests.get(url, params=params)
            return response
        except Exception as ex :
            print(ex)


    def _dump_json_to_file(self, data) :
        data_to_json = {"result" : data}
        with open("photoes_info.json", "w") as file :
            json.dump(data_to_json, file)
        print("Photoes descriptions have been saved to photoes_info.json")


    def dowload(self) :
        self._check_local_directory(self.directory)
        photo_list = self._get_photo().json()['response']["items"]
        name_photo = []
        self.return_list = []
        for photo in photo_list :
            name = f"{photo['likes']['count']}.jpg"
            date = photo['date']
            if name not in name_photo :
                name_photo.append(name)
            else :
                name_photo.append(name)
                name = f"{name}_{date}"

            url = ""
            max_size = 0
            size = ""
            for obj in photo['sizes'] :
                sum_size = int(obj['height']) + int(obj['width'])
                if sum_size > max_size :
                    max_size = sum_size
                    size =f"{obj['height']}x{obj['width']}"
                    url = obj['url']
            self.return_list.append({"file_name" : name, "size" : size})
            download_link = requests.get(url)
            print(f"{name} is dowloading to {self.directory}")
            with open(f"{self.directory}{name}", "wb") as file:
                file.write(download_link.content)
                print(f"{name} has been saved to {self.directory}")
        self._dump_json_to_file(self.return_list)
        return self.return_list




if __name__ == '__main__':
    vk = VkDownloader("begemot_korovin")
    print(vk.dowload())
