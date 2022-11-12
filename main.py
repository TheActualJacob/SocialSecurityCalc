import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
from calculate import Appe



class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.CreateWidgets()


    def CreateWidgets(self):




        
        
        self.btnFrame = tk.Frame(self)
        self.year1label = tk.Label(self.btnFrame, text='Amount of years')
        self.var1Entry = tk.Entry(self.btnFrame, text = int)
        self.yearsEntry = tk.Entry(self.btnFrame, text = int)
        self.txtResult = tk.Text(self, width=30, height=15)
        self.caclbutton = tk.Button(self.btnFrame, text = 'Calculate', command = self.calculate)
        self.yeaa = tk.Label(self.btnFrame, text='Monthly payments currently')
        

        
                


        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=3)
        self.var1Entry.grid(row=1, column=1, sticky="ns", padx=5, pady=5)
        self.yearsEntry.grid(row=1, column=2, sticky="ns",padx=5, pady=5)
        self.txtResult.grid(row=2, column=0, sticky="nsew")
        self.btnFrame.grid(row=1, column=0, sticky="ns")
        self.year1label.grid(row=0, column=2, sticky='e',padx=5,pady=5)
        self.caclbutton.grid(row=1, column=0, sticky="we",padx=5, pady=5)
        self.yeaa.grid(row=0, column=1,sticky='w')



    


    def calculate(self):
        try:
            money = int(self.var1Entry.get())
            year = int(self.yearsEntry.get())
        except:
            self.txtResult.insert(tk.END, 'Must be a valid integer inside boxes. \n Look at Read.me for more info \n \n')
        
        
        else:
            Appe.calculations(money, year)

     
        


        

 
        

   
        


   


        
        
                
        
        
    

root = tk.Tk()
root.geometry("600x900")
root.title("Social Security Calculator")
root.rowconfigure(0, minsize=800, weight=1)
root.columnconfigure(1, minsize=600, weight=1)
app = Application(master=root)
app.mainloop()
root.mainloop()

    



        
            
        
       
        



        
            

       
            

    

        

    


