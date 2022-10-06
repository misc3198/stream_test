#lib
import numpy as np
import pandas as pd
import streamlit as st
import datetime as dt
import requests


#user
import def_reqests


def get_all_video(url):
    nextpage = url
    all_video_list = []
    while nextpage != header:
        videolist, nextpage = def_reqests.get_video_list(nextpage)
        nextpage = header + nextpage
        print(nextpage, videolist)
        all_video_list.extend(videolist)
    
    return all_video_list

def form_adjust(videolist):
    columns = ["title", "username", "views", "likes", "date", "comments", "link"]
    DF = pd.DataFrame(videolist, columns = columns)
    DF["views"] = DF["views"].str.replace(",", "").astype(int)
    DF["likes"] = DF["likes"].str.replace(",", "").astype(int)
    DF["link"] = header + DF["link"]
    
    return DF

st.title("iwara video scanner(beta)")



st.sidebar.write("menu")


left_column, mid_column, right_column = st.columns(3)

mode = left_column.selectbox("search_mode", ["general", "ecchi"])
if mode == "general": header = "https://www.iwara.tv/"
if mode == "ecchi" : header = "https://ecchi.iwara.tv/"


now = dt.date.today()
year = int(now.strftime("%Y")) + 1
year = mid_column.selectbox("year", list(reversed(range(2014, year))))
month = right_column.selectbox("month", list(range(1,13)))

url_0 = "search?f[0]=type:video"
url_1 = f"&f[1]=created:{year}-{month}"
url = header + url_0 + url_1

if st.checkbox("category scan"):
    category = {\
            "Azur Lane":"31263",\
            "Genshin Impact":"31264",\
            "Hololive":"31265",\
            "Honey Select":"16104",\
            "iDOLM@STER":"33",\
            "KanColle":"1",\
            "Original Character":"34",\
            "Other":"2",\
            "Source FilmMaker":"16105",\
            "Virtual Youtuber":"16190",\
            "Vocaloid":"6",\
            "Windows 100%":"8"        
            }
    
    cat = st.selectbox("category", list(category.keys()))
    cat_number = category.get(cat)
    url_2 = f"&f[2]=field_categories:{cat_number}"
    url = url + url_2

button = st.button("Scan start")
if button:
    
    st.write(url)
    all_video_list = get_all_video(url)
    DF = form_adjust(all_video_list)
    st.dataframe(DF, width = 1500, height = 600)
    st.download_button('Download csv',\
        data = DF.to_csv(index = False).encode("utf-8_sig"),\
        file_name="data.csv",\
        mime="text_csv")

