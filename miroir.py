from tkinter import *
from PIL import ImageTk, Image
import random
from threading import Thread
import serial
import playsound
import time
class interface(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        global w,images, fenetre
        fenetre = Tk()
        fenetre.attributes("-fullscreen", 1)
        fenetre.configure(bg="black")  # background
        images = []
        for fname in range(1, 7):  # Randomiser les images
            img = ImageTk.PhotoImage(Image.open("C:\Program Files (x86)\%d.jpg" % (fname)))
            images.append(img)
        w = Label(fenetre, image=img)
        fenetre.mainloop()

class change(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        num = random.randint(0, 5)
        w.configure(image=images[num])
        w.pack(side="bottom", fill="both", expand="yes")
        sound = playsound.playsound("D:\M.wav", True)
        time.sleep(2)
        w.pack_forget()
        fenetre.update()
class Arduino(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        ser = serial.Serial('COM3', 9600)
        while True:
            line = ser.readline()
            line = line.decode('utf-8').replace('\n', '')
            print(line)
            line = int(line)
            if (line > 400):
                thread_3 = change()
                thread_3.start()

# Création des threads
thread_1 = interface()
thread_2 = Arduino()

# Lancement des threads
thread_1.start()
thread_2.start()