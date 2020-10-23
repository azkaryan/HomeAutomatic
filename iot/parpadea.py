#!usr/bin/env/ python
## parpadea.py
#Kita mengimpor Perpustakaan dan mengubah namanya menjadi GPIO
Impor RPi.GPIO sebagai GPIO

#Diperlukan untuk penundaan
Impor waktu

#Kami membangun sistem penomoran bahwa kita ingin, 
#dalam hal ini sistem BCM
GPIO.setmode(GPIO. BCM)

#Mengkonfigurasi GPIO pin 4 sebagai output
GPIO.setup(4, GPIO. KELUAR)

#Menghidupkan dan mematikan dipimpin 5 kali
untuk saya dalam kisaran(0,5):

        GPIO.output(4, GPIO. TINGGI)
        Time.Sleep(1)(1)
        GPIO.output(4, GPIO. RENDAH)
        Time.Sleep(1)(1)

#Dan kita membebaskan GPIO
GPIO.cleanup()
