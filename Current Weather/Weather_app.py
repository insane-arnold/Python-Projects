import tkinter as tk
import requests

HEIGHT = 500
WIDTH = 600

root = tk.Tk()
root.title("Current Weather")

#key = 75e0be8f993ab13cd50bd6c7716ba640
#API_url = api.openweathermap.org/data/2.5/forecast?q={city name},{country code}

def format_response(weather):
	print(weather)
	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']
		final = ("City: "+str(name)+"\nCondition: "+str(desc)+"\nTemp: "+str(temp)+"°C")

	except:
		final = "Error 404"

	return final	
	


def get_weather(city):
		weather_key = "75e0be8f993ab13cd50bd6c7716ba640"
		url = "https://api.openweathermap.org/data/2.5/weather"
		params = {"APPID" : weather_key, "q": city, "units":"Metric"}
		response = requests.get(url,params= params)
		weather = response.json()	
		label['text'] = format_response(weather)

canvas = tk.Canvas(root,height = HEIGHT,width = WIDTH )
canvas.pack()

background_image = tk.PhotoImage(file =  "C:\\Users\\HP\\Desktop\\Python\\Python Projects\\weather \\ccd7f44824f1364cc2a6b8d8dd0d2f7f.png")
background_label = tk.Label(root, image = background_image)
background_label.place(relwidth = 1,relheight=1)

frame = tk.Frame(root, bg = "#80c1ff")
frame.place(relx=0.5,rely = 0.15, relwidth = 0.75, relheight = 0.1,anchor = "n" )

entry = tk.Entry(frame,font = ("Courier",12 ))
entry.place(relwidth = 0.65, relheight = 1)

button = tk.Button(frame, text = "Get Weather",font = ("Courier",12),bd = 1, \
bg = "#f2f2f2",activebackground = "#ffffff",command = lambda: get_weather(entry.get()))
button.place(relx = 0.66, relwidth = 0.34, relheight = 1)

lowerframe = tk.Frame(root, bg = "#80c1ff", bd = 10)
lowerframe.place(relx=0.5,rely = 0.30, relwidth = 0.75, relheight = 0.65,anchor = "n" )

label = tk.Label(lowerframe,font = ("Terminal",15),justify = 'left')
label.place(relwidth = 1, relheight =1)

root.mainloop()
