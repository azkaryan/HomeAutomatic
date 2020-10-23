#!usr/bin/env/ python
## apaga.py
#Kita mengimpor Perpustakaan dan mengubah namanya menjadi GPIO
Impor RPi.GPIO sebagai GPIO
#Kami membangun sistem penomoran bahwa kita ingin, 
#dalam hal ini sistem BCM
GPIO.setmode(GPIO. BCM)
#Mengkonfigurasi GPIO pin 4 sebagai output
GPIO.setup(4, GPIO. KELUAR)
#Mematikan dipimpin
GPIO.output(4, GPIO. RENDAH)
#Dan kita membebaskan GPIO
GPIO.cleanup()
