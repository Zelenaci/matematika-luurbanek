#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
import random
from tkinter import (Label, Button, Scale, HORIZONTAL, Canvas, Frame, Entry, LEFT, RIGHT, N, S, E ,W, StringVar, IntVar)

# from tkinter import ttk

class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Počítání"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.lbl = tk.Label(self, text="Matematika")
        self.lbl.pack(anchor=S)
        self.btn = tk.Button(self, text="Zavřít", command=self.quit) #vytvoření
        self.btn.pack(anchor=S) #umístění
        self.btn2 = tk.Button(self, text="novy priklad", command=self.about)
        self.btn2.pack(anchor=S)


    def plus(self):
        self.cisloA = random.randint(1,99)
        self.cisloB = random.randint(1,100-self.cisloA) #vysledek nemuze byt vetsi nez 100
        self.vysledek = self.cisloA + self.cisloB
        self.lbl.config(text = (f"{self.cisloA} + {self.cisloB}"))


        self.varPlus = IntVar()
        self.framePlus = Frame(self)
        self.framePlus.pack()
        self.lblPlus = Label(self.framePlus,)
        self.lblPlus.pack(side=RIGHT, anchor=N)  # umisteni widgetu do programu
        self.entryPlus = Entry(self.framePlus, width=5, textvariable=self.varPlus)
        self.entryPlus.pack(side=RIGHT, anchor=N)

    def minus(self):
        self.cisloA = random.randint(1,99)
        self.cisloB = random.randint(1,99)
        if self.cisloB > self.cisloB:
                self.cisloA, self.cisloB = self.cisloB, self.cisloA
        self.vysledek = self.cisloA - self.cisloB
        self.lbl.config(text = (f"{self.cisloA} - {self.cisloB} = {self.vysledek} "))



    def krat(self):
        self.cisloA = random.randint(1,10)
        self.cisloB = random.randint(1,10)
        self.vysledek = self.cisloA * self.cisloB
        self.lbl.config(text = (f"{self.cisloA} * {self.cisloB} = {self.vysledek} "))


    def deleno(self):
        self.vysledek = random.randint(1,9)
        self.cisloB = random.randint(1,9)
        self.cisloA = self.vysledek * self.cisloB
        self.lbl.config(text = (f"{self.cisloA} / {self.cisloB} = {self.vysledek} "))

    def priklad(self):
        funkce = random.choice([self.plus,self.minus,self.krat,self.deleno])
        funkce()


    def about(self):
        self.priklad()

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()
