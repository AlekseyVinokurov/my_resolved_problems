import requests
url = "https://parsinger.ru/video_downloads/"
response = requests.get(url=url, stream=True)
with open("video.mp4", "wb") as file:
    for chunk in response.iter_content(chunk_size=4096):
        if chunk:
            file.write(chunk)
            file.flush()
            print("\rЗагрузка видео...", end="")
print("\nВидео успешно загружено")
print("Путь к видео: ", file.name)
print("Размер видео: ", file.tell(), "байт")

