from os import path
from notifypy import Notify
import time
from datetime import datetime

now =datetime.now()

def iniciar(vez):

    notification = Notify(default_notification_application_name ="ForYou")
    notification.title = vez
    notification.message = "Toma agua, cuis"

    audio="awa.wav"
    icono="agua.ico"

    direccion = path.abspath(path.dirname(__file__))

    notification.icon = path.join(direccion, icono)
    notification.audio = path.join(direccion, audio)
    notification.send() 

if now.hour==8:
    iniciar("1/8")
if now.hour==10:
    iniciar("2/8")
if now.hour==12:
    iniciar("3/8")
if now.hour==14:
    iniciar("4/8")
if now.hour==16:
    iniciar("5/8")
if now.hour==18:
    iniciar("6/8")
if now.hour==20:
    iniciar("7/8")
if now.hour==22:
    iniciar("8/8")