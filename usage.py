from utils import *
from bs4 import BeautifulSoup
import requests
from urllib.request import urlretrieve
from tqdm import tqdm
import os

def get_all_slides(url, filter_mark=''):
    h5 = requests.get(url).text 
    bsObj = BeautifulSoup(h5, "html.parser")
    links = get_all_extension(bsObj, '.pdf', filter_mark=filter_mark)
    return links

if __name__ == "__main__":
    url = input('give me the url:\n') 
    links = get_all_slides(url, filter_mark='lecture')
    newpath = './target' 
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    for link in tqdm(links):
        # sometimes they use relative url
        file_url = os.path.join(url, link) if ':' not in link[:5] else link

        # download
        file_name = os.path.join(newpath, os.path.basename(file_url))
        urlretrieve(file_url, file_name)
