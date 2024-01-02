import requests
from bs4 import BeautifulSoup

def scrape_news_headLine(url):
    response=requests.get(url)

    if response.status_code==200:
        soup=BeautifulSoup(response.text,'html.parser')
        headlines=soup.find_all("h2",class_='headline')

        for index,headline in enumerate(headlines,start=1):
            print(f"{index}.{headline.text}")
    else:
        print(f"Failed to scrape data .Status Code:{response.status_code}")

if __name__=="__main__":
    new_url="https://3news.com/category/politics"
    scrape_news_headLine(new_url)