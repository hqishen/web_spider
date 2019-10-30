import requests
import re

url = "https://www.pearvideo.com/"

def get_video_items(url):
    response = requests.get(url)
    url_list = re.findall("(video_\d{7})", response.text, re.S)
    return url_list

def download_video(url):
    response = requests.get(url)
    url_video = re.findall('srcUrl="(.*?)"', response.text, re.S)[0]
    name = re.findall('<title>(.*?)</title>', response.text, re.S)[0]
    write_video(url_video, name)

def write_video(url, name):
    response = requests.get(url)
    with open(name+".mp4", mode='wb') as f:
        f.write(response.content)

urls = ""
if __name__ ==  "__main__":
    urls = get_video_items(url)
    for a in urls:
        download_video(url+a)
        # write_video(url, name)
