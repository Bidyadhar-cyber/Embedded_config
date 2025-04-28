import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

gpio_output_low = GPIO.HIGH
gpio_output_high = GPIO.LOW

class OutputSetup:
    """ GPIO Output Setup """
    def __init__(self, pin_number):
        """ Class Initialize with Pin number """
        self.pin_number = pin_number
        GPIO.setup(self.pin_number, GPIO.OUT)
        GPIO.output(self.pin_number, gpio_output_low)

    def turn_on(self):
        """ Set GPIO output as HIGH """
        GPIO.output(self.pin_number, gpio_output_high)
        return True

    def turn_off(self):
        """ Set GPIO output as LOW """
        GPIO.output(self.pin_number, gpio_output_low)
