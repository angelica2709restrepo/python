from tkinter import *
from tkinter import messagebox
import mysql.connector
import os, sys 

conexion=mysql.connector.connect(
    host="localhost",
    user='root',
    password='',
    database='python',
    port=3306
)

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)



#Mostrar todos los pedidos
def revision():
        cursor = conexion.cursor()
        consulta = "SELECT id_pedido,total FROM pedidos"
        cursor.execute(consulta)
        resultados = cursor.fetchall()
        mensaje = ""
        for fila in resultados:
            mensaje += str(fila) + "\n"
        messagebox.showinfo("Registros", mensaje)
        conexion.commit()



def insertar_datos():
    #Hamburguesa
    valor = int(cont.get())
    if (valor>=1):
        cursor = conexion.cursor()
        consulta = "INSERT INTO pedidos_comida (id_c,cantidad) VALUES ('1',%s)"
        datos = (valor,)
        try:
            cursor.execute(consulta, datos)
            conexion.commit()
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"No se pudo insertar los datos: {error}")
        consulta0="INSERT INTO pedidos (total) SELECT comida.precio *(%s) FROM comida WHERE id_comida=('1')"
        try:
            cursor.execute(consulta0, datos)
            conexion.commit()
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"No se pudo insertar los datos: {error}")
        consulta1= "UPDATE pedidos_comida JOIN pedidos SET pedidos_comida.id_p = pedidos.id_pedido WHERE id_c=1 AND cantidad=(%s)"
        try:
            cursor.execute(consulta1, datos)
            conexion.commit()
            messagebox.showinfo("Éxito", "Datos insertados correctamente.")
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"No se pudo insertar los datos: {error}")

        cursor.close()
        conexion.close()

    #Sandwich
    valor1 = int(cont2.get())
    if (valor1>=1):
        cursor = conexion.cursor()
        consulta = "INSERT INTO pedidos_comida (id_c,cantidad) VALUES ('2',%s)"
        datos = (valor1,)
        try:
            cursor.execute(consulta, datos)
            conexion.commit()
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"No se pudo insertar los datos: {error}")
        consulta0="INSERT INTO pedidos (total) SELECT comida.precio *(%s) FROM comida WHERE id_comida=('2')"
        try:
            cursor.execute(consulta0, datos)
            conexion.commit()
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"No se pudo insertar los datos: {error}")
        consulta1= "UPDATE pedidos_comida JOIN pedidos SET pedidos_comida.id_p = pedidos.id_pedido WHERE id_c=2 AND cantidad=(%s)"
        try:
            cursor.execute(consulta1, datos)
            conexion.commit()
            messagebox.showinfo("Éxito", "Datos insertados correctamente.")
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"No se pudo insertar los datos: {error}")

        cursor.close()
        conexion.close()

    #Lasagna
    valor2 = int(cont3.get())
    if (valor2>=1):
        cursor = conexion.cursor()
        consulta = "INSERT INTO pedidos_comida (id_c,cantidad) VALUES ('3',%s)"
        datos = (valor2,)
        try:
            cursor.execute(consulta, datos)
            conexion.commit()
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"No se pudo insertar los datos: {error}")
        consulta0="INSERT INTO pedidos (total) SELECT comida.precio *(%s) FROM comida WHERE id_comida=('3')"
        try:
            cursor.execute(consulta0, datos)
            conexion.commit()
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"No se pudo insertar los datos: {error}")
        consulta1= "UPDATE pedidos_comida JOIN pedidos SET pedidos_comida.id_p = pedidos.id_pedido WHERE id_c=3 AND cantidad=(%s)"
        try:
            cursor.execute(consulta1, datos)
            conexion.commit()
            messagebox.showinfo("Éxito", "Datos insertados correctamente.")
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"No se pudo insertar los datos: {error}")

        cursor.close()
        conexion.close()

    #Coca de piña
    valor3 = int(cont5.get())
    if (valor3>=1):
        cursor = conexion.cursor()
        consulta = "INSERT INTO pedidos_bebida (id_b,cantidad) VALUES ('1',%s)"
        datos = (valor3,)
        try:
            cursor.execute(consulta, datos)
            conexion.commit()
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"No se pudo insertar los datos: {error}")
        consulta0="INSERT INTO pedidos (total) SELECT bebida.precio *(%s) FROM bebida WHERE id_bebida=('1')"
        try:
            cursor.execute(consulta0, datos)
            conexion.commit()
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"No se pudo insertar los datos: {error}")
        consulta1= "UPDATE pedidos_bebida JOIN pedidos SET pedidos_bebida.id_p = pedidos.id_pedido WHERE id_b=1 AND cantidad=(%s)"
        try:
            cursor.execute(consulta1, datos)
            conexion.commit()
            messagebox.showinfo("Éxito", "Datos insertados correctamente.")
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"No se pudo insertar los datos: {error}")

        cursor.close()
        conexion.close()

    #Ginger
    valor4 = int(cont6.get())
    if (valor4>=1):
        cursor = conexion.cursor()
        consulta = "INSERT INTO pedidos_bebida (id_b,cantidad) VALUES ('2',%s)"
        datos = (valor4,)
        try:
            cursor.execute(consulta, datos)
            conexion.commit()
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"No se pudo insertar los datos: {error}")
        consulta0="INSERT INTO pedidos (total) SELECT bebida.precio *(%s) FROM bebida WHERE id_bebida=('2')"
        try:
            cursor.execute(consulta0, datos)
            conexion.commit()
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"No se pudo insertar los datos: {error}")
        consulta1= "UPDATE pedidos_bebida JOIN pedidos SET pedidos_bebida.id_p = pedidos.id_pedido WHERE id_b=2 AND cantidad=(%s)"
        try:
            cursor.execute(consulta1, datos)
            conexion.commit()
            messagebox.showinfo("Éxito", "Datos insertados correctamente.")
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"No se pudo insertar los datos: {error}")

        cursor.close()
        conexion.close()

    #Juguito de si
    valor5 = int(cont7.get())
    if (valor5>=1):
        cursor = conexion.cursor()
        consulta = "INSERT INTO pedidos_bebida (id_b,cantidad) VALUES ('3',%s)"
        datos = (valor5,)
        try:
            cursor.execute(consulta, datos)
            conexion.commit()
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"No se pudo insertar los datos: {error}")
        consulta0="INSERT INTO pedidos (total) SELECT bebida.precio *(%s) FROM bebida WHERE id_bebida=('3')"
        try:
            cursor.execute(consulta0, datos)
            conexion.commit()
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"No se pudo insertar los datos: {error}")
        consulta1= "UPDATE pedidos_bebida JOIN pedidos SET pedidos_bebida.id_p = pedidos.id_pedido WHERE id_b=3 AND cantidad=(%s)"
        try:
            cursor.execute(consulta1, datos)
            conexion.commit()
            messagebox.showinfo("Éxito", "Datos insertados correctamente.")
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"No se pudo insertar los datos: {error}")

        cursor.close()
        conexion.close()



raiz=Tk()
raiz.geometry("1000x600")
raiz.title("Pedidos pro")

#Apartado 1
miF=Frame(raiz,width="500",height="800")
miF.config(bg="purple")
miF.config(relief="raised")
miF.pack(side=LEFT)
#Apartado 2
miF2=Frame(raiz,width="500",height="800")
miF2.config(bg="gray")
miF2.config(relief="raised")
miF2.pack(side=RIGHT)

#Comidas
comida=Label(miF,text="Comidas")
comida.place(x=230,y=30)
#Imagenes comidas
miI=PhotoImage(file=resource_path('h.png'))
miI=miI.subsample(2)
miL=Label(miF,image=miI)
miL.place(x=100,y=90)
cont=Spinbox(from_=0,to=5,increment=1,width=10)
cont.place(x=270,y=140)

miI2=PhotoImage(file=resource_path('s.png'))
miI2=miI2.subsample(2)
miL2=Label(miF,image=miI2)
miL2.place(x=100,y=250)
cont2=Spinbox(from_=0,to=5,increment=1,width=10)
cont2.place(x=270,y=300)

miI3=PhotoImage(file=resource_path('l.png'))
miI3=miI3.subsample(2)
miL3=Label(miF,image=miI3)
miL3.place(x=100,y=400)
cont3=Spinbox(from_=0,to=5,increment=1,width=10)
cont3.place(x=270,y=460)

#Bebidas
bebida=Label(miF2,text="Bebidas")
bebida.place(x=230,y=30)
#Imagenes bebidas
miI5=PhotoImage(file=resource_path('c.png'))
miI5=miI5.subsample(2)
miL5=Label(miF2,image=miI5)
miL5.place(x=100,y=90)
cont5=Spinbox(from_=0,to=5,increment=1,width=10)
cont5.place(x=780,y=140)

miI6=PhotoImage(file=resource_path('g.png'))
miI6=miI6.subsample(2)
miL6=Label(miF2,image=miI6)
miL6.place(x=100,y=240)
cont6=Spinbox(from_=0,to=5,increment=1,width=10)
cont6.place(x=780,y=300)

miI7=PhotoImage(file=resource_path('j.png'))
miI7=miI7.subsample(2)
miL7=Label(miF2,image=miI7)
miL7.place(x=100,y=400)
cont7=Spinbox(from_=0,to=5,increment=1,width=10)
cont7.place(x=780,y=460)



Boton1=Button(raiz,text="Enviar pedido",bg="cyan",command=insertar_datos)
Boton1.place(x=460,y=400)

Boton2=Button(raiz,text="Revisar pedidos",bg="cyan",command=revision)
Boton2.place(x=455,y=450)

raiz.mainloop()