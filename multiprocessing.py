import requests
import bs4
import threading
import os

def download_image(url, save_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)


def scrape_images(url, save_dir):
    response = requests.get(url)
    if response.status_code == 200:
        soup = bs4.BeautifulSoup(response.content, 'html.parser')
        img_tags = soup.find_all('img')

        for img_tag in img_tags:
            img_url = img_tag.get('src')
            if img_url and img_url.startswith('http'):
                img_name = img_url.split('/')[-1]
                save_path = os.path.join(save_dir, img_name)
                threading.Thread(target=download_image, args=(img_url, save_path)).start()

page_url = input("Введите адрес страницы: ")
save_directory = input("Введите название папки для сохранения изображений: ")
os.makedirs(save_directory, exist_ok=True)
scrape_images(page_url, save_directory)