from tkinter import *
from PIL import Image, ImageTk

class Window(Frame):

        def __init__(self, master=None):
                Frame.__init__(self, master)
                self.master = master
                self.init_Window()
                        
        def init_Window(self):
                self.master.title("COSMO")
                self.pack(fill=BOTH, expand=1)
                quitbutton = Button(self, text = "quit",command=self.client_exit)
                menu = Menu(self.master)
                self.master.config(menu=menu)
                file=Menu(menu)
                file.add_command(label="Exit",command=self.client_exit)
                menu.add_cascade(label="file",menu=file)

                edit=Menu(menu)
                edit.add_command(label="undo")
                menu.add_cascade(label="Edit", menu=edit)
                edit.add_command(label="text",command=self.show_text)
                edit.add_command(label="Img",command=self.show_img)
                quitbutton.place(x=0, y=0)
                
                
        def client_exit(self):
                exit()

        def show_text(self):
                text = Label(self,text="This is your peorsnal assisatant cosmo")
                text.pack()

        def show_img(self):
                load=Image.open("car.png")
                render = ImageTk.PhotoImage(load)

                img=Label(self,image=render)
                img.image = render
                img.place(x=0, y=0)
                
                
root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop
