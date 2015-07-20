# Open the vi and add the unofficial repositories:
#     root@edison:~# vi /etc/opkg/base-feeds.conf
#
# paste the following:
#         src/gz all http://repo.opkg.net/edison/repo/all
#         src/gz edison http://repo.opkg.net/edison/repo/edison
#         src/gz core2-32 http://repo.opkg.net/edison/repo/core2-32
#
# close the file and update:
#     root@edison:~# opkg update
#
# install python pip
# 	root@edison:~# opkg install python-pip
#
# download setuptools
# 	root@edison:~# wget https://pypi.python.org/packages/source/s/setuptools/setuptools-18.0.1.tar.gz# #md5=cecd172c9ff7fd5f2e16b2fcc88bba51 --no-check-certificate
#
# install setuptools
# 	root@edison:~# tar xvf setuptools-18.0.1.tar.gz
# 	root@edison:~# python setuptools-18.0.1/ez_setup.py
#
# we can use pip install now,let's' install smbus
# 	root@edison:~# pip install cffi
# 	root@edison:~# pip install smbus-cffi
# root@edison:~# opkg install python-pip-dev
# root@edison:~# wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py
# root@edison:~# python ez_setup.py
__author__ = 'Pillar'
from motor import motor as M
import  time
import mraa
import signal, sys
import interrupt_dev
from car_dev import car_dev as C

import termios
import tty
import select
#from Seeed_ADS1015 import ADS1x15

# class Counter:
#   count = 0
# c = Counter()
def signal_handler(signal, frame):
        print 'You pressed Ctrl+C!'
        # print adc.getLastConversionResults()/1000.0
        # adc.stopContinuousConversion()
        sys.exit(0)
# def test(args):
# 	c.count+=1
# def sig1_a_irq(args):
# 	print "sig1_a_irq"
# def sig2_a_irq(args):
# 	print "sig2_a_irq"
# def sig1_b_irq(args):
# 	print "sig1_b_irq"
# def sig2_b_irq(args):
# 	print "sig2_b_irq"
# def sig1_c_irq(args):
# 	print "sig1_c_irq"
# def sig2_c_irq(args):
# 	print "sig2_c_irq"
# def sig1_d_irq(args):
# 	print "sig1_d_irq"
# def sig2_d_irq(args):
# 	print "sig2_d_irq"

if __name__ == "__main__":
	'left1:       left2         right1:         right2' \
	'en:55        en:13         en:32           en:31'  \
	'ina:41       ina:40        ina:46          ina:15' \
	'inb:54       inb:25        inb:53          inb:45' \
	'pwm:21       pwm:0         pwm:20          pwm:14' \
	'test_a:23    test_a:51     test_a:48       test_a:36' \
	'test_b:52    test_b:37     test_b:47       test_b:49'
	# left1 = M(55,41,54,21)
	# left2 = M(13,40,25,0)
	# right1 = M(32,46,53,20)
	# right2 = M(31,15,45,14)
	# left1.set_speed(0.5)
	# left2.set_speed(0.5)
	# right1.set_speed(0.5)
	# right2.set_speed(0.5)

	# ADS1015 = 0x00	# 12-bit ADC
	# ADS1115 = 0x01	# 16-bit ADC
	#
	# # Initialise the ADC using the default mode (use default I2C address)
	# # Set this to ADS1015 or ADS1115 depending on the ADC you are using!
	# #adc = ADS1x15(ic=ADS1015)
	#
	# # start comparator on channel 2 with a thresholdHigh=200mV and low=100mV
	# # in traditional mode, non-latching, +/-1.024V and 250sps
	# #adc.startSingleEndedComparator(2, 200, 100, pga=1024, sps=250, activeLow=True, traditionalMode=True, latching=False, numReadings=1)
	#
	# sig1_a = mraa.Gpio(23)
	# sig1_a.dir(mraa.DIR_IN)
	# sig2_a = mraa.Gpio(52)
	# sig2_a.dir(mraa.DIR_IN)
	#
	# sig1_b = mraa.Gpio(51)
	# sig1_b.dir(mraa.DIR_IN)
	# sig2_b = mraa.Gpio(37)
	# sig2_b.dir(mraa.DIR_IN)
	#
	# sig1_c = mraa.Gpio(48)
	# sig1_c.dir(mraa.DIR_IN)
	# sig2_c = mraa.Gpio(47)
	# sig2_c.dir(mraa.DIR_IN)
	#
	# sig1_d = mraa.Gpio(36)
	# sig1_d.dir(mraa.DIR_IN)
	# sig2_d = mraa.Gpio(49)
	# sig2_d.dir(mraa.DIR_IN)
	#
	# sig1_a.isr(mraa.EDGE_BOTH,sig1_a_irq , sig1_a_irq)
	# sig2_a.isr(mraa.EDGE_BOTH,sig2_a_irq , sig2_a_irq)
	# sig1_b.isr(mraa.EDGE_BOTH,sig1_b_irq , sig1_b_irq)
	# sig2_b.isr(mraa.EDGE_BOTH,sig2_b_irq , sig2_b_irq)
	#
	# sig1_c.isr(mraa.EDGE_BOTH,sig1_c_irq , sig1_c_irq)
	# sig2_c.isr(mraa.EDGE_BOTH,sig2_c_irq , sig2_c_irq)
	#
	# sig1_d.isr(mraa.EDGE_BOTH,sig1_d_irq , sig1_d_irq)
	# sig2_d.isr(mraa.EDGE_BOTH,sig2_d_irq , sig2_d_irq)
	#interrupt_dev.interrupt_init()
	car = C()
	#car.full_speed()
	old_settings = termios.tcgetattr(sys.stdin)
	tty.setcbreak(sys.stdin.fileno())
	ch = "q"
	while True:
		#ch = getch.getch()
		if select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []):
		    ch = sys.stdin.read(1)
		#print  ch
		if (ch == 'w'):
			car.forward()
		elif (ch == 'a'):
			car.turn_left()
		elif (ch == 's'):
			car.back()
		elif (ch == 'd'):
			car.turn_right()
		elif (ch == 'q'):
			car.stop()
		elif (ch == 'e'):
			ch = 'r'
			car.accelerate()
		elif (ch == 'f'):
			ch = 'r'
			car.decelerate()

		# print "a>"+str(interrupt_dev.get_speed_a())
		# print "b>"+str(interrupt_dev.get_speed_b())
		# print "c>"+str(interrupt_dev.get_speed_c())
		# print "d>"+str(interrupt_dev.get_speed_d())
		# time.sleep(1)


