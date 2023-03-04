# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 13:54:52 2021

@author: Liu, Wen-Jia
"""
from IPython import get_ipython
get_ipython().magic('reset -sf')

import time
start_time = time.time()
#開啟EFDC
import subprocess
process = subprocess.Popen("C:\Program Files\DSI\EEMS10.3\EFDC_Explorer.exe")
time.sleep(15)

#隨機編碼
#計算需要多少字串 (精度0.001 for AHO)，數值範圍設定在0~10區間
ub_AHO =15; lb_AHO =5; precision_AHO=0.01;
for n1 in range(100):
    value = 2**n1
    if value >= (ub_AHO-lb_AHO)/precision_AHO:
        break
    else:
        continue
#計算需要多少字串 (精度0.001 for AHD)，數值範圍設定在0~0.5區間
ub_AHD =0.15;lb_AHD =0.05; precision_AHD=0.001;
for n2 in range(100):
    value = 2**n2
    if value >= (ub_AHD-lb_AHD)/precision_AHD:
        break
    else:
        continue
#計算需要多少字串 (精度0.001 for roughness)，數值範圍設定在0.02~0.04區間
ub_roughness =0.04;lb_roughness =0.01; precision_roughness=0.001;
for n3 in range(100):
    value = 2**n3
    if value >= (ub_roughness-lb_roughness)/precision_roughness:
        break
    else:
        continue
#計算需要多少字串 (精度0.001 for settling velocity)，數值範圍設定在0~0.04區間
ub_settling_velocity =0.0001;lb_settling_velocity =0.00001; precision_settling_velocity=0.00001;
for n4 in range(100):
    value = 2**n4
    if value >= (ub_settling_velocity-lb_settling_velocity)/precision_settling_velocity:
        break
    else:
        continue    
#計算需要多少字串 (精度0.001 for TAUD & TAUR)，數值範圍設定在0~0.04區間
ub_TAUDR =0.0001;lb_TAUDR =0.00001; precision_TAUDR=0.00001;
for n5 in range(100):
    value = 2**n5
    if value >= (ub_TAUDR-lb_TAUDR)/precision_TAUDR:
        break
    else:
        continue    
      
print(n1,n2,n3,n4,n5)
#染色體長度為每種基因長度加總
length = n1+n2+n3+n4+n5
#產生出初代染色體 Population設定為100
import random as rad
iteration_times =10
iteration = 0
restart =1
RMS_residual,AHO_residual,AHD_residual,Roughness_residual,settling_velocity_residual,TAUD_residual,TAUR_residual=[],[],[],[],[],[],[]
while iteration < iteration_times:
    #重新開啟EFDC
    if iteration == 12 and 24 and 36:
        process.kill()
        time.sleep(15)
        process = subprocess.Popen("C:\Program Files\DSI\EEMS10.3\EFDC_Explorer.exe")
        time.sleep(15)
        
    AHO, AHD, Roughness, set_velocity, TAUD, TAUR= [],[],[],[],[],[]
    fit_fun,RMS = [],[]
    print('第'+str(iteration)+'代')
    generation = 20
    best_gen = 10    
    if iteration == 0:
        gen = range(generation)
        name = 'chro' #初代染色體
        for population in range(generation):
            chro =[]
            for i in range(length): 
                chro.append(rad.randint(0,1))
                locals()[name + str(population)]= chro
    else:
        gen = range(best_gen,generation)
        name = 'offspring_last' #後續迭代的染色體
        for population in range(generation):
            locals()[name + str(population)] = locals()['offspring'+str(population)]
            
    for population in gen:
        #轉換染色體變為實際值帶入EFDC檔案
        #擷取各基因的編碼
        x = locals()[ name +str(population)][:n1]; y=locals()[ name +str(population)][n1:n1+n2]; z=locals()[ name +str(population)][n1+n2:n1+n2+n3]; 
        sett=locals()[ name +str(population)][n1+n2+n3:n1+n2+n3+n4]; tdr=locals()[ name +str(population)][n1+n2+n3+n4:];
        #先轉換為十進位制再計算實數值(for AHO)
        order = range(n1-1,-1,-1); num=[];
        for i in range(n1):
            num.append(x[i]*2**order[i])
        decimal = sum(num)
        #內差法回推實際值
        rv_AHO = round(lb_AHO + decimal*(ub_AHO-lb_AHO)/(2**n1-1),3)
        #先轉換為十進位制再計算實數值(for AHD)
        order = range(n2-1,-1,-1); num=[];
        for i in range(n2):
            num.append(y[i]*2**order[i])
        decimal2 = sum(num) 
        #內差法回推實際值
        rv_AHD = round(lb_AHD + decimal2*(ub_AHD-lb_AHD)/(2**n2-1),4)
        #先轉換為十進位制再計算實數值(for roughness)
        order = range(n3-1,-1,-1); num=[];
        for i in range(n3):
            num.append(z[i]*2**order[i])
        decimal3 = sum(num)
        #內差法回推實際值
        rv_roughness = round(lb_roughness + decimal3*(ub_roughness-lb_roughness)/(2**n3-1),4)
        #先轉換為十進位制再計算實數值(for settling velocity)
        order = range(n4-1,-1,-1); num=[];
        for i in range(n4):
            num.append(sett[i]*2**order[i])
        decimal4 = sum(num)
        #內差法回推實際值
        rv_settling_velocity = round(lb_settling_velocity + decimal4*(ub_settling_velocity-lb_settling_velocity)/(2**n4-1),5)
        #先轉換為十進位制再計算實數值(for TAUDR)
        order = range(n5-1,-1,-1); num=[];
        for i in range(n5):
            num.append(tdr[i]*2**order[i])
        decimal5 = sum(num)
        #內差法回推實際值
        rv_TAUDR = round(lb_TAUDR + decimal5*(ub_TAUDR-lb_TAUDR)/(2**n5-1),5)
        
        
        if iteration == 0:
            AHO.append(rv_AHO)
            AHD.append(rv_AHD)
            Roughness.append(rv_roughness)
            set_velocity.append(rv_settling_velocity)
            TAUD.append(rv_TAUDR)
            TAUR.append(rv_TAUDR)
        else:
            AHO = AHO_residual
            AHD = AHD_residual
            Roughness = Roughness_residual
            set_velocity = settling_velocity_residual
            TAUD = TAUD_residual
            TAUR = TAUR_residual
            AHO.append(rv_AHO)
            AHD.append(rv_AHD)
            Roughness.append(rv_roughness)
            set_velocity.append(rv_settling_velocity)
            TAUD.append(rv_TAUDR)
            TAUR.append(rv_TAUDR)            
            
        #帶入EFDC檔案進行模擬,Turbulence parameter修改        
        inputfile = open('efdc.inp','r') # 輸入檔案
        lines = inputfile.readlines() #找出對應行數
        inputfile.close()
        
        locals()['parameter'+str(population)] ="          "+str(AHO[population])+"      "+str(AHD[population])+"  1E-05     1E-06        1              1             0.0001         1    2E-06\n"
        
        str1 = "".join(lines[336])
        originstr = str1                         #原文字
        newstr =locals()['parameter'+str(population)]     #替代文字  
        strindex =lines.index(originstr)
        lines[strindex] = newstr
        newfile=open('efdc.inp','w')       
            
        for newline in lines:
            newfile.write(newline)
        newfile.close()

        #settling velocity & TAUD & TAUR 修改
        
        locals()['set_velocity'+str(population)]="500   10000 3.77358E-07    2.65   "+str(set_velocity[population])+"       0       0   "+str(TAUD[population])+"       0       0\n"

        str2 ="".join(lines[1027])
        originstr = str2                         #原文字
        newstr =locals()['set_velocity'+str(population)]     #替代文字  
        strindex =lines.index(originstr)
        lines[strindex] = newstr
        newfile=open('efdc.inp','w')       
            
        for newline in lines:
            newfile.write(newline)
        newfile.close()

        locals()['taudr'+str(population)]="    0       0  0.0005   "+str(TAUR[population])+"       0       1       0       0\n"

        str3 ="".join(lines[1058])
        originstr = str3                         #原文字
        newstr =locals()['taudr'+str(population)]     #替代文字  
        strindex =lines.index(originstr)
        lines[strindex] = newstr
        newfile=open('efdc.inp','w')       
            
        for newline in lines:
            newfile.write(newline)
        newfile.close()

        #Roughness更改數值
        import os
        fname = "dxdy.inp"
        path =r"D:\EEMS\official model"
        new_fname ='dxdy.txt'
        os.rename(os.path.join(path, fname),os.path.join(path, new_fname))
        
        #取出Roughness值
        rtfile = open(r"D:\EEMS\official model\dxdy.txt",'r') # 輸入檔案
        rtlines = rtfile.readlines() #找出對應行數
        rtfile.close()
        
        xr= Roughness[population]
                
        for line2 in range(4,5910):
            rou=rtlines[line2]
            rouv = rou.split()
            rouv[6]= str(xr)+'\n'
            rtlines[line2] = " "+" ".join(str(i) for i in rouv)
        
        newfile=open('dxdy.txt','w')
        for newline in rtlines[0:5910]:        
            newfile.write(newline)
        newfile.close()    
            
        fname = "dxdy.txt"
        path =r"D:\EEMS\official model"
        new_fname ='dxdy.inp'
        os.rename(os.path.join(path, fname),os.path.join(path, new_fname))

#EFDC自動化機制
    # 輸入EFDC模擬水位(自動化)    
        import pyautogui
        pyautogui.PAUSE = 3
        time.sleep(5)
        pyautogui.click(51,56, button='left', duration=1)
        time.sleep(1)
        pyautogui.click(571,360, button='left', duration=1)
        time.sleep(1)
        pyautogui.click(1051,720, button='left', duration=1)
        time.sleep(1)
        pyautogui.click(103,59, button='left', duration=1)
        time.sleep(1)
        pyautogui.click(584,513, button='left', duration=1)
        time.sleep(1)
        pyautogui.click(671,600, button='left', duration=1)
        time.sleep(5400)     #EFDC模擬時間
        
        import win32api
        import win32con
        win32api.keybd_event(13,0,0,0)
        win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)
        win32api.keybd_event(13,0,0,0)
        win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)
        time.sleep(1)
               
        pyautogui.click(19,87, button='left', duration=1) #刷新output
        time.sleep(3)
        pyautogui.click(164,59, button='left', duration=1) #開啟2DH
        time.sleep(1)
        pyautogui.click(118,406, button='left', duration=1) #選擇輸出網格位置
        time.sleep(1) 
        pyautogui.click(319,36, button='left', duration=1) #time series
        time.sleep(1) 
        pyautogui.click(333,57, button='left', duration=1) #new time series
        time.sleep(1)
        pyautogui.click(643,507, button='left', duration=1) #去除bottom elevation
        time.sleep(1)
        pyautogui.click(776,561, button='left', duration=1) #delet current parameter
        time.sleep(1)
        pyautogui.click(1021,594, button='left', duration=1) #選擇water level
        time.sleep(1)
        pyautogui.click(1010,618, button='left', duration=1) 
        time.sleep(1)
        pyautogui.click(962,617, button='left', duration=1) #選擇water elevation
        time.sleep(1)
        pyautogui.click(1027,702, button='left', duration=1) 
        time.sleep(1)
        pyautogui.click(782,526, button='left', duration=1) # add parameter to plot
        time.sleep(1)
        pyautogui.click(985,701, button='left', duration=1) # press ok
        time.sleep(1)
        pyautogui.click(319,36, button='left', duration=1) #time series
        time.sleep(1) 
        pyautogui.click(388,366, button='left', duration=1) #export data series
        time.sleep(1) 
        pyautogui.click(1008,618, button='left', duration=1) #press ok to save file
        time.sleep(1) 
        pyautogui.click(1662,89, button='left', duration=1) #close the active the model
        time.sleep(1) 
        pyautogui.click(850,586, button='left', duration=1) #press sure
        time.sleep(1)
    
        #更改水位檔名    
        fname = "TS_Water Elevation.dat"
        path =r"D:\EEMS\try\#analysis"
        new_fname =str(iteration)+str(population)+'.txt'
        os.rename(os.path.join(path, fname),os.path.join(path, new_fname))
    
        #取出水位值
        wtfile = open(r"D:\EEMS\try\#analysis"+'/'+str(iteration)+ str(population) +".txt",'r') # 輸入檔案
        wtlines = wtfile.readlines() #找出對應行數
        wtfile.close()
        
        rwtfile = open(r"D:\EEMS\try\#analysis\量測水位(內插).dat",'r') # 輸入檔案
        rwtlines = rwtfile.readlines() #找出對應行數
        rwtfile.close()
        simulation_w=[]
        import numpy as np
        for line in range(13,len(wtlines)):
            s=wtlines[line]
            sv = np.round(list(map(float,s.split())),4)
            simulation_w.append(sv[1])
        while len(simulation_w)<84:
            simulation_w.append(0)
            
        #計算RMS
        rwl_value, bias =[],[]
        for i in range(84):
            rwl = rwtlines[i].split()[1]
            rwl_value.append(float(rwl))
            bias.append((rwl_value[i]-simulation_w[i])**2)
             
        #適應函數與目標函數
        if iteration==0:
            RMS.append(np.sqrt(sum(bias)/len(rwl_value)))
            fit_fun = RMS
        else:
            RMS.append(np.sqrt(sum(bias)/len(rwl_value)))
            fit_fun = RMS_residual + RMS
            
    # 停止條件 (如果第8代的平均適應值與第10代的平均適應值相差0.05就停止)
    if iteration== 7:
        fit_8 = fit_fun
        mean_1 = sum(fit_fun)/len(fit_fun)
    elif iteration== 9:
        fit_10 = fit_fun
        mean_2 = sum(fit_fun)/len(fit_fun)
        import sys
        if abs(mean_1-mean_2) <= 0.05:
            print(mean_1, mean_2)
            print(abs(mean_1-mean_2))
            print('達到收斂條件')
            print("結束執行Genetic algorithm")
            end_time = time.time()
            print(str(end_time-start_time))
            sys.exit()            
        else:
            iteration+=1
            restart +=1
            print(abs(mean_1-mean_2))
            print('無達到收斂條件，增加迭代次數繼續運行')
            break
    else:
        pass    
        
    #利用rank讓fitness高的基因在輪盤上的機率也是高的
    import numpy as np
    import pandas as pd
    RMS_residual, AHO_residual, AHD_residual, Roughness_residual, settling_velocity_residual, TAUD_residual, TAUR_residual=[],[],[],[],[],[],[]
    fit_percentage = []
    fit = -1*pd.Series(fit_fun)
    fit_rk = fit.rank(False,'max')
    fit_percentage =[0]+[round(fit_rk[i]/sum(fit_rk),5) for i in range(population)]    
    #產生母體選擇適應函數前高的10組，剩下的利用輪盤法選擇
    import heapq
    result = list(map(list(fit_rk).index, heapq.nlargest(best_gen, list(fit_rk))))
    rk = 0
    while rk < best_gen:
        locals()['parrent'+str(rk)]=locals()[name +str(result[rk])]
        #留下前幾組較好的RMS值
        RMS_residual.append(fit_fun[result[rk]])
        AHO_residual.append(AHO[result[rk]])
        AHD_residual.append(AHD[result[rk]])
        Roughness_residual.append(Roughness[result[rk]])
        settling_velocity_residual.append(set_velocity[result[rk]])
        TAUD_residual.append(TAUD[result[rk]])
        TAUR_residual.append(TAUR[result[rk]])
        rk+=1
    #(輪盤法)計算累積機率，外加產生0~1的隨機亂數看落在哪個累積機率區間，進而選擇染色體型式產生子代
    probability_accum = np.cumsum(fit_percentage)
    for i in range(best_gen,generation):
        dice = round(rad.random(),4)
        n=0
        while n < generation:
            if dice <= probability_accum[n+1] and  dice > probability_accum[n]:
                locals()['parrent'+str(i)]=locals()[ name +str(n)]
                break
            elif dice > probability_accum[n+1]:
                locals()['parrent'+str(i)]=locals()[ name +str(n+1)]
                break
            else:
                n+= 1
                continue
    
    # croverover
    prabability_crossover = 0.9
    Probability_mutation = 0.01
    start = 0
    while start < population:
        dice = round(rad.random(),4)
        choice1, choice2,interval1, interval2 = rad.randint(0,population), rad.randint(0,population),rad.randint(1,length-1), rad.randint(1,length-1)
        if dice <= prabability_crossover:
            x1 = locals()['parrent'+str(choice1)][0:min(interval1,interval2)]
            x2 = locals()['parrent'+str(choice1)][min(interval1,interval2):max(interval1,interval2)]
            x3 = locals()['parrent'+str(choice1)][max(interval1,interval2):]
            y1 = locals()['parrent'+str(choice2)][0:min(interval1,interval2)]
            y2 = locals()['parrent'+str(choice2)][min(interval1,interval2):max(interval1,interval2)]
            y3 = locals()['parrent'+str(choice2)][max(interval1,interval2):]
            locals()['offspring'+str(start)] = x1 + y2 + x3
            locals()['offspring'+str(start+1)] = y1 + x2 + y3 
        else:
            locals()['offspring'+str(start)] = locals()['parrent'+str(choice1)]
            locals()['offspring'+str(start+1)] = locals()['parrent'+str(choice2)]
        start+=2
    
    # mutation
    start = 0
    while start < population:
        interval_all = 0
        while interval_all < length:
            dice = round(rad.random(),4)
            if dice <= Probability_mutation:
                if locals()['offspring'+str(start)][interval_all] == 0:
                    locals()['offspring'+str(start)][interval_all] = 1
                else:
                    locals()['offspring'+str(start)][interval_all] = 0
            else:
                pass
            interval_all+=1
        start+=1     
    iteration+=1




save =[AHO,AHD,Roughness,fit_fun]

import csv
path ="save.csv"
with open(path,'w') as f:
    csv_write =csv.writer(f)
    csv_head = [AHO,AHD,Roughness,fit_fun]
    csv_write.writerow(csv_head)

















