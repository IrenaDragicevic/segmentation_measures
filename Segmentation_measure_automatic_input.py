# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 21:15:59 2022

@author: Irena Dragicevic
"""
#ispis log-a
import numpy as np
filename = 'log.txt'
data = np.loadtxt(filename, delimiter=',', skiprows=1, dtype=str)
print(data)


#morat ćeš pretvoriti string u float
#želiš da ti prikaže samo broj, ne i naslov  
# initializing string   
data_list=list(data)
#print(data_list)

#ako je jedan simbol E zamijeni ga s *10**
#prvo moraš deklarirati novi string izvan for petlje jer su vrijednosti unutra privremene
new_string = ""
new_list= []
 
for value in data_list:
    for symbol in value:
        if symbol == "E":
            new_string = new_string + "*10**"
        else:
            new_string =  new_string + symbol
            
    new_string = new_string + " " #pazi na prijelom - ubacuješ unutar prve for petlje
    new_list.append(new_string)
    new_string = "" #moraš resetirati new_string na O inače će ti samo nadodavati vrijednosti

new_number = ""
new_number_list = []

for value in data_list:
    for symbol in value:
        if symbol.isdigit() or symbol == "." or symbol == "E":
            print(symbol)
            new_number = new_number + symbol
    
    new_number_list.append(new_number)
    new_number= ""
    
for number in new_number_list:
    print(float(number))
    
num1=float(new_number_list[0])
num2=float(new_number_list[1])
num3=float(new_number_list[2])
num4=float(new_number_list[3])
num5=float(new_number_list[4])

import math
num6=num1-num5
num7=num3-num4
num8=num2-num4
num9=num4/(num4+num7)
num10=num6/(num6+num7)
num11=(2*num4)/(num2+num3)

print("True positive area", num4)
print("True negative area: ", num6)
print("False positive area:", num7)
print("False negative area: ", num7)

#Sensitivity=true positives/(true positives+false negatives)
#Specificity=true negatives/(true negatives+false positives)
#DSC=2*overlap/area of ground truth mask + area of our segmentation mask

print("Sensitivity: ", num9)
print("Specificity: ", num10)
print("Dice-Sorensen Coefficient: ", num11)

