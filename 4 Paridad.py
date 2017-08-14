from random import randint
f=open('Paridad.txt','a')
estado=0
from tkinter import *

def Graficar():
    ventana = Tk()
    c = Canvas(ventana,width=500,height=500)
    ventana.geometry("500x500")
    
    c.create_oval(33,30,320,317,fill="Cyan")
    c.create_oval(48,45,305,302,fill="White")
    c.create_oval(41,41,126,126,fill="pink")####
    c.create_oval(56,56,109.5,109.5,fill="pink")
    c.create_oval(226,226,311,311,fill="pink")#abaj dere
    c.create_oval(41,226,126,311,fill="pink")#abaj izq
    c.create_oval(226,41,311,126,fill="pink")#arri dere

    c.create_oval(44,104,54,115,fill="black")
    c.create_oval(55,226,66,237,fill="black")
    c.create_oval(300,104,310,115,fill="black")
    c.create_oval(285,236,296,225,fill="black")
    c.create_oval(224,296,235,285,fill="black")
    c.create_oval(108,306,119,295,fill="black")
    c.create_oval(103,51,114,40,fill="black")
    c.create_oval(226,64,237,53,fill="black")

    estado0=Label(ventana,text="q0",bg="pink",font="Helvetica 16").place(x=68,y=68)
    estado1=Label(ventana,text="q1",bg="pink",font="Helvetica 16").place(x=255,y=68)
    estado2=Label(ventana,text="q2",bg="pink",font="Helvetica 16").place(x=68,y=255)
    estado3=Label(ventana,text="q3",bg="pink",font="Helvetica 16").place(x=255,y=255)
    cero1=Label(ventana,text="0",bg="white",font="Helvetica 12").place(x=288,y=170)
    cero2=Label(ventana,text="0",font="Helvetica 12").place(x=323,y=170)
    cero3=Label(ventana,text="0",bg="white",font="Helvetica 12").place(x=50,y=170)
    cero4=Label(ventana,text="0",font="Helvetica 12").place(x=15,y=170)
    uno1=Label(ventana,text="1",bg="white",font="Helvetica 12").place(x=167,y=47)
    uno2=Label(ventana,text="1",font="Helvetica 12").place(x=167,y=6)
    uno3=Label(ventana,text="1",bg="white",font="Helvetica 12").place(x=167,y=277)
    uno4=Label(ventana,text="1",font="Helvetica 12").place(x=167,y=320)

    c.create_line(10,80,41,80,fill="black")
    c.create_oval(38,77,43,84,fill="black")
    inicio=Label(ventana,text="inicio",font="Helvetica 10").place(x=9,y=46)



    c.place(x=0,y=0)
    ventana.mainloop()

c=input("Introducir m(manual), a(automatico), g(ver grafico), s(salir): ")
while(c!='s'):
    if(c=='m'):###########################################################
        cad=input("introduce la cadena: ")
        f=open('Paridad.txt','a')
        f.write("\n\nMODO MANUAL\n")
        f.write("-q0-\n")
        for i in cad:
            f.write(i+" ")
            if(i=='1'):
                if(estado==0):
                    estado=1
                    print("q"+str(estado))
                    f=open('Paridad.txt','a')
                    f.write("q"+str(estado)+"\n")
                elif(estado==1):
                    estado=0
                    print("q"+str(estado))
                    f.write("q"+str(estado)+"\n")
                elif(estado==3):
                    estado=2
                    print("q"+str(estado))
                    f.write("q"+str(estado)+"\n")
                else:
                    estado=3
                    print("q"+str(estado))
                    f.write("q"+str(estado)+"\n")
            elif(i=='0'):
                if(estado==0):
                    estado=2
                    print("q"+str(estado))
                    f.write("q"+str(estado)+"\n")
                elif(estado==2):
                    estado=0
                    print("q"+str(estado))
                    f.write("q"+str(estado)+"\n")
                elif(estado==1):
                    estado=3
                    print("q"+str(estado))
                    f.write("q"+str(estado)+"\n")
                else:
                    estado=1
                    print("q"+str(estado))
                    f.write("q"+str(estado)+"\n")
            else:
                print("invalido")
        if(int(estado)==0): #en if estado se castea con int... en print con str
            estado=0
            print("Hay paridad de ceros y unos")
            f.write("\nHay paridad de ceros y unos\n")
            c=input("Introducir m(manual), a(automatico), g(ver grafico), s(salir): ")
            
        else:
            estado=0
            print("NO hay paridad de ceros y unos")
            f.write("\nNo hay paridad de ceros y unos\n")
            
            c=input("Introducir m(manual), a(automatico), g(ver grafico), s(salir): ")
    elif(c=='a'):##############################################################
        long=randint(0,1000)#
        print("longitud: "+str(long))
        f=open('Paridad.txt','a')
        f.write("\n\nMODO AUTOMATICO\n")
        f.write("\nlongitud: "+str(long))
        cad3=""
        for h in range(0,long):#
            cad2=str(randint(0,1))
            cad3=str(cad3+cad2)
        print(""+str(cad3))
        print("q0, ")
        f.write("\n"+str(cad3)+"\n")
        f.write("\nq0, ")
        for i in cad3:
            if(i=='1'):
                if(estado==0):
                    estado=1
                    print("q"+str(estado))
                    f.write(" q"+str(estado)+" = 1,")
                elif(estado==1):
                    estado=0
                    print("q"+str(estado))
                    f.write(" q"+str(estado)+" = 1,")
                elif(estado==3):
                    estado=2
                    print("q"+str(estado))
                    f.write(" q"+str(estado)+" = 1,")
                else:
                    estado=3
                    print("q"+str(estado))
                    f.write(" q"+str(estado)+" = 1,")
            elif(i=='0'):
                if(estado==0):
                    estado=2
                    print("q"+str(estado))
                    f.write(" q"+str(estado)+" = 0,")
                elif(estado==2):
                    estado=0
                    print("q"+str(estado))
                    f.write(" q"+str(estado)+" = 0,")
                elif(estado==1):
                    estado=3
                    print("q"+str(estado))
                    f.write(" q"+str(estado)+" = 0,")
                else:
                    estado=1
                    print("q"+str(estado))
                    f.write(" q"+str(estado)+" = 0, ")
            else:
                print("invalido")
        if(int(estado)==0):
            estado=0
            print("Hay paridad de ceros y unos")
            f.write("\nHay paridad de ceros y unos\n")
            f.close()
            c=input("Introducir m(manual), a(automatico), g(ver grafico) s(salir): ")
        else:
            estado=0
            print("NO hay paridad de ceros y unos")
            f.write("\nNo hay paridad de ceros y unos\n")
            f.close
            c=input("Introducir m(manual), a(automatico), g(ver grafico), s(salir): ")
    elif(c=='g'):##############################################################
        Graficar()
        c=input("Introducir m(manual), a(automatico), g(ver grafico), s(salir): ")
    else:
        print("\nopcion no valida")
        c=input("Introducir m(manual), a(automatico), g(ver grafico), s(salir): ")

