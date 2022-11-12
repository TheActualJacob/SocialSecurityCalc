from graph import Apper

import tkinter as tk


class Appe(tk.Frame):
    def calculations(var1, years):
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

            Apper.plottingmoney(lin, trys, loss, years, mountpermon, trying)