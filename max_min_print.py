# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 17:46:51 2019

@author: Odeniran Qozeem
"""

largest = 0
smallest = 0

while True:
    inp = input('Enter a number:')
    if inp =='done': break
    
    try:
        num = float(inp)
    except:
        print('Invalid input')
        continue
    
    if smallest is None:
        smallest = num
        
    if num > largest:
        largest = num
        
    elif num < smallest:
        smallest = num
        
def done(largest, smallest):
    print('Maximum is',int(largest))
    print('Minimum is',int(smallest))
    
done(largest, smallest)
