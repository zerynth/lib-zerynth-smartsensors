"""
.. _analogSensor

.. module: analogSensor

*********************
Analog Sensor Library
*********************

This module contains class definitions for analog sensors. AnalogSensor class is a subclass of the generic Sensor class and provides a simple way to handle sensors sensing quantities that can assume more than two different values. Every AnalogSensor instance inherits the whole set of methods from generic Sensor class.

    """

import timers 
from smartsensors import sensors
import adc

class AnalogSensor(sensors.Sensor):
    """
    ==================
    AnalogSensor class
    ==================
    
    .. class:: AnalogSensor(pin)
    
        This is the class for sensing analog quantities
    
    Pin can be both a real device pin and a tuple containing an analog sensor object
    and a string for a window parameter to read.
    Example::

        lightSensor = AnalogSensor(A4)
        sensorOnAverage = AnalogSensor((lightSensor,'currentAverage'))

    the above code instantiates a light sensor on a device pin and another sensor that takes as input the lightSensor average.
    
    """

    def __init__(self,pin):
        sensors.Sensor.__init__(self)
        if type(pin) == 0:
            pinMode(pin,INPUT_ANALOG)
            self._readFunc = analogRead
        self.pin = pin
        self.storeMinMax = True
        self.storeAverage = True
        self.storeTrend = True 
        self._resetSamplingParams()

