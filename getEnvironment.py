from selenium import webdriver
import asyncio
from pyppeteer import launch

import time


def selenium_html():
    browser = webdriver.Chrome()
    browser.get("http://localhost/")
    time.sleep(100)


async def selenium_html():
    browser = await launch({"headless": False})
    page = await browser.newPage()
    await page.goto("http://localhost/")
    print(1)
    await asyncio.sleep(100)


if __name__ == "__main__":
    asyncio.run(selenium_html())
