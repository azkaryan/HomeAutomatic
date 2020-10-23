#!usr/bin/env/ python
## enciende.py
#Importamos la libreria y le cambiamos el nombre a GPIO
Impor RPi.GPIO sebagai GPIO
#Kami membangun sistem penomoran bahwa kita ingin, 
#dalam hal ini sistem BCM
GPIO.setmode(GPIO. BCM)
#Mengkonfigurasi GPIO pin 4 sebagai output
GPIO.setup(4, GPIO. KELUAR)
#Kami menyalakan led
GPIO.output(4, GPIO. TINGGI)
