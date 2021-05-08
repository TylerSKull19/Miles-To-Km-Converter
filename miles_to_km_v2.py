#csc102 - Class 8 
# Miles to Km app
#Tyler Smith
# 4/5/2021

from tkinter import *

class Miles2KmApp:
    def __init__(self):
        window = Tk()
        Label(window, text="Enter miles:").grid(row=1,column=1)
        
        
        self.miles = DoubleVar()
        self.miles_box = Entry(window, textvariable=self.miles)
        self.miles_box.grid(row=1,column=2)
        
        self.miles_box.bind("<Return>", self.enter_handler)
        
        
        Button(window, text= "Convert miles to Km",
               command=self.convertbtn_handler).grid(row=2,column=1,
                                                     padx=10,pady=10,
                                                     sticky=W+E,
                                                     columnspan=2)
        
        Label(window,text="Kilometers:").grid(row=3,column=1)
        
        self.km_label = Label(window, text="0")
        self.km_label.grid(row=3,column=2,sticky=W)
        
        
        
        
        window.mainloop()
        
    def enter_handler(self,event):
        self.convertbtn_handler()
        
    def convertbtn_handler(self):
        print("Miles Entered", self.miles.get() )
        km = self.miles.get() * 1.6
        print("The kilometers are", km)
        self.km_label["text"] = str(km)
        
        
Miles2KmApp()