import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

pri = 11 # G17
sec = 12 # G18

GPIO.setup([pri, sec], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# can't add separate callbacks for both rising and falling
#GPIO.add_event_detect(BTN_B, GPIO.RISING, lambda pin: GPIO.output(LED_B, False))
#GPIO.add_event_detect(BTN_B, GPIO.FALLING, lambda pin: GPIO.output(LED_B, True))

def rpm(pin):
	t1=time.time()
	if GPIO.input(pin):
		t2=time.time()
	dt=t2=t1
	rpm=60/dt
	print(rpm)		

GPIO.add_event_detect(BTN_G, GPIO.BOTH, rpm)
GPIO.add_event_detect(BTN_R, GPIO.BOTH, rpm)
