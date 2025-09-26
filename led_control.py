import serial
import time


arduino = serial.Serial(port="COM3",baudrate=9600,timeout=1)
time.sleep(2)


while True:
    scelta = input("Vuoi accendere il LED 1 o il LED 2? (0 per spegnere, q per uscire): ")


    if scelta == "q":
        print("Programa terminato.")
        break
    elif scelta in ["0","1","2","3"]:
        arduino.write(scelta.encode()) # INVIA IL COMNADO

    else:
        print("Comando non valido, scegli 0, 1, 2 ,3 o q.")
