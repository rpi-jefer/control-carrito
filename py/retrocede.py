"""
Retrocede, los dos motores marchan hacia la izquierda 
Gp 11: 0 |  Gp 16: 0   
Gp 15: 1 |  Gp 18: 1
"""
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)#Motor1
GPIO.setup(15,GPIO.OUT)

GPIO.setup(16,GPIO.OUT)#motor2
GPIO.setup(18,GPIO.OUT)

GPIO.output(11,True)
GPIO.output(15,False)

GPIO.output(16,True)
GPIO.output(18,False)



