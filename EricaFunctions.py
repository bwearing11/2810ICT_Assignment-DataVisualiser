import csv
import matplotlib.pyplot as plt
import numpy as np


csvfile = open('penalty_data_set_2.csv', 'r', newline='') 
reader = csv.DictReader(csvfile)

class functions:
    def offenceCode(self): # seaching for code via input 
        a = input("enter code")
        result = []
        for row in reader:
            if row['OFFENCE_CODE'] == a: # loop though 
                result.append(row)
            print(result)


    def plates(self):
        p1 = []
        for row in reader:
            if "P1" in row['OFFENCE_DESC']:
                p1.append(row)
            print(p1)


    def mobile_use(self):
        mobile = [] # create list and dictorys 
        v = 0
        dic = {}
        for row in reader:
            if "mobile" in row['OFFENCE_DESC']:
                mobile.append(row)
                code = row['OFFENCE_CODE']
                if code in dic.keys():  # if code is in the lsit add a 1 to the vaule to count
                    dic[code] += 1  #
                else:
                    dic[code] = 1  
            else:
                pass
        return dic  

   
    def seach_all(self):
        code_pie = {}
        for row in reader:  # loop though rows
            all = row['OFFENCE_CODE']
            if all in code_pie.keys():  # if code is in the lsit add a 1 to the vaule to count
                code_pie[all] += 1  #
            else:
                code_pie[all] = 1  # else add it to the list with the vaule 1
        return(code_pie)




    def offence_key_word(self):
        offence = []
        b = input(str("seach"))
        for row in reader:
            if b in row['OFFENCE_DESC']:
                offence.append(row)
            return offence
        if len(offence) > 0:
             return offence # print result
        else:
            print("no resluts found")


   def pie(dic):
        n = list(dic.values())
        codes = list(dic.keys())
        plt.pie(n, labels=codes)
        plt.tight_layout()
        plt.legend(title="codes with mobile:")
        plt.show()

        
        
    def pie_code(code_pie):

        l = list(code_pie.values())
        codes = list(code_pie.keys())
        plt.pie(l, labels=codes)
        plt.tight_layout()
        plt.legend(title="codes by Freq :")
        plt.show()

#functions().offenceCode()
functions().mobile_use()
#functions().pie()
#plates()
#offence_key_word()
#pie(mobile_use())
