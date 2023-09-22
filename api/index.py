from imgurpython import ImgurClient
import os
from datetime import datetime


def upload(client_data, local_img_file, album , name = 'test-name!' ,title = 'test-title' ):
    config = {
        'album':  album,
        'name': name,
        'title': title,
        'description': f'test-{datetime.now()}'
    }

    print("Uploading image... ")
    image = client_data.upload_from_path(local_img_file, config=config, anon=False)
    print("Done")

    return image


def delete(client_data, image = "9PHXMJh"):

    print("Delete image... ")
    is_deleted = client_data.delete_image(image)
    print("Done")

    return is_deleted

if __name__ == "__main__":
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')
    access_token = os.getenv('ACCESS_TOKEN')
    refresh_token = os.getenv('REFRESH_TOKEN')
    album = os.getenv('ALBUM')
    local_img_file = os.getenv('LOCAL_IMG_FILE')
    
    client = ImgurClient(client_id, client_secret, access_token, refresh_token)

    # ========== upload image =============
    # image = upload(client, local_img_file, album)
    # print(f"圖片網址: {image['link']}")

    # delete image
    # is_deleted = delete(client)
    # if is_deleted:
    #     print("Delete Success")