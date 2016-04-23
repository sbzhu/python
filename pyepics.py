#!/usr/bin/python
from epics import caget , caput
MT005 = caget('MAG-HTS-CL1:MT005-TT')
print MT005 
