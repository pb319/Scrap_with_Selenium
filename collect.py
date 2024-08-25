from bs4 import BeautifulSoup
import os
import pandas as pd

df = {"Title":[ ],"Price":[], "Link":[]}

for file in  os.listdir("/home/prasun/GitDemo/Scrap_with_Selenium/Data"):
    try:
        with open(f"/home/prasun/GitDemo/Scrap_with_Selenium/Data/{file}") as f:
            html_doc = f.read()
        soup = BeautifulSoup(html_doc, 'html.parser')

        t1 = soup.find("h2")
        t2 = soup.find("span",class_="a-price-whole")
        
        price = t2.text
        title = t1.get_text()
        link = "https://amazon.in/" + t1.a["href"]

        # print(f"Title: {title} \n\nPrice: {price} \n\nLink:{link} ")
        df["Title"].append(title)
        df["Price"].append(price)
        df["Link"].append(link )

    except Exception as e:
        print(e)

DF = pd.DataFrame(data= df)
DF.to_csv("/home/prasun/GitDemo/Scrap_with_Selenium/data.csv")
 