import requests, bs4,webbrowser, re
from selenium import webdriver

urls= open("H:\GoogleDrive\Computer\Python\urls_phi48.txt", "r") 
outF= open("H:\GoogleDrive\Computer\Python\urlsNotFound_phi48.txt", "a") 
for url in urls:
    res = requests.get(url)
    if res.status_code != requests.codes.ok:
        print('{0} is a broken link. Response: 404 Not Found'.format(url))
        outF.write('{0} is a broken link. Response: 404 Not Found'.format(url)) 
        outF.write("\n")
outF.close()




