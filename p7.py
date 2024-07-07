# model use ---> using GUI

from tkinter import *
from tkinter.messagebox import *
from pickle import *
import os
import sys

def resource_path2(relative_path):
	try:
		base_path = sys._MEIPASS
	except Exception :
		base_path = os.path.abspath(".")
	return os.path.join(base_path, relative_path)

root = Tk()
root.title("Housing Price Prediactor")
root.geometry("700x600+50+50")
root.iconbitmap(resource_path2("home.ico"))
f = ("Century", 35, "bold")


f1 = open(resource_path2("hpp.pkl"), "rb")
model = load(f1)
f1.close()

def find():
	try:
		area = float(ent_area.get())
	except ValueError:
		showerror("Issue", "area shud be in number only")
		ent_area.delete(0, END)
		ent_area.focus()
		return

	try:
		bedrooms = float(ent_br.get())
	except ValueError:
		showerror("Issue", "bedrooms shud be in number only")
		ent_br.delete(0, END)
		ent_br.focus()
		return

	price = model.predict([[area, bedrooms]])
	msg = "price " + str(round(price[0], 2)) + "crs"
	showinfo("Msg", msg)
	ent_area.delete(0, END)
	ent_br.delete(0, END)
	ent_area.focus()
	
lab_title = Label(root, text="Housing Price Predicator", font=f)
lab_area = Label(root, text="Enter area ", font=f)
ent_area = Entry(root, font=f)
lab_br = Label(root, text = "Enter Number of Bedrooms", font=f)
ent_br = Entry(root, font=f)
btn_find = Button(root, text = "Find Price ", font=f, command = find)

lab_title.pack(pady=20)
lab_area.pack(pady=5)
ent_area.pack(pady=5)
lab_br.pack(pady=5)
ent_br.pack(pady=5)
btn_find.pack(pady=20)

root.mainloop()
