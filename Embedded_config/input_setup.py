import RPi.GPIO as GPIO

class InputSetup:
    """ GPIO Input Setup """
    def __init__(self, pin_number):
        """ Class Initialize with Pin number """
        self.pin_number = pin_number
        GPIO.setup(self.pin_number, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def read_sensor(self):
        """ Read Sensor Data """
        return GPIO.input(self.pin_number)
