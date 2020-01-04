
import tkinter as kin
import tkinter as tk
from tkinter import *
from tkinter import messagebox as tkmessagebox
from tkinter.font import Font
from tkinter import messagebox
import time
import random
from time import sleep

import time
    
top = kin.Tk()
top.geometry("1920x1080")

def irsensor():
    import RPi.GPIO as IO
    IO.setwarnings(False)
    IO.setmode(IO.BOARD)
    
    IO.setup(8,IO.OUT) #GPIO 2 -> Red LED as output
    IO.setup(10,IO.OUT) #GPIO 3 -> Green LED as output
    IO.setup(16,IO.IN) #GPIO 14 -> IR sensor as input
    i=0
    win1=Toplevel(bg='black',height='1000',width='2000')
    win1.title('IR SENSOR')
    g=Label(win1,text='connect ir sensor to pins 5V-pin2: gnd-pin14: out-pin16 along with ground connection', font=('Blackletter', 17),fg='orange')
    g.pack()
    def df():
        while i==0:

            if(IO.input(16)==True): #object is far away
                IO.output(8,True) #Red led ON
                IO.output(10,False) # Green led OFF
    
            if(IO.input(16)==False): #object is near
                 IO.output(8,True) #Green led ON
                 IO.output(10,False) # Red led OFF
            i=1
    
            

    def ah():
        win1.destroy()
        
    exitbut=Button(win1,text='exit',fg='blue',height='1',width='4',command=ah)
    detect=Button(win1,text='lets detect',command=df,height='2',width='6')
    detect.place(x=20,y=56)
    detect.pack()
    exitbut.pack()
    IO.output(8,False) #Red led ON
    IO.output(10,False)
    
def uvsensor():
    import RPi.GPIO as GPIO
    import threading
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    
    TRIG=36
    ECHO=38
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    global is_busy,thread1 
    is_busy=0
  
    win=Toplevel(bg='black',height='1000',width='2000')  
    
    def exitProgram():
       # if messagebox.askyesno("Print", "Exit?"):
            thread1.exit = 1
            sleep(0.300)
            
            win.destroy()
            
    originalPlantImage = tk.PhotoImage(file="asd.png")
    image = originalPlantImage.subsample(15, 15)
    exitb = tk.Button(win,text="Exit",image=image,font=("Helvetica", 14,'bold'),compound="left",borderwidth=3,
            width = 60,height = 30,bg="lightskyblue",fg='black',command= exitProgram,
            activebackground="dark gray")
    g=Label(win,text='connect uv sensor in pins trig-36, echo-38 along with ground connection', font=('Blackletter', 10),)
    g.pack()
    
    exitb.pack(fill=X,padx=2)

    def measure_dis():
        GPIO.output(TRIG, False)
        sleep(2)
        GPIO.output(TRIG, True)
        sleep(0.00001)
        GPIO.output(TRIG, False)
        while GPIO.input(ECHO)==0:
            pulse_start= 0
        pulse_start= time.time()
        while GPIO.input(ECHO)==1:
            pulse_end= 0
        pulse_end= time.time()
        pulse_duration = pulse_end-pulse_start
        distance= pulse_duration*18000
        distance= round(distance,2)
        DistMax.set(str(distance)+' cm')
        print('dist:',distance,'cm')
    
    def do_task():
        global is_busy,thread1
        if is_busy:
            is_busy = 0
            thread1.doit = 0
            loop_it.configure(text="start")
        else:
            is_busy=1
            thread1.doit = 1
            loop_it.configure(text="stop")


    loop_it = tk.Button(win,text="start",font=("Helvetica", 12,'bold'),
            compound="left",
            borderwidth=3,
            width = 20,
            height = 10,              
            bg="lightskyblue",
            fg='white',
            command= do_task,
            activebackground="dark gray")
    loop_it.pack(side=LEFT,padx=20)

            
    class HC_SR04_Thread (threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
            self.doit=0
            self.exit = 0
        def run(self):
            while self.exit == 0:
                if self.doit == 1:
                    try:
                        measure_dis()
                    except:                                        
                        print('Error1')
                    pass
            
    GPIO.output(TRIG, False)
    sleep(2)
    thread1 = HC_SR04_Thread()
    thread1.start()
    DistMax=StringVar()
    DistMax.set('')
    dist_max = Label(win, textvariable=DistMax,width=10,height=2, font=("Helvetica", 14),bg= 'black',fg="white", borderwidth=2,relief="sunken")#ridge
    dist_max.pack(side =LEFT,padx=10)

    top.mainloop()

def ak():

    import RPi.GPIO as IO
    import time
    IO.setwarnings(False)
    IO.setmode(IO.BOARD)
    
    IO.setup(24,IO.OUT) #GPIO 2 -> Red LED as output
    win=Toplevel(bg='black',height='1000',width='2000')
    win.title('LED button clickz')
    g=Label(win,text='connect led to pin 24 along with ground connection pin 6', font=('Blackletter', 17),)
    g.pack()
    g.place(x=0, y=0)
    

    def lt():
        IO.output(24,True)
    def li():
        IO.output(24,False)
    def exitprogram():
        IO.output(24,False)    
        
        win.quit()
        win.destroy()

    ledbutton=kin.Button(win, text='TURN LED ON', command=lt, bg='pink' ,height=1, width=24)
    ledbutton.place(x=24 ,y=45)
    ledbutton=kin.Button(win, text='TURN LED OFF', command=li, bg='pink' ,height=1, width=24)
    ledbutton.place(x=24 ,y=75)

    exib=kin.Button(win, text='exit',  command=exitprogram, bg='cyan', height=1, width=4)
    exib.place(x=50, y=120)
def aran():
    win=Toplevel(bg='black',height='1000',width='2000')
    img5=PhotoImage(file="rsz_sensors.png", height='1000', width='2000')
    la1=Label(win, image=img5, height='1000', width='1500')
    la1.image=img5
    la1.pack()
    uv=kin.Button(win,text='UV SENSOR',height='2', width='7', bd=1, command=uvsensor)
    uv.pack()
    uv.place(x=380,y=100)
    ir=kin.Button(win,text='IR SENSOR',height='2', width='7', bd=1,command=irsensor)
    ir.pack()
    ir.place(x=380,y=175)
    gs=kin.Button(win,text='GAS SENSOR',height='2', width='7', bd=1)
    gs.pack()
    gs.place(x=380,y=250)
    win.quit()
  
def anil():
   
   b1.forget()
   img5=PhotoImage(file="background.png", height='1000', width='2000')
   la=Label(top, image=img5, height='1000', width='1500')
   la.image=img5
   la.pack()
  
  
   bla=kin.Button(top,text='LEDBULB',height='1',  width='5', font=('comicsans'), bd=0, command=ak)
 
   bla.pack()
   bla.place(x=290,y=110)

   redbutton = Button(top, text="SENSORs",fg="red", height='1', font=('comicsans'), width='5', bd=0, command=aran)
  
   redbutton.pack()
   redbutton.place(x=230,y=145) 
   
   greenbutton = Button(top, text="WIFI", fg="brown", bg='white', height='1', font=('comicsans'), width='5', bd=0)
   
   greenbutton.pack()
   greenbutton.place(x=360,y=145)
   
   bluebutton = Button(top,text='CLOUD',  fg="yellow", height='1', font=('comicsans'), width='5', bd=0 )
   
   
   bluebutton.pack()
   bluebutton.place(x=290,y=190)
   
   
   
img=kin.PhotoImage(file="asd.png")
b1=Button(top, justify=CENTER, image=img, height='1080', width='1920', command=anil)
b1.config(image=img, compound=LEFT )
b1.pack()

top.mainloop()

