from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import*
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import requests
import json
import pandas as pd
import urllib.request
import time
import bs4
import speech_recognition as sr

  
conn =sqlite3.connect("sms.db")
connn=sqlite3.connect("smss.db")
c=conn.cursor()
cc=connn.cursor()


c.execute('''CREATE TABLE IF NOT EXISTS stu(rno integer primary key,name text,marks integer)''')
cc.execute('''CREATE TABLE IF NOT EXISTS studs(rno integer primary key,name text,date integer,topic text,status text)''')

def f1():
	master_window.withdraw()
	add_window.deiconify()

def f2():
	add_window.withdraw()
	master_window.deiconify()

def f3():
	master_window.withdraw()
	view_window.deiconify()
	view_window_st_data.delete(1.0, END)
	conn = None
	try:
		conn =sqlite3.connect("sms.db")
		c=conn.cursor()
		c.execute("SELECT * FROM stu")
		records =c.fetchall()
		print_records=" "
		for record in records:
			print_records +="rno: " + str(record[0]) +"  name: " + str(record[1]) + "  marks: " + str(record[2]) + "\n" 
		view_window_st_data.insert(INSERT, print_records)
	


		conn.commit()
		conn.close()
		
	except Exception as e:
		showerror("Issue",e)
	finally:
		if conn is not None:
			conn.close()


def f4():
	view_window.withdraw()
	master_window.deiconify()
	

def f5():
	
	
	
			
	if(add_window_ent_rno.get() == "" or add_window_ent_name.get() == "" or add_window_ent_CO1.get() == "" or add_window_ent_CO2.get() == "" or add_window_ent_CO3.get() == "" or add_window_ent_CO4.get() == ""):
		showerror("OOPS!", "Please fill all the details")
	elif (add_window_ent_rno.get().isdigit() == False):
		showerror("OOPS!", "Roll number can have positive integers only")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_marks.delete(0, END)
	elif (int(add_window_ent_rno.get()) <= 0) :
		showerror("OOPS!", "Roll number can't be negative")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_marks.delete(0, END)
	elif (len(add_window_ent_name.get()) < 2):
		showerror("OOPS!", "Name can't consist of only one alphabet")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_marks.delete(0, END)
	elif ((((add_window_ent_name.get()).replace(" ","")).isalpha()) == False):
		showerror("OOPS!", "Name can't consist of digits")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_marks.delete(0, END)
	elif (add_window_ent_CO1.get().isdigit() == False):
		showerror("OOPS!", "Marks can be positive integers only")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_CO1.delete(0, END)
	elif (add_window_ent_CO2.get().isdigit() == False):
		showerror("OOPS!", "Marks can be positive integers only")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_CO2.delete(0, END)
	elif (add_window_ent_CO3.get().isdigit() == False):
		showerror("OOPS!", "Marks can be positive integers only")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_CO3.delete(0, END)
	elif (add_window_ent_CO4.get().isdigit() == False):
		showerror("OOPS!", "Marks can be positive integers only")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_CO4.delete(0, END)
	elif int(add_window_ent_CO1.get()) < 0:
		showerror("OOPS!", "Marks can't be negative")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_CO1.delete(0, END)
	elif int(add_window_ent_CO2.get()) < 0:
		showerror("OOPS!", "Marks can't be negative")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_CO2.delete(0, END)
	elif int(add_window_ent_CO3.get()) < 0:
		showerror("OOPS!", "Marks can't be negative")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_CO3.delete(0, END)
	elif int(add_window_ent_CO4.get()) < 0:
		showerror("OOPS!", "Marks can't be negative")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_CO4.delete(0, END)
	elif int(add_window_ent_CO1.get()) > 10:
		showerror("OOPS!", "Marks can't be greater than 10 for each question")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_CO1.delete(0, END)
	elif int(add_window_ent_CO2.get()) > 10:
		showerror("OOPS!", "Marks can't be greater than 10 for each question")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_CO2.delete(0, END)
	elif int(add_window_ent_CO3.get()) > 10:
		showerror("OOPS!", "Marks can't be greater than 10 for each question")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_CO3.delete(0, END)
	elif int(add_window_ent_CO4.get()) > 10:
		showerror("OOPS!", "Marks can't be greater than 10 for each question")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_CO4.delete(0, END)
	else:
		conn = None
		add_window_ent_marks=int(add_window_ent_CO1.get())+int(add_window_ent_CO2.get())+int(add_window_ent_CO3.get())+int(add_window_ent_CO4.get())
		try:	
			
			
			
			conn =sqlite3.connect("sms.db")
			c=conn.cursor()       
			c.execute("INSERT INTO stu VALUES(:rno,:name,:marks)",
				{
					"rno":add_window_ent_rno.get(),
					"name":add_window_ent_name.get(),
					"marks":add_window_ent_marks,
				})
	
			conn.commit()
			conn.close()
			showinfo("Success", "record added")
			add_window_ent_rno.delete(0,END)
			add_window_ent_name.delete(0,END)
			add_window_ent_CO1.delete(0,END)
			add_window_ent_CO2.delete(0,END)
			add_window_ent_CO3.delete(0,END)
			add_window_ent_CO4.delete(0,END)
		except Exception as e:
			showerror("Issue", "Roll no already exists")
			add_window_ent_rno.delete(0, END)
			add_window_ent_name.delete(0, END)
			add_window_ent_CO1.delete(0, END)
			add_window_ent_CO2.delete(0, END)
			add_window_ent_CO3.delete(0, END)
			add_window_ent_CO4.delete(0, END)	
			conn.rollback()
		finally:
			if conn is not None:
				conn.close()
	
	
	

def f6():
	master_window.withdraw()
	update_window.deiconify()

def f7():
	update_window.withdraw()
	master_window.deiconify()
	
def f8():
	conn = None
	if (delete_window_ent_rno.get() == ""):
		showerror("OOPS!", "Please enter roll number")
	elif ((delete_window_ent_rno.get()).isdigit() == False):
		showerror("OOPS!", "Roll number can consist of positive integers only")
		delete_window_ent_rno.delete(0, END)
	elif (int(delete_window_ent_rno.get()) <= 0):
		showerror("OOPS!", "Roll number can't be negative")
		delete_window_ent_rno.delete(0, END)
	else:
	
		try:
			conn =sqlite3.connect("sms.db")			
			c=conn.cursor()
	
			c.execute("DELETE from stu WHERE rno=" + delete_window_ent_rno.get())
			if c.rowcount > 0:
				conn.commit()
				showinfo("Success", "Deleted successfully")
				delete_window_ent_rno.delete(0, END)
			else:
				showerror("Error", "Student does not exist")
				delete_window_ent_rno.delete(0, END)
		except Exception as e:
			showerror("OOPS!", e)
			delete_window_ent_rno.delete(0, END)
		finally:
			if conn is not None:
				conn.close()
def f9():
	delete_window.withdraw()
	master_window.deiconify()	
def f10():
	master_window.withdraw()
	delete_window.deiconify()

def f11():
	if(update_window_ent_rno.get() == "" or update_window_ent_name.get() == "" or update_window_ent_CO1.get() == "" or update_window_ent_CO2.get() == "" or update_window_ent_CO3.get() == "" or update_window_ent_CO4.get() == ""):
		showerror("OOPS!", "Please fill all the details")
	elif (update_window_ent_rno.get().isdigit() == False):
		showerror("OOPS!", "Roll number can have positive integers only")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_marks.delete(0, END)
	elif (int(update_window_ent_rno.get()) <= 0) :
		showerror("OOPS!", "Roll number can't be negative")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_marks.delete(0, END)
	elif (len(update_window_ent_name.get()) < 2):
		showerror("OOPS!", "Name can't consist of only one alphabet")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_marks.delete(0, END)
	elif ((((update_window_ent_name.get()).replace(" ","")).isalpha()) == False):
		showerror("OOPS!", "Name can't consist of digits")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_marks.delete(0, END)
	elif (update_window_ent_CO1.get().isdigit() == False):
		showerror("OOPS!", "Marks can be positive integers only")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_CO1.delete(0, END)
	elif (update_window_ent_CO2.get().isdigit() == False):
		showerror("OOPS!", "Marks can be positive integers only")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_CO2.delete(0, END)
	elif (update_window_ent_CO3.get().isdigit() == False):
		showerror("OOPS!", "Marks can be positive integers only")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_CO3.delete(0, END)
	elif (update_window_ent_CO4.get().isdigit() == False):
		showerror("OOPS!", "Marks can be positive integers only")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_CO4.delete(0, END)
	elif int(update_window_ent_CO1.get()) < 0:
		showerror("OOPS!", "Marks can't be negative")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_CO1.delete(0, END)
	elif int(update_window_ent_CO2.get()) < 0:
		showerror("OOPS!", "Marks can't be negative")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_CO2.delete(0, END)
	elif int(update_window_ent_CO3.get()) < 0:
		showerror("OOPS!", "Marks can't be negative")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_CO3.delete(0, END)
	elif int(update_window_ent_CO4.get()) < 0:
		showerror("OOPS!", "Marks can't be negative")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_CO4.delete(0, END)
	elif int(update_window_ent_CO1.get()) > 10:
		showerror("OOPS!", "Marks can't be greater than 10 for each question")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_CO1.delete(0, END)
	elif int(update_window_ent_CO2.get()) > 10:
		showerror("OOPS!", "Marks can't be greater than 10 for each question")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_CO2.delete(0, END)
	elif int(update_window_ent_CO3.get()) > 10:
		showerror("OOPS!", "Marks can't be greater than 10 for each question")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_CO3.delete(0, END)
	elif int(update_window_ent_CO4.get()) > 10:
		showerror("OOPS!", "Marks can't be greater than 10 for each question")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_CO4.delete(0, END)
	else:
		conn = None
		try:
			update_window_ent_marks=int(update_window_ent_CO1.get())+int(update_window_ent_CO2.get())+int(update_window_ent_CO3.get())+int(update_window_ent_CO4.get())
			conn =sqlite3.connect("sms.db")
			c=conn.cursor()	

			c.execute("""UPDATE stu SET rno=:rno,name=:name,marks=:marks WHERE rno=:rno""",
				{
					"rno":update_window_ent_rno.get(),
					"name":update_window_ent_name.get(),
					"marks":update_window_ent_marks,
			
				})

			if c.rowcount > 0:
				conn.commit()
				showinfo("Success", "record updated")
				update_window_ent_rno.delete(0, END)
				update_window_ent_name.delete(0, END)
				update_window_ent_CO1.delete(0, END)
				update_window_ent_CO2.delete(0, END)
				update_window_ent_CO3.delete(0, END)
				update_window_ent_CO4.delete(0, END)
			else:
				showwarning("OOPS!", "Record does not exist")
				update_window_ent_rno.delete(0, END)
				update_window_ent_name.delete(0, END)
				update_window_ent_CO1.delete(0, END)
				update_window_ent_CO2.delete(0, END)
				update_window_ent_CO3.delete(0, END)
				update_window_ent_CO4.delete(0, END)

					
		except Exception as e:
			showerror("OOPS!", e)
		finally:
			if conn is not None:
				conn.close()
def f12():
	conn =sqlite3.connect("sms.db")
	c=conn.cursor()	

	c.execute('SELECT name,marks FROM stu')
	data = c.fetchall()

	name = []
	marks = []
    
	for row in data:
		name.append(row[0])
		marks.append(row[1])
	c=["red","green","blue"]

	plt.title("Batch Information")
	plt.bar(name,marks,color=c)
	plt.ylabel("Marks")
	
	
	
	plt.show()


def f13():
	main_window.withdraw()
	master_window.deiconify()
	


def f14():
	master_window.withdraw()
	main_window.deiconify()

def f15():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Speak Anything :")
		audio = r.listen(source)
		try:
			text = r.recognize_google(audio)
			print("You said : {}".format(text))
		except:
			print("Sorry could not recognize what you said")
	delete_window_ent_rno.insert(0,text)

def f16():
	main_window.withdraw()
	assignment_window.deiconify()

def f17():
	assignment_window.withdraw()
	main_window.deiconify()

def f18():
	assignment_window.withdraw()
	addass_window.deiconify()

def f19():
	assignment_window.withdraw()
	viewass_window.deiconify()
	viewass_window_st_data.delete(1.0, END)
	connn = None
	try:
		connn =sqlite3.connect("smss.db")
		cc=connn.cursor()
		cc.execute("SELECT * FROM studs")
		records =cc.fetchall()
		print_records=" "
		for record in records:
			print_records +="rno: " + str(record[0]) +"  name: " + str(record[1]) + "  date: " + str(record[2]) + "  topic: " + str(record[3]) + "  status: " + str(record[4]) + "\n" 
		viewass_window_st_data.insert(INSERT, print_records)
	


		connn.commit()
		connn.close()
		
	except Exception as e:
		showerror("Issue",e)
	finally:
		if connn is not None:
			connn.close()

def f20():
	assignment_window.withdraw()
	updateass_window.deiconify()

def f21():
	assignment_window.withdraw()
	deleteass_window.deiconify()

def f22():
	

	if(addass_window_ent_rno.get() == "" or addass_window_ent_name.get() == ""):
		showerror("OOPS!", "Please fill all the details")
	elif (addass_window_ent_rno.get().isdigit() == False):
		showerror("OOPS!", "Roll number can have positive integers only")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_marks.delete(0, END)
	elif (int(addass_window_ent_rno.get()) <= 0) :
		showerror("OOPS!", "Roll number can't be negative")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_marks.delete(0, END)
	elif (len(addass_window_ent_name.get()) < 2):
		showerror("OOPS!", "Name can't consist of only one alphabet")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_marks.delete(0, END)
	elif ((((addass_window_ent_name.get()).replace(" ","")).isalpha()) == False):
		showerror("OOPS!", "Name can't consist of digits")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_marks.delete(0, END)
	else:
		connn = None
		try:	
			
			
			
			connn =sqlite3.connect("smss.db")
			cc=connn.cursor()
			cc.execute("INSERT INTO studs VALUES(:rno,:name,:date,:topic,:status)",
				{
					"rno":addass_window_ent_rno.get(),
					"name":addass_window_ent_name.get(),
					"date":addass_window_ent_date.get(),
					"topic":addass_window_ent_topic.get(),
					"status":addass_window_ent_status.get(),
				})
	
			connn.commit()
			connn.close()
			showinfo("Success", "record added")
			addass_window_ent_rno.delete(0,END)
			addass_window_ent_name.delete(0,END)
			addass_window_ent_date.delete(0,END)
			addass_window_ent_topic.delete(0,END)
			addass_window_ent_status.delete(0,END)
			
		except Exception as e:
			showerror("Issue", "Roll no already exists")
			addass_window_ent_rno.delete(0, END)
			addass_window_ent_name.delete(0, END)
			addass_window_ent_date.delete(0,END)
			addass_window_ent_topic.delete(0,END)
			addass_window_ent_status.delete(0,END)
	
			connn.rollback()
		finally:
			if connn is not None:
				connn.close()

def f23():
	addass_window.withdraw()
	assignment_window.deiconify()

def f24():
	viewass_window.withdraw()
	assignment_window.deiconify()

def f25():
	connn = None
	if (deleteass_window_ent_rno.get() == ""):
		showerror("OOPS!", "Please enter roll number")
	elif ((deleteass_window_ent_rno.get()).isdigit() == False):
		showerror("OOPS!", "Roll number can consist of positive integers only")
		deleteass_window_ent_rno.delete(0, END)
	elif (int(deleteass_window_ent_rno.get()) <= 0):
		showerror("OOPS!", "Roll number can't be negative")
		deleteass_window_ent_rno.delete(0, END)
	else:
	
		try:
			connn =sqlite3.connect("smss.db")			
			cc=connn.cursor()
	
			cc.execute("DELETE from studs WHERE rno=" + deleteass_window_ent_rno.get())
			if cc.rowcount > 0:
				connn.commit()
				showinfo("Success", "Deleted successfully")
				deleteass_window_ent_rno.delete(0, END)
			else:
				showerror("Error", "Student does not exist")
				deleteass_window_ent_rno.delete(0, END)
		except Exception as e:
			showerror("OOPS!", e)
			deleteass_window_ent_rno.delete(0, END)
		finally:
			if conn is not None:
				connn.close()

def f26():
	deleteass_window.withdraw()
	assignment_window.deiconify()

def f27():
	if(updateass_window_ent_rno.get() == "" or updateass_window_ent_name.get() == ""):
		showerror("OOPS!", "Please fill all the details")
	elif (updateass_window_ent_rno.get().isdigit() == False):
		showerror("OOPS!", "Roll number can have positive integers only")
		updateass_window_ent_rno.delete(0, END)
		updateass_window_ent_name.delete(0, END)
		updateass_window_ent_marks.delete(0, END)
	elif (int(updateass_window_ent_rno.get()) <= 0) :
		showerror("OOPS!", "Roll number can't be negative")
		updateass_window_ent_rno.delete(0, END)
		updateass_window_ent_name.delete(0, END)
		updateass_window_ent_marks.delete(0, END)
	elif (len(updateass_window_ent_name.get()) < 2):
		showerror("OOPS!", "Name can't consist of only one alphabet")
		updateass_window_ent_rno.delete(0, END)
		updateass_window_ent_name.delete(0, END)
		updateass_window_ent_marks.delete(0, END)
	elif ((((updateass_window_ent_name.get()).replace(" ","")).isalpha()) == False):
		showerror("OOPS!", "Name can't consist of digits")
		updateass_window_ent_rno.delete(0, END)
		updateass_window_ent_name.delete(0, END)
		updateass_window_ent_marks.delete(0, END)
	else:
		connn = None
		try:
			connn =sqlite3.connect("smss.db")
			cc=connn.cursor()	

			cc.execute("""UPDATE studs SET rno=:rno,name=:name,date=:date,topic=:topic,status=:status WHERE rno=:rno""",
				{
					"rno":updateass_window_ent_rno.get(),
					"name":updateass_window_ent_name.get(),
					"date":updateass_window_ent_date.get(),
					"topic":updateass_window_ent_topic.get(),
					"status":updateass_window_ent_status.get(),
					
			
				})

			if cc.rowcount > 0:
				connn.commit()
				showinfo("Success", "record updated")
				updateass_window_ent_rno.delete(0, END)
				updateass_window_ent_name.delete(0, END)
				updateass_window_ent_date.delete(0, END)
				updateass_window_ent_topic.delete(0, END)
				updateass_window_ent_status.delete(0, END)
				
			else:
				showwarning("OOPS!", "Record does not exist")
				updateass_window_ent_rno.delete(0, END)
				updateass_window_ent_name.delete(0, END)
				updateass_window_ent_date.delete(0, END)
				updateass_window_ent_topic.delete(0, END)
				updateass_window_ent_status.delete(0, END)

					
		except Exception as e:
			showerror("OOPS!", e)
		finally:
			if connn is not None:
				connn.close()

def f28():
	updateass_window.withdraw()
	assignment_window.deiconify()	

main_window=Tk()
main_window.title("Teacher's Help Kit")
main_window.geometry("500x500")
main_window["bg"] = "#e6ffee"


f=("Calibri",12,"bold")
main_window_btn_marks=Button(main_window,text="Marks",width=10,font=f,command=f13,relief=SOLID)
main_window_btn_assignment=Button(main_window,text="Assignment",width=10,font=f,command=f16,relief=SOLID)


main_window_btn_marks.pack(pady=5)
main_window_btn_assignment.pack(pady=5)


data = requests.get('https://ipinfo.io/').text
data = json.loads(data)
state = data['region']
city = data['city']


apikey = '8340ec56fda019d2e329f592771132a5'
url = "http://api.openweathermap.org/data/2.5/weather?"
complete_url = url + "appid=" + apikey + "&q=" + city
response = requests.get(complete_url).text
response = json.loads(response)
kelvin=response['main']['temp']
celcius=int(kelvin-273.15)
degree_sign = u"\N{DEGREE SIGN}"



loca=Label(main_window,text=f"    Location:{state}/{city}         TEMP:{celcius}{degree_sign}C     ",font=f,relief=SOLID,bg="#e6ffee")
loca.pack(pady=10)

try:
	web_address = "https://www.brainyquote.com/quote_of_the_day"
	response = requests.get(web_address)
	
	data = bs4.BeautifulSoup(response.text, 'html.parser')
	#print(data)

	info = data.find('img', {'class' : 'p-qotd'})
	#print(info)

	qotd = info['alt']
		
except Exception as e:
	print(e)

quote=Label(main_window,text= f"QOTD= {qotd}",font=f,relief=SOLID,wraplength = 500,bg="#e6ffee")
quote.pack(pady=10,side = LEFT,anchor=NW)



master_window= Toplevel(main_window)
master_window.title("Marks Section")
master_window.geometry("500x500")
master_window["bg"] ="#ccd9ff"

master_window_btn_add=Button(master_window,text="Add",width=10,font=f,command=f1,relief=SOLID)
master_window_btn_view=Button(master_window,text="View",width=10,font=f,command=f3,relief=SOLID)
master_window_btn_update=Button(master_window,text="Update",width=10,font=f,command=f6,relief=SOLID)
master_window_btn_delete=Button(master_window,text="Delete",width=10,font=f,command=f10,relief=SOLID)
master_window_btn_charts=Button(master_window,text="Charts",width=10,font=f,command=f12,relief=SOLID)
master_window_btn_back=Button(master_window,text='Back',font=f,command=f14,relief=SOLID,width=10)

master_window_btn_add.pack(pady=5)
master_window_btn_view.pack(pady=5)
master_window_btn_update.pack(pady=5)
master_window_btn_delete.pack(pady=5)
master_window_btn_charts.pack(pady=10)
master_window_btn_back.pack(pady=5)

master_window.withdraw()




assignment_window= Toplevel(main_window)
assignment_window.title("Assignment Section")
assignment_window.geometry("500x500")
assignment_window["bg"] ="#ccd9ff"

assignment_window_btn_add=Button(assignment_window,text="Add",width=10,font=f,command=f18,relief=SOLID)
assignment_window_btn_view=Button(assignment_window,text="View",width=10,font=f,command=f19,relief=SOLID)
assignment_window_btn_update=Button(assignment_window,text="Update",width=10,font=f,command=f20,relief=SOLID)
assignment_window_btn_delete=Button(assignment_window,text="Delete",width=10,font=f,command=f21,relief=SOLID)
assignment_window_btn_back=Button(assignment_window,text='Back',font=f,command=f17,relief=SOLID,width=10)

assignment_window_btn_add.pack(pady=5)
assignment_window_btn_view.pack(pady=5)
assignment_window_btn_update.pack(pady=5)
assignment_window_btn_delete.pack(pady=5)
assignment_window_btn_back.pack(pady=5)

assignment_window.withdraw()



addass_window= Toplevel(master_window)
addass_window.title("Add Information")
addass_window.geometry("500x500")
addass_window["bg"] ="#ccd9ff"


addass_window_lbl_rno=Label(addass_window,text="enter rno:",font=f,bg="#ccd9ff")
addass_window_ent_rno=Entry(addass_window,bd=5,font=f,relief=SOLID)
addass_window_lbl_name=Label(addass_window,text="enter name:",font=f,bg="#ccd9ff")
addass_window_ent_name=Entry(addass_window,bd=5,font=f,relief=SOLID)
addass_window_lbl_date=Label(addass_window,text="enter date:",font=f,bg="#ccd9ff")
addass_window_ent_date=Entry(addass_window,bd=5,font=f,relief=SOLID)
addass_window_lbl_topic=Label(addass_window,text="enter topic:",font=f,bg="#ccd9ff")
addass_window_ent_topic=Entry(addass_window,bd=5,font=f,relief=SOLID)
addass_window_lbl_status=Label(addass_window,text="enter status:",font=f,bg="#ccd9ff")
addass_window_ent_status=Entry(addass_window,bd=5,font=f,relief=SOLID)






addass_window_btn_save=Button(addass_window,text='Save',font=f,command=f22,relief=SOLID,width=10)
addass_window_btn_back=Button(addass_window,text='Back',font=f,command=f23,relief=SOLID,width=10)


addass_window_lbl_rno.pack(pady=10)
addass_window_ent_rno.pack(pady=10)
addass_window_lbl_name.pack(pady=10)
addass_window_ent_name.pack(pady=10)
addass_window_lbl_date.pack(pady=10)
addass_window_ent_date.pack(pady=10)
addass_window_lbl_topic.pack(pady=10)
addass_window_ent_topic.pack(pady=10)
addass_window_lbl_status.pack(pady=10)
addass_window_ent_status.pack(pady=10)



addass_window_btn_save.pack(pady=10)
addass_window_btn_back.pack(pady=10)


addass_window.withdraw()



viewass_window= Toplevel(master_window)
viewass_window.title("View Stu.")
viewass_window.geometry("720x720")
viewass_window["bg"] ="#ffffe6"

viewass_window_st_data= ScrolledText(viewass_window,width=70,height=20,bg="#ffffe6",font=("bold"))
viewass_window_btn_back= Button(viewass_window,text="Back",font=f,command=f24,width=10,relief=SOLID)

viewass_window_st_data.pack(pady=10)
viewass_window_btn_back.pack(pady=10)

viewass_window.withdraw()




deleteass_window= Toplevel(master_window)
deleteass_window.title("Delete Stu.")
deleteass_window.geometry("500x500")
deleteass_window["bg"] ="#ccd9ff"

deleteass_window_lbl_rno=Label(deleteass_window,text="enter rno:",font=f,bg="#ccd9ff")
deleteass_window_ent_rno=Entry(deleteass_window,bd=5,font=f,relief=SOLID)
deleteass_window_lbl_rno.pack(pady=10)
deleteass_window_ent_rno.pack(pady=10)

deleteass_window_btn_record=Button(deleteass_window,text='Record',font=f,command=f15,relief=SOLID,width=10)
deleteass_window_btn_delete=Button(deleteass_window,text='Delete',font=f,command=f25,relief=SOLID,width=10)
deleteass_window_btn_back=Button(deleteass_window,text='Back',font=f,command=f26,relief=SOLID,width=10)
deleteass_window_btn_record.pack(pady=10)
deleteass_window_btn_delete.pack(pady=10)
deleteass_window_btn_back.pack(pady=10)

deleteass_window.withdraw()



updateass_window= Toplevel(master_window)
updateass_window.title("Update Information")
updateass_window.geometry("500x500")
updateass_window["bg"] ="#ccd9ff"


updateass_window_lbl_rno=Label(updateass_window,text="enter rno:",font=f,bg="#ccd9ff")
updateass_window_ent_rno=Entry(updateass_window,bd=5,font=f,relief=SOLID)
updateass_window_lbl_name=Label(updateass_window,text="enter name:",font=f,bg="#ccd9ff")
updateass_window_ent_name=Entry(updateass_window,bd=5,font=f,relief=SOLID)
updateass_window_lbl_date=Label(updateass_window,text="enter date:",font=f,bg="#ccd9ff")
updateass_window_ent_date=Entry(updateass_window,bd=5,font=f,relief=SOLID)
updateass_window_lbl_topic=Label(updateass_window,text="enter topic:",font=f,bg="#ccd9ff")
updateass_window_ent_topic=Entry(updateass_window,bd=5,font=f,relief=SOLID)
updateass_window_lbl_status=Label(updateass_window,text="enter status:",font=f,bg="#ccd9ff")
updateass_window_ent_status=Entry(updateass_window,bd=5,font=f,relief=SOLID)






updateass_window_btn_save=Button(updateass_window,text='Save',font=f,command=f27,relief=SOLID,width=10)
updateass_window_btn_back=Button(updateass_window,text='Back',font=f,command=f28,relief=SOLID,width=10)


updateass_window_lbl_rno.pack(pady=10)
updateass_window_ent_rno.pack(pady=10)
updateass_window_lbl_name.pack(pady=10)
updateass_window_ent_name.pack(pady=10)
updateass_window_lbl_date.pack(pady=10)
updateass_window_ent_date.pack(pady=10)
updateass_window_lbl_topic.pack(pady=10)
updateass_window_ent_topic.pack(pady=10)
updateass_window_lbl_status.pack(pady=10)
updateass_window_ent_status.pack(pady=10)



updateass_window_btn_save.pack(pady=10)
updateass_window_btn_back.pack(pady=10)


updateass_window.withdraw()







add_window= Toplevel(master_window)
add_window.title("Add St.")
add_window.geometry("500x500")
add_window["bg"] ="#ccd9ff"


add_window_lbl_rno=Label(add_window,text="enter rno:",font=f,bg="#ccd9ff")
add_window_ent_rno=Entry(add_window,bd=5,font=f,relief=SOLID)
add_window_lbl_name=Label(add_window,text="enter name:",font=f,bg="#ccd9ff")
add_window_ent_name=Entry(add_window,bd=5,font=f,relief=SOLID)


add_window_lbl_CO1=Label(add_window,text="enter CO1:",font=f,bg="#ccd9ff")
add_window_ent_CO1=Entry(add_window,bd=5,font=f,relief=SOLID)
add_window_lbl_CO2=Label(add_window,text="enter CO2:",font=f,bg="#ccd9ff")
add_window_ent_CO2=Entry(add_window,bd=5,font=f,relief=SOLID)
add_window_lbl_CO3=Label(add_window,text="enter CO3:",font=f,bg="#ccd9ff")
add_window_ent_CO3=Entry(add_window,bd=5,font=f,relief=SOLID)
add_window_lbl_CO4=Label(add_window,text="enter CO4:",font=f,bg="#ccd9ff")
add_window_ent_CO4=Entry(add_window,bd=5,font=f,relief=SOLID)



add_window_btn_save=Button(add_window,text='Save',font=f,command=f5,relief=SOLID,width=10)
add_window_btn_back=Button(add_window,text='Back',font=f,command=f2,relief=SOLID,width=10)


add_window_lbl_rno.pack(pady=10)
add_window_ent_rno.pack(pady=10)
add_window_lbl_name.pack(pady=10)
add_window_ent_name.pack(pady=10)
add_window_lbl_CO1.pack(pady=10)
add_window_ent_CO1.pack(pady=10)
add_window_lbl_CO2.pack(pady=10)
add_window_ent_CO2.pack(pady=10)
add_window_lbl_CO3.pack(pady=10)
add_window_ent_CO3.pack(pady=10)
add_window_lbl_CO4.pack(pady=10)
add_window_ent_CO4.pack(pady=10)
add_window_btn_save.pack(pady=10)
add_window_btn_back.pack(pady=10)


add_window.withdraw()



view_window= Toplevel(master_window)
view_window.title("View Stu.")
view_window.geometry("600x600")
view_window["bg"] ="#ffffe6"

view_window_st_data= ScrolledText(view_window,width=50,height=20,bg="#ffffe6",font=("bold"))
view_window_btn_back= Button(view_window,text="Back",font=f,command=f4,width=10,relief=SOLID)

view_window_st_data.pack(pady=10)
view_window_btn_back.pack(pady=10)

view_window.withdraw()

update_window= Toplevel(master_window)
update_window.title("Update St.")
update_window.geometry("500x500")
update_window["bg"] ="#ffe6ee"


update_window_lbl_rno=Label(update_window,text="enter rno:",font=f,bg="#ffe6ee")
update_window_ent_rno=Entry(update_window,bd=5,font=f,relief=SOLID)
update_window_lbl_name=Label(update_window,text="enter name:",font=f,bg="#ffe6ee")
update_window_ent_name=Entry(update_window,bd=5,font=f,relief=SOLID)



update_window_lbl_CO1=Label(update_window,text="enter CO1:",font=f,bg="#ffe6ee")
update_window_ent_CO1=Entry(update_window,bd=5,font=f,relief=SOLID)
update_window_lbl_CO2=Label(update_window,text="enter CO2:",font=f,bg="#ffe6ee")
update_window_ent_CO2=Entry(update_window,bd=5,font=f,relief=SOLID)
update_window_lbl_CO3=Label(update_window,text="enter CO3:",font=f,bg="#ffe6ee")
update_window_ent_CO3=Entry(update_window,bd=5,font=f,relief=SOLID)
update_window_lbl_CO4=Label(update_window,text="enter CO4:",font=f,bg="#ffe6ee")
update_window_ent_CO4=Entry(update_window,bd=5,font=f,relief=SOLID)




update_window_btn_save=Button(update_window,text='Save',font=f,command=f11,relief=SOLID,width=10)
update_window_btn_back=Button(update_window,text='Back',font=f,command=f7,relief=SOLID,width=10)

update_window_lbl_rno.pack(pady=10)
update_window_ent_rno.pack(pady=10)
update_window_lbl_name.pack(pady=10)
update_window_ent_name.pack(pady=10)

update_window_lbl_CO1.pack(pady=10)
update_window_ent_CO1.pack(pady=10)
update_window_lbl_CO2.pack(pady=10)
update_window_ent_CO2.pack(pady=10)
update_window_lbl_CO3.pack(pady=10)
update_window_ent_CO3.pack(pady=10)
update_window_lbl_CO4.pack(pady=10)
update_window_ent_CO4.pack(pady=10)

update_window_btn_save.pack(pady=10)
update_window_btn_back.pack(pady=10)

update_window.withdraw()

delete_window= Toplevel(master_window)
delete_window.title("Delete Stu.")
delete_window.geometry("500x500")
delete_window["bg"] ="#ccd9ff"

delete_window_lbl_rno=Label(delete_window,text="enter rno:",font=f,bg="#ccd9ff")
delete_window_ent_rno=Entry(delete_window,bd=5,font=f,relief=SOLID)
delete_window_lbl_rno.pack(pady=10)
delete_window_ent_rno.pack(pady=10)

delete_window_btn_record=Button(delete_window,text='Record',font=f,command=f15,relief=SOLID,width=10)
delete_window_btn_delete=Button(delete_window,text='Delete',font=f,command=f8,relief=SOLID,width=10)
delete_window_btn_back=Button(delete_window,text='Back',font=f,command=f9,relief=SOLID,width=10)
delete_window_btn_record.pack(pady=10)
delete_window_btn_delete.pack(pady=10)
delete_window_btn_back.pack(pady=10)

delete_window.withdraw()

conn.commit()


conn.close()
connn.commit()


connn.close()


main_window.mainloop()

