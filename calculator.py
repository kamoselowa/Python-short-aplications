from tkinter import *

window = Tk()
window.title('calculator')

e = Entry(window,width=35,borderwidth=5)

e.grid(row=0, columnspan=3,padx=10,pady=10)
#--------button def-------$#
def buttontap():
    return
    

buttom_1 = Button(window,text='1',padx=40,pady=20,command=buttontap)
buttom_2 = Button(window,text='1',padx=40,pady=20,command=buttontap)
buttom_3 = Button(window,text='1',padx=40,pady=20,command=buttontap)
buttom_4 = Button(window,text='1',padx=40,pady=20,command=buttontap)
buttom_5 = Button(window,text='1',padx=40,pady=20,command=buttontap)
buttom_6 = Button(window,text='1',padx=40,pady=20,command=buttontap)
buttom_7 = Button(window,text='1',padx=40,pady=20,command=buttontap)
buttom_8 = Button(window,text='1',padx=40,pady=20,command=buttontap)
buttom_9 = Button(window,text='1',padx=40,pady=20,command=buttontap)
buttom_0 = Button(window,text='1',padx=40,pady=20,command=buttontap)

buttom_1.grid(row=3,colum=0)
buttom_2.grid(row=3,colum=1)
buttom_3.grid(row=3,colum=2)
buttom_4.grid(row=2,colum=0)
buttom_5.grid(row=2,colum=1)
buttom_6.grid(row=2,colum=2)
buttom_7.grid(row=1,colum=0)
buttom_8.grid(row=1,colum=1)
buttom_9.grid(row=1,colum=2)
buttom_0.grid(row=4,colum=0)
                  
