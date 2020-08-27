# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 05:32:16 2019

@author: Odeniran Qozeem
"""

hrs = input("Enter Hours:")
h = float(hrs)

rates = input("Enter Rates:")
r = float(rates)

reg_grosspay = 40 * 10.5
overtime_grosspay = ((h-40)*(r*1.5))

if h > 40:
    print('OVERTIME PAY IS',overtime_grosspay + reg_grosspay)
else:
    print(reg_grosspay)