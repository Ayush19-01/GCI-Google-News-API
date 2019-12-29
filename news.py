from newsapi import NewsApiClient
import time
newsapi = NewsApiClient(api_key='6ccb142565e249ccb935e1ee6572e9e8')
def getnews(query):
       all_articles = newsapi.get_everything(q=query,sort_by='publishedAt',page=1,language="en")
       all_articles=all_articles['articles']
       x=1
       for i in all_articles:
              tmpstr = ""
              author=i["author"]
              title=i["title"]
              date=i["publishedAt"]
              date=date[:9]
              url=i["url"]
              try:
                  tmpstr+=str(x)+") "+"Title: "+title+"\n    Author: "+author+"\n    "+"Published On: "+date+"\n    "+"URL: "+url
                  x+=1
              except:
                     print("Insufficient Data!")

              print(tmpstr)
              print("")
              print("")
              time.sleep(1.5)
       print("End of news!")
       print("")
       print("")
while True:
       print("Welcome to the Google News API service")
       print("Choose from the following topic of news\n    1)Linux\n    2)Open-Source\n    3)Android\n    4)Exit from the service")
       choice=int(input("Enter your choice:"))
       if choice==1:
           print("")
           print("News on the topic Linux:\n")
           getnews("Linux")
       if choice==2:
           print("")
           print("News on the topic Open-Source:\n")
           getnews("Open-Source")
       if choice==3:
           print("")
           print("News on the topic Android:\n")
           getnews("Android")
       if choice>3:
              print("")
              print("Closing...")
              break
