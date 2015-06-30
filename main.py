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

__author__ = 'Pillar'
from motor import motor as M
import  time
import mraa
import signal, sys
from Seeed_ADS1015 import ADS1x15

class Counter:
  count = 0
c = Counter()
def signal_handler(signal, frame):
        print 'You pressed Ctrl+C!'
        print adc.getLastConversionResults()/1000.0
        adc.stopContinuousConversion()
        sys.exit(0)
def test(args):
	c.count+=1
def sig1_a_irq(args):
	print "sig1_a_irq"
def sig2_a_irq(args):
	print "sig2_a_irq"
def sig1_b_irq(args):
	print "sig1_b_irq"
def sig2_b_irq(args):
	print "sig2_b_irq"
def sig1_c_irq(args):
	print "sig1_c_irq"
def sig2_c_irq(args):
	print "sig2_c_irq"
def sig1_d_irq(args):
	print "sig1_d_irq"
def sig2_d_irq(args):
	print "sig2_d_irq"
if __name__ == "__main__":
	'left1:       left2         right1:         right2' \
	'en:55        en:13         en:32           en:31'  \
	'ina:41       ina:40        ina:46          ina:15' \
	'inb:54       inb:25        inb:53          inb:45' \
	'pwm:21       pwm:0         pwm:20          pwm:14'
	left1 = M(55,41,54,21)
	left2 = M(13,40,25,0)
	right1 = M(32,46,53,20)
	right2 = M(31,15,45,14)
	print "runing......."
	left1.set_speed(0.5)
	left2.set_speed(0.5)
	right1.set_speed(0.5)
	right2.set_speed(0.5)

	ADS1015 = 0x00	# 12-bit ADC
	ADS1115 = 0x01	# 16-bit ADC

	# Initialise the ADC using the default mode (use default I2C address)
	# Set this to ADS1015 or ADS1115 depending on the ADC you are using!
	adc = ADS1x15(ic=ADS1015)

	# start comparator on channel 2 with a thresholdHigh=200mV and low=100mV
	# in traditional mode, non-latching, +/-1.024V and 250sps
	#adc.startSingleEndedComparator(2, 200, 100, pga=1024, sps=250, activeLow=True, traditionalMode=True, latching=False, numReadings=1)
	left1.anticlockwise()
	left2.anticlockwise()
	right1.anticlockwise()
	right2.anticlockwise()

	#sig1_a = mraa.Gpio(39)
	#sig1_a.dir(mraa.DIR_OUT)
	sig2_a = mraa.Gpio(52)
	sig2_a.dir(mraa.DIR_IN)

	sig1_b = mraa.Gpio(51)
	sig1_b.dir(mraa.DIR_IN)
	sig2_b = mraa.Gpio(37)
	sig2_b.dir(mraa.DIR_IN)

	sig1_c = mraa.Gpio(48)
	sig1_c.dir(mraa.DIR_IN)
	sig2_c = mraa.Gpio(47)
	sig2_c.dir(mraa.DIR_IN)

	sig1_d = mraa.Gpio(36)
	sig1_d.dir(mraa.DIR_IN)
	sig2_d = mraa.Gpio(49)
	sig2_d.dir(mraa.DIR_IN)

	sig2_a.isr(mraa.EDGE_BOTH,sig2_a_irq , sig2_a_irq)
	sig1_b.isr(mraa.EDGE_BOTH,sig1_b_irq , sig1_b_irq)
	sig2_b.isr(mraa.EDGE_BOTH,sig2_b_irq , sig2_b_irq)

	sig1_c.isr(mraa.EDGE_BOTH,sig1_c_irq , sig1_c_irq)
	sig2_c.isr(mraa.EDGE_BOTH,sig2_c_irq , sig2_c_irq)

	sig1_d.isr(mraa.EDGE_BOTH,sig1_d_irq , sig1_d_irq)
	sig2_d.isr(mraa.EDGE_BOTH,sig2_d_irq , sig2_d_irq)
	while True:

		time.sleep(1)
		# print c.count
		# if c.count == 65535:
		# 	c.count = 0
		# time.sleep(2)
		# left1.stop()
		# left2.stop()
		# right1.stop()
		# right2.stop()
		# time.sleep(0.5)
		# left1.clockwise()
		# left2.clockwise()
		# right1.clockwise()
		# right2.clockwise()
		# adc1 =  adc.readADCSingleEnded(0, 4096, 475) / 1000
		#
		#
		# print "adc1>"+str(adc.readADCSingleEnded(0, 4096, 475) / 1000)
		# time.sleep(0.1)
		# print "adc2>"+str(adc.readADCSingleEnded(1, 4096, 475) / 1000)
		# time.sleep(0.1)
		# print "adc3>"+str(adc.readADCSingleEnded(2, 4096, 475) / 1000)
		# time.sleep(0.1)
		# print "adc4>"+str(adc.readADCSingleEnded(3, 4096, 475) / 1000)
		# time.sleep(0.1)
		#time.sleep(0.25)
		# left1.stop()
		# left2.stop()
		# right1.stop()
		# right2.stop()
		# time.sleep(0.5)

