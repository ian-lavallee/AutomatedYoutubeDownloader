# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 15:01:43 2018

@author: Ian55
"""

from selenium import webdriver
import pytube

videos = []
path_to_chromedriver = 'D:\ChromeDriver\chromdriver.exe' # change path as needed
driver = webdriver.Chrome("D:\ChromeDriver\chromedriver.exe")
url = 'https://www.youtube.com'
driver.get("https://www.youtube.com/channel/UC-9-kyTW8ZkZNDHQJ6FgpwQ")
driver.maximize_window()
# driver.find_element_by_link_text("Music").click()
videos = driver.find_elements_by_css_selector("a[id='video-title']")
str(videos[0].get_property("href"))
str(videos[0].get_attribute("href"))
links = []
for i in range (0, 5):
    links = videos[i].get_attribute("href")
    print(links)
    yt = pytube.YouTube(links)
    print("Reached under yt")
    yt = yt.streams.filter(only_audio=True).all()
    print("Reached under yt strreams")
    yt[0].download("D:\Downloads\YoutubeDownloader")
    print("downloaded" + str(i))    
    
    
    
