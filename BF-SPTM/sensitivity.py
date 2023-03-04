# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 12:21:26 2021

@author: user
"""

#水位RMSE (root-mean-square error of water elevatino)
rtfile = open(r"D:\EEMS\try\#analysis\50p水位\量測水位(內插).dat",'r') # 輸入檔案(input data)
rtlines = rtfile.readlines() #找出對應行數(read data)
rtfile.close()

time,WL =[],[]
for i in range(0,84):
    str1 = rtlines[i].split()
    time.append(float(str1[0]))
    WL.append(float(str1[1]))

mean_data_water_elevation = sum(WL)/len(WL)

for i in range(1,16):
    filename =r"D:\EEMS\try\#analysis\50p水位\%d.dat" %i
    rtfile = open(filename,'r') # 輸入檔案(input data)
    rtlines = rtfile.readlines() #找出對應行數(read data)
    rtfile.close()
    
    locals()['time'+str(i)],locals()['WL'+str(i)] =[],[]
    for p in range(13,97):
        str1 = rtlines[p].split()
        locals()['time'+str(i)].append(float(str1[0]))
        locals()['WL'+str(i)].append(float(str1[1]))
    
for i in range(1,16):
    locals()['WL_RMSE'+str(i)] = []
    locals()['WL_RSQ'+str(i)] = []
    n, total_square, total_R_square=0,0,0
    while n < 84:
        total_square += (locals()['WL'+str(i)][n]-WL[n])**2
        total_R_square += (WL[n]-mean_data_water_elevation)**2  
        n+=1
    locals()['WL_RMSE'+str(i)]= (total_square/len(WL))**0.5
    locals()['WL_RSQ'+str(i)]= 1-total_square/total_R_square


#泥沙濃度RMSE
rtfile = open(r"D:\EEMS\try\#analysis\50p濃度\濃度(內插).dat",'r') # 輸入檔案(input data)
rtlines = rtfile.readlines() #找出對應行數(read data)
rtfile.close()

time,SED =[],[]
for i in range(0,74):
    str1 = rtlines[i].split()
    time.append(float(str1[0]))
    SED.append(float(str1[1]))

mean_data_SED = sum(SED)/len(SED)

for i in range(1,16):
    filename =r"D:\EEMS\try\#analysis\50p濃度\%d (Elev. 195.5 m).dat" %i
    rtfile = open(filename,'r') # 輸入檔案(input data)
    rtlines = rtfile.readlines() #找出對應行數(read data)
    rtfile.close()
    
    locals()['time'+str(i)],locals()['SED'+str(i)] =[],[]
    for p in range(13,97):
        str1 = rtlines[p].split()
        locals()['time'+str(i)].append(float(str1[0]))
        locals()['SED'+str(i)].append(float(str1[1]))
    
for i in range(1,16):
    locals()['SED_RMSE'+str(i)] = []
    locals()['SED_RSQ'+str(i)] = []
    n, total_square,total_R_square=0,0,0
    while n < 74:
        total_square += (locals()['SED'+str(i)][n]-SED[n])**2
        total_R_square += (SED[n]-mean_data_SED)**2
        n+=1
    locals()['SED_RMSE'+str(i)]= (total_square/len(SED))**0.5
    locals()['SED_RSQ'+str(i)]= 1-total_square/total_R_square









