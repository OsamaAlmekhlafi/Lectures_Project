# *BY Osama Abdo Modhish*

import requests
from bs4 import BeautifulSoup
import re

url = " https://www.youtube.com/watch?v=KIynZtAzmHc"


response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
script_tags = soup.find_all('script')


video_url = ''
for script_tag in script_tags:
    if 'streamingData' in str(script_tag):
        match = re.search(r'"adaptiveFormats":\[(.*?)\]', str(script_tag))
        if match:
            data = match.group(1)
            video_url_match = re.search(r'"url":"(.*?)"', data)
            if video_url_match:
                video_url = video_url_match.group(1)
                break


if video_url:
    video_response = requests.get(video_url)

    file_name = "video.mp4"  
    with open(file_name, 'wb') as file:
        file.write(video_response.content)
        print("Video downloaded successfully!")
else:
    print("Video URL not found.")
