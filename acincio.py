import os
import asyncio
import bs4
import aiohttp

async def download_image(session, url, save_path):
    async with session.get(url) as response:
        with open(save_path, 'wb') as file:
            while True:
                chunk = await response.content.read(1024)
                if not chunk:
                    break
                file.write(chunk)

async def scrape_images(url, save_dir):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text()
            soup = bs4.BeautifulSoup(html, 'html.parser')
            img_urls = soup.find_all('img')
            tasks = []
            for img_url in img_urls:
                image_url = img_url['src']
                save_path = os.path.join(save_dir, os.path.basename(image_url))
                tasks.append(asyncio.create_task(download_image(session, image_url, save_path)))

        await asyncio.gather(*tasks)

page_url = input("Введите адрес страницы: ")
save_directory = input("Введите название папки для сохранения изображений: ")
os.makedirs(save_directory, exist_ok=True)