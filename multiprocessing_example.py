import multiprocessing
import os

import bs4
import requests

from normalize_image_url import normalize_image_url


def download_image(url, save_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
    else:
        print("Не удалось открыть страницу")


def scrape_images(url, save_dir, domain):
    lst = list()
    response = requests.get(url)
    if response.status_code == 200:
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        img_tags = soup.select('img')
        for img_tag in img_tags:
            img_url = img_tag.attrs['src']
            img_name = img_url.split('/')[-1]
            img_url = normalize_image_url(img_url, domain)
            save_path = os.path.join(save_dir, img_name)
            lst.append((img_url, save_path))
            multiprocessing.Process(target=download_image, args=(img_url, save_path)).start()


if __name__ == "__main__":
    page_url = input("Введите адрес страницы: ")
    page_domain = input("Введите домен: ")
    save_directory = input("Введите название папки для сохранения изображений: ")
    os.makedirs(save_directory, exist_ok=True)
    scrape_images(page_url, save_directory, page_domain)
