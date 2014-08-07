from unittest import TestCase
from alarm import (
    Alarm,
    RealSensor
)

from mock import MagicMock, patch


class FakeSensor(object):

    def __init__(self, val=42):
        self.val = val
        self.called = 0

    def get_value(self):
        self.called += 1
        return self.val

    def set_value(self, val):
        self.val = val


class TestAlarm(TestCase):

    def setUp(self):
        self.sensor = FakeSensor()
        self.alarm = Alarm(self.sensor)

    def test_alarm_is_off_by_default(self):
        self.assertFalse(self.alarm.is_on)

    def test_alarm_is_off_for_normal_readout(self):
        self.sensor.set_value(40)
        self.alarm.check_readout()
        self.assertFalse(self.alarm.is_on)

    def test_alarm_is_on_for_high_readout(self):
        self.sensor.set_value(100)
        self.alarm.check_readout()
        self.assertTrue(self.alarm.is_on)

    def test_alarm_is_on_for_low_readout(self):
        self.sensor.set_value(5)
        self.alarm.check_readout()
        self.assertTrue(self.alarm.is_on)

    def test_alarm_sensor_get_value_is_called_only_once(self):
        self.alarm.check_readout()
        self.assertEqual(1, self.sensor.called)


class TestAlarmUsingMM(TestCase):

    def test_alarm_is_on_for_low_readout_using_MM(self):
        sensor = MagicMock(RealSensor)
        sensor.get_value.return_value = 5
        alarm = Alarm(sensor)
        alarm.check_readout()
        self.assertTrue(alarm.is_on)

    def test_alarm_is_on_for_high_readout_using_MM(self):
        with patch.object(RealSensor, "get_value", return_value=5):
            alarm = Alarm()
            alarm.check_readout()
            self.assertTrue(alarm.is_on)
