# -- coding: utf-8 --
"""
Created on Fri Oct  1 20:28:26 2021

@author: Camilo
"""
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
import matplotlib.pyplot as plt 
import numpy as np
import openpyxl
#import libraries
wb = openpyxl.load_workbook('ClimateData.xlsx')
sheet = wb.active
years = []
avgytemp_sydney = {}
avgytemp_london = {}
avgytemp_new_york = {}
avgytemp_jakarta = {}
tem_temperat = {}
#set variables
def appendData(arr, key, value):      
    if key in arr:
        arr[key].append(value)
    else:
        arr[key] = [value]    
    return arr
#arranging data into an array 
def arrayAvg(yearsArr,obj):
    arr = []   
    for year in yearsArr:
        arr.append(sum(obj[year]) / len(obj[year]))
    return arr
# getting the average value by year       
for row_cells in sheet.iter_rows():
    if(row_cells[0].row != 1 ):
        if((row_cells[0].value.year >= 1900 and row_cells[0].value.year <= 2000)):
#filter for the range of dates 1900 and 2000
            if(row_cells[3].value == 'Sydney'):
                avgytemp_sydney = appendData(avgytemp_sydney,row_cells[0].value.year,row_cells[1].value)
            if(row_cells[3].value == 'London'):
                avgytemp_london = appendData(avgytemp_london,row_cells[0].value.year,row_cells[1].value)                
            if(row_cells[3].value == 'New York'):
                avgytemp_new_york = appendData(avgytemp_new_york,row_cells[0].value.year,row_cells[1].value)                
            if(row_cells[3].value == 'Jakarta'):
                avgytemp_jakarta = appendData(avgytemp_jakarta,row_cells[0].value.year,row_cells[1].value)                
            if(row_cells[0].value.year not in years):
                years.append(row_cells[0].value.year)
# Sorting our information by city adding the average vaue and date
#print(years)
avgytemp_sydney = arrayAvg(years,avgytemp_sydney)
avgytemp_london = arrayAvg(years,avgytemp_london)
avgytemp_new_york = arrayAvg(years,avgytemp_new_york)
avgytemp_jakarta = arrayAvg(years,avgytemp_jakarta)
#setting the properties of the graph (width, labels, title, and save image)
f = plt.figure()
f.set_figwidth(25)
plt.plot(years, avgytemp_sydney, 'b-', label='Sydney')
plt.plot(years, avgytemp_london, 'r-', label='London')
plt.plot(years, avgytemp_new_york, 'g-', label='New York')
plt.plot(years, avgytemp_jakarta, 'y-', label='Jakarta')
plt.legend(loc="upper left")
plt.xlabel('Year')
plt.ylabel('Temperature')
plt.title('Average Yearly Temperatures') 
plt.gcf().autofmt_xdate()
plt.savefig('avgyt.png', dpi=300, bbox_inches='tight')
plt.show()