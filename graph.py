
import matplotlib.pyplot as plt
import tkinter as tk
class Apper(tk.Frame):
    def plottingmoney(x, y, loss, z, m, p):

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