import requests
from bs4 import BeautifulSoup

def get_video_list(url):
    print(url)
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    
    video_master = soup.select_one(".view-content")
    videos = video_master.select(".views-column")
    
    videolist = []
    for video in videos:
        title = video.select_one(".title a").text
        username = video.select_one(".username").text
        info = video.select_one(".video-info").text
        views = info.split(" ")[1].replace("\t", "")
        likes = info.split(" ")[2].replace("\t", "")
        date = str(video.select_one(".submitted"))[-22:-6]
        try:
            comments = video.select_one("p").text
        except:
            comments = ""
        link = video.select_one(".title a").attrs["href"]
        
        videolist.append([title, username, views, likes, date, comments, link])
        
    try: 
        nextpage = soup.select_one(".pager-next a").attrs["href"]
    except:
        nextpage = ""
        
    return videolist, nextpage
