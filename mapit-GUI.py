from tkinter import *
import webbrowser
import sys
import pyperclip


root = Tk()
root.geometry('350x100')
root.title("Mapit")
Label(root,text = "Welcome to Mapit:\n Enter the City, State, Country:").grid()
user_address = StringVar()
Entry(root, textvariable = user_address).grid(row = 2, column = 1)
def mapit():
	#if user_address.get():
		webbrowser.open('https://www.google.com/maps/place/' + user_address.get())
Button(root,text = 'Map-it', command = mapit).grid(row = 3, column = 2)
root.resizable(width = False, height = False)
root.mainloop()


