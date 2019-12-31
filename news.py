from newsapi import NewsApiClient
import time
from tkinter import *
apikey=''
newsapi = NewsApiClient(api_key=apikey)
def getnews(query):
    global gl1
    global root2
    root2.destroy()
    all_articles = newsapi.get_everything(q=query,sort_by='publishedAt',page=1,language="en")
    all_articles=all_articles['articles']
    x=1
    for i in all_articles:
        xtmp=[]
        author=i["author"]
        title=i["title"]
        date=i["publishedAt"]
        date=date[:9]
        url=i["url"]

        try:
            title = str(x) + ") Title: " + title
            author="Author: "+author
            date="Published On: "+ date
            url="URL: "+url
            xtmp.append(title)
            xtmp.append(author)
            xtmp.append(date)
            xtmp.append(url)
            x+=1
            gl1.append(xtmp)
        except:
            print("Insufficient Data!")

    gui(query)
def gui(a):
    global root1
    root1 = Tk()
    root1.resizable(0, 0)
    root1.title("News API")
    root1.config(bg="#220047")
    root1.geometry("1300x300")
    label1= Label(root1, text="News on the topic "+a,font=("roboto",30), bg="#220047", fg="#CE9141")
    label1.place(x=460, y=12)
    news1()
    root1.mainloop()
def news1():
    global crsr
    global gl1
    global label2
    global button2
    global button1
    global label3
    global label4
    global label5
    l=len(gl1)
    tmplist=gl1[crsr]
    if crsr==l-1:
        label2 = Label(root1, text=tmplist[0], font=("roboto", 15), bg="#220047", fg="#CE9141")
        label2.place(x=10, y=80)
        label3 = Label(root1, text=tmplist[1], font=("roboto", 15), bg="#220047", fg="#CE9141")
        label3.place(x=41, y=120)
        label4 = Label(root1, text=tmplist[2], font=("roboto", 15), bg="#220047", fg="#CE9141")
        label4.place(x=41, y=160)
        label5 = Label(root1, text=tmplist[3], font=("roboto", 15), bg="#220047", fg="#CE9141")
        label5.place(x=41, y=200)
        button1= Button(root1, text="Back", font=("roboto", 15), bg="#CE9141", fg="#220047",activeforeground="#CE9141",activebackground="#220047")
        button1.bind("<Button-1>", back1)
        button1.place(x=300, y=240)
    if crsr==0:
        label2 = Label(root1, text=tmplist[0], font=("roboto", 15), bg="#220047", fg="#CE9141")
        label2.place(x=10, y=80)
        label3 = Label(root1, text=tmplist[1], font=("roboto", 15), bg="#220047", fg="#CE9141")
        label3.place(x=41, y=120)
        label4 = Label(root1, text=tmplist[2], font=("roboto", 15), bg="#220047", fg="#CE9141")
        label4.place(x=41, y=160)
        label5 = Label(root1, text=tmplist[3], font=("roboto", 15), bg="#220047", fg="#CE9141")
        label5.place(x=41, y=200)
        button2= Button(root1, text="Next", font=("roboto", 15), bg="#CE9141", fg="#220047",activeforeground="#CE9141",activebackground="#220047")
        button2.bind("<Button-1>", next1)
        button2.place(x=400, y=240)
    if 0<crsr<l-1:
        label2 = Label(root1, text=tmplist[0], font=("roboto", 15), bg="#220047", fg="#CE9141")
        label2.place(x=10, y=80)
        label3 = Label(root1, text=tmplist[1], font=("roboto", 15), bg="#220047", fg="#CE9141")
        label3.place(x=41, y=120)
        label4 = Label(root1, text=tmplist[2], font=("roboto", 15), bg="#220047", fg="#CE9141")
        label4.place(x=41, y=160)
        label5 = Label(root1, text=tmplist[3], font=("roboto", 15), bg="#220047", fg="#CE9141")
        label5.place(x=41, y=200)
        button1 = Button(root1, text="Back", font=("roboto", 15), bg="#CE9141", fg="#220047",activeforeground="#CE9141",activebackground="#220047")
        button1.bind("<Button-1>", back2)
        button1.place(x=300, y=240)
        button2 = Button(root1, text="Next", font=("roboto", 15), bg="#CE9141", fg="#220047",activeforeground="#CE9141",activebackground="#220047")
        button2.bind("<Button-1>", next2)
        button2.place(x=400, y=240)
def next1(x):
    global label2
    global button2
    global button1
    global label3
    global label4
    global label5
    global crsr
    crsr += 1
    label2.place_forget()
    label3.place_forget()
    label4.place_forget()
    label5.place_forget()
    button2.place_forget()
    news1()
def back1(x):
    global label2
    global button2
    global button1
    global label3
    global label4
    global label5
    global crsr
    crsr-=1
    label2.place_forget()
    label3.place_forget()
    label4.place_forget()
    label5.place_forget()
    button1.place_forget()
    news1()
def next2(x):
    global label2
    global label3
    global label4
    global label5
    global button2
    global button1
    global crsr
    crsr+=1
    label2.place_forget()
    label3.place_forget()
    label4.place_forget()
    label5.place_forget()
    button1.place_forget()
    button2.place_forget()
    news1()
def back2(x):
    global label2
    global button2
    global button1
    global label3
    global label4
    global label5
    global crsr
    crsr-=1
    label2.place_forget()
    label3.place_forget()
    label4.place_forget()
    label5.place_forget()
    button1.place_forget()
    button2.place_forget()
    news1()
def call1(event):
    quit()
while True:
    gl1 = []
    crsr = 0
    root2 = Tk()
    root2.resizable(0, 0)
    root2.geometry("500x220")
    root2.config(bg="#220047")
    root2.title("API")
    label_1 = Label(root2, text="Google News API", font=("roboto", 30), bg="#220047", fg="#CE9141")
    label_1.place(x=90, y=10)
    label_2 = Label(root2, text="Choose from the following topics", font=("roboto", 19), bg="#220047", fg="#CE9141")
    label_2.place(x=55, y=80)
    button_1 = Button(root2, text="Linux", font=("roboto", 15),bg="#CE9141", fg="#220047", activeforeground="#CE9141",activebackground="#220047",command=lambda:getnews("Linux"))
    button_1.place(x=50, y=140)
    button_2 = Button(root2, text="Open-Source", font=("roboto",15), bg="#CE9141", fg="#220047", activeforeground="#CE9141",activebackground="#220047",command=lambda:getnews("Open-Source"))
    button_2.place(x=130, y=140)
    button_3 = Button(root2, text="Android", font=("roboto", 15), bg="#CE9141", fg="#220047", activeforeground="#CE9141",activebackground="#220047",command=lambda:getnews("Android"))
    button_3.place(x=280, y=140)
    button_4 = Button(root2, text="EXIT", font=("roboto", 15), bg="#CE9141", fg="#220047",activeforeground="#CE9141", activebackground="#220047")
    button_4.bind("<Button-1>", call1)
    button_4.place(x=380, y=140)
    root2.mainloop()

