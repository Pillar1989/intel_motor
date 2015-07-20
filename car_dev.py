__author__ = 'Pillar'
import  time
import threading
from motor import motor as M
import interrupt_dev

class car_dev(object):
	'''car function'''
	__speed = 0.5
	__left1_speed = 0.5
	__left2_speed = 0.5
	__right1_speed = 0.5
	__right2_speed = 0.5
	__current_l1_speed = 0
	__current_l2_speed = 0
	__current_r1_speed = 0
	__current_r2_speed = 0
	__full_speed = 21.0
	__left_flag = 0
	__right_flag = 0
	__current_status = "stop"
	__last_status = "stop"
	def __init__(self):
		'left1:       right1:       left2:         right2' \
		'en:55        en:13         en:32           en:31'  \
		'ina:41       ina:40        ina:46          ina:15' \
		'inb:54       inb:25        inb:53          inb:45' \
		'pwm:21       pwm:0         pwm:20          pwm:14'
		self.left1 = M(55,41,54,21)
		self.left2 = M(32,46,53,20)
		self.right1 = M(13,40,25,0)
		self.right2 = M(31,15,45,14)


		self.left1.set_speed(0.5)
		self.left2.set_speed(0.5)
		self.right1.set_speed(0.5)
		self.right2.set_speed(0.5)
		interrupt_dev.interrupt_init()
		self.pid()
	def forward(self):
		self.left1.anticlockwise()
		self.left2.anticlockwise()

		self.right1.clockwise()
		self.right2.clockwise()
		self.__current_status = "forward"
	def back(self):
		self.left1.clockwise()
		self.left2.clockwise()
		self.right1.anticlockwise()
		self.right2.anticlockwise()
		self.__current_status = "back"

	def turn_left(self):
		#self.left1.clockwise()
		self.left1.clockwise()
		#self.right1.anticlockwise()
		self.right1.clockwise()
		self.right2.clockwise()
		self.left2.clockwise()
		self.__current_status = "turn_left"
	def full_speed(self):
		self.__left1_speed = 1
		self.__left2_speed = 1
		self.__right1_speed = 1
		self.__right2_speed = 1
		self.left1.set_speed(self.__left1_speed)
		self.left2.set_speed(self.__left2_speed)
		self.right1.set_speed(self.__right1_speed)
		self.right2.set_speed(self.__right2_speed)
	def turn_right(self):
		#self.left1.clockwise()
		self.left2.anticlockwise()
		#self.right1.anticlockwise()
		self.right2.anticlockwise()
		self.right1.anticlockwise()
		self.left1.anticlockwise()
		self.__current_status = "turn_right"
	def stop(self):
		self.left1.stop()
		self.left2.stop()
		self.right1.stop()
		self.right2.stop()
	def accelerate(self):
		self.__speed += 0.01
		self.__left1_speed += 0.01
		self.__left2_speed += 0.01
		self.__right1_speed += 0.01
		self.__right2_speed += 0.01
		if (self.__left1_speed >= 1):
			self.__left1_speed = 1
		if (self.__left2_speed >= 1):
			self.__left2_speed = 1
		if (self.__right1_speed >= 1):
			self.__right1_speed = 1
		if (self.__right2_speed >= 1):
			self.__right2_speed = 1

		self.left1.set_speed(self.__left1_speed)
		self.left2.set_speed(self.__left2_speed)
		self.right1.set_speed(self.__right1_speed)
		self.right2.set_speed(self.__right2_speed)

	def decelerate(self):
		self.__speed -= 0.01
		self.__left1_speed -= 0.01
		self.__left2_speed -= 0.01
		self.__right1_speed -= 0.01
		self.__right2_speed -= 0.01
		if (self.__left1_speed <= 0):
			self.__left1_speed = 0
		if (self.__left2_speed <= 0):
			self.__left2_speed = 0
		if (self.__right1_speed <= 0):
			self.__right1_speed = 0
		if (self.__right2_speed <= 0):
			self.__right2_speed = 0

		self.left1.set_speed(self.__left1_speed)
		self.left2.set_speed(self.__left2_speed)
		self.right1.set_speed(self.__right1_speed)
		self.right2.set_speed(self.__right2_speed)
	def pid_irq(self):
		#print "pid_irq"
		self.__current_l1_speed = interrupt_dev.get_speed_a()
		self.__current_l2_speed = interrupt_dev.get_speed_c()

		self.__current_r1_speed = interrupt_dev.get_speed_b()
		self.__current_r2_speed = interrupt_dev.get_speed_d()

		if (abs(self.__current_l1_speed  - self.__current_l2_speed ) > 4  ):
			self.__last_status = self.__current_status
			self.__current_status = "fault"
			if ((self.__left1_speed - self.__current_l1_speed/self.__full_speed) > 0.15):
				self.__left2_speed = self.__current_l1_speed/self.__full_speed
				self.left2.set_speed(self.__left2_speed)
				self.__left_flag += 1
				print "1,>"+str(self.__left2_speed) + "<=>" +str(self.__current_l1_speed)


			if ((self.__left2_speed - self.__current_l2_speed/self.__full_speed) > 0.15):
				self.__left1_speed = self.__current_l2_speed/self.__full_speed
				self.left1.set_speed(self.__left1_speed)
				self.__left_flag += 1
				print "2,>"+str(self.__left2_speed) + "<=>" +str(self.__current_l2_speed)

			if (self.__left_flag == 0 ):
				if (self.__left1_speed > self.__left2_speed):
					self.left2.set_speed(self.__left1_speed)
					self.__left2_speed = self.__left1_speed
				else:
					self.left1.set_speed(self.__left2_speed)
					self.__left1_speed = self.__left2_speed
				self.__current_status = self.__last_status
			else:
				self.__left_flag = 0

		if (abs(self.__current_r1_speed  - self.__current_r2_speed ) > 4 or self.__right1_speed != self.__right2_speed ):
			self.__last_status = self.__current_status
			self.__current_status = "fault"
			if ((self.__right1_speed - self.__current_r1_speed/self.__full_speed) > 0.15):
				self.__right2_speed = self.__current_r1_speed/self.__full_speed
				self.right2.set_speed(self.__right2_speed)
				self.__right_flag += 1

			if ((self.__right2_speed - self.__current_r2_speed/self.__full_speed) > 0.15):
				self.__right1_speed = self.__current_r2_speed/self.__full_speed
				self.right1.set_speed(self.__right1_speed)
				self.__right_flag += 1

			if (self.__right_flag == 0 ):
				if (self.__right1_speed > self.__right2_speed):
					self.right2.set_speed(self.__right1_speed)
					self.__right2_speed = self.__right1_speed
				else:
					self.right1.set_speed(self.__right2_speed)
					self.__right1_speed = self.__right2_speed
				self.__current_status = self.__last_status
			else:
				self.__right_flag = 0

		if (self.__current_status == "forward" or self.__current_status == "back"):
			average_speed = (self.__current_l1_speed + self.__current_l2_speed + \
			self.__current_r1_speed + self.__current_r2_speed)/4.0
			current_speed = average_speed/self.__full_speed
			print "current->" + str(average_speed)
			if (abs(self.__speed - current_speed) > 0.05):
				current_left1_speed = self.__current_l1_speed/self.__full_speed
				current_left2_speed = self.__current_l2_speed/self.__full_speed
				current_right1_speed = self.__current_r1_speed/self.__full_speed
				current_right2_speed = self.__current_r2_speed/self.__full_speed
				if (abs(self.__speed - current_left1_speed) > 0.08):
					if current_left1_speed > self.__speed:
						self.__left1_speed -= 0.01
					else:
						self.__left1_speed += 0.01
					self.left1.set_speed(self.__left1_speed)
				if (abs(self.__speed - current_left2_speed) > 0.08):
					if current_left2_speed > self.__speed:
						self.__left2_speed -= 0.01
					else:
						self.__left2_speed += 0.01
					self.left2.set_speed(self.__left2_speed)

				if (abs(self.__speed - current_right1_speed) > 0.08):
					if current_right1_speed > self.__speed:
						self.__right1_speed -= 0.01
					else:
						self.__right1_speed += 0.01
					self.right1.set_speed(self.__right1_speed)
				if (abs(self.__speed - current_right2_speed) > 0.08):
					if current_right2_speed > self.__speed:
						self.__right2_speed -= 0.01
					else:
						self.__right2_speed += 0.01
					self.right2.set_speed(self.__right2_speed)
		if self.__current_status == "turn_left":
			self.left1.set_speed((self.__right1_speed + self.__right2_speed)/4)
			self.left2.set_speed((self.__right1_speed + self.__right2_speed)/4)
		if self.__current_status == "turn_left":
			self.left1.set_speed((self.__right1_speed + self.__right2_speed)/4)
			self.left2.set_speed((self.__right1_speed + self.__right2_speed)/4)
		#print self.__current_status
		global t    #Notice: use global variable!
		t = threading.Timer(0.1, self.pid_irq)
		t.start()
	def pid(self):
		self.t = threading.Timer(0.1, self.pid_irq)
		self.t.start()