from tkinter import *


GUI = Tk()
GUI.geometry("500x700")
GUI.state("icon")
GUI.title("Dashboard Die Hard 4.0")


bg = "#2b2b2b"
fg = "#149414"

ww = 1920
wh = 1080

GUI.configure(background=bg)

# Fullscreen
#def Fullscreen(event):
#    GUI.attributes("-fullscreen", True)

#def ExitFullscreen(event):
#    GUI.attributes("-fullscreen", False)

#GUI.bind("<F11>", Fullscreen)
#GUI.bind("<F12>", ExitFullscreen)

GUI.attributes("-fullscreen", False)
GUI.bind("<F10>", lambda event: GUI.attributes("-fullscreen", not GUI.attributes("-fullscreen")))

# Front
f1 = ("Sprite Coder", 20, "bold")
f2 = ("Sprite Coder", 15, "bold")
f3 = ("Sprite Coder", 12, "bold")

# CANVAS
canvas = Canvas(GUI, width=ww, height=wh, background=bg, bd=0, relief="ridge", highlightthickness=0)
canvas.place(x=0,y=0)

def MyFrame(x, y, width=300, height=100):
    frame1 = canvas.create_rectangle(0, 0, width, height, fill=bg, outline=fg, width=2)
    canvas.move(frame1,x,y) 

def FixedLabel(text="This is text", x=50, y=50, font=f1, color=fg):
    L1 = Label(GUI, text=text, font=f1, bg=bg, fg=color, justify=LEFT)
    L1.place(x=x,y=y)

#L1 = Label(GUI, text="Portfolio", font=f1, bg=bg, fg=fg)
#L1.place(x=50,y=100)

#L2 = Label(GUI, text="Chart", font=f2, bg=bg, fg=fg)
#L2.place(x=50,y=150)

#L3 = Label(GUI, text="Profit n Loss", font=f2, bg=bg, fg=fg)
#L3.place(x=50,y=200)

# F1
MyFrame(500,300,600,700)
FixedLabel("List of Indecies", 520, 280)
#FixedLabel("Chart", 50, 200, font=("Angsana New", 20, "bold"), color="yellow")

# F2
MyFrame(1200,30,700,500)
FixedLabel("Thailand Set Index Historical Prices", 1250, 15)
FixedLabel("Set 100 Index", 1250, 45)

v_result1 = StringVar()
v_result1.set("Set 100")

L1 = Label(GUI, textvariable=v_result1, font=f3, bg=bg, fg=fg, justify=LEFT)
L1.place(x=1225,y=70)

import investpy as ip
import pandas as pd
data = ip.get_index_recent_data(index='set 100', country='thailand')
v_result1.set(data)

# F3
MyFrame(1200,550,700,450)
FixedLabel("Chart", 1250, 535, font=f2, color=fg)

v_result2 = StringVar()
v_result2.set("Set 100 Chart")

L3 = Label(GUI, textvariable=v_result2, font=f3, bg=bg, fg=fg, justify=LEFT)
L3.place(x=1225,y=565)

df = ip.get_index_historical_data(index='set 100', country='thailand', from_date='01/01/2010', to_date='02/12/2021')
df1 = df.Close.plot()
print(df1.plot())
v_result2.set(df1.plot())

# IoT Frame1
MyFrame(20,30,400,200)
FixedLabel("IoT-Device 1", 25, 15, font=f2)
FixedLabel("TEMP (C) : 30\nHUMID (%) : 55\nSTATUS : OK", 25, 50, font=f2)

# IoT Frame2
MyFrame(20,300,400,200)
FixedLabel("IoT-Device 2", 25, 280, font=f2)
FixedLabel("TEMP (C) : 30\nHUMID (%) : 55\nSTATUS : OK", 25, 315, font=f2)

# IoT Frame3
MyFrame(20,550,400,200)
FixedLabel("IoT-Device 3", 25, 530, font=f2)
FixedLabel("TEMP (C) : 30\nHUMID (%) : 55\nSTATUS : OK", 25, 565, font=f2)

# IoT Frame4
MyFrame(20,800,400,200)
FixedLabel("IoT-Device 4", 25, 780, font=f2)
FixedLabel("TEMP (C) : 30\nHUMID (%) : 55\nSTATUS : OK", 25, 815, font=f2)

# Check STOCK
MyFrame(500,30,600,200)
FixedLabel("Quote", 520, 15, font=f2)

v_stockname = StringVar() # StringVar for GUI

E1 = Entry(GUI, textvariable=v_stockname, font=f1, bg=bg, fg=fg)
E1.configure(insertbackground=fg) # cursor color
E1.configure(highlightthickness=2, highlightbackground=fg, highlightcolor=fg)
E1.place(x=570,y=50)

v_result = StringVar()
v_result.set("Type ticker name")

L2 = Label(GUI, textvariable=v_result, font=f1, bg=bg, fg=fg, justify=LEFT)
L2.place(x=570,y=100)

from uncleengineer import thaistock

def CheckStockPrice(event):
    stockname = v_stockname.get()
    print(stockname)
    result = thaistock(stockname)
    text = "TICKER: {}\nPrice: {}".format(result[0], result[1])
    v_result.set(text)

E1.bind("<Return>", CheckStockPrice)


GUI.mainloop()