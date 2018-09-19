# -*- coding: utf-8 -*-
import sys

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from pandas import *
import xlrd
import csv
import openpyxl


columns=["name","id","xx","yyy"]
tw = pd.read_excel('/Users/wenxinchen/test.xlsx','Sheet 2',skiprows=1)
df = pd.DataFrame.from_dict(file).fillna('Nan')
df.to_csv('/Users/wenxinchen/testoutput.csv',index=False,columns=columns)
