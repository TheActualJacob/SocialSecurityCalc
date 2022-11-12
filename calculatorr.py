import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np


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
            self.calculations(money, year)

        
    def calculations(self, var1, years):
        #intvals = self.yearsEntry.get()
        
        #years = int(intvals)
        i = int(0)
        

        yearly = var1*12
        
        trying = []
        lin = []
        trys = []
        
        for i in range (years):
            yearly = yearly*.1+yearly
            lin.append(int(yearly))

            trying.append(i-i)
            
            
            

            i= i+1
            mountpermon = yearly/12
        

        

        for u in range(years+years):
            trys.append(u)
            u = u+1


        
       
        loss = []

        b = 0
        var112 = var1
        org = var112
        for b in range(int(len(trying+trying))):
            var112 = var112 + org
            loss.append(var112)

            b = b+1
            
        

        #print(loss)

        self.plottingmoney(lin, trys, loss, years, mountpermon, trying)
        


        

       

    def plottingmoney(self, x, y, loss, z, m, p):

        figure, axis = plt.subplots(2, 2)

        
        axis[0 ,0].set_xlabel("Amount of years")
        axis[0, 0].set_ylabel("Payment per month")
        axis[0, 0].plot(x)
        axis[0, 0].set_title("New money per month after each year of waiting for ss")

        axis[1, 0].set_title("Money lossed every year before social secuirity")
        axis[1, 0].set_ylabel("Amount of years")
        axis[1, 0].set_xlabel('Amount of loss per month')
        axis[1, 0].plot(loss, y)
        #print(y)
        
        mm = p
        ll = []
        for l in range(z):
            m = m+m
            mm.append(m)

            ll.append(l)


            l = l +1




        
        axis[0,1].plot([ll])
        axis[0, 1].set_title("Lossed vs Per month after wait")
        axis[0,1].plot(mm, label = 'Time to make back money')
        axis[0,1].plot(loss, label = 'Money missed out on')
        

        

        
        
        plt.show()
        

   
        


   


        
        
                
        
        
    

root = tk.Tk()
root.geometry("600x900")
root.title("Social Security Calculator")
root.rowconfigure(0, minsize=800, weight=1)
root.columnconfigure(1, minsize=600, weight=1)
app = Application(master=root)
app.mainloop()
root.mainloop()

    



        
            
        
       
        



        
            

       
            

    

        

    


