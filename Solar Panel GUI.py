import tkinter as tk
# ~ from adafruit_motorkit import MotorKit
# ~ from adafruit_motor import stepper
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from PIL import ImageTk,Image
import csv
import time
#import RPi.GPIO as GPIO


#Setting fonts and color of background.
LARGE_FONT= ("Times New Roman", 50)
color = "light blue"





#Declare class to create main frame.
class signIn(tk.Tk):
	#This is a method in python, it is like a function in python.  
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		#Create a frame
		container = tk.Frame(self)
		#Place the frame on screen.
		container.grid(row=0)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)
		container.grid_rowconfigure(1, weight=1)
		container.grid_columnconfigure(1, weight=1)
		self.frames = {}
        #The page you create goes here.    
		for page in (MainPage, ManualControl):
            					
			frame = page(container, self)
			self.frames[page] = frame
			frame.grid(row=0, column=0, sticky="nsew")
		#This starts code at log in page.
		self.show_frame(MainPage)
	#Method that allows to jump from page to page.
	def show_frame(self, cont):

		frame = self.frames[cont]
		frame.tkraise()
        
#This is the main menu page.    
class MainPage(tk.Frame):
    
	#Link frame with main frame.
	def __init__(self, parent, controller):
		
		tk.Frame.__init__(self, parent)
		tk.Frame.config(self, bg = color)
		self.grid_rowconfigure(1, weight=1)
		self.grid_columnconfigure(1, weight=1)
	

		#Defining Functions
		def AFunction():				# Include the Value of the weight here by calling the Load Cell Programs
			messagebox.showinfo("Powering Off", "Program is no longer running...")


	
	

		#Create Widgets and stuff

		#Buttons
		AButton = tk.Button(self, text = "Manual Control", command = lambda: controller.show_frame(ManualControl) , height= 10, width =20)
		BButton = tk.Button(self, text = "Poweroff", command = AFunction, height = 10, width = 20)

		#Labels
		FLabel = tk.Label(self, width = "50", height = "5" ,  text = "Power Generated (W): ", font = (40),bg = 'light blue' )
		XLabel = tk.Label(self, width = "10", height = "5" ,  text = "124 W", font = (40), fg = 'black', bg = 'green',relief = RAISED)
		XLabel.config(font=("Times New Roman", 30))

		#Picture
		self.root = tk.Frame()
		self.root.grid()
		self.image = tk.PhotoImage(file='Solar Panel.png')
		self.gmail = tk.Label(self.root, image=self.image, bg = 'light blue')
		self.gmail.grid(row = 10, column = 5)
		# ~ img = ImageTk.PhotoImage(Image.open("Solar Panel.png"))
		# ~ panel = tk.Label(self, image = img , bg = 'light blue')


		#Sizing the Window
		# ~ self.geometry("500x300+700+250")

		#Placing them in the window
		# ~ panel.grid(row = 5, column = 3)
		XLabel.grid( row = 3, column = 4)
		FLabel.grid( row = 3, column = 3)
		AButton.grid(row = 3, column = 2)
		BButton.grid(row = 3, column = 6, padx = 100)
		
		#This give the code a live clock.
		# ~ clock = tk.Label(self, bg = 'white')
		# ~ clock.grid(row=0,column = 0,padx = 10, pady =10)
		# ~ def tick():
			# ~ s = time.strftime('%a, %m/%d/%Y %I:%M:%S')
			# ~ if s != clock["text"]:
				# ~ clock["text"] = s
			# ~ clock.after(200, tick)
		# ~ tick()
		

		
		

class ManualControl(tk.Frame):
	
	def __init__(self, parent, controller):
		
		tk.Frame.__init__(self, parent)
		tk.Frame.config(self, bg = color)
		self.grid_rowconfigure(1, weight=1)
		self.grid_columnconfigure(1, weight=1)
		
		#Defining Functions
		def DFunction():				# Include the Value of the weight here by calling the Load Cell Programs
			messagebox.showinfo("Powering off", "Program has stopped...")


		
	
		def UpMove():
			print("Moving up...")
	
		def DownMove():
			print("Moving down...")
	
		def LeftMove():
			print("Moving left...")	
	
		def RightMove():
			print("Moving right...")	

		#Create Widgets and stuff

		#Buttons
		AButton = tk.Button(self, text = "Automatic", command = lambda:controller.show_frame(MainPage) , height= 10, width =20)
		BButton = tk.Button(self, text = "Poweroff", command = DFunction, height = 10, width = 20)
		UPButton = tk.Button(self, text = "Up", command = UpMove, height = 5, width = 10, bg = 'orange')
		DOWNButton = tk.Button(self, text = "Down", command = DownMove, height = 5, width = 10, bg = 'orange')
		LEFTButton = tk.Button(self, text = "Left", command = LeftMove, height = 5, width = 10, bg = 'orange')
		RIGHTButton = tk.Button(self, text = "Right", command = RightMove, height = 5, width = 10, bg = 'orange')

#Labels
		FLabel = tk.Label(self, width = "50", height = "5" ,  text = "Power Generated (W): ", font = (40),bg = 'light blue' )
		XLabel = tk.Label(self, width = "10", height = "5" ,  text = "124 W", font = (40), fg = 'black', bg = 'green',relief = RAISED)
		XLabel.config(font=("Times New Roman", 30))

#Picture
# ~ img = ImageTk.PhotoImage(Image.open("Solar Panel.png"))
# ~ panel = Label(Main, image = img , bg = 'light blue')


#Sizing the Window
		# ~ Main.geometry("500x300+700+250")

#Placing them in the window
# ~ panel.pack(side = "bottom", fill = "both", expand = "no")
		UPButton.grid( row = 2, column = 4)
		DOWNButton.grid( row = 4, column = 4)
		LEFTButton.grid( row = 3, column = 3)
		RIGHTButton.grid( row = 3, column = 5)
		AButton.grid(row = 3, column = 2, padx = 200)
		BButton.grid(row = 3, column = 6, padx = 200)
		
    


        

if __name__ == "__main__":
	window = signIn()
	# ~ window.grid(sticky="nsew")
	window.grid_rowconfigure(0, weight=1)
	window.grid_columnconfigure(0, weight=1)
	window.title("EEME MedDis 1819 V1.1")
	window.attributes('-fullscreen',True)
# ~ window.geometry("1000x700")
	window.configure(background = color)
	window.mainloop()
