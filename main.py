# Scrape top 10 trending videos on YouTube using Selenium

## importing libraries
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

## Path for the driver in case
path = "C:\Program Files (x86)\chromedriver.exe"


## Function to get the driver for selenium


def get_driver():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                    options=chrome_options)
    return driver


def get_videos(driver):
    url = 'https://www.youtube.com/feed/trending'
    driver.get(url)
    videos = driver.find_elements(By.TAG_NAME, "ytd-video-renderer")
    return videos


def parse_video(video):
    title_tag = video.find_element(By.ID, 'video-title')
    title = title_tag.text
    url = title_tag.get_attribute('href')
    thumbnail_tag = video.find_element(By.TAG_NAME, 'img')
    thumbnail_url = thumbnail_tag.get_attribute('src')
    channel_name = video.find_element(
        By.CLASS_NAME, "style-scope ytd-video-meta-block").text.split('\n')[0]
    views = video.find_element(
        By.CLASS_NAME, "style-scope ytd-video-meta-block").text.split('\n')[1]
    date_uploaded = video.find_element(
        By.CLASS_NAME, "style-scope ytd-video-meta-block").text.split('\n')[2]
    description = video.find_element(By.ID, 'description-text').text
    return {
        'title': title,
        'url': url,
        'thumbnail_url': thumbnail_url,
        'channel_name': channel_name,
        'views': views,
        'date': date_uploaded,
        'description': description
    }


if __name__ == "__main__":
    print('Creating Driver...')
    driver = get_driver()
    print('Success!!!')
    print('Fetching the page...')
    videos = get_videos(driver)
    print(f"found {len(videos)} videos")
    videos_data = [parse_video(video) for video in videos[:10]]
    print('Saving data to CSV...')
    videos_df = pd.DataFrame(videos_data)
    print(videos_df)
    videos_df.to_csv('trending.csv', index=None)
