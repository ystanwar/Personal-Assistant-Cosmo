from tkinter import *

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

                
                quitbutton.place(x=0, y=0)
                
                
        def client_exit(self):
                exit()
                
root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop
