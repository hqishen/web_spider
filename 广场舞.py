import requests
import re

url = "http://www.tangdou.com/playlist/view/2685/page/"
def get_video_items(url):
    print("root url:", url)
    response = requests.get(url)
    url_list = re.findall('<h2><a target="tdplayer" href="(.*?)"', response.text, re.S)
    return url_list

def download_video(url):
    response = requests.get(url)
    # try:
    url_video = re.findall("\n\t\t\t\t\t                video:'(.*?)'", response.text, re.S)[0]
    name = re.findall('<div class="title">(.*?)</div>', response.text, re.S)[0]
    write_video(url_video, name)


def write_video(url, name):
    response = requests.get(url)
    with open(name+".mp4", mode='wb') as f:
        f.write(response.content)

if __name__ ==  "__main__":
    for item in range(2, 6):
        urls = get_video_items(url + "{}".format(item))
        for a in urls:
            download_video(a)
        print("download done~~")