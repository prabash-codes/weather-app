from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder  import TimezoneFinder
import requests
import pytz
from tkinter.font import BOLD
from datetime import datetime



root = tk.Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)

def getweather():
    try:
        city = textfield.get()

        geolocator = Nominatim(user_agent="geopixercises")
        location = geolocator.geocode(city)
    
        lat = location.latitude
        lon = location.longitude
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=lon,lat=lat)
    

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M:%p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        #weather
        api = f"https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=eea79ec321d3a2129cf71c524f9658c7"
    
    
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=str(temp)+"°C")
        c.config(text=(condition,"|","FEELS,""LIKE",str(temp)+"°C"))
        w.config(text=str(wind)+"m/s")
        h.config(text=str(humidity)+"%")
        d.config(text=description)
        p.config(text=str(pressure)+"hPa")
    except Exception as e:
        messagebox.showerror("Error","City not found")
        textfield.delete(0,END)

#search bx

search_image = PhotoImage(file='images\search.png')
myimage = Label(image=search_image)
myimage.place(x=20,y=20)

textfield = Entry(root,justify="center",width=17,font=("poppins",25,BOLD),bg="#404040",border=0,fg="white")
textfield.place(x=50,y=40)
textfield.focus()

search_icon = PhotoImage(file='images\search_icon.png')
myimage_icon = Button(image=search_icon,borderwidth=0,cursor="hand2",command=getweather)
myimage_icon.place(x=400,y=34)

#logo
Logo_image = PhotoImage(file='images\logo.png')
logo = Label(image=Logo_image)
logo.place(x=150,y=100)

#Bottom box
Frame_image = PhotoImage(file='images\Box.png')
frame_myimage = Label(image=Frame_image)
frame_myimage.pack(padx=5,side=BOTTOM)


#time
name = Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock = Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)

#label
label1 = Label(root,text="wind",font=("helvetica",15,BOLD),bg="#1ab5ef",fg="white")
label1.place(x=120,y=400)

label2 = Label(root,text="Humidity",font=("helvetica",15,BOLD),bg="#1ab5ef",fg="white")
label2.place(x=250,y=400)

label3 = Label(root,text="Description",font=("helvetica",15,BOLD),bg="#1ab5ef",fg="white")
label3.place(x=400,y=400)

label4 = Label(root,text="Presure",font=("helvetica",15,BOLD),bg="#1ab5ef",fg="white")
label4.place(x=650,y=400)


t = Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c = Label(font=("arial",15,"bold"),bg="#1ab5ef")
c.place(x=400,y=250)

w = Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=120,y=430)
h = Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=280,y=430)
d = Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
d.place(x=420,y=430)
p = Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
p.place(x=670,y=430)




root.mainloop()