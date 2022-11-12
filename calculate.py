from graph import Apper

import tkinter as tk


class Appe(tk.Frame):
    def calculations(var1, years):
            #intvals = self.yearsEntry.get()
            
            #years = int(intvals)
            
            

            yearly = var1*12
            
            trying = []
            lin = []
            trys = []
            
            for i in range (years+years):
                yearly = yearly*.1+yearly
                lin.append(int(yearly))

                
            
                
                

                i= i+1
                mountpermon = yearly

            ii = 0
            for ii in range (years):
                trying.append(ii-ii)
                ii = ii +1

            slop = []

            iii = 0
            for iii in range (years+1):
                slop.append(iii-iii)
                iii = iii +1

        

            

            
            u =1
            for u in range(years+years):
                trys.append(u)
                u = u+1

            e = []
            er = 1
            for er in range(len(lin)):
                e.append(er)
                er = er+1

            print(e)
            print(lin)
            
            print(trys)
                

            loss = []

            b = 0
            var112 = 0
            org = var1*12
            for b in range(int(len(trying+trying)+1)):
                loss.append(var112)
                var112 = var112 + org
                

                b = b+1
                
            

            print(loss)

            Apper.plottingmoney(lin, e, trys, loss, years, mountpermon, slop)