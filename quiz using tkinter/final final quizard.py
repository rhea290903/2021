import tkinter
from tkinter import*
from tkinter import messagebox
import tkinter.font as font
import mysql.connector as mys
from  tabulate import tabulate



rt1=Tk()


'''----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
#buttoncommands


arts=0
def artscore():
     global arts
     arts+=100
def storeart(user1):
     art5.destroy()
     username=user1.get()
     print(username)
     print(arts)
     mycon=mys.connect(host="localhost",user="root",passwd="root",database="login")
     mycur=mycon.cursor()
     mycur.execute("select*from main")
     l=mycur.fetchall()
     
     
     
     sql="update main set art={} where username='{}' ".format(arts,username)
     mycur.execute(sql)
     mycon.commit()
     mycon.close()
     if arts==100:
          root=Tk()
          canvas = Canvas(root)
          canvas.pack()
          x, y= 0, 0
          for _ in range(100):
              canvas.create_text(x, y, text='\ud83d\ude4f', anchor=NW)
              y += 10

def art5(user1):
     art4.destroy()
     print(user1)
     global art5
     #art4.destroy()
     art5=Tk()
     
     art5.configure(background="white")
     art5.geometry("500x250+725+335")
     
     #question5
     v5=IntVar()
     q5=Label(art5,text='5.Creation of Adam is one of nine scenes featured on the \n ceiling  of which Rome landmark?' , fg='black', bg='white' ,font=('ink free',14))
     val_=5
     r_51=Radiobutton(art5,text= "The Sistine Chapel",fg="black",bg="white",variable=v5,value=1,command =artscore)
     r_52=Radiobutton(art5,text= "The Greta Chapel",fg="black",bg="white",variable=v5,value=2)
     r_53=Radiobutton(art5,text= "Adam's Celing",fg="black",bg="white",variable=v5,value=3)
     r_54=Radiobutton(art5,text= "The Roman enclave",fg="black",bg="white",variable=v5,value=4)
     q5.place(x=20 ,y=25)
     r_51.place(x=20 ,y=75)
     r_52.place(x=20 ,y=105)
     r_53.place(x=20 ,y=135)
     r_54.place(x=20 ,y=165)
     next5=Button(art5,text= "submit",fg="black",bg="white",command =lambda  user1=user1: storeart(user1)).place(x=20,y=210)

def art4(user1):
     art3.destroy()
     print(user1)
     global art4
    # art3.destroy()
     art4=Tk()
     
     art4.configure(background="white")
     art4.geometry("500x250+725+335")
    
     #question4
     v4=IntVar()
     q4=Label(art4,text='4.What is the name of the fourth book in the Harry Potter  \n series?' , fg='black', bg='white' ,font=('ink free',14))
     val_=4
     r_41=Radiobutton(art4,text= "Harry Potter and the Goblet of Fire",fg="black",bg="white",variable=v4,value=1,command =artscore)
     r_42=Radiobutton(art4,text= "Harry Potter and the Prizoner Of Azkaban",fg="black",bg="white",variable=v4,value=2)
     r_43=Radiobutton(art4,text= "Harry Potter and the Deathly Hallowa",fg="black",bg="white",variable=v4,value=3)
     r_44=Radiobutton(art4,text= "Harry Potter and the philosopher's stone",fg="black",bg="white",variable=v4,value=4)
     q4.place(x=20 ,y=25)
     r_41.place(x=20 ,y=75)
     r_42.place(x=20 ,y=105)
     r_43.place(x=20 ,y=135)
     r_44.place(x=20 ,y=165)
     next4=Button(art4,text= "next",fg="black",bg="white",command =lambda  user1=user1: art5(user1)).place(x=20,y=210)
def art3(user1):
     art2.destroy()
     print(user1)
     global art3
     #art2.destroy()
     art3=Tk()
     
     art3.configure(background="white")
     art3.geometry("500x250+725+335")
     
     v3=IntVar()
     q3=Label(art3,text='3.Which artist painted the Poppy Field in 1873?', fg='black', bg='white' ,font=('ink free',14) )
     r_31=Radiobutton(art3,text= "Luna Anthony",fg="black",bg="white",variable=v3,value=1)
     r_32=Radiobutton(art3,text= "Mark Johanson",fg="black",bg="white",variable=v3,value=2)
     r_33=Radiobutton(art3,text= "laude Monet",fg="black",bg="white",variable=v3,value=3,command =artscore)
     r_34=Radiobutton(art3,text= "Emma Stone",fg="black",bg="white",variable=v3,value=4)
     q3.place(x=20 ,y=25)
     r_31.place(x=20 ,y=75)
     r_32.place(x=20 ,y=105)
     r_33.place(x=20 ,y=135)
     r_34.place(x=20 ,y=165)
     next3=Button(art3,text= "next",fg="black",bg="white",command =lambda  user1=user1: art4(user1)).place(x=20,y=210)
def art2(user1):
     print(user1)
     art.destroy()
     global art2
     #art.destroy()
     #question2
     art2=Tk()
     
     
     art2.configure(background="white")
     art2.geometry("500x250+725+335")
     
     v2=IntVar()
     q2=Label(art2,text='2.The Mona Lisa by Leonardo da Vinci is on display in  \n which Paris museum?', fg='black', bg='white' ,font=('ink free',14) )
     r_21=Radiobutton(art2,text= "Enomre",fg="black",bg="white",variable=v2,value=1)
     r_22=Radiobutton(art2,text= "Louvre",fg="black",bg="white",variable=v2,value=2,command =artscore)
     r_23=Radiobutton(art2,text= "Musée De Paris",fg="black",bg="white",variable=v2,value=3)
     r_24=Radiobutton(art2,text= "National meuseum of france",fg="black",bg="white",variable=v2,value=4)
     q2.place(x=20 ,y=25)
     r_21.place(x=20 ,y=75)
     r_22.place(x=20 ,y=105)
     r_23.place(x=20 ,y=135)
     r_24.place(x=20 ,y=165)
     next2=Button(art2,text= "next",fg="black",bg="white",command =lambda  user1=user1: art3(user1)).place(x=20,y=210)
    
def art_literature(user1):
     print(user1)
     global art
     art=Tk()
     
     art.configure(background="white")
     art.geometry("500x250+725+335")
     
     #question1
     v1=IntVar()
     q1=Label(art,text="1.Hippolyta is a character from which of these shakespearean \n books?", fg='black', bg='white' ,font=('ink free',14))
     r11=Radiobutton(art,text= "A Midsummer Night's Dream",fg="black",bg="white",variable=v1,value=1,command =artscore)
     r12=Radiobutton(art,text= "Othello",fg="black",bg="white",variable=v1,value=2)
     r13=Radiobutton(art,text= "MacBeth",fg="black",bg="white",variable=v1,value=3)
     r14=Radiobutton(art,text= "Hamlet",fg="black",bg="white",variable=v1,value=4)
     q1.place(x=20 ,y=25)
     r11.place(x=20 ,y=75)
     r12.place(x=20 ,y=105)
     r13.place(x=20 ,y=135)
     r14.place(x=20 ,y=165)
     next1=Button(art,text= "next",fg="black",bg="white",command = lambda  user1=user1: art2(user1)).place(x=20,y=210)
##################################################################################################################################################################
astro=0
def astroscore():
     global astro
     astro+=100
def storeastro(user1):
     astro5.destroy()
     print(astro)
     mycon=mys.connect(host="localhost",user="root",passwd="root",database="login")
     mycur=mycon.cursor()
     mycur.execute("select*from main")
     l=mycur.fetchall()
     username=user1.get()
     print(username)
     
     sql="update main set astronomy={} where username='{}' ".format(astro,username)
     #where username='i'
     mycur.execute(sql)
     mycon.commit()
     mycon.close()
def astro5(user1):
     astro4.destroy()
     global astro5
     astro5=Tk()
     astro5.configure(background="white")
     astro5.geometry("500x250+725+335")
     #question5
     v5=IntVar()
     q52=Label(astro5,text='5. Which one of the following planet is also called morning star or evening star?', fg='black', bg='white' ,font=('ink free',14) )
     
     r_512=Radiobutton(astro5,text= "Mercury",fg="black",bg="white",variable=v5,value=15)
     r_522=Radiobutton(astro5,text= "Venus",fg="black",bg="white",variable=v5,value=15,command=astroscore)
     r_532=Radiobutton(astro5,text= "Earth",fg="black",bg="white",variable=v5,value=15)
     r_542=Radiobutton(astro5,text= "Mars",fg="black",bg="white",variable=v5,value=15)
   
     q52.place(x=20 ,y=25)
     r_512.place(x=20 ,y=75)
     r_522.place(x=20 ,y=105)
     r_532.place(x=20 ,y=135)
     r_542.place(x=20 ,y=165)
     next5=Button(astro5,text= "submit",fg="black",bg="white",command = lambda  user1=user1: storeastro(user1)).place(x=20,y=210)

def astro4(user1):
     astro3.destroy()
     global astro4
     astro4=Tk()
     astro4.configure(background="white")
     astro4.geometry("500x250+725+335")
     #question4
     v4=IntVar()
     q42=Label(astro4,text='4.The stellar and solar source of energy is:', fg='black', bg='white' ,font=('ink free',14) )
     r_412=Radiobutton(astro4,text= "Nuclear fusion",fg="black",bg="white",variable=v4,value=14,command=astroscore)
     r_422=Radiobutton(astro4,text= " Nuclear fission",fg="black",bg="white",variable=v4,value=14)
     r_432=Radiobutton(astro4,text= "Electromagnetic induction",fg="black",bg="white",variable=v4,value=14)
     r_442=Radiobutton(astro4,text= "Fire",fg="black",bg="white",variable=v4,value=14)
     q42.place(x=20 ,y=25)
     r_412.place(x=20 ,y=75)
     r_422.place(x=20 ,y=105)
     r_432.place(x=20 ,y=135)
     r_442.place(x=20 ,y=165)
     next4=Button(astro4,text= "next",fg="black",bg="white",command = lambda  user1=user1: astro5(user1)).place(x=20,y=210)
def astro3(user1):
     astro2.destroy()
     global astro3
     astro3=Tk()
     astro3.configure(background="white")
     astro3.geometry("500x250+725+335")
     #question3
     v3=IntVar()
     q32=Label(astro3,text='3.Which one of the following elements occurs most abundantly in our universe?', fg='black', bg='white' ,font=('ink free',14) )
     r_312=Radiobutton(astro3,text= "Hydrogen",fg="black",bg="white",variable=v3,value=13)
     r_322=Radiobutton(astro3,text= "Nitrogen",fg="black",bg="white",variable=v3,value=13,command=astroscore)
     r_332=Radiobutton(astro3,text= "Sulphur",fg="black",bg="white",variable=v3,value=13)
     r_342=Radiobutton(astro3,text= "Stone",fg="black",bg="white",variable=v3,value=13)
     q32.place(x=20 ,y=25)
     r_312.place(x=20 ,y=75)
     r_322.place(x=20 ,y=105)
     r_332.place(x=20 ,y=135)
     r_342.place(x=20 ,y=165)
     next3=Button(astro3,text= "next",fg="black",bg="white",command = lambda user1=user1: astro4(user1)).place(x=20,y=210)
def astro2(user1):
     
     astro1.destroy()
     global astro2
     astro2=Tk()
     astro2.configure(background="white")
     astro2.geometry("500x250+725+335")
     #question2
     v2=IntVar()
     q22=Label(astro2,text='2.Who had propounded the planetary laws?', fg='black', bg='white' ,font=('ink free',14))
     r_212=Radiobutton(astro2,text= "Kepler",fg="black",bg="white",variable=v2,value=12,command=astroscore)
     r_222=Radiobutton(astro2,text= "Newton",fg="black",bg="white",variable=v2,value=12)
     r_232=Radiobutton(astro2,text= "Galileo",fg="black",bg="white",variable=v2,value=12)
     r_242=Radiobutton(astro2,text= "Copernicus",fg="black",bg="white",variable=v2,value=12)
     q22.place(x=20 ,y=25)
     r_212.place(x=20 ,y=75)
     r_222.place(x=20 ,y=105)
     r_232.place(x=20 ,y=135)
     r_242.place(x=20 ,y=165)
     next2=Button(astro2,text= "next",fg="black",bg="white",command = lambda user1=user1: astro3(user1)).place(x=20,y=210)

def astronomy(user1):
    global astro1 
   
    astro1=Tk()
    astro1.configure(background="white")
    astro1.geometry("500x250+725+335")
    #question1
    v1=IntVar()
    q12=Label(astro1,text='1. Who speculated that our universe is expanding?', fg='black', bg='white' ,font=('ink free',14) )
    r112=Radiobutton(astro1,text= "Edwin Hubble",fg="black",bg="white",variable=v1,value=11,command=astroscore)
    r122=Radiobutton(astro1,text= "Galilio",fg="black",bg="white",variable=v1,value=11)
    r132=Radiobutton(astro1,text= "Newton",fg="black",bg="white",variable=v1,value=11)
    r142=Radiobutton(astro1,text= "Copernicus",fg="black",bg="white",variable=v1,value=11)
    q12.place(x=20 ,y=25)
    r112.place(x=20 ,y=75)
    r122.place(x=20 ,y=105)
    r132.place(x=20 ,y=135)
    r142.place(x=20 ,y=165)
    next1=Button(astro1,text= "next",fg="black",bg="white",command = lambda  user1=user1: astro2(user1)).place(x=20,y=210)
   
    
    
##################################################################################################################################################################33    
gk=0
def gkscore():
     global gk
     gk+=100
def storegk(user1):
     gk5.destroy()
     print(gk)
     mycon=mys.connect(host="localhost",user="root",passwd="root",database="login")
     mycur=mycon.cursor()
     mycur.execute("select*from main")
     l=mycur.fetchall()
     username=user1.get()
     
     sql="update main set gk={} where username='{}' ".format(gk,username)
     #where username='i'
     mycur.execute(sql)
     mycon.commit()
     mycon.close()
def gk5(user1):
     gk4.destroy()
     global gk5
     gk5=Tk()
     gk5.configure(background="white")
     gk5.geometry("500x250+725+335")
     #question5
     v=IntVar()
     q5=Label(gk5,text='5. The members of the Rajya Sabha are elected by', fg='black', bg='white' ,font=('ink free',14) )
     val_=5
     r_51=Radiobutton(gk5,text= "the people",fg="black",bg="white",variable=v,value=1)
     r_52=Radiobutton(gk5,text= "Lok Sabha",fg="black",bg="white",variable=v,value=2)
     r_53=Radiobutton(gk5,text= "elected members of the legislative assembly",fg="black",bg="white",variable=v,value=3,command= gkscore)
     r_54=Radiobutton(gk5,text= "elected members of the legislative council",fg="black",bg="white",variable=v,value=4)
     q5.place(x=20 ,y=25)
     r_51.place(x=20 ,y=75)
     r_52.place(x=20 ,y=105)
     r_53.place(x=20 ,y=135)
     r_54.place(x=20 ,y=165)
     next5=Button(gk5,text= "submit",fg="black",bg="white",command = lambda  user1=user1: storegk(user1)).place(x=20,y=210)
def gk4(user1):
     gk3.destroy()
     global gk4
     gk4=Tk()
     gk4.configure(background="white")
     gk4.geometry("500x250+725+335")
     #question4
     v=IntVar()
     q4=Label(gk4,text='4.Ozone hole refers to', fg='black', bg='white' ,font=('ink free',14) )
     val_=4
     r_41=Radiobutton(gk4,text= "hole in ozone layer",fg="black",bg="white",variable=v,value=1)
     r_42=Radiobutton(gk4,text= " decrease in the ozone layer in troposphere",fg="black",bg="white",variable=v,value=2)
     r_43=Radiobutton(gk4,text= "decrease in thickness of ozone layer in stratosphere",fg="black",bg="white",variable=v,value=3,command= gkscore)
     r_44=Radiobutton(gk4,text= "increase in the thickness of ozone layer in troposphere",fg="black",bg="white",variable=v,value=4)
     q4.place(x=20 ,y=25)
     r_41.place(x=20 ,y=75)
     r_42.place(x=20 ,y=105)
     r_43.place(x=20 ,y=135)
     r_44.place(x=20 ,y=165)
     next4=Button(gk4,text= "next",fg="black",bg="white",command = lambda  user1=user1: gk5(user1)).place(x=20,y=210)
def gk3(user1):
     gk2.destroy()
     global gk3
     gk3=Tk()
     gk3.configure(background="white")
     gk3.geometry("500x300+200+50")
     #question3
     v=IntVar()
     q3=Label(gk3,text='3.Ordinary table salt is sodium chloride. What is baking soda?', fg='black', bg='white' ,font=('ink free',14))
     val_=3
     r_31=Radiobutton(gk3,text= "Potassium chloride",fg="black",bg="white",variable=v,value=1)
     r_32=Radiobutton(gk3,text= "Potassium carbonate",fg="black",bg="white",variable=v,value=2)
     r_33=Radiobutton(gk3,text= "Potassium hydroxide",fg="black",bg="white",variable=v,value=3)
     r_34=Radiobutton(gk3,text= "Sodium bicarbonate",fg="black",bg="white",variable=v,value=4,command= gkscore)
     q3.place(x=20 ,y=25)
     r_31.place(x=20 ,y=75)
     r_32.place(x=20 ,y=105)
     r_33.place(x=20 ,y=135)
     r_34.place(x=20 ,y=165)
     next3=Button(gk3,text= "next",fg="black",bg="white",command = lambda  user1=user1: gk4(user1)).place(x=20,y=210)
def gk2(user1):
     gk1.destroy()
     global gk2
     gk2=Tk()
     gk2.configure(background="white")
     gk2.geometry("500x250+725+335")
     #question2
     v=IntVar()
     q2=Label(gk2,text='2.Which county did Ravi Shastri play for?', fg='black', bg='white' ,font=('ink free',14) )
     val_=2
     r_21=Radiobutton(gk2,text= "Glamorgan",fg="black",bg="white",variable=v,value=1,command= gkscore)
     r_22=Radiobutton(gk2,text= "Leicestershire",fg="black",bg="white",variable=v,value=2)
     r_23=Radiobutton(gk2,text= "Gloucestershire",fg="black",bg="white",variable=v,value=3)
     r_24=Radiobutton(gk2,text= "Lancashire",fg="black",bg="white",variable=v,value=4)
     q2.place(x=20 ,y=25)
     r_21.place(x=20 ,y=75)
     r_22.place(x=20 ,y=105)
     r_23.place(x=20 ,y=135)
     r_24.place(x=20 ,y=165)
     next2=Button(gk2,text= "next",fg="black",bg="white",command = lambda  user1=user1: gk3(user1)).place(x=20,y=210)
def gk1(user1):
     global gk1
     gk1=Tk()
     gk1.configure(background="white")
     gk1.geometry("500x250+725+335")
     #question1
     v=IntVar()
     q1=Label(gk1,text='1. What is part of a database that holds only one type of information??', fg='black', bg='white' ,font=('ink free',14) )
     val_=1
     r11=Radiobutton(gk1,text= "Report",fg="black",bg="white",variable=v,value=1)
     r12=Radiobutton(gk1,text= "Field",fg="black",bg="white",variable=v,value=2,command= gkscore)
     r13=Radiobutton(gk1,text= "Record",fg="black",bg="white",variable=v,value=3)
     r14=Radiobutton(gk1,text= "File",fg="black",bg="white",variable=v,value=4)
     q1.place(x=20 ,y=25)
     r11.place(x=20 ,y=75)
     r12.place(x=20 ,y=105)
     r13.place(x=20 ,y=135)
     r14.place(x=20 ,y=165)
     next1=Button(gk1,text= "next",fg="black",bg="white",command = lambda  user1=user1: gk2(user1)).place(x=20,y=210)
     
     
##########################################################################################################################################33     
brain=0 
def brainscore():
     global brain
     brain+=100
def storebrain(user1):
     brain5.destroy()
     print(brain)
     mycon=mys.connect(host="localhost",user="root",passwd="root",database="login")
     mycur=mycon.cursor()
     mycur.execute("select*from main")
     l=mycur.fetchall()
     
     username=user1.get()
     
     sql="update main set brain={} where username='{}' ".format(brain,username)
     mycur.execute(sql)
     mycon.commit()
     mycon.close()
def brain5(user1):
     brain4.destroy()
     global brain5
     brain5=Tk()
     brain5.configure(background="white")
     brain5.geometry("500x250+725+335")
     #question5
     v=IntVar()
     q5=Label(brain5,text='5. What’s full of holes but still holds water?', fg='black', bg='white' ,font=('ink free',14) )
     val_=5
     r_51=Radiobutton(brain5,text= "skin pores",fg="black",bg="white",variable=v,value=1)
     r_52=Radiobutton(brain5,text= "leather",fg="black",bg="white",variable=v,value=2)
     r_53=Radiobutton(brain5,text= "A sponge",fg="black",bg="white",variable=v,value=3,command=brainscore)
     r_54=Radiobutton(brain5,text= "cotton",fg="black",bg="white",variable=v,value=4)
     q5.place(x=20 ,y=25)
     r_51.place(x=20 ,y=75)
     r_52.place(x=20 ,y=105)
     r_53.place(x=20 ,y=135)
     r_54.place(x=20 ,y=165)
     next5=Button(brain5,text= "submit",fg="black",bg="white",command = lambda  user1=user1: storebrain(user1)).place(x=20,y=210)
def brain4(user1):
     brain3.destroy()
     global brain4
     brain4=Tk()
     brain4.configure(background="white")
     brain4.geometry("500x250+725+335")
     #question4
     v=IntVar()
     q4=Label(brain4,text='4. Why can’t a man living in the USA be buried in Canada?', fg='black', bg='white' ,font=('ink free',14) )
     val_=4
     r_41=Radiobutton(brain4,text= "His last wish wasn't fulfilled",fg="black",bg="white",variable=v,value=1)
     r_42=Radiobutton(brain4,text= " He died while cursing Canada's PM",fg="black",bg="white",variable=v,value=2)
     r_43=Radiobutton(brain4,text= "You cannot bury a living man.",fg="black",bg="white",variable=v,value=3,command=brainscore)
     r_44=Radiobutton(brain4,text= "He would be too heavy to be carried to Canada",fg="black",bg="white",variable=v,value=4)
     q4.place(x=20 ,y=25)
     r_41.place(x=20 ,y=75)
     r_42.place(x=20 ,y=105)
     r_43.place(x=20 ,y=135)
     r_44.place(x=20 ,y=165)
     next4=Button(brain4,text= "next",fg="black",bg="white",command = lambda  user1=user1: brain5(user1)).place(x=20,y=210)
def brain3(user1):
     brain2.destroy()
     global brain3
     brain3=Tk()
     brain3.configure(background="white")
     brain3.geometry("500x250+725+335")
     #question3
     v=IntVar()
     q3=Label(brain3,text='3.What occurs once in every minute, twice in every moment, yet never in a thousand yeARS?', fg='black', bg='white' ,font=('ink free',14) )
     val_=3
     r_31=Radiobutton(brain3,text= "second",fg="black",bg="white",variable=v,value=1)
     r_32=Radiobutton(brain3,text= "life",fg="black",bg="white",variable=v,value=2)
     r_33=Radiobutton(brain3,text= "comet shower",fg="black",bg="white",variable=v,value=3)
     r_34=Radiobutton(brain3,text= "The letter “M”.",fg="black",bg="white",variable=v,value=4,command=brainscore)
     q3.place(x=20 ,y=25)
     r_31.place(x=20 ,y=75)
     r_32.place(x=20 ,y=105)
     r_33.place(x=20 ,y=135)
     r_34.place(x=20 ,y=165)
     next3=Button(brain3,text= "next",fg="black",bg="white",command = lambda  user1=user1: brain4(user1)).place(x=20,y=210)
def brain2(user1):
     brain1.destroy()
     global brain2
     brain2=Tk()
     brain2.configure(background="white")
     brain2.geometry("500x250+725+335")
     #question2
     v=IntVar()
     q2=Label(brain2,text='2.What word looks the same upside down and backward?', fg='black', bg='white' ,font=('ink free',14) )
     val_=2
     r_21=Radiobutton(brain2,text= "SWIMS.",fg="black",bg="white",variable=v,value=1,command=brainscore)
     r_22=Radiobutton(brain2,text= "SLURPS.",fg="black",bg="white",variable=v,value=2)
     r_23=Radiobutton(brain2,text= "SWING.",fg="black",bg="white",variable=v,value=3)
     r_24=Radiobutton(brain2,text= "SWATS.",fg="black",bg="white",variable=v,value=4)
     q2.place(x=20 ,y=25)
     r_21.place(x=20 ,y=75)
     r_22.place(x=20 ,y=105)
     r_23.place(x=20 ,y=135)
     r_24.place(x=20 ,y=165)
     next2=Button(brain2,text= "next",fg="black",bg="white",command = lambda  user1=user1: brain3(user1)).place(x=20,y=210)
def brain1(user1):
     global brain1
     brain1=Tk()
     brain1.configure(background="white")
     brain1.geometry("500x250+725+335")
     #question1
     v=IntVar()
     q1=Label(brain1,text='1. The more it dries, the wetter it gets. What is it?', fg='black', bg='white' ,font=('ink free',14) )
     val_=1
     r11=Radiobutton(brain1,text= "bread",fg="black",bg="white",variable=v,value=1)
     r12=Radiobutton(brain1,text= "sand",fg="black",bg="white",variable=v,value=2)
     r13=Radiobutton(brain1,text= "towel",fg="black",bg="white",variable=v,value=3,command=brainscore)
     r14=Radiobutton(brain1,text= "plate",fg="black",bg="white",variable=v,value=4)
     q1.place(x=20 ,y=25)
     r11.place(x=20 ,y=75)
     r12.place(x=20 ,y=105)
     r13.place(x=20 ,y=135)
     r14.place(x=20 ,y=165)
     next1=Button(brain1,text= "next",fg="black",bg="white",command = lambda  user1=user1: brain2(user1)).place(x=20,y=210)
     
     
##################################################################################################################################################3   
tv=0    
def tvscore():
     global tv
     tv+=100
def storetv(user1):
     tv5.destroy()
     print(tv)
     mycon=mys.connect(host="localhost",user="root",passwd="root",database="login")
     mycur=mycon.cursor()
     mycur.execute("select*from main")
     l=mycur.fetchall()
     username=user1.get()
     
     sql="update main set tv={} where username='{}' ".format(tv,username)
     #where username='i'
     mycur.execute(sql)
     mycon.commit()
     mycon.close()
def tv5(user1):
     global tv5
     tv4.destroy()
     tv5=Tk()
     tv5.configure(background="white")
     tv5.geometry("500x250+725+335")
     #question5
     v=IntVar()
     q5=Label(tv5,text="5.Who is the director of the film 'Baahubali: The Beggining?", fg='black', bg='white' ,font=('ink free',14) )
     val_=5
     r_51=Radiobutton(tv5,text= "Amitabh Bhattacharya",fg="black",bg="white",variable=v,value=1)
     r_52=Radiobutton(tv5,text= "Karan Johar",fg="black",bg="white",variable=v,value=2)
     r_53=Radiobutton(tv5,text= "Rajamouli",fg="black",bg="white",variable=v,value=3)
     r_54=Radiobutton(tv5,text= "Mahesh Bhatt",fg="black",bg="white",variable=v,value=4)
     q5.place(x=20 ,y=25)
     r_51.place(x=20 ,y=75)
     r_52.place(x=20 ,y=105)
     r_53.place(x=20 ,y=135)
     r_54.place(x=20 ,y=165)
     next5=Button(tv5,text= "submit",fg="black",bg="white",command = lambda  user1=user1: storetv(user1)).place(x=20,y=210)
def tv4(user1):
     global tv4
     tv3.destroy()
     tv4=Tk()
     tv4.configure(background="white")
     tv4.geometry("500x250+725+335")
     #question4
     v=IntVar()
     q4=Label(tv4,text='who is the producer of the  Kapil Sharma Show', fg='black', bg='white' ,font=('ink free',14) )
     val_=4
     r_41=Radiobutton(tv4,text= "Karan Johar",fg="black",bg="white",variable=v,value=1)
     r_42=Radiobutton(tv4,text= "Salman Khan",fg="black",bg="white",variable=v,value=2,command=tvscore)
     r_43=Radiobutton(tv4,text= "Kangana Ranaut",fg="black",bg="white",variable=v,value=3)
     r_44=Radiobutton(tv4,text= "Amir Khan",fg="black",bg="white",variable=v,value=4)
     q4.place(x=20 ,y=25)
     r_41.place(x=20 ,y=75)
     r_42.place(x=20 ,y=105)
     r_43.place(x=20 ,y=135)
     r_44.place(x=20 ,y=165)
     next4=Button(tv4,text= "next",fg="black",bg="white",command = lambda  user1=user1: tv5(user1)).place(x=20,y=210)
def tv3(user1):
     global tv3
     tv2.destroy()
     tv3=Tk()
     tv3.configure(background="white")
     tv3.geometry("500x250+725+335")
     #question
     v=IntVar()
     q3=Label(tv3,text='3.which show has the highestTRP in America', fg='black', bg='white' ,font=('ink free',14) )
     val_=3
     r_31=Radiobutton(tv3,text= "Young Sheldon",fg="black",bg="white",variable=v,value=1)
     r_32=Radiobutton(tv3,text= "Blue Bloods",fg="black",bg="white",variable=v,value=2)
     r_33=Radiobutton(tv3,text= "60 minutes",fg="black",bg="white",variable=v,value=3)
     r_34=Radiobutton(tv3,text= "NCIS",fg="black",bg="white",variable=v,value=4,command=tvscore)
     q3.place(x=20 ,y=25)
     r_31.place(x=20 ,y=75)
     r_32.place(x=20 ,y=105)
     r_33.place(x=20 ,y=135)
     r_34.place(x=20 ,y=165)
     next3=Button(tv3,text= "next",fg="black",bg="white",command = lambda  user1=user1: tv4(user1)).place(x=20,y=210)
def tv2(user1):
     global tv2
     tv1.destroy()
     tv2=Tk()
     tv2.configure(background="white")
     tv2.geometry("500x250+725+335")
     #question2
     v=IntVar()
     q2=Label(tv2,text='which is the 2nd most disliked video in youtube india ?', fg='black', bg='white' ,font=('ink free',14))
     val_=2
     r_21=Radiobutton(tv2,text= "Despasito",fg="black",bg="white",variable=v,value=1)
     r_22=Radiobutton(tv2,text= "everyone controls rewind.",fg="black",bg="white",variable=v,value=2)
     r_23=Radiobutton(tv2,text= "baby shark dance.",fg="black",bg="white",variable=v,value=3)
     r_24=Radiobutton(tv2,text= "Sadak 2 trailer",fg="black",bg="white",variable=v,value=4,command=tvscore)
     q2.place(x=20 ,y=25)
     r_21.place(x=20 ,y=75)
     r_22.place(x=20 ,y=105)
     r_23.place(x=20 ,y=135)
     r_24.place(x=20 ,y=165)
     next2=Button(tv2,text= "next",fg="black",bg="white",command = lambda  user1=user1: tv3(user1)).place(x=20,y=210)
def tv1(user1):
     global tv1
     tv1=Tk()
     tv1.configure(background="white")
     tv1.geometry("500x250+725+335")
     #question1
     v=IntVar()
     q1=Label(tv1,text='1. what is Hrithik Roshan\'s name in the movie Zindagi Na Milegi Dobar ' , fg='black', bg='white' ,font=('ink free',14))
     val_=1
     r11=Radiobutton(tv1,text= "Kabir",fg="black",bg="white",variable=v,value=1)
     r12=Radiobutton(tv1,text= "salman habib",fg="black",bg="white",variable=v,value=2)
     r13=Radiobutton(tv1,text= "arjun",fg="black",bg="white",variable=v,value=3,command=tvscore)
     r14=Radiobutton(tv1,text= "irman",fg="black",bg="white",variable=v,value=4)
     q1.place(x=20 ,y=25)
     r11.place(x=20 ,y=75)
     r12.place(x=20 ,y=105)
     r13.place(x=20 ,y=135)
     r14.place(x=20 ,y=165)
     next1=Button(tv1,text= "next",fg="black",bg="white",command = lambda  user1=user1: tv2(user1)).place(x=20,y=210)
     
     
     
     
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def signup():
     def movetodatabase():
          def topics():
               #sn.destroy()
               hj=Tk()
               
               
               hj.configure(background='black')
               hj.geometry("2000x2000")
               l=tkinter.Label(hj,text='KEEP CALM ITS QUIZ TIME ', fg='purple', bg='black', font=('ink free',60)).place(x=80,y=5)
               optionframe=Frame(hj,bd=2,bg="black",relief="groove",cursor="dot",height=500,width=600)
               optionframe.place(x=50,y=100)
               questionframe=Frame(hj,bd=2,bg="black",relief="groove",cursor="dot",height=500,width=550)
               questionframe.place(x=700,y=100)
               i2=Label(  questionframe,text='RULES ',font=('ink free',40), fg='orange', bg='black')
               i3=Label(  questionframe,text='Click on the options only once',font=('ink free',20), fg='white', bg='black')
               i4=Label(  questionframe,text='take one quiz only once',font=('ink free',20), fg='white', bg='black')
               i2.place(x=20,y=20)
               i3.place(x=20,y=90)
               i4.place(x=20,y=160)
               
               i1=Label(  optionframe,text='Click on the topics you want to take the quiz on!',font=('ink free',20), fg='white', bg='black')
               a1=Button(  optionframe,text='Art and Literature',bg='white',fg='black', height=3,width=40, command=lambda user1=user1: art_literature(user1))
               a2=Button(  optionframe,text='Astronomy', height=3,width=40,bg='white',fg='black',command=lambda user1=user1: astronomy(user1))
               a3=Button(  optionframe,text='General knowledge', height=3,width=40,bg='white',fg='black',command=lambda user1=user1: gk1(user1))
               a4=Button(  optionframe,text='Brain teasers', height=3,width=40,bg='white',fg='black',command=lambda user1=user1: brain1(user1))
               a5=Button(  optionframe,text='tv and films', height=3,width=40,bg='white',fg='black',command=lambda user1=user1: tv1(user1))
               k= font.Font(family='ink free', size=20, weight='bold')
               a1['font'] = k
               a2['font'] = k
               a3['font'] = k
               a4['font'] = k
               a5['font'] = k
               i1.place(x=20,y=20)
               a1.place(x=55,y=90)
               a2.place(x=55,y=160)
               a3.place(x=55,y=230)
               a4.place(x=55,y=300)
               a5.place(x=55,y=370)
          db=mys.connect(host = "localhost", user = "root", passwd="root",database="login")
          cur=db.cursor()
          username=user1.get()
          password=passwd1.get()
          sql="insert into main(username,password) values('{}',{})".format(username,password)
          cur.execute(sql)
          db.commit()
          db.close()
          topics=Button(sn,text="start quiz",command=topics)
          topics.place(x=238,y=350)


     sn=Tk()
     #filename1 = PhotoImage(file =r"C:\Users\Nirav Seth\OneDrive\Documents\quiz final\quiz bg.PNG")
     #background_label1 = Label(sn, image=filename1)
     #background_label1.place(x=0, y=0)'''


     sn.configure(bg="black")
     sn.geometry("400x400")
     user = Label(sn, text = "Username :",font=('ink free',20),fg='purple',bg='black')
     passwd = Label(sn, text = "Password  :",font=('ink free',20),fg='purple',bg='black')
     global user1
     user1 = Entry(sn, textvariable = StringVar())
     passwd1 = Entry(sn, textvariable = IntVar().set(""))
     enter = Button(sn, text = "Enter", bd = 0, command=movetodatabase,height=0,width=8)
     enter.configure(bg = "pink")
     user1.place(x = 200, y = 235)
     passwd1.place(x = 200, y = 285)
     user.place(x = 50, y = 220)
     passwd.place(x = 50, y = 270)
     enter.place(x = 238, y = 325)
##     global a
##     a=user1.get()
##     
##     print(user1)
     sn.mainloop()



#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import matplotlib.pyplot as plt 
def scoreboard():
    def view():
         
          mycon=mys.connect(host = "localhost", user = "root", passwd="root",database="login")
          mycur=mycon.cursor()
          p=user.get()
          sql="select art,astronomy,gk,brain,tv from main where username='{}' ".format(p)
          mycur.execute(sql)
          a=mycur.fetchall()
          print(user1)
          for i in a:
               global k
               k=list(i)
               print(k)
          
          
         
    
          # x-coordinates of left sides of bars  
          left = [1, 2, 3, 4, 5] 

          # heights of bars 
          height =k
                
          # labels for bars 
          tick_label = ['ART', 'ASTRO', 'GK', 'BRAIN', 'TV'] 
                
          # plotting a bar chart 
          plt.bar(left, height, tick_label = tick_label, 
          width = 0.8, color = ['red', 'green']) 
                
          # naming the x-axis 
          plt.xlabel('x - axis') 
          # naming the y-axis 
          plt.ylabel('y - axis') 
          # plot title 
          plt.title('My bar chart!') 
                
          # function to show the plot 
          plt.show()
          mycon.close()
          
         
              
    global tki
    tki=Tk()
    tki.geometry("300x300+200+50")
    tki.configure(bg="black")
    user1 = Label(tki, text = "Username :",font=('ink free',20),fg='purple',bg='black')
    user1.place(x=20,y=40)
    global user
    user = Entry(tki, textvariable = StringVar())
    user.place(x=160,y=50)
    print(user.get())
    l=Button(tki,text="show analysis",command=view)
    l.place(x=20,y=100)
    tki.mainloop()
    
def topics():
     
     hj=Tk()
     hj.configure(background='black')
     hj.geometry("2000x2000")
     l=tkinter.Label(hj,text='KEEP CALM ITS QUIZ TIME ', fg='purple', bg='black', font=('ink free',60)).place(x=80,y=5)
     optionframe=Frame(hj,bd=2,bg="black",relief="groove",cursor="dot",height=500,width=600)
     optionframe.place(x=50,y=100)
     questionframe=Frame(hj,bd=2,bg="black",relief="groove",cursor="dot",height=500,width=550)
     questionframe.place(x=700,y=100)
     i2=Label(  questionframe,text='RULES ',font=('ink free',40), fg='orange', bg='black')
     i3=Label(  questionframe,text='Click on the option only once',font=('ink free',20), fg='white', bg='black')
     i4=Label(  questionframe,text='Take one quiz only once',font=('ink free',20), fg='white', bg='black')
     i2.place(x=20,y=20)
     i3.place(x=20,y=90)
     i4.place(x=20,y=160)
     i1=Label(  optionframe,text='Click on the topics you want to take the quiz on!',font=('ink free',20), fg='white', bg='black')
     a1=Button(  optionframe,text='Art and Literature',bg='white',fg='black', height=3,width=40,command=lambda user1=user1: art_literature(user1))
     a2=Button(  optionframe,text='Astronomy', height=3,width=40,bg='white',fg='black',command=lambda user1=user1: astronomy(user1))
     a3=Button(  optionframe,text='General knowledge', height=3,width=40,bg='white',fg='black',command=lambda user1=user1: gk1(user1))
     a4=Button(  optionframe,text='Brain teasers', height=3,width=40,bg='white',fg='black',command=lambda user1=user1: brain1(user1))
     a5=Button(  optionframe,text='tv and films', height=3,width=40,bg='white',fg='black',command=lambda user1=user1: tv1(user1))
     k= font.Font(family='ink free', size=20, weight='bold')
     a1['font'] = k
     a2['font'] = k
     a3['font'] = k
     a4['font'] = k
     a5['font'] = k
     i1.place(x=20,y=20)
     a1.place(x=55,y=90)
     a2.place(x=55,y=160)
     a3.place(x=55,y=230)
     a4.place(x=55,y=300)
     a5.place(x=55,y=370)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

     
def login():
     
     def checkwithdatabase():
          
          cdb=mys.connect(host = "localhost", user = "root", passwd="root",database="login")
          cur=cdb.cursor()
          cur.execute("select*from main")
          a=cur.fetchall()
          print("ya now",a)
          for i in a:
               print(i[0])
               if i[0]==str(user1.get()) and i[1]==int(passwd1.get()) :
                    print(i[0])
                    button=Button(lg,text="play quiz",command=topics)
                    button.place(x=238,y=350)
               


          cdb.commit()
          cdb.close()

     global lg 
         
     lg=Tk()
     lg.configure(bg="black")
     lg.geometry("400x400")
     user = Label(lg, text = "Username :",font=('ink free',20),fg='purple',bg='black')
     passwd = Label(lg, text = "Password  :",font=('ink free',20),fg='purple',bg='black')
     global user1
     user1 = Entry(lg, textvariable = StringVar())
     passwd1 = Entry(lg, textvariable = IntVar().set(""))
     enter = Button(lg, text = "Enter", bd = 0, command=checkwithdatabase,height=0,width=8)
     enter.configure(bg = "pink")
     user1.place(x = 200, y = 235)
     passwd1.place(x = 200, y = 285)
     user.place(x = 50, y = 220)
     passwd.place(x = 50, y = 270)
     enter.place(x = 238, y = 325)
     
     
     print(user1)
     lg.mainloop()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def competitors():
     '''rt1.destroy()'''
     cdb=mys.connect(host = "localhost", user = "root", passwd="root",database="login")
     cur=cdb.cursor()
     cur.execute('SELECT * FROM main')
     r=cur.fetchall()
     print("hi")
     print("%20s"%"username","%20s"%"art","%20s"%"astronomy","%20s"%"gk","%20s"%"brain","%20s"%"tv")
     print("=======================================================================================================")
     for i in r:
               global k
               k=list(i)
               
               print("%20s"%k[0],"%20s"%k[2],"%20s"%k[3],"%20s"%k[4],"%20s"%k[5],"%20s"%k[6])
          
               
        

    
     
 
     
#############################################################################################################################################

filename1 = PhotoImage(file = r"C:\Users\Nirav Seth\OneDrive\Documents\image4.png")
background_label1 = Label(rt1, image=filename1)
background_label1.place(x=200, y=370)

filename2 = PhotoImage(file =r"C:\Users\Nirav Seth\OneDrive\Desktop\image1.gif")
background_label2 = Label(rt1, image=filename2)
background_label2.place(x=800, y=370)

rt1.title("WELCOME TO QUIZZARD")
rt1.configure(background='black' )
a=tkinter.Label(rt1,text='WELCOME TO QUIZZARD!', fg='purple', bg='black', font=('ink free',80)).grid(column="0",row="1")
rt1.geometry("2000x2000")
#mainmenu
introlabel=Label(rt1,text="knowledge is the new rich,arm yourselves with it",fg='white', bg='black',font=('ink free',40)).grid(column="0",row="6")
#signupbuttton(sb)
myFont = font.Font(family='ink free', size=20, weight='bold')
sb=Button(rt1,text="sign up",fg="white",bg="black",height=0,width=8,command=signup)
sb['font'] = myFont
sb.place(x=50,y=300)
#loginbutton
lb=Button(rt1,text="log in",fg="white",bg="black",height=0,width=8,command=login)
lb['font'] = myFont
lb.place(x=400,y=300)
#score(sc)
sc=Button(rt1,text="score board",fg="white",bg="black",height=0,width=10,command=scoreboard)
sc['font'] = myFont
sc.place(x=700,y=300)
#competitors(ct)
ct=Button(rt1,text="competitors",fg="white",bg="black",height=0,width=10,command=competitors)
ct['font'] = myFont
ct.place(x=1050,y=300)
#########################################################################################################################################



