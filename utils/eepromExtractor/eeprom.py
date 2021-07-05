#!/usr/bin/python

import sys
from ehelper import *
from dformatter import *

from v9_3_10 import *

hexFile = 'eeprom.bin'

if len(sys.argv) > 1:
    hexFile = sys.argv[1]

x = Data()
f = open(hexFile, 'rb')
f.readinto(x)


checkVersion(x, CHEALI_CHARGER_EPPROM_VERSION_STRING)

def checkAllCRC():
    checkCRC(x, 'calibration')
    checkCRC(x, 'programData')
    checkCRC(x, 'settings')


print(dump(x))
# fails on programData
#checkAllCRC();
checkCRC(x, 'calibration')


#save defaultCalibration.cpp file
defaultCalibrationFile = 'defaultCalibration.cpp'

fmt = DFormatter()
f = open(defaultCalibrationFile + '.template', 'r')
template = f.read()
out = fmt.vformat(template, [],x)
f = open(defaultCalibrationFile, 'w')
f.write(out)


sys.exit()

#example

x.programData[5].name = 'zosia'
restoreCRC(x,'programData');
checkAllCRC();

f = open('output.bin', 'wb')
f.write(x);
