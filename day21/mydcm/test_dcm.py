# -*- coding:utf-8 -*-
# Author: Evan Mi
import pydicom
mydcm = pydicom.dcmread("e:/000000.dcm")
print(mydcm.PatientID)
