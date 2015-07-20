__author__ = 'Pillar'
import mraa
import threading
import sys
import  time
from motor import motor as M
class Counter:
  count = 0
  direct = 2

a = Counter()
b = Counter()
c = Counter()
d = Counter()
speed_a = 0
speed_b = 0
speed_c = 0
speed_d = 0


def sig1_a_irq(args):
	a.count += 1
	a.direct += 1
	#print "sig1_a_irq"
def sig2_a_irq(args):
	a.direct -= 1
	#print "sig2_a_irq"

def sig1_b_irq(args):
	b.count += 1
	b.direct += 1
	#print "sig1_b_irq"
def sig2_b_irq(args):
	b.direct -= 1
	#print "sig2_b_irq"

def sig1_c_irq(args):
	c.count += 1
	#c.direct += 1
	#print "sig1_c_irq"
def sig2_c_irq(args):
	c.direct -= 1
	#print "sig2_c_irq"

def sig1_d_irq(args):
	d.count += 1
	d.direct += 1
	#print "sig1_d_irq"
def sig2_d_irq(args):
	d.direct -= 1
	#print "sig2_d_irq"


def get_speed_a():
	return  speed_a

def get_speed_b():
	return  speed_b
def get_speed_c():
	return  speed_c
def get_speed_d():
	return  speed_d

def time_irq():
	global speed_a
	speed_a = a.count
	global speed_b
	speed_b = b.count
	global speed_c
	speed_c = c.count
	global speed_d
	speed_d = d.count

	a.count = 0
	b.count = 0
	c.count = 0
	d.count = 0
	#print "time........"
	global t    #Notice: use global variable!
	t = threading.Timer(0.1, time_irq)
	t.start()

def interrupt_init():
	global  sig1_a
	sig1_a = mraa.Gpio(23)
	sig1_a.dir(mraa.DIR_IN)
	global sig2_a
	sig2_a = mraa.Gpio(52)
	sig2_a.dir(mraa.DIR_IN)

	global sig1_b
	sig1_b = mraa.Gpio(51)
	sig1_b.dir(mraa.DIR_IN)
	global sig2_b
	sig2_b = mraa.Gpio(37)
	sig2_b.dir(mraa.DIR_IN)

	global sig1_c
	sig1_c = mraa.Gpio(48)
	sig1_c.dir(mraa.DIR_IN)
	global sig2_c
	sig2_c = mraa.Gpio(47)
	sig2_c.dir(mraa.DIR_IN)

	global sig1_d
	sig1_d = mraa.Gpio(36)
	sig1_d.dir(mraa.DIR_IN)
	global sig2_d
	sig2_d = mraa.Gpio(49)
	sig2_d.dir(mraa.DIR_IN)

	sig1_a.isr(mraa.EDGE_RISING,sig1_a_irq , sig1_a_irq)
	sig2_a.isr(mraa.EDGE_RISING,sig2_a_irq , sig2_a_irq)

	sig1_b.isr(mraa.EDGE_RISING,sig1_b_irq , sig1_b_irq)
	sig2_b.isr(mraa.EDGE_RISING,sig2_b_irq , sig2_b_irq)

	sig1_c.isr(mraa.EDGE_RISING,sig1_c_irq , sig1_c_irq)
	sig2_c.isr(mraa.EDGE_RISING,sig2_c_irq , sig2_c_irq)

	sig1_d.isr(mraa.EDGE_RISING,sig1_d_irq , sig1_d_irq)
	sig2_d.isr(mraa.EDGE_RISING,sig2_d_irq , sig2_d_irq)

	t = threading.Timer(0.1, time_irq)
	t.start()

if __name__ == "__main__":
	# left1 = M(55,41,54,21)
	# left1.clockwise()
	# left1.set_speed(0.5)
	left1 = M(55,41,54,21)
	left2 = M(32,46,53,20)
	right1 = M(13,40,25,0)
	right2 = M(31,15,45,14)
	left1.set_speed(.5)
	left2.set_speed(0.5)
	right1.set_speed(0.5)
	right2.set_speed(0.5)
	left1.stop()
	left2.clockwise()
	right1.stop()
	right2.stop()
	interrupt_init()
	print ".........."

	while True:

		print "a>"+str(get_speed_a())
		print "c>"+str(get_speed_c())
		# print "b>"+str(get_speed_b())
		# print "c>"+str(get_speed_c())
		# print "d>"+str(get_speed_d())
		#time.sleep(1)