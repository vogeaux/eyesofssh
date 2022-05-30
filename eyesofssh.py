from pynput.keyboard import Key, Listener
import os, shutil, datetime, winshell, tempfile, smtplib
from win32com.client import Dispatch
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import threading, socket
from tkinter import *
from tkinter import filedialog, messagebox
import down as down
import self as self
import smtplib
from email import encoders
from os import *
from fabric.api import *
from fabric import *
import os
from pythonping import ping
import fabric
import threading
import socket
import sys
from paramiko import SSHClient
from paramiko import AutoAddPolicy
from tkinter import tix
import tkinter as tk




def connection ():
    user = mentuser.get()
    password = mentpassword.get()
    IP = mentIP.get()
    port = mentPort.get()
    env.host_string = IP
    env.user = user
    env.password = password
    sshConnection = SSHClient()
    sshConnection.set_missing_host_key_policy(AutoAddPolicy())
    try:
        sshConnection.connect(IP, port=int(port), username=user, password=password, timeout=int("2"),allow_agent=False, look_for_keys=False)
        status = 'Succeeded'
        valide_connect.configure(text="V", background="green")
        entry_1.configure(background="green")
        valide_connection.configure(text="V", background="green")
        entry_2.configure(background="green")
        entry_21.configure(background="green")
        valide_connect.configure(text="V", background="green")
        entry_3.configure(background="green")
        sshConnection.close()
    except:
        status = 'Failed'
        print(status)
        print("erreur")
        valide_connect.configure(text="X", background="red")
        entry_1.configure(background="red")
        valide_connection.configure(text="X", background="red")
        entry_2.configure(background="red")
        entry_21.configure(background="red")
        valide_connect.configure(text="X", background="red")
        entry_3.configure(background="red")



myApp = Tk()
myApp.geometry('500x500')
myApp.title("eyesofssh")
myApp.resizable(width=False, height=False)

mentIP = StringVar()
mentPort = StringVar()
mentuser = StringVar()
mentpassword = StringVar()


label_0 = Label(myApp, text="eyesofssh-storm",width=20,font=("bold", 20),background=None)
label_0.place(x=90,y=20)


label_2 = Label(myApp, text="IP de la machine: ",width=20,font=("bold", 10))
label_2.place(x=15,y=60)
entry_2 = Entry(myApp,textvariable=mentIP)
entry_2.place(x=150,y=60)

label_21 = Label(myApp, text="Port: ",width=20,font=("bold", 10))
label_21.place(x=250,y=60,width=50)
entry_21 = Entry(myApp,textvariable=mentPort)
entry_21.place(x=300,y=60,width=50)

label_3 = Label(myApp, text="nom d'utilisateur : ",width=20,font=("bold", 10))
label_3.place(x=15,y=90)
entry_3 = Entry(myApp,textvariable=mentuser)
entry_3.place(x=150,y=90)

label_1 = Label(myApp, text="mots de passe : ",width=20,font=("bold", 10))
label_1.place(x=15,y=110)
entry_1 = Entry(myApp,textvariable=mentpassword)
entry_1.place(x=150,y=110)

mButton_valide = Button(myApp,text="test de connetion", command = None).place(x=300,y=150)
valide_connect = Label(myApp, text="V",background= "green")
valide_connect.place(x=450,y=150)

mButton_valide = Button(myApp,text="test de conf", command = None).place(x=300,y=200)
valide_connect = Label(myApp, text="V",background= "green")
valide_connect.place(x=450,y=200)



mButton_connection = Button(myApp,text="test de compte", command = connection).place(x=300,y=100)
valide_connection = Label(myApp, text="V",background= "green")
valide_connection.place(x=450,y=100)

myApp.mainloop()