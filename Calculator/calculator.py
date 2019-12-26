import tkinter as tk
import math

#for hightlighting the button when the cursor points it 

class HoverButton(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']

    def on_leave(self, e):
    	self['background'] = self.defaultBackground

class button_func():
	def getandreplace():
		expression = entry.get()
		newtext = expression.replace('÷','/')
		return newtext.replace('x','*')

	def press(num):
		entry.insert(END,num)

	def clear():
		entry.delete(0,END)

	def back():
		new_text = entry.get()[:-1]
		entry.delete(0,END)
		entry.insert(END,new_text)

	def equals():
		newtext = button_func.getandreplace()
		try:
			value = eval(newtext)
		except SyntaxError or NameError:
			entry.delete(0,END)
			entry.insert(0,'Invalid Input!!')
		else:
			entry.delete(0,END)
			entry.insert(0,value)

	def square():
		newtext = button_func.getandreplace()
		try:
			value= eval(newtext)
		except SyntaxError or NameError:
			entry.delete(0,END)
			entry.insert(0,'Invalid Input!!')
		else:
			sqval=math.pow(value,2)
			entry.delete(0,END)
			entry.insert(0,sqval)

	def sqroot():
		newtext = button_func.getandreplace()
		try:
			value = eval(newtext)
		except SyntaxError or NameError:
			entry.delete(0,END)
			entry.insert(0,"Invalid Input!!")
		else:
			squroot = math.sqrt(value)
			entry.delete(0,END)
			entry.insert(0,squroot)



#creating the button
def button():
	button_root = HoverButton(lower_frame,text ='\u221A',bd = 1,font = ('Helvetica', '20'),
		activebackground='#8c8c8c',bg = '#595959',command= lambda:button_func.sqroot())
	button_root.place(relwidth = 0.25,relheight = 0.02)

	button_pow = HoverButton(lower_frame,text = 'x²',bd = 1,font = ('Helvetica', '20'),
		activebackground='#8c8c8c',bg = '#595959',command= lambda:button_func.square())
	button_pow.place(relx=0.25,relwidth = 0.25,relheight = 0.02)

	button_C = HoverButton(lower_frame,text = 'C',bd = 1,font = ('Helvetica', '25'),fg = "red",
		activebackground='#8c8c8c',bg = '#595959',activeforeground='red',command= lambda:button_func.clear())
	button_C.place(relx=0.5,relwidth = 0.25,relheight = 0.02)

	button_back = HoverButton(lower_frame,text = chr(171),bd = 1,font = ('Helvetica', '20'),
		activebackground='#8c8c8c',bg = '#595959',command = lambda:button_func.back())
	button_back.place(relx= 0.75,relwidth = 0.25,relheight = 0.02)

	button_1 = HoverButton(lower_frame,text = '1',bd = 1,font = ('Helvetica', '20'),command = lambda: button_func.press(1),
		activebackground='#8c8c8c',bg = '#595959')
	button_1.place(rely = 0.02,relwidth = 0.25,relheight = 0.02)

	button_2 = HoverButton(lower_frame,text = '2',bd = 1,font = ('Helvetica', '20'),command = lambda: button_func.press(2),
		activebackground='#8c8c8c',bg = '#595959')
	button_2.place(rely= 0.02,relx = 0.25,relwidth = 0.25,relheight = 0.02)

	button_3 = HoverButton(lower_frame,text = '3',bd = 1,font = ('Helvetica', '20'),command = lambda: button_func.press(3),
		activebackground='#8c8c8c',bg = '#595959')
	button_3.place(relx=0.5,rely = 0.02,relwidth = 0.25,relheight = 0.02)

	button_4 = HoverButton(lower_frame,text = '4',bd = 1,font = ('Helvetica', '20'),command = lambda: button_func.press(4),
		activebackground='#8c8c8c',bg = '#595959')
	button_4.place(rely = 0.04,relwidth = 0.25,relheight = 0.02)

	button_5 = HoverButton(lower_frame,text = '5',bd = 1,font = ('Helvetica', '20'),command = lambda: button_func.press(5),
		activebackground='#8c8c8c',bg = '#595959')
	button_5.place(relx=0.25,rely = 0.04,relwidth = 0.25,relheight = 0.02)

	button_6 = HoverButton(lower_frame,text = '6',bd = 1,font = ('Helvetica', '20'),command = lambda: button_func.press(6),
		activebackground='#8c8c8c',bg = '#595959')
	button_6.place(relx=0.5,rely = 0.04,relwidth = 0.25,relheight = 0.02)

	button_7 = HoverButton(lower_frame,text = '7',bd = 1,font = ('Helvetica', '20'),command = lambda: button_func.press(7),
		activebackground='#8c8c8c',bg = '#595959')
	button_7.place(rely = 0.06,relwidth = 0.25,relheight = 0.02)

	button_8 = HoverButton(lower_frame,text = '8',bd = 1,font = ('Helvetica', '20'),command = lambda: button_func.press(8),
		activebackground='#8c8c8c',bg = '#595959')
	button_8.place(relx=0.25,rely = 0.06,relwidth = 0.25,relheight = 0.02)

	button_9 = HoverButton(lower_frame,text = '9',bd = 1,font = ('Helvetica', '20'),command = lambda: button_func.press(9),
		activebackground='#8c8c8c',bg = '#595959')
	button_9.place(relx=0.5,rely = 0.06,relwidth = 0.25,relheight = 0.02)

	button_0 = HoverButton(lower_frame,text = '0',bd = 1,font = ('Helvetica', '20'),command = lambda: button_func.press(0),
		activebackground='#8c8c8c',bg = '#595959')
	button_0.place(rely = 0.08,relwidth = 0.25,relheight = 0.02)

	button_dot = HoverButton(lower_frame,text = '.',bd = 1,font = ('Helvetica', '20'),command = lambda: button_func.press("."),
		activebackground='#8c8c8c',bg = '#595959')
	button_dot.place(relx=0.25,rely = 0.08,relwidth = 0.25,relheight = 0.02)

	button_equal = HoverButton(lower_frame,text = '=',bd = 1,font = ('Helvetica', '20'),activebackground='#8c8c8c',
		bg = '#595959',command= lambda: button_func.equals())
	button_equal.place(relx=0.5,rely = 0.08,relwidth = 0.25,relheight = 0.02)

	button_plus = HoverButton(lower_frame,text = '+',bd = 1,font = ('Helvetica', '20'),activebackground='#8c8c8c',
		bg = '#595959',command= lambda: button_func.press("+"))
	button_plus.place(rely=0.02,relx=0.75,relwidth = 0.25,relheight = 0.02)

	button_minus = HoverButton(lower_frame,text = '-',bd = 1,font = ('Helvetica', '20'),activebackground='#8c8c8c',
		bg = '#595959',command= lambda: button_func.press("-"))
	button_minus.place(relx=0.75,rely = 0.04,relwidth = 0.25,relheight = 0.02)

	button_multiply = HoverButton(lower_frame,text = 'x',bd = 1,font = ('Helvetica', '20'),activebackground='#8c8c8c',
		bg = '#595959',command= lambda: button_func.press("x"))
	button_multiply.place(relx=0.75,rely = 0.06,relwidth = 0.25,relheight = 0.02)

	button_div = HoverButton(lower_frame,text = '÷',bd = 1,font = ('Helvetica', '20'),activebackground='#8c8c8c',
		bg = '#595959',command= lambda: button_func.press("÷"))
	button_div.place(relx=0.75,rely = 0.08,relwidth = 0.25,relheight = 0.02)


#gui program mian window

window = tk.Tk()
window.title("Calculator")

canvas = tk.Canvas(window,height = 500, width = 400)
canvas.pack()

upper_frame = tk.Frame(window,bg = '#8c8c8c',bd = 2)
upper_frame.place(relheight = 0.26,relwidth = 1)

lower_frame = tk.Frame(window,bg = '#cccccc',bd = 1)
lower_frame.place(rely = 0.26,relheight=7.5,relwidth=1)

button()

END = 99
entry = tk.Entry(upper_frame,font = ('Helvetica',35),bg = '#8c8c8c',bd = 10)
entry.place(relwidth=1,relheight=1)
entry.focus_set()

window.mainloop()