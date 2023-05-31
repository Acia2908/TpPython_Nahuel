import pandas as pd
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import openpyxl 



root=Tk()
root.title("Entrada de datos")
root.geometry("500x300")
root.title("Formulario Ingreso Datos")

miFrame=Frame(root)
miFrame.pack()


ListaContactos=[]
VectorContacto=[]
Vector=[]
     

def ventanaCapturaDatos():

  
    #FRAME DE ENTRADA DE DATOS
    
    apellido=StringVar()
    nombre=StringVar()
    telefono=StringVar()

    bienvenido = Label(miFrame, text="BIENVENIDOS")
    bienvenido.grid(row=0, column=0, columnspan = 2)
    bienvenido.config(font=('Arial', 16))


    #seccion de Nombre
    nombre_label= Label(miFrame, text="Ingresa tu Nombre:")
    nombre_label.grid(row=2, column=0)
    nombre_label.config(padx=10, pady=10)
    #datos de entrada nombre
    cuadro_nombre=Entry(miFrame, justify=CENTER ,textvariable=nombre)
    textoCaja=cuadro_nombre.get()
    nombre.set(textoCaja)
    cuadro_nombre.grid(row=2, column=1)

    #-----Seccion de Apellido-----
    apellido_label=Label(miFrame, text="Ingresa tu Apellido: ")
    apellido_label.grid(row=3, column=0)
    apellido_label.config(padx=10, pady=10)
    cuadro_Apellido=Entry(miFrame, justify=CENTER ,textvariable=apellido)
    textoCaja=cuadro_Apellido.get()
    apellido.set(textoCaja)
    cuadro_Apellido.grid(row=3, column=1)


    #Seccion de Telefono-----
    direccion=Label(miFrame, text="Ingresa tu Telefono: ")
    direccion.grid(row=4, column=0)
    direccion.config(padx=10, pady=10)
    cuadro_Telefono=Entry(miFrame, justify=CENTER ,textvariable=telefono)
    cuadro_Telefono.grid(row=4, column=1)
    textoCajaTel=cuadro_Telefono.get()
    telefono.set(textoCajaTel)
    




    #Botones

    guardamos = Button(miFrame, text="Guardar", command=guardar, bg='lightblue', fg='black')
    guardamos.grid(row=11, column=4, columnspan = 2)
    guardamos.config(padx=5, pady=5)
    cuadro_Guardamos=Entry(miFrame)
    root.mainloop()
    cuentas= []
    datos = {
        "apellido": apellido.get(),
        "Nombre": nombre.get(),
        "telefono": telefono.get()
    }
    cuentas.append(datos)
        
    file = openpyxl.Workbook()
    hoja= file.active
    hoja.cell(row= 1, column= 1, value= "Nombre")
    hoja.cell(row= 1, column= 2, value= "Apellido")
    hoja.cell(row= 1, column= 3, value= "Telefono")
                
    row = 2
    ''''
    for valor in cuentas:
        hoja.cell(row=row, column= 1, value=valor[0])
        hoja.cell(row=row, column= 2, value=valor[1])
        hoja.cell(row=row, column= 3, value=valor[2])
        row += 1'''
    
               
    file.save("C:/Users/icbc/Documents/MasterChechu/MasterChechu/cursoPython/tp1/Inventario.xlsx")
    file.close()
    return apellido.get(), nombre.get(), telefono.get()
    
    
    
    
#Alerta otra ventana
def guardar ():
    messagebox.showinfo("Alerta", "Guardado !")
    #Button(root, text='Close',command=root.destroy).grid(row=1, column=1, justify=CENTER )
    
    root.destroy()
    


print("Llamamos a la ventana de entrada de datos")

texto=ventanaCapturaDatos()

print("El texto que has introducido es:")
print(texto)

