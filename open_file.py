
import os
from exceptions import OpenTokenErrors


def read_my_token(site_id : str, path="./") -> str :
    """
    This function opens and reads token from file
    Tokens must be saved in the same folder and contains token and site id in the file name
    default folder is local
    """

    if "yandex" == site_id.lower() or "vk" == site_id.lower() :
        is_file_exist = False
        for file in os.listdir(path) :
            if site_id in file and "token" in file :
                is_file_exist = True
                with open(f"{path}{file}", "r") as f :
                    token = f.read().strip()
                    print(f"Token for {site_id} has been readed")
                    return token
        if is_file_exist is False :
            raise OpenTokenErrors(f"There are no tokens for yandex or vk in the folder = {path}")
    else :
        raise OpenTokenErrors("There are must be yandex or vk as a site_id")





if __name__ == '__main__':
    print(read_my_token("vk"))
