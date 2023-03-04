# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 11:11:48 2021

@author: s2054
"""

rtfile = open(r"E:\異重流密度福祿數\Sec25.dat",'r') # 輸入檔案
rtlines = rtfile.readlines() #找出對應行數
rtfile.close()


time,froude_num =[],[]
for p in range(8,97):
    str1 = rtlines[p].split()
    time.append(float(str1[0]))
    froude_num.append(float(str1[1]))

water_depth =[]
for p in range(102,191):
   str1 = rtlines[p].split()
   water_depth.append(float(str1[1]))   

import numpy as np
den_froude25 = np.zeros(89)
for i in range(0,89):
    den_froude25[i] =froude_num[i]/1.1**0.5

rtfile = open(r"E:\異重流密度福祿數\Sec26.dat",'r') # 輸入檔案
rtlines = rtfile.readlines() #找出對應行數
rtfile.close()


time,froude_num =[],[]
for p in range(8,97):
    str1 = rtlines[p].split()
    time.append(float(str1[0]))
    froude_num.append(float(str1[1]))

water_depth =[]
for p in range(102,191):
   str1 = rtlines[p].split()
   water_depth.append(float(str1[1]))   


import numpy as np
den_froude26 = np.zeros(89)
for i in range(0,89):
    den_froude26[i] =froude_num[i]/1.1**0.5


rtfile = open(r"E:\異重流密度福祿數\Sec27.dat",'r') # 輸入檔案
rtlines = rtfile.readlines() #找出對應行數
rtfile.close()


time,froude_num =[],[]
for p in range(8,97):
    str1 = rtlines[p].split()
    time.append(float(str1[0]))
    froude_num.append(float(str1[1]))

water_depth =[]
for p in range(102,191):
   str1 = rtlines[p].split()
   water_depth.append(float(str1[1]))   


import numpy as np
den_froude27 = np.zeros(89)
for i in range(0,89):
    den_froude27[i] =froude_num[i]/1.1**0.5


rtfile = open(r"E:\異重流密度福祿數\Sec28.dat",'r') # 輸入檔案
rtlines = rtfile.readlines() #找出對應行數
rtfile.close()


time,froude_num =[],[]
for p in range(8,97):
    str1 = rtlines[p].split()
    time.append(float(str1[0]))
    froude_num.append(float(str1[1]))

water_depth =[]
for p in range(102,191):
   str1 = rtlines[p].split()
   water_depth.append(float(str1[1]))   

import numpy as np
den_froude28 = np.zeros(89)
for i in range(0,89):
    den_froude28[i] =froude_num[i]/1.1**0.5

rtfile = open(r"E:\異重流密度福祿數\Sec29.dat",'r') # 輸入檔案
rtlines = rtfile.readlines() #找出對應行數
rtfile.close()


time,froude_num =[],[]
for p in range(8,97):
    str1 = rtlines[p].split()
    time.append(float(str1[0]))
    froude_num.append(float(str1[1]))

water_depth =[]
for p in range(102,191):
   str1 = rtlines[p].split()
   water_depth.append(float(str1[1]))   

import numpy as np
den_froude29 = np.zeros(89)
for i in range(0,89):
    den_froude29[i] =froude_num[i]/1.1**0.5
    
    
#將密度福路數畫在一起    
    
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(20,15),dpi=300)
plt.xticks(fontsize=40,family='Times New Roman')
plt.yticks(fontsize=40,family='Times New Roman')
plt.grid()

plt.xlabel('time',fontsize=40,family='Times New Roman')
plt.ylabel('Densimetric Froude',fontsize=40,family='Times New Roman')        
plt.scatter(time,den_froude25,s=200,c='b',label='Sec 25')
plt.scatter(time,den_froude26,s=200,c='y',label='Sec 26')
plt.scatter(time,den_froude27,s=200,c='g',label='Sec 27')
plt.scatter(time,den_froude28,s=200,c='k',label='Sec 28')
plt.scatter(time,den_froude29,s=200,c='r',label='Sec 29')

plt.legend(loc='upper right',fontsize=40)

plt.savefig('E:\異重流密度福祿數\密度福路數.png',dpi =300)#儲存圖片
plt.show
    


    
    
    
    
    
    
    
    
    
    
    
    
    
    