import timers
from libs.smartsensors import analogSensors
from libs.smartsensors import digitalSensors

class SensorPool():
    """
    ==================
    SensorPool class
    ==================
    
    .. class:: SensorPool()
    
        This is the class for handling pool of sensors. 


    """
    def __init__(self,sensors):
        self._sensors = sensors
        self._samplingTimes = []
        self._diffTimes = []
        self._getTypes = []
        self._samplingTimer = None
        self._sensorsN = len(sensors)
        self._readIndexes = []
        self._stopSampling = False

    def _sample(self):
        for i in self._readIndexes:
            if self._getTypes[i] == "norm":
                self._sensors[i].getNormalized()
            elif self._getTypes[i] == "raw":
                self._sensors[i].getRaw()
        m = min(*self._diffTimes)
        self._readIndexes = []
        for i in range(0,self._sensorsN):
            if self._diffTimes[i] == m:
                self._readIndexes.append(i)
                self._diffTimes[i] = self._samplingTimes[i]
            else:
                self._diffTimes[i] = self._diffTimes[i]-m
        if not self._stopSampling:
            self._samplingTimer.one_shot(m,self._sample)
        else:
            self._stopSampling = False

    def startSampling(self,sampling_times,observation_windows,get_types):
        self._stopSampling = False
        self._samplingTimer = timers.timer()
        self._samplingTimes = sampling_times
        self._diffTimes = self._samplingTimes[:]
        self._getTypes = get_types
        for i in range(0,self._sensorsN):
            if observation_windows[i]:
                self._sensors[i].setSamplingTime(sampling_times[i])
                self._sensors[i].setObservationWindow(observation_windows[i])
            else:
                self._sensors[i].skipEval = True
        self._sample()

    def stopSampling(self):
        ### !
        self._samplingTimer.clear()
        self._stopSampling = True

