class RealSensor:

    def get_value(self):
        return 42


class Alarm(object):

    def __init__(self, sensor=None):
        self.sensor = sensor or RealSensor()
        self.alarmed = False

    def check_readout(self):
        current_readout = self.sensor.get_value()
        if 30 < current_readout < 50:
            self.alarmed = False
        else:
            self.alarmed = True

    @property
    def is_on(self):
        return self.alarmed
