#Import tkinter Package for create GUI
from tkinter import *
from tkinter import ttk

#Caluclate Aria of circle
def calculate(*args):
    try:
        #convert radiouse in to float
        value = float(radiuse.get())
        #Set aria
        aria.set(float(22/7*value**2))
        #if user enter any non numbers
    except ValueError:
        pass


#initialize Window
window=Tk()
##Everything related to window  will here
#Setting the form properties
window.title("Aria Calculator")
mainframe=ttk.Frame(window,padding="3 3 12 12")
mainframe.grid(column=0,row=0,sticky=(N,W,E,S))

#Add Two controlers to explain What is this form
ttk.Label(mainframe, text="Calculating Aria of Cricle").grid(column=1, row=0, sticky=W)
ttk.Label(mainframe, text="Please Enter the Length of radiuse in cetnimeters =").grid(column=0, row=3, sticky=W)
ttk.Label(mainframe, text="Cetnimeters ").grid(column=2, row=3, sticky=W)
#Setting up text boxes
radiuse = StringVar()
radiuse_entry = ttk.Entry(mainframe, width=7, textvariable=radiuse)
radiuse_entry.grid(column=1, row=3, sticky=(W, E))

ttk.Button(mainframe, text="Calculate",command=calculate).grid(column=1, row=4, sticky=E)


#Lets setup output section
aria=StringVar()
ttk.Label(mainframe, text="Aria of Circle  =").grid(column=0, row=5, sticky=E)
ttk.Label(mainframe, textvariable=aria).grid(column=1, row=5, sticky=E)
ttk.Label(mainframe, text="Square centimeters").grid(column=2, row=5, sticky=E)
print(aria)

#Running loop until user close window
window.mainloop()
