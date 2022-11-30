# Scraping Top 10 trending videos from Youtube
- Scrape trending videos on Youtube using selenium

### Import all the required library
- Import WebDriver Manager for Python
- Use install() to get the location used by the manager and pass it to the driver in a service class instance
- Need to pass driver as arguement in other fuction for it to actually work
```
  def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                            options=chrome_options)
  return driver
  ```
 ### Funtion to get videos form youtube
 - Youtube has its own tag called `ytd-video-renderer` that we can parse using selenium to get the datas.

  ```
  def get_videos(driver):
  url = 'https://www.youtube.com/feed/trending'
  driver.get(url)
  videos = driver.find_elements(By.TAG_NAME, "ytd-video-renderer")
  return videos
  ```
  
  ### Parsing Video 
- Getting the title, url, thumbnail url, channel name, views, date, and the video description.
- 
```
  def parse_video(video):
  title_tag = video.find_element(By.ID, 'video-title')
  title = title_tag.text
  url = title_tag.get_attribute('href')
  thumbnail_tag = video.find_element(By.TAG_NAME, 'img')
  thumbnail_url = thumbnail_tag.get_attribute('src')
  channel_name, views, date_uploaded = video.find_element(
    By.CLASS_NAME, "style-scope ytd-video-meta-block").text.split('\n')
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
  
  ```
