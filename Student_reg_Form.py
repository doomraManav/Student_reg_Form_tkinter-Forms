from tkinter import *
from tkinter import ttk
from tkinter import Text
window=Tk()
window.title('STUDENT REGISTRATION FORM')
window.configure(bg='#797EF6')

Label(window,text='FIRST NAME',fg='white',bg='#797EF6').grid(row=1,sticky='W')
Label(window,text='LAST NAME',fg='white',bg='#797EF6').grid(row=2,sticky='W')
Entry(window).grid(row=1,column=1)
Entry(window).grid(row=2,column=1)
Label(window,text='(max 30 characters a-z and A-Z)',fg='white',bg='#797EF6').grid(row=1,column=2,pady=10)
Label(window,text='(max 30 characters a-z and A-Z)',fg='white',bg='#797EF6').grid(row=2,column=2,pady=10)

#########

Label(window,text='DATE OF BIRTH',fg='white',bg='#797EF6').grid(row=3,sticky='W')
frame = Frame(window)
frame.configure(bg='#797EF6')
frame.grid(row=3, column=1, pady=10)
combo=ttk.Combobox(frame,width='4')
combo['values']=("Day:",1,2,3,4,5,6,7,8,9,10,11,12,13,"furthur")
combo.current(0)
combo.pack( side = LEFT ,padx = 10)
#combo.grid(row=3,column=1,padx=5)
comb=ttk.Combobox(frame,width='8')

comb['values']=("Month:","JANUARY","FEBRUARY","MARCH","APRIL","MAY","JUNE","furthur")
comb.current(0)
comb.pack( side = LEFT ,padx = 10)
#comb.grid(row=3,column=2)
com=ttk.Combobox(frame,width='4')

com['values']=("Year:",1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002)
com.current(0)
com.pack( side = LEFT ,padx = 10)
#com.grid(row=3,column=3,pady=10)

Label(window,text='EMAIL ID',fg='white',bg='#797EF6').grid(row=4,sticky='W')
Entry(window).grid(row=4,column=1)

Label(window,text='MOBILE NUMBER',fg='white',bg='#797EF6').grid(row=5,sticky='W',pady=10)
Entry(window).grid(row=5,column=1,padx=10)

Label(window,text='(10 digit number)',fg='white',bg='#797EF6').grid(row=5,column=2)

Label(window,text='GENDER',fg='white',bg='#797EF6').grid(row=6,column=0,sticky='W')
v=IntVar()

Radiobutton(window,text='Male',fg='black',bg='#797EF6',variable=v,value=1).grid(row=6,column=1)

Radiobutton(window,text='Female',fg='black',bg='#797EF6',variable=v,value=2).grid(row=6,column=2)

Label(window,text='ADDRESS',fg='white',bg='#797EF6').grid(row=7,sticky='W',column=0)
Text(window,width='30',height='5').grid(row=7,column=1,pady=10)

Label(window,text='CITY',fg='white',bg='#797EF6').grid(row=8,column=0,sticky='W')
Entry(window).grid(row=8,column=1)

Label(window,text='(max 30 characters a-z and A-Z)',fg='white',bg='#797EF6').grid(row=8,column=2,pady=10)

Label(window,text='PINCODE',fg='white',bg='#797EF6').grid(row=9,column=0,sticky='W')
Entry(window).grid(row=9,column=1)

Label(window,text='(6 digit number)',fg='white',bg='#797EF6').grid(row=9,column=2,pady=10)

Label(window,text='State',fg='white',bg='#797EF6').grid(row=10,column=0,sticky='W')
Entry(window).grid(row=10,column=1)

Label(window,text='(max 30 characters a-z and A-Z)',fg='white',bg='#797EF6').grid(row=10,column=2,pady=10)

Label(window,text='Country',fg='white',bg='#797EF6').grid(row=11,column=0,sticky='W')
Entry(window).grid(row=11,column=1)

Label(window,text='HOBBIES',fg='white',bg='#797EF6').grid(row=12,column=0,sticky='W')
var1=IntVar()

Checkbutton(window,text='Drawing',variable=var1,fg='black',bg='#797EF6').grid(row=12,column=1)
var2=IntVar()

Checkbutton(window,text='Singing',variable=var2,fg='black',bg='#797EF6').grid(row=12,column=2)
var3=IntVar()

Checkbutton(window,text='Dancing',variable=var3,fg='black',bg='#797EF6').grid(row=12,column=3)
var4=IntVar()

Checkbutton(window,text='Sketching',variable=var4,fg='black',bg='#797EF6').grid(row=12,column=4)
var5=IntVar()

Checkbutton(window,text='Others',variable=var5,fg='black',bg='#797EF6').grid(row=13,column=1,pady=10)
Entry(window).grid(row=13,column=2)

Label(window,text='QUALIFICATION',fg='white',bg='#797EF6').grid(row=14,column=0,sticky='W')
Label(window,text='SI.No.',fg='white',bg='#797EF6').grid(row=14,column=1)
Label(window,text='Examination',fg='white',bg='#797EF6').grid(row=14,column=2)
Label(window,text='Board',fg='white',bg='#797EF6').grid(row=14,column=3)
Label(window,text='Percentage',fg='white',bg='#797EF6').grid(row=14,column=4)
Label(window,text='Year of passing',fg='white',bg='#797EF6').grid(row=14,column=5)
Label(window,text='1',fg='white',bg='#797EF6').grid(row=15,column=1)
Label(window,text='2',fg='white',bg='#797EF6').grid(row=16,column=1)
Label(window,text='3',fg='white',bg='#797EF6').grid(row=17,column=1)
Label(window,text='4',fg='white',bg='#797EF6').grid(row=18,column=1)
Label(window,text='ClassX',fg='white',bg='#797EF6').grid(row=15,column=2)
Label(window,text='ClassXII',fg='white',bg='#797EF6').grid(row=16,column=2)
Label(window,text='Graduation',fg='white',bg='#797EF6').grid(row=17,column=2)
Label(window,text='Masters',fg='white',bg='#797EF6').grid(row=18,column=2)
Entry(window).grid(row=15,column=3)
Entry(window).grid(row=16,column=3)
Entry(window).grid(row=17,column=3)
Entry(window).grid(row=18,column=3)
Entry(window).grid(row=15,column=4)
Entry(window).grid(row=16,column=4)
Entry(window).grid(row=17,column=4)
Entry(window).grid(row=18,column=4)
Entry(window).grid(row=15,column=5)
Entry(window).grid(row=16,column=5)
Entry(window).grid(row=17,column=5)
Entry(window).grid(row=18,column=5)
Label(window,text='(10 char max)',fg='white',bg='#797EF6').grid(row=19,column=3)
Label(window,text='(upto 2 decimal)',fg='white',bg='#797EF6').grid(row=19,column=4)
Label(window,text='COURSES APPLIED FOR',fg='white',bg='#797EF6').grid(row=20,column=0)
k=IntVar()
Radiobutton(window,text='BCA',fg='black',bg='#797EF6',variable=k,value=1).grid(row=20,column=1)
Radiobutton(window,text='B.Com',fg='black',bg='#797EF6',variable=k,value=2).grid(row=20,column=2)
Radiobutton(window,text='B.Sc',fg='black',bg='#797EF6',variable=k,value=3).grid(row=20,column=3)
Radiobutton(window,text='B.A',fg='black',bg='#797EF6',variable=k,value=4).grid(row=20,column=4)
Button(window,text='Submit',width=10,height=1).grid(row=21,column=4)
Button(window,text='Reset',width=10,height=1).grid(row=21,column=5)
Button(window,text='Submit',width=10,height=1).grid(row=21,column=4,ipadx = 100)
mainloop()
