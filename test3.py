# -*- coding: utf-8 -*-
import sys

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from pandas import *
import xlrd
import csv
import openpyxl

tw = pd.read_excel('/Users/wenxinchen/test.xlsx','Sheet 2',skiprows=1)
tw.drop(tw.index[3])


tw_dict = {}

print(tw.index)
for i in tw.index:
    tw_dict[tw['id'][i]] = [tw['name'][i],tw['id'][i],tw['xx'][i],tw['yyy'][i]]
    print i


print(tw_dict)
final_dict = {'id': [], 'name': [], 'xx': [],'yyy':[]}


for i in tw_dict:
    final_dict['id'].append(tw_dict[i][0])
    final_dict['name'].append(tw_dict[i][1])
    final_dict['xx'].append(tw_dict[i][2])
    final_dict['yyy'].append(tw_dict[i][3])
               
print(final_dict)
df = pd.DataFrame.from_dict(final_dict)


# print (df)

df.to_csv('/Users/wenxinchen/testoutput.csv',index=False)
