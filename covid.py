from tkinter import *;
from PIL import ImageTk,Image
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''-----------------------------------------------------------------'''

home= Tk()
home.geometry('900x900')
home.title('Covid-19 Analysis')
home.config(bg='white')

my_img = ImageTk.PhotoImage(Image.open('image/main.jfif'))
my_label = Label(image = my_img)
my_label.pack()



L1 = Label(text = 'Data Analysis')
L1.config(font =('arial bold', 20), bg='white')
L1.pack(pady=20)

'''-----------------------------------------------------------------'''

df = pd.read_csv('Covid19India.csv')
data= df.iloc[ :, 1:]

def St_wise():
    st_wise = data[data['Current Status']=='Hospitalized'].groupby('Detected State')['Num Cases'].sum().sort_values(ascending = False)
    st_wise.plot.bar(figsize=(15,6))
    plt.title('State Wise Analysis of COVID-19',fontsize=20)
    plt.show()

def Age_wise():
    ab = data.groupby('Age Bracket')['Num Cases'].sum().sort_values(ascending= False).head(20)
    ab.plot.bar(figsize=(15,6))
    plt.title('Age Wise Analysis of COVID-19',fontsize=20)
    plt.show()

def Gender_wise():
    ab = data.groupby('Gender')['Num Cases'].sum().head(2)
    ab.plot.bar(figsize=(12,6),color= 'red')
    plt.xticks(rotation=0)
    plt.title('Gender Wise Analysis of COVID-19',fontsize=20)
    plt.show()
    
def Month_wise():
    ll = data.groupby('Month')['Num Cases'].sum()
    ll.plot.bar(figsize=(12,6),color= 'red')
    plt.xticks(rotation=0)
    plt.title('Month Wise Analysis of COVID-19',fontsize=20)
    plt.show()

def Total_wise():
    act = data[data['Current Status']=='Hospitalized'].groupby('Month')['Num Cases'].sum()
    act.plot(label= 'Active Cases',color='orange',marker='o',markerfacecolor='orange',markersize='5',linewidth= 1,figsize=(12,6))

    rec = data[data['Current Status']=='Recovered'].groupby('Month')['Num Cases'].sum()
    rec.plot(label = 'Recovered Cases',color='green',marker='^',markerfacecolor='green',markersize='5',linewidth= 1,figsize=(12,6))

    death = data[data['Current Status']=='Deceased'].groupby('Month')['Num Cases'].sum()
    death.plot(label = 'Death Cases',color='red',marker='s',markerfacecolor='orange',markersize='5',linewidth= 1,figsize=(12,6))

    plt.title('Total Case Analysis of COVID-19',fontsize=20)
    plt.legend()
    plt.show()

def Month_Day():
    home.destroy()
    import permonth

def reset():
    home.destroy()
    import main_window


'''-----------------------------------------------------------------'''

B1 = Button(home, text = ' State Wise Analysis ', command = St_wise)
B1.config(font=('',20),fg='red', bd=10)
B1.place(x=50,y=300)

B2 = Button(home, text = ' Age Wise Analysis  ', command = Age_wise)
B2.config(font=('',20),fg='red', bd=10)
B2.place(x=550, y= 300)


B3 = Button(home, text = 'Gender Wise Analysis', command = Gender_wise)
B3.config(font=('',20),fg='red', bd=10)
B3.place(x=50, y= 400)

B4 = Button(home, text = 'Month Wise Analysis ', command = Month_wise)
B4.config(font=('',20),fg='red', bd=10)
B4.place(x=550, y= 400)

B5 = Button(home, text = ' Total Case Analysis  ', command = Total_wise)
B5.config(font=('',20),fg='red', bd=10)
B5.place(x=50, y= 500)

B6 = Button(home, text = ' Month-Day Analysis ', command = Month_Day)
B6.config(font=('',20),fg='red', bd=10)
B6.place(x=550, y= 500)

B7 = Button(home, text = 'Return Home', command = reset)
B7.config(font=('',10),fg='white', bg = 'red')
B7.place(x=40, y= 40)

home.mainloop()
