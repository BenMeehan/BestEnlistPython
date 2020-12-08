from tkinter import *
from tkinter import messagebox as mb
import sqlite3
# from resources import resources, money
from MenuItem import MenuItem

conn = sqlite3.connect("coffee.db")
print("connected to db")

conn.execute('''CREATE TABLE resources
         (money INT,
          milk INT,
          water INT,
          coffee INT);''')
print("Table created successfully")

conn.execute(
    "INSERT INTO resources (money,milk,water,coffee) VALUES (0,200,300,100 )")

conn.commit()

cursor = conn.execute("SELECT money,milk,water,coffee from resources")

resources = {}
money = 0

for row in cursor:
    money = row[0]
    resources['milk'] = row[1]
    resources['water'] = row[2]
    resources['coffee'] = row[3]


def payment(dollars):
    global money
    if dollars < item.cost:
        e1.delete(0, 'end')
        l1.config(text="Sorry thats not enough money. Money refunded.")
    else:
        if(item.name != 'espresso'):
            resources['Milk'] -= item.milk
        resources['Water'] -= item.water
        resources['Coffee'] -= item.coffee
        money += item.cost
        change = dollars-item.cost
        e1.delete(0, 'end')
        l1.config(
            text=f"Here is ${change} in change.\nHere is your {item.name}☕ enjoy!\n\n\nWould you like an another drink?\nEnter its name")


def handleInsert(e2, e3, e4, e5):
    if(e2.get() == ''):
        q = 0
    else:
        q = int(e2.get())
    if(e3.get() == ''):
        d = 0
    else:
        d = int(e3.get())
    if(e4.get() == ''):
        n = 0
    else:
        n = int(e4.get())
    if(e5.get() == ''):
        p = 0
    else:
        p = int(e5.get())
    l1.config(text="")
    for widget in f1.winfo_children():
        widget.destroy()
    dollars = ((q*25)+(d*10)+(n*5)+(p))/100
    payment(dollars)


def get_coins():
    l1.config(text="Please Insert Coins")
    l2 = Label(f1, text="How many Quaters ? ", pady=5, font=("Helvetica", "9"))
    l2.pack()
    l2.configure(background="white")
    e2 = Entry(f1, font=("Helvetica", "9"), highlightbackground="black", highlightcolor="gold",
               highlightthickness=1, relief="flat")
    e2.pack()
    l3 = Label(f1, text="How many Dimes ? ", pady=5, font=("Helvetica", "9"))
    l3.pack()
    l3.configure(background="white")
    e3 = Entry(f1, font=("Helvetica", "9"), highlightbackground="black", highlightcolor="gold",
               highlightthickness=1, relief="flat")
    e3.pack()
    l4 = Label(f1, text="How many Nickels ? ", pady=5, font=("Helvetica", "9"))
    l4.pack()
    l4.configure(background="white")
    e4 = Entry(f1, font=("Helvetica", "9"), highlightbackground="black", highlightcolor="gold",
               highlightthickness=1, relief="flat")
    e4.pack()
    l5 = Label(f1, text="How many Pennies ? ", pady=5, font=("Helvetica", "9"))
    l5.pack()
    l5.configure(background="white")
    e5 = Entry(f1, font=("Helvetica", "9"), highlightbackground="black", highlightcolor="gold",
               highlightthickness=1, relief="flat")
    e5.pack()

    b2 = Button(f1, text="Insert",
                command=lambda: handleInsert(e2, e3, e4, e5), font=("Helvetica", "9"), relief="groove", bd=2, activeforeground="green", activebackground="white")
    b2.pack(pady=10, ipadx=2, ipady=2)


def check_resources(item):
    if(item.name != 'espresso' and resources['Milk'] < item.milk):
        l1.config(text="Sorry there is not enough milk.")
        return False
    elif(resources['Water'] < item.water):
        l1.config(text="Sorry there is not enough water.")
        return False
    elif(resources['Coffee'] < item.coffee):
        l1.config(text="Sorry there is not enough coffee.")
        return False
    else:
        return True


item = 0


def handleEntry():
    global item
    if(e1.get() == 'report'):
        l1.config(text="")
        keys = list(resources.keys())
        e1.delete(0, 'end')
        mb.showinfo(
            "Resources", f"{keys[0]} : {resources[keys[0]]}ml\n{keys[1]} : {resources[keys[1]]}ml\n{keys[2]} : {resources[keys[2]]}gm\nMoney : ${money}")
    elif(e1.get() == 'latte' or e1.get() == "cappuccino" or e1.get() == "espresso"):
        txt = e1.get()
        item = MenuItem(txt)
        enough = check_resources(item)
        if enough == True:
            get_coins()

    else:
        e1.delete(0, 'end')
        l1.config(text="please enter a valid drink")


top = Tk()
top.geometry("500x500")
top.configure(background="white")

message = Message(top, text='Welcome to The Coffee Machine', width=450,
                  pady=20, font=("Times", "24", "bold italic"), fg='#6f4e37')
message.pack()
message.configure(background="white")

label = Label(
    top, text='What would you like ? (espresso/latte/cappuccino) : ', pady=20, font=("Helvetica", "11"))
label.pack()
label.configure(background="white")

e1 = Entry(top, highlightbackground="black", highlightcolor="#c7956d",
           highlightthickness=1, font=("Helvetica", "10"), relief='flat')
e1.pack(ipadx=2, ipady=2)
e1.configure(background="white")

b1 = Button(top, text="Enter", command=lambda: handleEntry(),
            font=("Helvetica", "9"), relief="groove", bd=2, activeforeground="green", activebackground="white")
b1.pack(pady=10, ipadx=2, ipady=2)

l1 = Label(top, text="", pady=0, font=("Helvetica", "11"))
l1.pack()
l1.configure(background="white")

f1 = Frame(top)
f1.pack()
f1.configure(background="white")

top.mainloop()

conn.close()
