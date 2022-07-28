# ----------------------
# imports
# ----------------------
import requests
import os
from bs4 import BeautifulSoup as bs4
from urllib.request import urlretrieve
from urllib.parse import urlparse

# ----------------------
# Defs
# ----------------------

def get_soup(url):
    return bs4( requests.get(url).text, 'html.parser')

def extractSoup(source: str):
    ''' Extration of informations from a website via soup
    :paramm source : site used on scraping

    : return: site parser
    '''
    return bs4(source, 'html.parser')


def downloadFileUrl(urlPath, filename):
    ''' Execute the file download via urlretrieve
        :urlPath : link to the file
        :filename : name for save the file on disk
        : return: site parser
        '''
    urlretrieve(urlPath, filename)

# ----------------------
# Accesing  site
# ----------------------
# defining the url
path = 'C:\\Users\\bruce.DESKTOP-U0NC12D\\Documents\\Python'
url = "https://open.canada.ca/data/en/dataset/90fed587-1364-4f33-a9ee-208181dc0b97"

# ----conf headers
headers = {
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'pt-BR,pt;q=0.9'
}
response = requests.get(url, headers=headers)

# Extrat the texts fom site returning the tag/id
html = extractSoup(response.text)


# ===========================
# Scraping the site
# ===========================
listlinks = []

# Get the links and structure to generate the dowload list
for link in get_soup(url).find_all('a', class_='btn btn-primary btn-sm resource-url-analytics'):
    file_link = link.get('href')
    listlinks.append(file_link)


# Start the numerator
i = 0
# Downloading the files
for item in listlinks:

    parse = urlparse(item)
    file = os.path.basename(parse.path)
    num = str(file).rfind('.')
    fileNameCsv = ''.join([file[0:num] , '_' , str(i),file[num:num+5]])

    i = i + 1
    print(str(fileNameCsv))
    #Conditional top remofe french files and download the files
    if '_fr' in(str(file)) or '_FR' in(str(file)) :
         print('french')
    else:
         try:
            downloadFileUrl(item, fileNameCsv.rstrip())
         except Exception:
             print('Error')