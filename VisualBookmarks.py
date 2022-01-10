from tkinter import *
import webbrowser

def clickedMainPage():
    lbl.configure(text="Open favorite sites in your browser")
    widget.title("VisualBookmarks")
def clickedAbout():
    lbl.configure(text="About\nVisualBookmarks - Your favorite sites in one place\nFast. Easy. One click.")
    widget.title("About VisualBookmarks")
def clickedContacts():
    lbl.configure(text="Contacts\n e-mail: sikuzmin@yandex.ru")
    widget.title("Contacts VisualBookmarks")

def clickedG():
    webbrowser.open('https://google.com', autoraise=True)
def clickedFb():
    webbrowser.open('https://facebook.com', autoraise=True)
def clickedAm():
    webbrowser.open('https://amazon.com', autoraise=True)
def clickedAe():
    webbrowser.open('https://aliexpress.com', autoraise=True)
def clickedYt():
    webbrowser.open('https://youtube.com', autoraise=True)
def clickedVk():
    webbrowser.open('https://vk.com',  autoraise=True)
def clickedIn():
    webbrowser.open('https://instagram.com', autoraise=True)
def clickedAb():
    webbrowser.open('https://alibaba.com', autoraise=True)
def clickedYh():
    webbrowser.open('https://yahoo.com', autoraise=True) 
def clickedTt():
    webbrowser.open('https://tiktok.com', autoraise=True)
def clickedTw():
    webbrowser.open('https://twitter.com', autoraise=True)
def clickedWp():
    webbrowser.open('https://wikipedia.com', autoraise=True)

    
widget = Tk()
widget['bg'] = 'white'
widget.title("VisualBookmarks - Your favorite sites in one place")
widget.geometry("700x450+350+190")


lbl = Label(widget, text="Open favorite sites in your browser", font=("Tahoma", 20))
lbl.place(x=290, y=10, width=750, height=120)
lbl['bg'] = 'white'

# MainPage
btnMainPage = Button(widget, text="Home", font=("Tahoma", 15), command=clickedMainPage)
btnMainPage.grid(column=1, row=0)

# About
btnAbout = Button(widget, text="About", font=("Tahoma", 15), command=clickedAbout)
btnAbout.grid(column=2, row=0)

# Contacts
btnContacts = Button(widget, text="Contacts", font=("Tahoma", 15), command=clickedContacts)
btnContacts.grid(column=3, row=0)

# Google
btnG = Button(widget, text="Google.com", font=("Tahoma", 15), command=clickedG)
btnG.place(x=250, y=200, width=170, height=50)
btnG['bg'] = 'white'

# Facebook
btnFb = Button(widget, text="Facebook.com", font=("Tahoma", 15), command=clickedFb)
btnFb.place(x=450, y=200, width=170, height=50)

# Amazon
btnAm = Button(widget, text="Amazon.com", font=("Tahoma", 15), command=clickedAm)
btnAm.place(x=650, y=200, width=170, height=50)
btnAm['bg'] = 'white'

# Aliexpress
btnAe = Button(widget, text="Aliexpress.com", font=("Tahoma", 15), command=clickedAe)
btnAe.place(x=850, y=200, width=170, height=50)

# Youtube
btnYt = Button(widget, text="Youtube.com", font=("Tahoma", 15), command=clickedYt)
btnYt.place(x=250, y=300, width=170, height=50)
btnYt['bg'] = 'white'

# Vk.com
btnVk = Button(widget, text="Vk.com", font=("Tahoma", 15), command=clickedVk)
btnVk.place(x=450, y=300, width=170, height=50)

# Instagram
btnIn = Button(widget, text="Instagram.com", font=("Tahoma", 15), command=clickedIn)
btnIn.place(x=650, y=300, width=170, height=50)
btnIn['bg'] = 'white'

# Alibaba
btnAb = Button(widget, text="Alibaba.com", font=("Tahoma", 15), command=clickedAb)
btnAb.place(x=850, y=300, width=170, height=50)

# Yahoo
btnYh = Button(widget, text="Yahoo.com", font=("Tahoma", 15), command=clickedYh)
btnYh.place(x=250, y=400, width=170, height=50)
btnYh['bg'] = 'white'

# TikTok
btnTt = Button(widget, text="Tiktok.com", font=("Tahoma", 15), command=clickedTt)
btnTt.place(x=450, y=400, width=170, height=50)

# Twitter
btnTw = Button(widget, text="Twitter.com", font=("Tahoma", 15), command=clickedTw)
btnTw.place(x=650, y=400, width=170, height=50)
btnTw['bg'] = 'white'

# Wikipedia
btnWp = Button(widget, text="Wikipedia.com", font=("Tahoma", 15), command=clickedWp)
btnWp.place(x=850, y=400, width=170, height=50)

lbl1 = Label(widget, text="2021-2022 © All rights reserved")
lbl1.place(x=250, y=620, width=250, height=120)
lbl1['bg'] = 'white'

widget.mainloop()
