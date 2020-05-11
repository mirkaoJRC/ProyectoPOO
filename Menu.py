import tkinter as tk
from tkinter import messagebox
from tkinter import *
import cv2




class ImageStorage:

        def __init__(self):
                pass

        @staticmethod
        def read_image(path_img):
                """Leer una imagen desde el disco y devolver in objeto imagen"""
                if isinstance(path_img, str):
                        try:
                                img = cv2.imread(path_img)
                        except:
                                print("Error de path")
                        return img
                else:
                        print("formato no valido")
                        return None

        @staticmethod
        def save_img(img, name_img):
                # write image on disk
                # escribir validador de string, regex, validar que un string termine en jpg
                name_img = name_img + ".png"
                cv2.imwrite(name_img, img)


def img_to_gray_scale(img):
        """Recibe un objeto imagen y devuleve la imagen en blanco y negro"""
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return gray_img


if __name__ == '__main__':

        img = ImageStorage.read_image("leon.png")
        img_gray = img_to_gray_scale(img)
        ImageStorage.save_img(img=img_gray, name_img="Leon Hola mundo")
        print("Comenzando...")


class windowclass():

        def __init__(self,master):
                self.master = master
                self.frame = tk.Frame(master)
                self.lbl = Label(master , text = "Bienvenido a la Degradacion de Imagen", font=("Helvetica", 14), bg="#115111", fg= "#fff"  )
                self.lbl.pack()
                self.lbl.place(x = 50, y =20)
                self.Usuario = Label(self.master, text = "Introduzca usuario:",font=("Helvetica", 10), bg="#115111", fg= "#fff" )
                self.Usuario.pack()
                self.Usuario.place(x=20, y=75)
                # Encapsulando el usuario de entrada
                self.__entrada = Entry(master)
                self.__entrada.pack()
                self.__entrada.place(x=150, y = 75)
                self.btn = Button(master , text = "Confirmar" ,bg="green",fg="#fff", command = self.validar )
                self.btn.pack()
                self.btn.place(x= 120, y = 110)
                self.btn2 = Button(master, text= "Salir del programa",bg="green",fg="#fff" ,command = self.cerrar)
                self.btn2.pack()
                self.btn2.place(x= 190, y = 110)
                self.frame.pack()

        def cerrar(self):
            self.master.destroy()


        def validar(self):
                usuario = self.__entrada.get()
                t=usuario.lower()
                if t == 'mirkao':
                      
                        self.newWindow = tk.Toplevel(self.master)
                        self.app = windowclass1(self.newWindow)
                else:
                        messagebox.showwarning("Cuidado", "Passwoed Incorrecto\n***Vuelva a intenetar***")


class windowclass1():

        def __init__(self , master):
                self.master = master
                self.frame = Frame(master)
                self.master.title("Ventana de Inicio")
                self.master.geometry("500x500")
                self.master.config(bg="#102121")
                self.master.iconbitmap("icono1.ico")
                self.frame1=Frame(self.master, width= 300, height= 200)
                self.frame1.place(x=50, y=400)
                self.frame1.config(bg="#102121")
                self.frame1.pack()
                self.frame2 = Frame(self.master, width=300, height=200)
                self.frame2.place(x=350, y=400)
                self.frame2.config(bg="#102121")
                self.frame2.pack()
                self.lbl= Label(self.master, text="El Proyecto agarra una imagen y en gris \n Atravez de la biblioteca OPEN CV...", bg="#102121",fg="white")
                self.lbl.place(x=20,y=100)
                self.lbl.pack()
                self.btn1= Button(self.master, text="Iniciar Programa", command = self.Correr_Programa)
                self.btn1.pack()
                self.btn1.place(x=50,y= 440)
                self.quitButton = Button(self.master, text = 'Salir de la aplicacion', width = 25 , command = self.close_window)
                self.quitButton.pack()
                self.quitButton.place(x=160, y =440)
                self.frame.pack()



        def Correr_Programa(self):
                self.imagen= PhotoImage(file="leon.png")
                self.label=Label(self.frame1, image = self.imagen,width= 250, height=200)
                self.label.place(x=100, y=100)
                self.label.pack()
                self.imagen1 = PhotoImage(file="Leon Hola mundo.png")
                self.label = Label(self.frame2, image=self.imagen1, width=250, height=200)
                self.label.place(x=200, y=200)
                self.label.pack()



        def close_window(self):
                self.master.destroy()


root = Tk()

root.title("window")

root.iconbitmap("iconoPrincipal.ico")

root.config(bg="#115111")

root.geometry("450x150")

cls = windowclass(root)

root.mainloop()