from tkinter import *
from tkinter import messagebox as tkMessageBox
from tkinter import ttk
import sys
import tkinter
import os
import requests
import shutil

from module import blogSerch

def serch(event):
    input_string = editBox.get()
    num = numCoutBox.get()
    keywordSerch = blogSerch.GoogleSerch()
    if int(num) >= 5:
        tkMessageBox.showerror("タブ数が多いです。", "検索するタブの数が多すぎます。1~5で入力してください。")
    else:
        keywordSerch.googleSarch(num, input_string)

if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Google Serch...")

    root.geometry("600x300")

    label = tkinter.Label(root, text="検索キーワード:", bg="#F5F5F5")
    label.place(x=50, y=70)

    editBox = tkinter.Entry(width=30)
    editBox.place(x=150, y=70)

    label2 = tkinter.Label(root, text="開くタブの数(1~5):", bg="#F5F5F5")
    label2.place(x=50, y=100)

    numCoutBox = tkinter.Entry(width=5)
    numCoutBox.place(x=170, y=100)

    # ボタン配置
    button = tkinter.Button(root, text=u'検索', width=30)
    button.bind("<Button-1>", serch)
    button.place(x=130, y=170)

    root.mainloop()
