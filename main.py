import turtle
from bs4 import BeautifulSoup
import requests
import tkinter
import webbrowser


# CONNECTING
url = "https://news.ycombinator.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")

# LISTS

links_list = []
title_list = []

# OPEN WEB FUNC


def click_link(web):
    webbrowser.open_new_tab(web)

# SCANNING LINKS


for link in soup.find_all("a"):
    found_link = link.get("href")
    if "https" in found_link:
        if found_link == "https://news.ycombinator.com":
            pass
        else:
            if found_link not in links_list:
                links_list.append(found_link)

# SCANNING TITLE


def title_finder():
        tt = soup.find_all("tr", class_="athing")
        tt = tt[0:31]

        for rit in tt:
            title_list.append(rit.get_text())


title_finder()


# WINDOW

window = tkinter.Tk()
window.minsize(width=900,height=900)
window.title("HackerNews")
window.config(background="red")

# SCROLLBAR

scrollbar = tkinter.Scrollbar(window)
scrollbar.pack(side="right", fill="y")

# CANVAS
canvas = tkinter.Canvas(window, yscrollcommand=scrollbar.set,background="red")
canvas.pack(side="left", fill="both", expand=True)

scrollbar.config(command=canvas.yview)

# FRAME
frame = tkinter.Frame(canvas,background="red")
canvas.create_window((0, 0), window=frame, anchor="nw")

# NUMBER OF LINKS
links_count = len(title_list)

# LABEL

label1 = tkinter.Label(text="HackerNews Articles",font=("times new roman",10,"italic","bold"),background="red")
label1.pack()

label2 = tkinter.Label(text=f"Total number of posts: {links_count} ",font=("times new roman",10,"italic","bold"),background="red")
label2.pack()


# SHOW WINDOW
for i, url in enumerate(links_list):
    if i < len(title_list):
        title = title_list[i]
        buttons = tkinter.Button(frame,background="orange" ,height=1, width=120,
                                font=("times new roman", 10, "italic", "bold"),
                                text=title,
                                command=lambda a=url: click_link(a),
                                borderwidth=8)

        buttons.pack(anchor='w', pady=2)

# SCROLLBAR UP
canvas.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))
canvas.yview_moveto(0)

window.mainloop()