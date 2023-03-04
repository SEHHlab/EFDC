# -*- coding: utf-8 -*-
"""
Created on Sun May 16 14:30:05 2021

@author: user
"""

# 底床高程資料
rtfile = open(r"D:\BF-SPTM\Data\TS_Bottom Elevation.dat",'r') # 輸入檔案
rtlines = rtfile.readlines() #找出對應行數
rtfile.close()

time1,botel =[],[]
n=0
while n<=14:
    r =range(8+96*n,99+96*n)
    for i in r:
        str1 = rtlines[i].split()
        time1.append(str1[0])
        botel.append(str1[1])        
    n+=1

# 水位高程
rtfile = open(r"D:\BF-SPTM\Data\TS_Water Elevation.dat",'r') # 輸入檔案
rtlines = rtfile.readlines() #找出對應行數
rtfile.close()

wl=[]
n=0
while n<=14:
    r =range(8+96*n,99+96*n)
    for i in r:
        str1 = rtlines[i].split()
        wl.append(str1[1])        
    n+=1

# X方向速度(layer1)
rtfile = open(r"D:\BF-SPTM\Data\TS_X-Velocity (Layer 1).dat",'r') # 輸入檔案
rtlines = rtfile.readlines() #找出對應行數
rtfile.close()

v_x1=[]
n=0
while n<=14:
    r =range(8+96*n,99+96*n)
    for i in r:
        str1 = rtlines[i].split()
        v_x1.append(str1[1])        
    n+=1

# X方向速度(layer2)
rtfile = open(r"D:\BF-SPTM\Data\TS_X-Velocity (Layer 2).dat",'r') # 輸入檔案
rtlines = rtfile.readlines() #找出對應行數
rtfile.close()

v_x2=[]
n=0
while n<=14:
    r =range(8+96*n,99+96*n)
    for i in r:
        str1 = rtlines[i].split()
        v_x2.append(str1[1])        
    n+=1

# X方向速度(layer3)
rtfile = open(r"D:\BF-SPTM\Data\TS_X-Velocity (Layer 3).dat",'r') # 輸入檔案
rtlines = rtfile.readlines() #找出對應行數
rtfile.close()

v_x3=[]
n=0
while n<=14:
    r =range(8+96*n,99+96*n)
    for i in r:
        str1 = rtlines[i].split()
        v_x3.append(str1[1])        
    n+=1

# X方向速度(layer4)
rtfile = open(r"D:\BF-SPTM\Data\TS_X-Velocity (Layer 4).dat",'r') # 輸入檔案
rtlines = rtfile.readlines() #找出對應行數
rtfile.close()

v_x4=[]
n=0
while n<=14:
    r =range(8+96*n,99+96*n)
    for i in r:
        str1 = rtlines[i].split()
        v_x4.append(str1[1])        
    n+=1

# y方向速度(layer1)
rtfile = open(r"D:\BF-SPTM\Data\TS_Y-Velocity (Layer 1).dat",'r') # 輸入檔案
rtlines = rtfile.readlines() #找出對應行數
rtfile.close()

v_y1=[]
n=0
while n<=14:
    r =range(8+96*n,99+96*n)
    for i in r:
        str1 = rtlines[i].split()
        v_y1.append(str1[1])        
    n+=1

# y方向速度(layer2)
rtfile = open(r"D:\BF-SPTM\Data\TS_Y-Velocity (Layer 2).dat",'r') # 輸入檔案
rtlines = rtfile.readlines() #找出對應行數
rtfile.close()

v_y2=[]
n=0
while n<=14:
    r =range(8+96*n,99+96*n)
    for i in r:
        str1 = rtlines[i].split()
        v_y2.append(str1[1])        
    n+=1

# y方向速度(layer3)
rtfile = open(r"D:\BF-SPTM\Data\TS_Y-Velocity (Layer 3).dat",'r') # 輸入檔案
rtlines = rtfile.readlines() #找出對應行數
rtfile.close()

v_y3=[]
n=0
while n<=14:
    r =range(8+96*n,99+96*n)
    for i in r:
        str1 = rtlines[i].split()
        v_y3.append(str1[1])        
    n+=1
    
# y方向速度(layer4)
rtfile = open(r"D:\BF-SPTM\Data\TS_Y-Velocity (Layer 4).dat",'r') # 輸入檔案
rtlines = rtfile.readlines() #找出對應行數
rtfile.close()

v_y4=[]
n=0
while n<=14:
    r =range(8+96*n,99+96*n)
    for i in r:
        str1 = rtlines[i].split()
        v_y4.append(str1[1])        
    n+=1

# Z方向速度(layer1)
rtfile = open(r"D:\BF-SPTM\Data\TS_Z-Velocity (Layer 1).dat",'r') # 輸入檔案
rtlines = rtfile.readlines() #找出對應行數
rtfile.close()

v_z1=[]
n=0
while n<=14:
    r =range(8+96*n,99+96*n)
    for i in r:
        str1 = rtlines[i].split()
        v_z1.append(str1[1])        
    n+=1

# Z方向速度(layer2)
rtfile = open(r"D:\BF-SPTM\Data\TS_Z-Velocity (Layer 2).dat",'r') # 輸入檔案
rtlines = rtfile.readlines() #找出對應行數
rtfile.close()

v_z2=[]
n=0
while n<=14:
    r =range(8+96*n,99+96*n)
    for i in r:
        str1 = rtlines[i].split()
        v_z2.append(str1[1])        
    n+=1

# Z方向速度(layer3)
rtfile = open(r"D:\BF-SPTM\Data\TS_Z-Velocity (Layer 3).dat",'r') # 輸入檔案
rtlines = rtfile.readlines() #找出對應行數
rtfile.close()

v_z3=[]
n=0
while n<=14:
    r =range(8+96*n,99+96*n)
    for i in r:
        str1 = rtlines[i].split()
        v_z3.append(str1[1])        
    n+=1

# Z方向速度(layer4)
rtfile = open(r"D:\BF-SPTM\Data\TS_Z-Velocity (Layer 4).dat",'r') # 輸入檔案
rtlines = rtfile.readlines() #找出對應行數
rtfile.close()

v_z4=[]
n=0
while n<=14:
    r =range(8+96*n,99+96*n)
    for i in r:
        str1 = rtlines[i].split()
        v_z4.append(str1[1])        
    n+=1

#底床剪應力
rtfile = open(r"D:\BF-SPTM\Data\TS_Total Bed Shear.dat",'r') # 輸入檔案
rtlines = rtfile.readlines() #找出對應行數
rtfile.close()

shear_stress=[]
n=0
while n<=14:
    r =range(8+96*n,99+96*n)
    for i in r:
        str1 = rtlines[i].split()
        shear_stress.append(str1[1])        
    n+=1





#網格距離計算(公尺)
import numpy as np
rtfile = open(r"D:\BF-SPTM\Data\study Grid.xyz",'r') # 輸入檔案
rtlines = rtfile.readlines() #找出對應行數
rtfile.close()

distance = np.zeros(45).reshape(15,3)
for i in range(0,int(len(rtlines))):
    distance[i,0] = rtlines[i].split()[0]
    distance[i,1]= rtlines[i].split()[1]
    distance[i,2]= rtlines[i].split()[2]

#網格建置

from matplotlib import pyplot as plt
import numpy as np
x=np.zeros(5)
y=np.zeros(3)
for i in range(0,5):
    if i ==0:
        x[i] =abs(distance[0+3*i,0]-distance[0+3*i,0])
    else:
        x[i] =abs(distance[0+3*i,0]-distance[0+3*(i-1),0])+x[i-1]

for i in range(0,3):
    if i ==0:
        y[i] =abs(distance[i,1]-distance[i,1])
    else:
        y[i] =abs(distance[i,1]-distance[i-1,1])+y[i-1]
        
z = np.linspace(220,245,101)


X,Y =np.meshgrid(x,y)
Z=np.zeros([3,5])
Wl=np.zeros([3,5])

#輸入資料進入網格(Z軸)
#(底床隨時間改變)
start_final = 8
for time in range(0,1):
    for i in range(0,5):
        for n in range(0,3):            
            if x[i] == 0:
                m = n
            else:
                m =2*i+n
            Z[n,i]=X[n,i]*0+Y[n,i]*0+float(botel[start_final+96*(m)]) #底床
            Wl[n,i]=X[n,i]*0+Y[n,i]*0+float(wl[start_final+96*(m)])   #水位


    #地形圖
    fig = plt.figure(figsize=(15,10),dpi=300) 
    ax = fig.gca(projection='3d') 
    mappable=ax.plot_surface(X,Y,Z,alpha=0.8,cmap='copper') 
    ax.set_xlim3d(0,max(x)) 
    ax.set_ylim3d(max(y),0)
    ax.set_zlim3d(220, 250)
    fig.colorbar(mappable, ax=ax,fraction=0.05, pad=0.05)
    plt.title('Time='+str(time1[time+start_final]))
    #水位圖
    ax1 = fig.gca(projection='3d') 
    mappable1=ax1.plot_surface(X,Y,Wl,alpha=0.9,cmap='Blues',vmin=240,vmax=247)
    fig.colorbar(mappable1, ax=ax,fraction=0.05, pad=0.05)
    plt.title('Time='+str(time1[time+start_final]))
      
    plt.show()
                                    
    
# Backward particles tracking model

#建立流速場(x,y,z以及layer1~4)
Vx1,Vx2,Vx3,Vx4= np.zeros([3,5]),np.zeros([3,5]),np.zeros([3,5]),np.zeros([3,5])
Vy1,Vy2,Vy3,Vy4= np.zeros([3,5]),np.zeros([3,5]),np.zeros([3,5]),np.zeros([3,5])
Vz1,Vz2,Vz3,Vz4= np.zeros([3,5]),np.zeros([3,5]),np.zeros([3,5]),np.zeros([3,5])

import numpy as np                
for p in range(0,101):
    for i in range(0,5):
        for n in range(0,3):
            if x[i] == 0:
                m = n
            else:
                m =2*i+n
            if z[p]-float(botel[start_final+96*(m)])<=0.25*(float(wl[start_final+96*(m)])-float(botel[start_final+96*(m)])):
                Vx1[n,i] = float(v_x1[start_final+96*(m)])
                Vy1[n,i] = float(v_y1[start_final+96*(m)])
                Vz1[n,i] = float(v_z1[start_final+96*(m)])
            elif 0.25*(float(wl[start_final+96*(m)])-float(botel[start_final+96*(m)]))<z[p]-float(botel[start_final+96*(m)])<= 0.5*(float(wl[start_final+96*(m)])-float(botel[start_final+96*(m)])):
                Vx2[n,i] = float(v_x2[start_final+96*(m)])
                Vy2[n,i] = float(v_y2[start_final+96*(m)])
                Vz2[n,i] = float(v_z2[start_final+96*(m)])                   
            elif 0.5*(float(wl[start_final+96*(m)])-float(botel[start_final+96*(m)]))<z[p]-float(botel[start_final+96*(m)])<= 0.75*(float(wl[start_final+96*(m)])-float(botel[start_final+96*(m)])):     
                Vx3[n,i] = float(v_x3[start_final+96*(m)])
                Vy3[n,i] = float(v_y3[start_final+96*(m)])
                Vz3[n,i] = float(v_z3[start_final+96*(m)])                            
            else:
                Vx4[n,i] = float(v_x4[start_final+96*(m)])
                Vy4[n,i] = float(v_y4[start_final+96*(m)])
                Vz4[n,i] = float(v_z4[start_final+96*(m)]) 


                
settling_velocity = 0.0025
shear_velocity = 0.0086
initial_position_x = 130; initial_position_y = 10; initial_position_z = 223
horizontal_diffusivity =1
vertical_diffusivuty =0.001
dt = 60
number = 60*60/dt-1
particles = 1000
                
for iteration in range(0,particles):
    locals()['x_backnew'+str(iteration)], locals()['y_backnew'+str(iteration)], locals()['z_backnew'+str(iteration)] =np.zeros(int(number)),np.zeros(int(number)),np.zeros(int(number))
    for time in range(0,int(number)):
        Nx = np.random.normal(0, 0.1**0.5,1)
        Ny = np.random.normal(0, 0.1**0.5,1)
        Nz = np.random.normal(0, 0.1**0.5,1)
        if  time == 0:
                for q in range(0,5-1):
                    if x[q] <= initial_position_x <=x[q+1]:
                        l = q
                        break
                    else:
                        continue
                for g in range(0,3-1):       
                    if y[g] <= initial_position_y <=y[g+1]:
                        k = g
                        break
                    else:
                        continue
                if x[l] == 0:
                    m = k
                else:
                    m =3*l+k                        
                if initial_position_z-float(botel[start_final+96*(m)])<=0.25*(float(wl[start_final+96*(m)])-float(botel[start_final+96*(m)])):
    
                    locals()['x_backnew'+str(iteration)][time] = initial_position_x - Vx1[k,l]*dt - Nx[0]*horizontal_diffusivity**0.5
                    locals()['y_backnew'+str(iteration)][time] = initial_position_y - Vy1[k,l]*dt - Ny[0]*horizontal_diffusivity**0.5           
                    locals()['z_backnew'+str(iteration)][time] = initial_position_z - (Vz1[k,l]-settling_velocity)*dt - Nz[0]*vertical_diffusivuty**0.5
                                                                                        
                elif 0.25*(float(wl[start_final+96*(m)])-float(botel[start_final+96*(m)]))<initial_position_z-float(botel[start_final+96*(m)])<= 0.5*(float(wl[start_final+96*(m)])-float(botel[start_final+96*(m)])):
                    for q in range(0,5-1):
                        if x[q] <= initial_position_x <=x[q+1]:
                            l = q
                            break
                        else:
                            continue
                    for g in range(0,3-1):       
                        if y[g] <= initial_position_y <=y[g+1]:
                            k = g
                            break
                        else:
                            continue
                    locals()['x_backnew'+str(iteration)][time] = initial_position_x - Vx2[k,l]*dt - Nx[0]*horizontal_diffusivity**0.5
                    locals()['y_backnew'+str(iteration)][time] = initial_position_y - Vy2[k,l]*dt - Ny[0]*horizontal_diffusivity**0.5           
                    locals()['z_backnew'+str(iteration)][time] = initial_position_z - (Vz2[k,l]-settling_velocity)*dt - Nz[0]*vertical_diffusivuty**0.5
                elif 0.5*(float(wl[start_final+96*(m)])-float(botel[start_final+96*(m)]))<initial_position_z-float(botel[start_final+96*(m)])<= 0.75*(float(wl[start_final+96*(m)])-float(botel[start_final+96*(m)])):     
                    for q in range(0,5-1):
                        if x[q] <= initial_position_x <=x[q+1]:
                            l = q
                            break
                        else:
                            continue
                    for g in range(0,3-1):       
                        if y[g] <= initial_position_y <=y[g+1]:
                            k = g
                            break
                        else:
                            continue
                    locals()['x_backnew'+str(iteration)][time] = initial_position_x - Vx3[k,l]*dt - Nx[0]*horizontal_diffusivity**0.5
                    locals()['y_backnew'+str(iteration)][time] = initial_position_y - Vy2[k,l]*dt - Ny[0]*horizontal_diffusivity**0.5           
                    locals()['z_backnew'+str(iteration)][time] = initial_position_z - (Vz3[k,l]-settling_velocity)*dt - Nz[0]*vertical_diffusivuty**0.5                            
                else:
                    for q in range(0,5-1):
                        if x[q] <= initial_position_x <=x[q+1]:
                            l = q
                            break
                        else:
                            continue
                    for g in range(0,3-1):       
                        if y[g] <= initial_position_y <=y[g+1]:
                            k = g
                            break
                        else:
                            continue
                    locals()['x_backnew'+str(iteration)][time] = initial_position_x - Vx4[k,l]*dt - Nx[0]*horizontal_diffusivity**0.5
                    locals()['y_backnew'+str(iteration)][time] = initial_position_y - Vy4[k,l]*dt - Ny[0]*horizontal_diffusivity**0.5           
                    locals()['z_backnew'+str(iteration)][time] = initial_position_z - (Vz4[k,l]-settling_velocity)*dt - Nz[0]*vertical_diffusivuty**0.5                                                                 
    
        else:
                for q in range(0,5-1):
                    if x[q] <= locals()['x_backnew'+str(iteration)][time-1] <=x[q+1]:
                        l = q
                        break
                    elif locals()['x_backnew'+str(iteration)][time-1]<x[0]:
                        locals()['x_backnew'+str(iteration)][time-1] = x[0]
                        l = 0
                    else:
                        continue
                for g in range(0,3-1):       
                    if y[g] <= locals()['y_backnew'+str(iteration)][time-1] <=y[g+1]:
                        k = g
                        break
                    elif locals()['y_backnew'+str(iteration)][time-1]<y[0]:
                        locals()['y_backnew'+str(iteration)][time-1] = y[0]
                        k = 0
                    else:
                        continue                                    
                
                #限制邊界條件                      
                if x[l] == 0:
                    m = k
                else:
                    m =3*l+k                        
                
                if locals()['z_backnew'+str(iteration)][time-1]<float(botel[start_final+96*(m)]):
                    locals()['z_backnew'+str(iteration)][time-1] = float(botel[start_final+96*(m)])
                elif locals()['z_backnew'+str(iteration)][time-1]>float(wl[start_final+96*(m)]):
                    locals()['z_backnew'+str(iteration)][time-1] = float(wl[start_final+96*(m)])    
                else:
                    pass         
                if locals()['x_backnew'+str(iteration)][time-1] > max(x):
                    locals()['x_backnew'+str(iteration)][time-1] = max(x)
                elif locals()['x_backnew'+str(iteration)][time-1] < min(x):
                    locals()['x_backnew'+str(iteration)][time-1] = min(x)    
                else:
                    pass
                if locals()['y_backnew'+str(iteration)][time-1] > max(y):
                    locals()['y_backnew'+str(iteration)][time-1] = max(y)
                elif locals()['y_backnew'+str(iteration)][time-1] < min(y):
                    locals()['y_backnew'+str(iteration)][time-1] = min(y)    
                else:
                    pass
                            
                
                if locals()['z_backnew'+str(iteration)][time-1]-float(botel[start_final+96*(m)])<=0.25*(float(wl[start_final+96*(m)])-float(botel[start_final+96*(m)])):
                    for q in range(0,5-1):
                        if x[q] <= locals()['x_backnew'+str(iteration)][time-1] <=x[q+1]:
                            l = q
                            break
                        else:
                            continue
                    for g in range(0,3-1):       
                        if y[g] <= locals()['y_backnew'+str(iteration)][time-1] <=y[g+1]:
                            k = g
                            break
                        else:
                            continue
                    if locals()['z_backnew'+str(iteration)][time-1]== float(botel[start_final+96*(m)]) and float(shear_stress[start_final+96*(m)])<=0.001402:
                        locals()['x_backnew'+str(iteration)][time] = locals()['x_backnew'+str(iteration)][time-1] 
                        locals()['y_backnew'+str(iteration)][time] = locals()['y_backnew'+str(iteration)][time-1]            
                        locals()['z_backnew'+str(iteration)][time] = locals()['z_backnew'+str(iteration)][time-1]    
                    else:       
                        locals()['x_backnew'+str(iteration)][time] = locals()['x_backnew'+str(iteration)][time-1] - Vx1[k,l]*dt - Nx[0]*horizontal_diffusivity**0.5
                        locals()['y_backnew'+str(iteration)][time] = locals()['y_backnew'+str(iteration)][time-1] - Vy1[k,l]*dt - Ny[0]*horizontal_diffusivity**0.5           
                        locals()['z_backnew'+str(iteration)][time] = locals()['z_backnew'+str(iteration)][time-1] - (Vz1[k,l]-settling_velocity)*dt - Nz[0]*vertical_diffusivuty**0.5 
                                                                                        
                elif 0.25*(float(wl[start_final+96*(m)])-float(botel[start_final+96*(m)]))<locals()['z_backnew'+str(iteration)][time-1]-float(botel[start_final+96*(m)])<= 0.5*(float(wl[start_final+96*(m)])-float(botel[start_final+96*(m)])):
                    for q in range(0,5-1):
                        if x[q] <= locals()['x_backnew'+str(iteration)][time-1] <=x[q+1]:
                            l = q
                            break
                        else:
                            continue
                    for g in range(0,3-1):       
                        if y[g] <= locals()['y_backnew'+str(iteration)][time-1] <=y[g+1]:
                            k = g
                            break
                        else:
                            continue
                    if locals()['z_backnew'+str(iteration)][time-1]== float(botel[start_final+96*(m)]) and  float(shear_stress[start_final+96*(m)])<=0.001402:
                        locals()['x_backnew'+str(iteration)][time] = locals()['x_backnew'+str(iteration)][time-1] 
                        locals()['y_backnew'+str(iteration)][time] = locals()['y_backnew'+str(iteration)][time-1]            
                        locals()['z_backnew'+str(iteration)][time] = locals()['z_backnew'+str(iteration)][time-1]    
                    else: 
                        locals()['x_backnew'+str(iteration)][time] = locals()['x_backnew'+str(iteration)][time-1] - Vx2[k,l]*dt - Nx[0]*horizontal_diffusivity**0.5
                        locals()['y_backnew'+str(iteration)][time] = locals()['y_backnew'+str(iteration)][time-1] - Vy2[k,l]*dt - Ny[0]*horizontal_diffusivity**0.5           
                        locals()['z_backnew'+str(iteration)][time] = locals()['z_backnew'+str(iteration)][time-1] - (Vz2[k,l]-settling_velocity)*dt - Nz[0]*vertical_diffusivuty**0.5 
                elif 0.5*(float(wl[start_final+96*(m)])-float(botel[start_final+96*(m)]))<locals()['z_backnew'+str(iteration)][time-1]-float(botel[start_final+96*(m)])<= 0.75*(float(wl[start_final+96*(m)])-float(botel[start_final+96*(m)])):     
                    for q in range(0,5-1):
                        if x[q] <= locals()['x_backnew'+str(iteration)][time-1] <=x[q+1]:
                            l = q
                            break
                        else:
                            continue
                    for g in range(0,3-1):       
                        if y[g] <= locals()['y_backnew'+str(iteration)][time-1] <=y[g+1]:
                            k = g
                            break
                        else:
                            continue
                    if locals()['z_backnew'+str(iteration)][time-1]== float(botel[start_final+96*(m)]) and  float(shear_stress[start_final+96*(m)])<=0.001402:
                        locals()['x_backnew'+str(iteration)][time] = locals()['x_backnew'+str(iteration)][time-1] 
                        locals()['y_backnew'+str(iteration)][time] = locals()['y_backnew'+str(iteration)][time-1]            
                        locals()['z_backnew'+str(iteration)][time] = locals()['z_backnew'+str(iteration)][time-1]    
                    else: 
                        locals()['x_backnew'+str(iteration)][time] = locals()['x_backnew'+str(iteration)][time-1] - Vx3[k,l]*dt - Nx[0]*horizontal_diffusivity**0.5
                        locals()['y_backnew'+str(iteration)][time] = locals()['y_backnew'+str(iteration)][time-1] - Vy3[k,l]*dt - Ny[0]*horizontal_diffusivity**0.5           
                        locals()['z_backnew'+str(iteration)][time] = locals()['z_backnew'+str(iteration)][time-1] - (Vz3[k,l]-settling_velocity)*dt - Nz[0]*vertical_diffusivuty**0.5                            
                else:
                    for q in range(0,5-1):
                        if x[q] <= locals()['x_backnew'+str(iteration)][time-1] <=x[q+1]:
                            l = q
                            break
                        else:
                            continue
                    for g in range(0,3-1):       
                        if y[g] <= locals()['y_backnew'+str(iteration)][time-1] <=y[g+1]:
                            k = g
                            break
                        else:
                            continue
                    if locals()['z_backnew'+str(iteration)][time-1]== float(botel[start_final+96*(m)]) and  float(shear_stress[start_final+96*(m)])<=0.001402:
                        locals()['x_backnew'+str(iteration)][time] = locals()['x_backnew'+str(iteration)][time-1] 
                        locals()['y_backnew'+str(iteration)][time] = locals()['y_backnew'+str(iteration)][time-1]          
                        locals()['z_backnew'+str(iteration)][time] = locals()['z_backnew'+str(iteration)][time-1]    
                    else:                     
                        locals()['x_backnew'+str(iteration)][time] = locals()['x_backnew'+str(iteration)][time-1] - Vx4[k,l]*dt - Nx[0]*horizontal_diffusivity**0.5
                        locals()['y_backnew'+str(iteration)][time] = locals()['y_backnew'+str(iteration)][time-1] - Vy4[k,l]*dt - Ny[0]*horizontal_diffusivity**0.5           
                        locals()['z_backnew'+str(iteration)][time] = locals()['z_backnew'+str(iteration)][time-1] - (Vz4[k,l]-settling_velocity)*dt - Nz[0]*vertical_diffusivuty**0.5          

px_back,py_back,pz_back =np.ones([int(number),int(particles-1)]),np.ones([int(number),int(particles-1)]),np.ones([int(number),int(particles-1)])

#計算mean & variance
for i in range(0,int(particles)-1):
    px_back[:,i] = locals()['x_backnew'+str(i)][:]
    py_back[:,i] = locals()['y_backnew'+str(i)][:]
    pz_back[:,i] = locals()['z_backnew'+str(i)][:]
    
mean_x_backward, mean_y_backward, mean_z_backward = np.zeros([int(number)]),np.zeros([int(number)]),np.zeros([int(number)])
for i in range(0,int(number)):
    mean_x_backward[i] = sum(px_back[i,:])/int(particles)
    mean_y_backward[i] = sum(py_back[i,:])/int(particles)
    mean_z_backward[i] = sum(pz_back[i,:])/int(particles)

var_x_backward, var_y_backward, var_z_backward = np.zeros([int(number)]),np.zeros([int(number)]),np.zeros([int(number)])
for i in range(0,int(number)):
    var_x_backward[i] = sum((px_back[i,:]-mean_x_backward[i])**2)/int(particles)
    var_y_backward[i] = sum((py_back[i,:]-mean_y_backward[i])**2)/int(particles)
    var_z_backward[i] = sum((pz_back[i,:]-mean_z_backward[i])**2)/int(particles)
del px_back,py_back,pz_back

                
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # 空间三维画图               
                             
fig = plt.figure(figsize=(15,10),dpi=300)
ax = Axes3D(fig)

ax.set_zlabel('Z', fontdict={'size': 15, 'color': 'red'})
ax.set_ylabel('Y', fontdict={'size': 15, 'color': 'red'})
ax.set_xlabel('X', fontdict={'size': 15, 'color': 'red'})
"""
ax.set_ylim(0,max(y))
ax.set_xlim(0,max(x))
"""
plt.plot(mean_x_backward,mean_y_backward,mean_z_backward,linestyle='solid',color='red')
plt.show()     
                          
bkxpoint,bkypoint,bkzpoint =np.ones([particles,1]),np.ones([particles,1]),np.ones([particles,1])
# x,z 點分布圖
for iteration in range(0,particles):
    bkxpoint[iteration,0] = locals()['x_backnew'+str(iteration)][-1]
    bkypoint[iteration,0] = locals()['y_backnew'+str(iteration)][-1]
    bkzpoint[iteration,0] = locals()['z_backnew'+str(iteration)][-1]
import numpy as np
fig = plt.figure(figsize=(15,10),dpi=300)
plt.grid(True)
plt.scatter(bkxpoint,bkzpoint)
plt.xlabel('X')
plt.ylabel('Z')
plt.title('X,Z backward-scatter')
plt.show()

fig = plt.figure(figsize=(15,10),dpi=300)
plt.grid(True)
plt.scatter(bkxpoint,bkypoint)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('X,Y backward-scatter')
plt.show()

fig = plt.figure(figsize=(15,10),dpi=300)
plt.grid(True)
plt.scatter(bkypoint,bkzpoint)
plt.xlabel('Y')
plt.ylabel('Z')
plt.title('Y,Z backward-scatter')
plt.show()                

                
               
                
                
# Forward particles tracking model
import numpy as np
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # 空间三维画图  
for pp in range(0,particles): 
    start_269 = 8
    for time in range(0,1):
        for i in range(0,5):
            for n in range(0,3):            
                if x[i] == 0:
                    m = n
                else:
                    m =2*i+n
                Z[n,i]=X[n,i]*0+Y[n,i]*0+float(botel[start_269+96*(m)]) #底床
                Wl[n,i]=X[n,i]*0+Y[n,i]*0+float(wl[start_269+96*(m)])   #水位
                
    #建立流速場(x,y,z以及layer1~4)
    Vx1,Vx2,Vx3,Vx4= np.zeros([3,5]),np.zeros([3,5]),np.zeros([3,5]),np.zeros([3,5])
    Vy1,Vy2,Vy3,Vy4= np.zeros([3,5]),np.zeros([3,5]),np.zeros([3,5]),np.zeros([3,5])
    Vz1,Vz2,Vz3,Vz4= np.zeros([3,5]),np.zeros([3,5]),np.zeros([3,5]),np.zeros([3,5])
                   
    for p in range(0,101):
        for i in range(0,5):
            for n in range(0,3):
                if x[i] == 0:
                    m = n
                else:
                    m =2*i+n
                if z[p]-float(botel[start_final+96*(m)])<=0.25*(float(wl[start_final+96*(m)])-float(botel[start_final+96*(m)])):
                    Vx1[n,i] = float(v_x1[start_final+96*(m)])
                    Vy1[n,i] = float(v_y1[start_final+96*(m)])
                    Vz1[n,i] = float(v_z1[start_final+96*(m)])
                elif 0.25*(float(wl[start_final+96*(m)])-float(botel[start_final+96*(m)]))<z[p]-float(botel[start_final+96*(m)])<= 0.5*(float(wl[start_final+96*(m)])-float(botel[start_final+96*(m)])):
                    Vx2[n,i] = float(v_x2[start_final+96*(m)])
                    Vy2[n,i] = float(v_y2[start_final+96*(m)])
                    Vz2[n,i] = float(v_z2[start_final+96*(m)])                   
                elif 0.5*(float(wl[start_final+96*(m)])-float(botel[start_final+96*(m)]))<z[p]-float(botel[start_final+96*(m)])<= 0.75*(float(wl[start_final+96*(m)])-float(botel[start_final+96*(m)])):     
                    Vx3[n,i] = float(v_x3[start_final+96*(m)])
                    Vy3[n,i] = float(v_y3[start_final+96*(m)])
                    Vz3[n,i] = float(v_z3[start_final+96*(m)])                            
                else:
                    Vx4[n,i] = float(v_x4[start_final+96*(m)])
                    Vy4[n,i] = float(v_y4[start_final+96*(m)])
                    Vz4[n,i] = float(v_z4[start_final+96*(m)]) 
    
    
    initial_position_x = locals()['x_backnew'+str(pp)][-1]
    initial_position_y = locals()['y_backnew'+str(pp)][-1]
    initial_position_z = locals()['z_backnew'+str(pp)][-1]
    for iteration in range(0,particles):
        #起始位置分別為向後算的終點        
        locals()['x_fornew'+str(pp)+'顆'+str(iteration)], locals()['y_fornew'+str(pp)+'顆'+str(iteration)], locals()['z_fornew'+str(pp)+'顆'+str(iteration)] =np.zeros(int(number)),np.zeros(int(number)),np.zeros(int(number))
        for time in range(0,int(number)):
            Nx = np.random.normal(0, 0.1**0.5,1)
            Ny = np.random.normal(0, 0.1**0.5,1)
            Nz = np.random.normal(0, 0.1**0.5,1)
            if  time == 0:
                    for q in range(0,5-1):
                        if x[q] <= initial_position_x <=x[q+1]:
                            l = q
                            break
                        else:
                            continue
                    for g in range(0,3-1):       
                        if y[g] <= initial_position_y <=y[g+1]:
                            k = g
                            break
                        else:
                            continue
                    if x[l] == 0:
                        m = k
                    else:
                        m =3*l+k                        
                    if initial_position_z-float(botel[start_269+96*(m)])<=0.25*(float(wl[start_269+96*(m)])-float(botel[start_269+96*(m)])):
        
                        locals()['x_fornew'+str(pp)+'顆'+str(iteration)][time] = initial_position_x + Vx1[k,l]*dt + Nx[0]*horizontal_diffusivity**0.5
                        locals()['y_fornew'+str(pp)+'顆'+str(iteration)][time] = initial_position_y + Vy1[k,l]*dt + Ny[0]*horizontal_diffusivity**0.5           
                        locals()['z_fornew'+str(pp)+'顆'+str(iteration)][time] = initial_position_z + (Vz1[k,l]-settling_velocity)*dt + Nz[0]*vertical_diffusivuty**0.5
                                                                                            
                    elif 0.25*(float(wl[start_269+96*(m)])-float(botel[start_269+96*(m)]))<initial_position_z-float(botel[start_269+96*(m)])<= 0.5*(float(wl[start_269+96*(m)])-float(botel[start_269+96*(m)])):
                        for q in range(0,5-1):
                            if x[q] <= initial_position_x <=x[q+1]:
                                l = q
                                break
                            else:
                                continue
                        for g in range(0,3-1):       
                            if y[g] <= initial_position_y <=y[g+1]:
                                k = g
                                break
                            else:
                                continue
                        locals()['x_fornew'+str(pp)+'顆'+str(iteration)][time] = initial_position_x + Vx2[k,l]*dt + Nx[0]*horizontal_diffusivity**0.5
                        locals()['y_fornew'+str(pp)+'顆'+str(iteration)][time] = initial_position_y + Vy2[k,l]*dt + Ny[0]*horizontal_diffusivity**0.5           
                        locals()['z_fornew'+str(pp)+'顆'+str(iteration)][time] = initial_position_z + (Vz2[k,l]-settling_velocity)*dt + Nz[0]*vertical_diffusivuty**0.5
                    elif 0.5*(float(wl[start_269+96*(m)])-float(botel[start_269+96*(m)]))<initial_position_z-float(botel[start_269+96*(m)])<= 0.75*(float(wl[start_269+96*(m)])-float(botel[start_269+96*(m)])):     
                        for q in range(0,5-1):
                            if x[q] <= initial_position_x <=x[q+1]:
                                l = q
                                break
                            else:
                                continue
                        for g in range(0,3-1):       
                            if y[g] <= initial_position_y <=y[g+1]:
                                k = g
                                break
                            else:
                                continue
                        locals()['x_fornew'+str(pp)+'顆'+str(iteration)][time] = initial_position_x + Vx3[k,l]*dt + Nx[0]*horizontal_diffusivity**0.5
                        locals()['y_fornew'+str(pp)+'顆'+str(iteration)][time] = initial_position_y + Vy2[k,l]*dt + Ny[0]*horizontal_diffusivity**0.5           
                        locals()['z_fornew'+str(pp)+'顆'+str(iteration)][time] = initial_position_z + (Vz3[k,l]-settling_velocity)*dt + Nz[0]*vertical_diffusivuty**0.5                            
                    else:
                        for q in range(0,5-1):
                            if x[q] <= initial_position_x <=x[q+1]:
                                l = q
                                break
                            else:
                                continue
                        for g in range(0,3-1):       
                            if y[g] <= initial_position_y <=y[g+1]:
                                k = g
                                break
                            else:
                                continue
                        locals()['x_fornew'+str(pp)+'顆'+str(iteration)][time] = initial_position_x + Vx4[k,l]*dt + Nx[0]*horizontal_diffusivity**0.5
                        locals()['y_fornew'+str(pp)+'顆'+str(iteration)][time] = initial_position_y + Vy4[k,l]*dt + Ny[0]*horizontal_diffusivity**0.5           
                        locals()['z_fornew'+str(pp)+'顆'+str(iteration)][time] = initial_position_z + (Vz4[k,l]-settling_velocity)*dt + Nz[0]*vertical_diffusivuty**0.5                                                                 
        
            else:
                    for q in range(0,5-1):
                        if x[q] <= locals()['x_fornew'+str(pp)+'顆'+str(iteration)][time-1] <=x[q+1]:
                            l = q
                            break
                        elif locals()['x_fornew'+str(pp)+'顆'+str(iteration)][time-1]<x[0]:
                            locals()['x_fornew'+str(pp)+'顆'+str(iteration)][time-1] = x[0]
                            l = 0
                        else:
                            continue
                    for g in range(0,3-1):       
                        if y[g] <= locals()['y_fornew'+str(pp)+'顆'+str(iteration)][time-1] <=y[g+1]:
                            k = g
                            break
                        elif locals()['y_fornew'+str(pp)+'顆'+str(iteration)][time-1]<y[0]:
                            locals()['y_fornew'+str(pp)+'顆'+str(iteration)][time-1] = y[0]
                            k = 0
                        else:
                            continue                                    
                    
                    #限制邊界條件                      
                    if x[l] == 0:
                        m = k
                    else:
                        m =3*l+k                        
                    
                    if locals()['z_fornew'+str(pp)+'顆'+str(iteration)][time-1]<float(botel[start_269+96*(m)]):
                        locals()['z_fornew'+str(pp)+'顆'+str(iteration)][time-1] = float(botel[start_269+96*(m)])
                    elif locals()['z_fornew'+str(pp)+'顆'+str(iteration)][time-1]>float(wl[start_269+96*(m)]):
                        locals()['z_fornew'+str(pp)+'顆'+str(iteration)][time-1] = float(wl[start_269+96*(m)])    
                    else:
                        pass         
                    if locals()['x_fornew'+str(pp)+'顆'+str(iteration)][time-1] > max(x):
                        locals()['x_fornew'+str(pp)+'顆'+str(iteration)][time-1] = max(x)   
                    elif locals()['x_fornew'+str(pp)+'顆'+str(iteration)][time-1] < min(x):
                        locals()['x_fornew'+str(pp)+'顆'+str(iteration)][time-1] = min(x)
                    else:
                        pass
                    if locals()['y_fornew'+str(pp)+'顆'+str(iteration)][time-1] > max(y):
                        locals()['y_fornew'+str(pp)+'顆'+str(iteration)][time-1] = max(y)   
                    elif locals()['y_fornew'+str(pp)+'顆'+str(iteration)][time-1] < min(y):
                        locals()['y_fornew'+str(pp)+'顆'+str(iteration)][time-1] = min(y)
                    else:
                        pass
                                
                    
                    if locals()['z_fornew'+str(pp)+'顆'+str(iteration)][time-1]-float(botel[start_269+96*(m)])<=0.25*(float(wl[start_269+96*(m)])-float(botel[start_269+96*(m)])):
                        for q in range(0,5-1):
                            if x[q] <= locals()['x_fornew'+str(pp)+'顆'+str(iteration)][time-1] <=x[q+1]:
                                l = q
                                break
                            else:
                                continue
                        for g in range(0,3-1):       
                            if y[g] <= locals()['y_fornew'+str(pp)+'顆'+str(iteration)][time-1] <=y[g+1]:
                                k = g
                                break
                            else:
                                continue
                        if locals()['z_fornew'+str(pp)+'顆'+str(iteration)][time-1]== float(botel[start_269+96*(m)]) and float(shear_stress[start_269+96*(m)])<=0.001402:
                            locals()['x_fornew'+str(pp)+'顆'+str(iteration)][time] = locals()['x_fornew'+str(pp)+'顆'+str(iteration)][time-1] 
                            locals()['y_fornew'+str(pp)+'顆'+str(iteration)][time] = locals()['y_fornew'+str(pp)+'顆'+str(iteration)][time-1]            
                            locals()['z_fornew'+str(pp)+'顆'+str(iteration)][time] = locals()['z_fornew'+str(pp)+'顆'+str(iteration)][time-1]    
                        else:       
                            locals()['x_fornew'+str(pp)+'顆'+str(iteration)][time] = locals()['x_fornew'+str(pp)+'顆'+str(iteration)][time-1] + Vx1[k,l]*dt + Nx[0]*horizontal_diffusivity**0.5
                            locals()['y_fornew'+str(pp)+'顆'+str(iteration)][time] = locals()['y_fornew'+str(pp)+'顆'+str(iteration)][time-1] + Vy1[k,l]*dt + Ny[0]*horizontal_diffusivity**0.5           
                            locals()['z_fornew'+str(pp)+'顆'+str(iteration)][time] = locals()['z_fornew'+str(pp)+'顆'+str(iteration)][time-1] + (Vz1[k,l]-settling_velocity)*dt + Nz[0]*vertical_diffusivuty**0.5 
                                                                                            
                    elif 0.25*(float(wl[start_269+96*(m)])-float(botel[start_269+96*(m)]))<locals()['z_fornew'+str(pp)+'顆'+str(iteration)][time-1]-float(botel[start_269+96*(m)])<= 0.5*(float(wl[start_269+96*(m)])-float(botel[start_269+96*(m)])):
                        for q in range(0,5-1):
                            if x[q] <= locals()['x_fornew'+str(pp)+'顆'+str(iteration)][time-1] <=x[q+1]:
                                l = q
                                break
                            else:
                                continue
                        for g in range(0,3-1):       
                            if y[g] <= locals()['y_fornew'+str(pp)+'顆'+str(iteration)][time-1] <=y[g+1]:
                                k = g
                                break
                            else:
                                continue
                        if locals()['z_fornew'+str(pp)+'顆'+str(iteration)][time-1]== float(botel[start_269+96*(m)]) and  float(shear_stress[start_269+96*(m)])<=0.001402:
                            locals()['x_fornew'+str(pp)+'顆'+str(iteration)][time] = locals()['x_fornew'+str(pp)+'顆'+str(iteration)][time-1] 
                            locals()['y_fornew'+str(pp)+'顆'+str(iteration)][time] = locals()['y_fornew'+str(pp)+'顆'+str(iteration)][time-1]            
                            locals()['z_fornew'+str(pp)+'顆'+str(iteration)][time] = locals()['z_fornew'+str(pp)+'顆'+str(iteration)][time-1]    
                        else: 
                            locals()['x_fornew'+str(pp)+'顆'+str(iteration)][time] = locals()['x_fornew'+str(pp)+'顆'+str(iteration)][time-1] + Vx2[k,l]*dt + Nx[0]*horizontal_diffusivity**0.5
                            locals()['y_fornew'+str(pp)+'顆'+str(iteration)][time] = locals()['y_fornew'+str(pp)+'顆'+str(iteration)][time-1] + Vy2[k,l]*dt + Ny[0]*horizontal_diffusivity**0.5           
                            locals()['z_fornew'+str(pp)+'顆'+str(iteration)][time] = locals()['z_fornew'+str(pp)+'顆'+str(iteration)][time-1] + (Vz2[k,l]-settling_velocity)*dt + Nz[0]*vertical_diffusivuty**0.5 
                    elif 0.5*(float(wl[start_269+96*(m)])-float(botel[start_269+96*(m)]))<locals()['z_fornew'+str(pp)+'顆'+str(iteration)][time-1]-float(botel[start_269+96*(m)])<= 0.75*(float(wl[start_269+96*(m)])-float(botel[start_269+96*(m)])):     
                        for q in range(0,5-1):
                            if x[q] <= locals()['x_fornew'+str(pp)+'顆'+str(iteration)][time-1] <=x[q+1]:
                                l = q
                                break
                            else:
                                continue
                        for g in range(0,3-1):       
                            if y[g] <= locals()['y_fornew'+str(pp)+'顆'+str(iteration)][time-1] <=y[g+1]:
                                k = g
                                break
                            else:
                                continue
                        if locals()['z_fornew'+str(pp)+'顆'+str(iteration)][time-1]== float(botel[start_269+96*(m)]) and  float(shear_stress[start_269+96*(m)])<=0.001402:
                            locals()['x_fornew'+str(pp)+'顆'+str(iteration)][time] = locals()['x_fornew'+str(pp)+'顆'+str(iteration)][time-1] 
                            locals()['y_fornew'+str(pp)+'顆'+str(iteration)][time] = locals()['y_fornew'+str(pp)+'顆'+str(iteration)][time-1]            
                            locals()['z_fornew'+str(pp)+'顆'+str(iteration)][time] = locals()['z_fornew'+str(pp)+'顆'+str(iteration)][time-1]    
                        else: 
                            locals()['x_fornew'+str(pp)+'顆'+str(iteration)][time] = locals()['x_fornew'+str(pp)+'顆'+str(iteration)][time-1] + Vx3[k,l]*dt + Nx[0]*horizontal_diffusivity**0.5
                            locals()['y_fornew'+str(pp)+'顆'+str(iteration)][time] = locals()['y_fornew'+str(pp)+'顆'+str(iteration)][time-1] + Vy3[k,l]*dt + Ny[0]*horizontal_diffusivity**0.5           
                            locals()['z_fornew'+str(pp)+'顆'+str(iteration)][time] = locals()['z_fornew'+str(pp)+'顆'+str(iteration)][time-1] + (Vz3[k,l]-settling_velocity)*dt + Nz[0]*vertical_diffusivuty**0.5                            
                    else:
                        for q in range(0,5-1):
                            if x[q] <= locals()['x_fornew'+str(pp)+'顆'+str(iteration)][time-1] <=x[q+1]:
                                l = q
                                break
                            else:
                                continue
                        for g in range(0,3-1):       
                            if y[g] <= locals()['y_fornew'+str(pp)+'顆'+str(iteration)][time-1] <=y[g+1]:
                                k = g
                                break
                            else:
                                continue
                        if locals()['z_fornew'+str(pp)+'顆'+str(iteration)][time-1]== float(botel[start_269+96*(m)]) and  float(shear_stress[start_269+96*(m)])<=0.001402:
                            locals()['x_fornew'+str(pp)+'顆'+str(iteration)][time] = locals()['x_fornew'+str(pp)+'顆'+str(iteration)][time-1] 
                            locals()['y_fornew'+str(pp)+'顆'+str(iteration)][time] = locals()['y_fornew'+str(pp)+'顆'+str(iteration)][time-1]          
                            locals()['z_fornew'+str(pp)+'顆'+str(iteration)][time] = locals()['z_fornew'+str(pp)+'顆'+str(iteration)][time-1]    
                        else:                     
                            locals()['x_fornew'+str(pp)+'顆'+str(iteration)][time] = locals()['x_fornew'+str(pp)+'顆'+str(iteration)][time-1] + Vx4[k,l]*dt + Nx[0]*horizontal_diffusivity**0.5
                            locals()['y_fornew'+str(pp)+'顆'+str(iteration)][time] = locals()['y_fornew'+str(pp)+'顆'+str(iteration)][time-1] + Vy4[k,l]*dt + Ny[0]*horizontal_diffusivity**0.5           
                            locals()['z_fornew'+str(pp)+'顆'+str(iteration)][time] = locals()['z_fornew'+str(pp)+'顆'+str(iteration)][time-1] + (Vz4[k,l]-settling_velocity)*dt + Nz[0]*vertical_diffusivuty**0.5          
    
    px_for,py_for,pz_for =np.ones([int(number),int(particles)]),np.ones([int(number),int(particles)]),np.ones([int(number),int(particles)])
    
    #計算mean & variance
    for i in range(0,int(particles)-1):
        px_for[:,i] = locals()['x_fornew'+str(pp)+'顆'+str(i)][:]
        py_for[:,i] = locals()['y_fornew'+str(pp)+'顆'+str(i)][:]
        pz_for[:,i] = locals()['z_fornew'+str(pp)+'顆'+str(i)][:]
        
    mean_x_forward, mean_y_forward, mean_z_forward = np.zeros([int(number),int(particles)]),np.zeros([int(number),int(particles)]),np.zeros([int(number),int(particles)])
    for i in range(0,int(number)):        
        mean_x_forward[i,pp] = sum(px_for[i,:])/int(particles)
        mean_y_forward[i,pp] = sum(py_for[i,:])/int(particles)
        mean_z_forward[i,pp] = sum(pz_for[i,:])/int(particles)
    
    var_x_forward, var_y_forward, var_z_forward = np.zeros([int(number),int(particles)]),np.zeros([int(number),int(particles)]),np.zeros([int(number),int(particles)])
    for i in range(0,int(number)):
        var_x_forward[i,pp] = sum((px_for[i,:]-mean_x_forward[i,pp])**2)/int(particles)
        var_y_forward[i,pp] = sum((py_for[i,:]-mean_y_forward[i,pp])**2)/int(particles)
        var_z_forward[i,pp] = sum((pz_for[i,:]-mean_z_forward[i,pp])**2)/int(particles)
    del px_for,py_for,pz_for
    
                                
fig = plt.figure(figsize=(15,10),dpi=300)
ax = Axes3D(fig)

ax.set_zlabel('Z', fontdict={'size': 15, 'color': 'red'})
ax.set_ylabel('Y', fontdict={'size': 15, 'color': 'red'})
ax.set_xlabel('X', fontdict={'size': 15, 'color': 'red'})
"""
ax.set_ylim(0,max(y))
ax.set_xlim(0,max(x))
"""
for i in range(0,int(number)):
    plt.plot(mean_x_forward[i,:],mean_y_forward[i,:],mean_z_forward[i,:],linestyle='solid',color='red')
plt.show()                  
                    
"""                    
forxpoint,forypoint,forzpoint =np.ones([particles,1]),np.ones([particles,1]),np.ones([particles,1])
# x,z 點分布圖
for iteration in range(0,particles):
    forxpoint[iteration,0] = locals()['x_fornew'+str(pp)+'顆'+str(iteration)][-1]
    forypoint[iteration,0] = locals()['y_fornew'+str(pp)+'顆'+str(iteration)][-1]
    forzpoint[iteration,0] = locals()['z_fornew'+str(pp)+'顆'+str(iteration)][-1]

fig = plt.figure(figsize=(15,10),dpi=300)
plt.grid(True)
plt.scatter(forxpoint,forzpoint)
plt.xlabel('X')
plt.ylabel('Z')
plt.title('X,Z forward-scatter')
plt.show()

fig = plt.figure(figsize=(15,10),dpi=300)
plt.grid(True)
plt.scatter(forxpoint,forypoint)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('X,Y forward-scatter')
plt.show()

fig = plt.figure(figsize=(15,10),dpi=300)
plt.grid(True)
plt.scatter(forypoint,forzpoint)
plt.xlabel('Y')
plt.ylabel('Z')
plt.title('Y,Z forward-scatter')
plt.show()                
"""                    
                
                
                
                
































