#python -m pip install requests
#=> get data from web (html,json,xml)
#python -m pip install beautifulsoup4
#=>prase html

#go to git bash
#git config --global user.name "shreeya shakya"
#git config --global.email "shreya.shakya2064@gmail.com"

#git init
#git status => if you wany to check what are the status of files
#git diff => if you want to check what are the changes
#git add .
#git commit -m "your message"
#copy paste git code from git hub

###########################
# 1. change the ccode
# 2. git add .
# 3. git commit -m "your message"
# 4. git push
###########################



import requests
import json
import csv


from bs4 import BeautifulSoup



#URL of the website to scrape
url ="http://books.toscrape.com/" 



def scrape_books(url):
    response = requests.get(url)
    print(response)


scrape_books(url)

def scrape_books(url):
    response=requests.get(url)
    if response.status_code !=200:
        return[]
    response.encoding = response.apparent_encoding

    all_books=[]
    soup= BeautifulSoup(response.text,"html.parser")
    books=soup.find_all('article',class_='product_pod')
    for book in books:
        title=book.h3.a['title']
        price_text=book.find("p",class_="price_color").text
        currency=price_text[0]
        price=float(price_text[1:])

        all_books.append(
            {
                "title":title,
                "currency":currency,
                "price":price
            }
        )
    return all_books


books=scrape_books(url)

with open("books.json",'w',encoding="utf-8") as f:
   
    json.dump (books,f ,indent=4,ensure_ascii=False) 

with open("books.csv",'w',encoding="utf-8",newline="") as f:
    writer=csv.DictWriter(f,fieldnames=["title","currency",'price'])
    writer.writeheader()
    writer.writerows(books)






