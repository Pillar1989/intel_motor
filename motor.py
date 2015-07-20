__author__ = 'Pillar'
import mraa
import time



class motor(object):
	'motor driver'
	__speed = 0.5

	def __init__(self,en,ina,inb,pwm):
		self.__pin_en = mraa.Gpio(en)
		self.__pin_ina = mraa.Gpio(ina)
		self.__pin_inb = mraa.Gpio(inb)
		self.__pin_pwm = mraa.Pwm(pwm)


		self.__pin_en.dir(mraa.DIR_OUT)
		self.__pin_ina.dir(mraa.DIR_OUT)
		self.__pin_inb.dir(mraa.DIR_OUT)
		self.__pin_pwm.period_us(100)
		self.__pin_pwm.write(self.__speed)
		self.__pin_pwm.enable(True)


	def stop(self):
		'stop move'
		self.__pin_en.write(0)
		self.__pin_ina.write(0)
		self.__pin_inb.write(0)

	def clockwise(self):
		'a clockwise rotation'
		self.__pin_ina.write(1)
		self.__pin_inb.write(0)
		self.__pin_en.write(1)
	def anticlockwise(self):
		'a anticlockwise rotation'
		self.__pin_ina.write(0)
		self.__pin_inb.write(1)
		self.__pin_en.write(1)
	def get_speed(self):
		return self.__speed
		'return wheel speed'
	def set_speed(self,value):
		self.__speed = value
		if self.__speed < 0:
			self.__speed = 0
		elif self.__speed > 1:
			self.__speed = 1
		self.__pin_pwm.write(self.__speed)
		'set wheel speed'
	def get_current(self):
		'return driver electric current'
	def accelerate(self):
		'accelerate motor speed'
		self.__speed = self.__speed + 0.02
		if self.__speed < 0:
			self.__speed = 0
		elif self.__speed > 1:
			self.__speed = 1
		self.__pin_pwm.write(self.__speed)

	def decelerate(self):
		'decelerate motor speed'
		self.__speed = self.__speed - 0.02
		if self.__speed < 0:
			self.__speed = 0
		elif self.__speed > 1:
			self.__speed = 1
		self.__pin_pwm.write(self.__speed)






