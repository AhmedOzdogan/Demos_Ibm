# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 00:16:37 2020

@author: Ahmed
"""

from tkinter import *

root = Tk() 


class Buttons:
    def __init__(self, master):
        #master = root
        
        frame = Frame(master)
        frame.pack()     
        
        self.printButton = Button(frame, text = "Print Message", command = self.printMessage)
        self.printButton.pack(side = LEFT)
        
        self.quitButton = Button(frame, text = "Quit", command = frame.quit)
        self.quitButton.pack(side = LEFT)
        
    
    def printMessage(self):
        print("Wow worked!! :)")
        
b = Buttons(root)






















root.mainloop()
