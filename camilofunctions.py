# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 20:03:45 2021

@author: Camilo
"""

# First things, first. Import the wxPython package.
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
#import matplotlib as plt

class functions:
    
    def removeFrist(self, sheet):
        data = []
        for row_cells in sheet:
            if(row_cells[0].row != 1 ):
                data.append(row_cells)
        return data
    
    def orderDataByDate(self,sorted_data,range_a,range_b):
        offences = []
        for row_cells in sorted_data:
            if((row_cells[1].value >= range_a and row_cells[1].value <= range_b)):
                offences.append(row_cells)
        def orderByPos1(elem):
            if(elem[1].value):
                return elem[1].value
            else:
                return ''
        offences.sort(key=orderByPos1)
        return offences
    
    def offenceCamera(self,sorted_data):        
        offencesCamera = []
        for row_cells in sorted_data:
            if (row_cells[7].value):
                offencesCamera.append(row_cells)
                
        def orderByPos8(elem):
            if(elem[8].value):
                return elem[8].value
            else:
                return ''
        offencesCamera.sort(key=orderByPos8)        
        return offencesCamera
    
    def offenceLicenseType(self,sorted_data):
        offences = []
        for row_cells in sorted_data:
            if('P1' in row_cells[3].value or 'P2' in row_cells[3].value or ' L ' in row_cells[3].value):
                offences.append(row_cells)
        return offences
    
    def offencesByDate(self,sorted_data):
        def appendData(arr, key, value):      
            if key in arr:
                arr[key].append(value)
            else:
                arr[key] = [value]    
            return arr
        result = {}
        for row in sorted_data:
            result = appendData(result,str(row[1].value),row)
        for row in result:
            result[row] = len(result[row])
        return result
    
# remove first column


#option = input("Select an option (1,2,3): ")
#data = options[option](data)

    
    
    
    
    
    
    
