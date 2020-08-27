# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 05:39:18 2019

@author: Odeniran Qozeem
"""

score = input("Enter Score: ")

score = float(score)

if score >= 0.9:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("C")
elif score >= 0.6:
    print("D")
else:
    print("F")