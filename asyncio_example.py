import asyncio
import os

import aiohttp
import bs4

from normalize_image_url import normalize_image_url


async def download_image(session, url, save_path):
    async with session.get(url) as response:
        with open(save_path, 'wb') as file:
            while True:
                chunk = await response.content.read(1024)
                if not chunk:
                    break
                file.write(chunk)


async def scrape_images(url, save_dir, domain):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text()
            soup = bs4.BeautifulSoup(html, 'html.parser')
            img_urls = soup.find_all('img')
            tasks = []
            for img_url in img_urls:
                image_url = normalize_image_url(img_url['src'], domain)
                save_path = os.path.join(save_dir, os.path.basename(image_url))
                tasks.append(asyncio.create_task(download_image(session, image_url, save_path)))
        await asyncio.gather(*tasks)


page_url = input("Введите адрес страницы: ")
domain = input("Введите домен: ")
save_directory = input("Введите название папки для сохранения изображений: ")
os.makedirs(save_directory, exist_ok=True)
asyncio.run(scrape_images(page_url, save_directory, domain))
