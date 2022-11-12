
import matplotlib.pyplot as plt
import tkinter as tk
class Apper(tk.Frame):
    def plottingmoney(x, e, y, loss, z, m, p):

        figure, axis = plt.subplots(2, 2)

        
        axis[0 ,0].set_xlabel("Amount of years")
        axis[0, 0].set_ylabel("Payment per month")
        axis[0, 0].plot(e,x)
        axis[0, 0].set_title("New money per year after each year of waiting for ss")

        axis[1, 0].set_title("Money lossed every year before social secuirity")
        axis[1, 0].set_ylabel("Amount of years")
        axis[1, 0].set_xlabel('Amount of loss')
        axis[1, 0].plot(loss[:-1],y)
        print(y)
        
        mm = p
        ll = []
        orgm = m
        for l in range(z):
            mm.append(m)
            m = m+orgm
            

            ll.append(l)


            l = l +1

        print(mm)
        print(ll)




        
        
        #axis[0,1].plot([ll])
        axis[0, 1].set_title("Lossed vs Per month after wait")
        axis[0,1].plot(mm, label = 'Time to make back money')
        axis[0,1].plot(loss, label = 'Money missed out on')
        axis[0,1].set_ylabel('Money')
        axis[0,1].set_xlabel('years')
        
        

        

        
        
        plt.show()