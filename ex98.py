

from tkinter import *
import sqlite3

window = Tk()


def add_line():
    conn = sqlite3.connect("ex98.db")
    cur = conn.cursor()
    word =e1_value.get()
    print(word)
    cur.execute("INSERT INTO line VALUES (?)", [word] )
    conn.commit()
    conn.close()
    e1.delete(0,END)

  


def save_to_file():
     file = open("software_Data.txt","a+")
     conn = sqlite3.connect("ex98.db")
     cur = conn.cursor()
     for row in cur.execute("SELECT * from line"):
            print(type(row))
            file.write(row[0] + "\n")
     

     cur.execute("DELETE from line;")
     file.close()
     conn.commit()
     conn.close()     
  
def save_close():
    
    window.destroy()   



#Label
l1 = Label(window, height =1 , width=10, text = "Enter")
l1.grid(row=0,column=0)

#Entry box
e1_value = StringVar()
e1= Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

#button add line
b1 = Button(window, text="Add line", command=add_line)
b1.grid(row=0, column=3)
#button save changes
b2 = Button(window, text="Save Changes",command=save_to_file)
b2.grid(row=0, column=4)
#button Save and Close
b2 = Button(window, text="Close", command=save_close)
b2.grid(row=0, column=5)
window.mainloop()