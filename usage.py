from utils import *
import requests
from urllib.request import urlretrieve
from tqdm import tqdm
import os

def get_all_slides(url, filter_mark=''):
    h5 = requests.get(url).text 
    links = get_all_extension(h5, '.pdf', filter_mark=filter_mark, raw_url=url)
    return links

def download_them(urls, folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
    for url in urls:
        # download
        file_name = os.path.join(newpath, os.path.basename(url))
        urlretrieve(url, file_name)

def record_them(urls, filename):
    with open(filename, 'w') as handle:
        for url in urls: 
            handle.write(url+'\n')

if __name__ == "__main__":
    url = input('give me the url:\n') 
    filter_mark = input('optionally give me a filter marker\n')
    will_down = input('do you want to download them? (y/n)')
    will_down = will_down.lower() != 'n'

    links = get_all_slides(url, filter_mark=filter_mark)

    
    if will_down:
        download_them(links, folder)
        print("download completed!")
    else:
        record_them(links, 'links.txt')
        print("links saved to ./links.txt")
