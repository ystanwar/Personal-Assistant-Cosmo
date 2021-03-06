import speech_recognition as sr
import shutil
import pyttsx
import os
import os.path
import requests
from urllib import request
from bs4 import BeautifulSoup
import smtplib
import webbrowser
import numpy as np
import cv2
import sys
import string
import winsound
from time import sleep
from tkinter import *
from PIL import Image, ImageTk

engine = pyttsx.init()
found_files = ["HELLO"]
crd = ""


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_Window()

    def init_Window(self):
        self.master.title("COSMO")
        self.pack(fill=BOTH, expand=1)
        startbutton = Button(self, text="Bulid Cosmo", command=self.build_cosmo)
        startbutton.place(x=280, y=10)

    def print_som(self):
        print("I m here")

    def speechinput(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print(".........")
            crd = "........."
            listbox.insert(END, crd)
            # engine.say('say something')
            # engine.runAndWait()
            audio = r.listen(source)
        try:
            outString = r.recognize_google(audio)

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            crd = "Google Speech Recognition could not understand audio"
            listbox.insert(END, crd)
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            crd = "Could not request results from Google Speech Recognition service; {0}".format(e)
            listbox.insert(END, crd)
        return outString

    def exit(self):
        exit()

    def show_text(self):
        text = Label(self, text="This is your peorsnal assisatant cosmo")
        text.pack()

    def g_crawler(self, query):
        url = "https://www.google.co.in/search?q=" + query + "&source=lnms&tbm=isch"
        print(url)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        for link in soup.findAll("img"):
            if link.parent.name == 'a':
                print(link["src"])
                image_link = link["src"]
        dec = input("Do you want to download images")
        crd = "Do you want to download images"
        listbox.insert(END, crd)
        engine.say('Do you want to download images')
        engine.runAndWait()
        if dec == "yes":
            self.download_web_image(image_link, query)

    def download_web_image(self, url, query):
        f_name = query + '.jpg'
        request.urlretrieve(url, f_name)
        self.g_image_viewer(f_name)

    def tour_around(self, query):
        url = "https://www.google.co.in/search?q=near by " + query
        source_code = requests.get(url)
        plain_text = source_code.text
        alt = "Image result for " + query
        listbox.insert(END, alt)
        soup = BeautifulSoup(plain_text, "html.parser")
        i = 0
        for link in soup.findAll('span'):
            if link.has_attr('class'):
                pass
            else:
                if i == 2:
                    desc = link.text.split('.')
                    for lines in desc:
                        listbox.insert(END, lines)
                        print(lines)
                i = i + 1
        j = 0
        for link in soup.findAll('span', {'class': '_G0d'}):
            if j == 0:
                pass
            else:
                crd = link.text[1:]
                listbox.insert(END, crd)
                listbox.update()
                print(j, link.text[1:])
            j = j + 1

    goog_url = 'http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=8&e=14&f=2016&g=d&a=7&b=19&c=2004&ignore=.csv'

    def download_stock_data(self, csv_url):
        response = request.urlopen(csv_url)
        csv = response.read()
        csv_str = str(csv)
        lines = csv_str.split("\\n")
        dest_url = r'goog.csv'
        fx = open(dest_url, 'w')
        for line in lines:
            fx.write(line + "\n")
        fx.close()

    def image_viewer(self, i_name):
        img = cv2.imread(i_name, 1)
        res = cv2.resize(img, None, fx=0.1, fy=0.1, interpolation=cv2.INTER_LINEAR)
        cv2.imshow('image', res)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def g_image_viewer(self, i_name):
        img = cv2.imread(i_name, 1)
        res = cv2.resize(img, None, fx=2.5, fy=2.5, interpolation=cv2.INTER_LINEAR)
        cv2.imshow('image', res)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    Freq = 2500
    Dur = 1000

    def setreminder(self, minute, reminder):
        minutes = int(minute)
        print(minutes)
        Freq = 2500
        Dur = 1000
        if minutes < 0:
            crd = "Invalid value for minutes, should be >= 0"
            listbox.insert(END, crd)
            print("Invalid value for minutes, should be >= 0")
            sys.exit(1)

        seconds = minutes * 60
        print(seconds)
        if minutes == 1:
            time = " minute"
        else:
            time = " minutes"

        if minutes >= 0:
            print('I will remind you after ' + str(minutes) + ' minutes')
            crd = 'I will remind you after ' + str(minutes) + ' minutes'
            listbox.insert(END, crd)
            engine.say('OK I will remind you')
            sleep(seconds)
            engine.say('reminder for')
            engine.say(reminder)
            engine.runAndWait()
            print("reminder for", reminder)
            for i in range(5):
                winsound.Beep(Freq, Dur)
                sleep(1)

    def build_cosmo(self):
        crd = "Greetings!"
        listbox.insert(END, crd)
        engine.say('Greetings!')
        listbox.update()
        crd = "How are you today?"
        engine.say('How are you today?')
        listbox.insert(END, crd)
        listbox.update()

        crd = "Say Something"
        engine.say('say something')
        listbox.insert(END, crd)
        listbox.update()
        engine.runAndWait()

        program = "yes"
        while program == "yes":

            print("----------------PERSONAL ASSISTANT--------------")

            stm = str(self.speechinput())
            #stm = "display current directory"
            print("You said: " + stm)
            listbox.insert(END, stm)
            listbox.update()
            if "display current directory" in stm:
                crd = str(os.getcwd())
                # print(crd)
                listbox.insert(END, crd)

                print(crd)
            elif "display list of directory" in stm:
                crd = str(os.listdir())
                listbox.insert(END, crd)
                print(crd)
            elif "make new directory" in stm:
                n_dir = stm[19:]
                os.mkdir(n_dir)
                engine.say('directory created')
                engine.runAndWait()
                crd = "directory created"
                listbox.insert(END, crd)
                print("directory created")
            elif "delete file" in stm:
                d_file = stm[12:]
                os.remove(d_file)
                engine.say('file deleted')
                engine.runAndWait()
                crd = "file deleted"
                listbox.insert(END, crd)
                print("file deleted")
            elif "rename directory" in stm:
                old_n = stm[17:]
                print("Enter new Direcctory name")
                new_n = self.speechinput()
                os.rename(old_n, new_n)
                engine.say('file renamed')
                engine.runAndWait()
                crd = "file renamed"
                listbox.insert(END, crd)
                print("file renamed")
            elif "rename file" in stm:
                old_f = stm[12:] + ".txt"
                engine.say('Enter new File name')
                engine.runAndWait()
                crd = "Enter new File name"
                listbox.insert(END, crd)
                print("Enter new File name")
                new_f = self.speechinput() + ".txt"
                os.rename(old_f, new_f)
            elif "delete directory" in stm:
                del_d = stm[17:]
                os.rmdir(del_d)
                engine.say('directory deleted')
                crd = "directory deleted"
                listbox.insert(END, crd)
                engine.runAndWait()
                print("directory deleted")
            elif "delete file" in stm:
                del_f = stm[12:] + ".txt"
                os.remove(del_f) + ".txt"
                engine.say('file deleted')
                engine.runAndWait()
                crd = "file deleted"
                listbox.insert(END, crd)
                print("file deleted")
            elif "copy file" in stm[:10]:
                file_name = stm[10:]
                print(stm[10:] + ".txt")
                if os.path.exists(file_name + ".txt"):
                    print("File exist")
                    crd = "File exist"
                    listbox.insert(END, crd)
                    engine.say('Say the name of destination file')
                    engine.runAndWait()
                    crd = "Say the name of destination file"
                    listbox.insert(END, crd)
                    print("Say the name of destination file")
                    dest = str(self.speechinput()) + ".txt"
                    print(dest)
                    shutil.copy2(file_name + '.txt', dest)
                    crd = "file copied"
                    listbox.insert(END, crd)
                    engine.say('File copied')
                    engine.runAndWait()
                else:
                    engine.say('The said File does not exist')
                    engine.say('Creating new text file')
                    engine.say('Say File Name: ')
                    crd = "The said File does not exist"
                    listbox.insert(END, crd)
                    crd = "Creating new text file"
                    listbox.insert(END, crd)
                    crd = "Say File Name: "
                    listbox.insert(END, crd)
                    print("The said File does not exist")
                    print('Creating new text file')
                    print("Say File Name: ")
                    newFName = str(self.speechinput())
                    engine.say("You said: " + newFName)
                    engine.runAndWait()
                    print("You said: " + newFName)
                    name = newFName + '.txt'
                    try:
                        file = open(name, 'a')  # Trying to create a new file or open one
                        print("File " + name + ".txt created")
                        crd = "File " + name + ".txt created"
                        listbox.insert(END, crd)
                        engine.say('File  created')
                        crd = "file created"
                        listbox.insert(END, crd)

                        engine.runAndWait()
                        file.close()

                    except:
                        print('Something went wrong! Can\'t tell what?')

            elif "images of" in stm:
                search = stm[10:]
                self.g_crawler(search)
            elif "places to visit in" in stm:
                city = stm
                self.tour_around(city)
            elif "send email" in stm:
                sender = "YOUREMAIL@gmail.com"
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(sender, "PASSWORD")
                print("Say the email address of receiver")
                receiver = input("To whom do you want to send email")
                print(receiver)
                print("what message do you want to send")
                msg = str(speechinput())
                print(msg)
                server.sendmail(sender, receiver, msg)
                server.quit()
            elif "search in Chrome" in stm:
                header = 'http://google.com/?#q='
                engine.say('what do you want to search ')
                crd = "what do you want to search "
                listbox.insert(END, crd)
                engine.runAndWait()
                query = str(speechinput())
                chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                url = header + query
                webbrowser.get(chrome_path).open(url)
            elif "download csv file for Google" in stm:
                self.download_stock_data(goog_url)
            elif "open image" in stm:
                i_name = stm[11:] + ".jpg"
                self.image_viewer(i_name)
            elif "open text file" in stm:
                name = stm[15:] + ".txt"
                webbrowser.open(name)
            elif "show video for" in stm:
                video = stm[15:]
                webbrowser.open("https://www.youtube.com/results?search_query=" + video)
            elif "set reminder for" in stm:
                reminder = stm[17:]

                engine.say('please enter time in minutes after which you want to be reminded')
                crd = "please enter time in minutes after which you want to be reminded"
                listbox.insert(END, crd)
                engine.runAndWait()
                min = input("please enter time in minutes after which you want to be reminded")
                self.setreminder(min, reminder)
            elif "thank you":
                crd = "good bye"
                listbox.insert(END, crd)
                listbox.update()
                engine.say('Good Bye')
                engine.runAndWait()
                self.exit()
                program = "no"
            else:
                print("you need to be more specific")
                crd = "you need to be more specific"
                listbox.insert(END, crd)
            listbox.update()
            # print("Do u want to continue")
            # engine.say('Do you want to continue')
            # engine.runAndWait()
            # program = str(self.speechinput())


root = Tk()
root.geometry("640x480")
listbox = Listbox(root)

for a in found_files:
    listbox.insert(END, a)
    listbox.insert(END, crd)

listbox.pack(fill=BOTH, expand=YES)
listbox.update_idletasks()

app = Window(root)
root.mainloop()
