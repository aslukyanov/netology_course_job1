"""
To do
add logger
ask folder optional
ask if yo want to save
token via property
exceptions
"""


from vk_downloader import VkDownloader
from yandex_upload import YaUploader


def main(vk_id, current_file_path="/var/tmp/vk_temp/", remote_file_path="/api_test_upload/dowload_vk/", photoes_to_upload=5) :
    """This is the main function"""

    vk = VkDownloader(vk_id, current_file_path)
    vk.dowload()

    ya = YaUploader(current_file_path, remote_file_path, photoes_to_upload)
    ya.upload()


if __name__ == '__main__':
    # main("begemot_korovin", "/var/tmp/vk_temp2/", "/api_test_upload/from_vk/", 3)
    main("begemot_korovin")







