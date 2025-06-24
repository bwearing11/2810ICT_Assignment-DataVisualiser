# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 22:15:46 2021

@author: Camilo
"""

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg as NavigationToolbar
from matplotlib.figure import Figure
import wx
import wx.adv
import wx.grid
import wx
import openpyxl
import numpy as np
from camilofunctions import functions




class MyNavigationToolbar(NavigationToolbar):
    """Extend the default wx toolbar with your own event handlers."""

    def __init__(self, canvas, cankill):
        NavigationToolbar.__init__(self, canvas)

class Frame(wx.Frame):
    options = {
                0 : functions().offenceCamera,
                1 : functions().offenceLicenseType,
            }
    sampleList = [
            'Offence by Camera',
            'offenceLicenseType',
            '3'
        ]
    def OnClickedTable(self,event):
        self.data = functions().orderDataByDate(self.sheet,self.ddStartDate.GetValue(),self.ddEndDate.GetValue())
        self.data = self.options[self.list.GetSelection()](self.data)
        self.showTable()
        
    def OnClickedGraph(self,event):
        self.data = functions().orderDataByDate(self.sheet,self.ddStartDate.GetValue(),self.ddEndDate.GetValue())
        self.data = self.options[self.list.GetSelection()](self.data)
        self.data = functions().offencesByDate(self.data)
        self.showGraph()
        
    def OnClicked(self,event):
        self.data = self.options[self.list.GetSelection()](self.sheet,self.ddStartDate.GetValue(),self.ddEndDate.GetValue())
        self.showTable()
        
    def showGraph(self):
        self.panel1_1 = wx.Panel(parent=self.panel,pos=(20, 200), size=(900, 450))
        if (self.grid and self.grid.GetNumberCols() > 0 ):
            self.grid.Destroy()
        if(len(self.data) > 0 ):
            self.figure = Figure(figsize=(5, 4), dpi=100)
            self.axes = self.figure.add_subplot(111)
            x = list(self.data.keys())
            y = list(self.data.values())
            self.axes.plot(x, y)
    
            self.canvas = FigureCanvas(self.panel1_1, 20, self.figure)
    
    
            self.sizer = wx.BoxSizer(wx.VERTICAL)
            self.sizer.Add(self.canvas, 1, wx.TOP | wx.LEFT | wx.EXPAND)
    
            self.toolbar = MyNavigationToolbar(self.canvas, True)
            self.toolbar.Realize()
            # By adding toolbar in sizer, we are able to put it at the bottom
            # of the frame - so appearance is closer to GTK version.
            self.sizer.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)
    
            # update the axes menu on the toolbar
            self.toolbar.update()
            self.SetSizer(self.sizer)
        
    def showTable(self):
        if (hasattr(self.panel1_1, 'Destroy')):
            self.panel1_1.Destroy()
            self.panel1_1 = {}
        if (self.grid and self.grid.GetNumberCols() > 0 ):
            self.grid.Destroy()
        self.grid = wx.grid.Grid(self.panel, -1, pos=(20, 200), size=(900, 450))
        self.grid.CreateGrid(len(self.data)+1, 10)
        self.grid.SetRowLabelSize(0)
        self.grid.SetColLabelSize(0)
        self.grid.SetCellValue(0, 0,'OFFENCE_FINYEA')
        self.grid.SetCellValue(0, 1,'OFFENCE_MONTH')
        self.grid.SetCellValue(0, 2,'OFFENCE_CODE')
        self.grid.SetCellValue(0, 3,'OFFENCE_DESC')
        self.grid.SetCellValue(0, 4,'LEGISLATION')
        self.grid.SetCellValue(0, 5,'SECTION_CLAUSE')
        self.grid.SetCellValue(0, 6,'FACE_VALUE')
        self.grid.SetCellValue(0, 7,'CAMERA_IND')
        self.grid.SetCellValue(0, 8,'CAMERA_TYPE')
        self.grid.SetCellValue(0, 9,'LOCATION_CODE')

        for idx, row in enumerate(self.data):
            pos = idx + 1
            getValue = lambda x : str(x) if x else ''            
            self.grid.SetCellValue(pos, 0, getValue(row[0].value))
            self.grid.SetReadOnly(pos, 0)
            self.grid.SetCellValue(pos, 1, getValue(row[1].value))
            self.grid.SetReadOnly(pos, 1)
            self.grid.SetCellValue(pos, 2, getValue(row[2].value))
            self.grid.SetReadOnly(pos, 2)
            self.grid.SetCellValue(pos, 3, getValue(row[3].value))
            self.grid.SetReadOnly(pos, 3)
            self.grid.SetCellValue(pos, 4, getValue(row[4].value))
            self.grid.SetReadOnly(pos, 4)
            self.grid.SetCellValue(pos, 5, getValue(row[5].value))
            self.grid.SetReadOnly(pos, 5)
            self.grid.SetCellValue(pos, 6, getValue(row[6].value))
            self.grid.SetReadOnly(pos, 6)
            self.grid.SetCellValue(pos, 7, getValue(row[7].value))
            self.grid.SetReadOnly(pos, 7)
            self.grid.SetCellValue(pos, 8, getValue(row[8].value))
            self.grid.SetReadOnly(pos, 8)
            self.grid.SetCellValue(pos, 9, getValue(row[9].value))
            self.grid.SetReadOnly(pos, 9)
        self.grid.AutoSizeColumns()
        
    def __init__(self):
        wb = openpyxl.load_workbook('C:/Users/benja/OneDrive/Desktop/2810AssignmentP2/penalty_data_set_2.xlsx')
        self.sheet = wb.active
        self.sheet = functions().removeFrist(self.sheet)
        wx.Frame.__init__(self, None, -1, 'App', size=(1000, 700))
        self.panel = wx.Panel(self, -1)
                
        wx.StaticText(self.panel, -1, "Start Date:", (20, 20))
        self.ddStartDate = wx.adv.DatePickerCtrl(self.panel, -1 , style=wx.adv.DP_DROPDOWN, pos=(20, 40))
        wx.StaticText(self.panel, -1, "End Date:", (150, 20))
        self.ddEndDate = wx.adv.DatePickerCtrl(self.panel, -1 , style=wx.adv.DP_DROPDOWN, pos=(150, 40))
        
        wx.StaticText(self.panel, -1, "Search:", (280, 20))
        wx.TextCtrl(self.panel, 5 , style=wx.TE_PROCESS_ENTER, pos=(280, 42), size=(300, -1))
        
        
        
        wx.StaticText(self.panel, -1, "Type of Report:", (20, 80))
        self.list = wx.Choice(self.panel, -1, (20, 100), choices=self.sampleList)
        
        self.btnTable = wx.Button(self.panel, 1 , label='Generate Table', pos=(20, 140))        
        self.btnGraph =  wx.Button(self.panel, 2 , label='Generate Graph', pos=(150, 140))
        wx.Button(self.panel, 3 , label='Generate Chart', pos=(280, 140))
        wx.Button(self.panel, 4 , label='Generate Trend', pos=(410, 140))
        self.btnTable.Bind(wx.EVT_BUTTON, self.OnClickedTable) 
        self.btnGraph.Bind(wx.EVT_BUTTON, self.OnClickedGraph)
        
        #grid
        self.grid = {}
        self.panel1_1 = {}
        
        
        
        
        
        
        
app = wx.App()
Frame().Show()
app.MainLoop()