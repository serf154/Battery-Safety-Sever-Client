#!/usr/bin/python3
import inspect

class Status(object):
    """docstring for Status"""
    def __init__(self):

        self.temperature_voliated_battery = [];
        self.battery_cell_voltage_voilated = [];

        self.isPcanTempWarning = False;
        self.isPcanTempDangerous = False;

        self.isPcanVoltageCellLowWarning = False;
        self.isPcanVoltageCMALowWarning = False;

        self.isPcanVoltageCellHighWarning = False;
        self.isPcanVoltageCMAHighWarning = False;

        self.isPcanVoltageCellHighDangerous = False;
        self.isPcanVoltageCMAHighDangerous = False;

        self.isPcanVoltageCellLowDangerous = False;
        self.isPcanVoltageCMALowDangerous = False;

        ## modbus status
        self.isModbusHighVoltageWarning = False;
        self.isModbusHighVoltageDagnerous = False;
        self.isModbusLowVoltageWarning = False;
        self.isModbusLowVoltageDangerous = False;

        ## device
        self.isRelayOff = False;
        self.isModbusOff = False;
        self.isPumpFanOff = True;

        ## Total Status
        self.warning = False;
        self.dangerous = False

        ## all voltage

    def InitStatus(self):
        for i in inspect.getmembers(self):
            if (not (i[0].startswith('_')) and i[0].startswith('is')):
                if not inspect.ismethod(i[1]):
                    setattr(self, i[0], False);
        self.warning = False;
        self.dangerous = False;

# --------------------------------- get function ---------------------------------------

    def getStatusDatas(self):
        # return [self.isCMAVolVio, self.isCMATempVio, self.isCellVolVio, self.isArduTempHigh, self.isArduPressViolated, self.isModbusCurrentViolated, self.isModbusVoltageViolated, self.isModbusPowerViolated, self.warning, self.dangerous]
        labelList = self.getLabels();
        dataList = [];
        for i in labelList:
            dataList.append(getattr(self, i))
        return dataList;


    def getLabels(self):
        labelList = [];
        for i in inspect.getmembers(self):
            if (not i[0].startswith('_')) and i[0].startswith('is'):
                if not inspect.ismethod(i[1]):
                    labelList.append(i[0]);
        labelList.sort();
        labelList.append("warning")
        labelList.append("dangerous")
        return labelList

# ------------------------------------------ judge function ---------------------------------------------

    def isVoltageVio(self):
        if  self.isPcanVoltageCellLowWarning or self.isPcanVoltageCellLowWarning or self.isPcanVoltageCellHighWarning or self.isPcanVoltageCMAHighWarning or self.isPcanVoltageCellHighDangerous or self.isPcanVoltageCMAHighDangerous or self.isPcanVoltageCellLowDangerous or self.isPcanVoltageCMALowDangerous:
            return True;
        if self.isModbusHighVoltageWarning or self.isModbusHighVoltageDagnerous or self.isModbusLowVoltageWarning or self.isModbusLowVoltageDangerous:
            return True;
        return False; 

    def isVoltageLowVio(self):
        if self.isPcanVoltageCellLowWarning or self.isPcanVoltageCMALowWarning or self.isPcanVoltageCellLowDangerous or self.isPcanVoltageCMALowDangerous or self.isModbusLowVoltageWarning or self.isModbusLowVoltageDangerous:
            return True;
        return False;

    def isVoltageHighVio(self):
        if self.isPcanVoltageCellHighWarning or self.isPcanVoltageCMAHighWarning or self.isPcanVoltageCellHighDangerous or self.isPcanVoltageCMAHighDangerous or self.isModbusHighVoltageWarning or self.isModbusHighVoltageDagnerous:
            return True;
        return False; 

    def istempHighVio(self):
        if(self.isPcanTempWarning or self.isPcanTempDangerous):
            return True;
        else:
            return False;

    # def judgeifStatus
    # def