# -*- coding: utf-8 -*-
"""
Trunky data, QSense-Motion application

Author: CJ Ensink

"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import samplerate
import ahrs
from ahrs.common.orientation import q_prod, q_conj, acc2q, am2q, q2R, q_rot
import pyquaternion
from scipy import signal
from scipy.spatial.transform import Rotation as R

sensor1 = pd.read_csv('V:/research_reva_studies/807_TrunkyXL/II_Onderzoeksdata/Databestanden/Pilot metingen/testdata QSense/QSM_20220915141805/R/Back/Sensor 1.csv', delimiter='\t', decimal=',', engine='python', skiprows = 6, names=['ax','ay','az','gx','gy','gz','mx','my','mz','Reference']) # Bovenrug
sensor2 = pd.read_csv('V:/research_reva_studies/807_TrunkyXL/II_Onderzoeksdata/Databestanden/Pilot metingen/testdata QSense/QSM_20220915141805/R/Back/Sensor 2.csv', delimiter='\t', decimal=',', engine='python', skiprows = 6, names=['ax','ay','az','gx','gy','gz','mx','my','mz','Reference']) # Onderrug
sensor3 = pd.read_csv('V:/research_reva_studies/807_TrunkyXL/II_Onderzoeksdata/Databestanden/Pilot metingen/testdata QSense/QSM_20220915141805/R/Back/Sensor 3.csv', delimiter='\t', decimal=',', engine='python', skiprows = 6, names=['ax','ay','az','gx','gy','gz','mx','my','mz','Reference']) # Pelvis

fs_qsense = 25

def orientationqsens (fs, sensordata):
    time = np.arange(0, len(sensordata)/fs, 1/fs)
    gyrX = sensordata['gx'].to_numpy()
    gyrY = sensordata['gy'].to_numpy()
    gyrZ = sensordata['gz'].to_numpy()
    accX = sensordata['ax'].to_numpy()
    accY = sensordata['ay'].to_numpy()
    accZ = sensordata['az'].to_numpy()

    fig = plt.figure(figsize=(10, 5))
    ax1 = fig.add_subplot(2,1,1)
    ax2 = fig.add_subplot(2,1,2)
    ax1.plot(time,gyrX,c='r',linewidth=0.5)
    ax1.plot(time,gyrY,c='g',linewidth=0.5)
    ax1.plot(time,gyrZ,c='b',linewidth=0.5)
    ax1.set_title("gyroscope")
    ax1.set_xlabel("time (s)")
    ax1.set_ylabel("angular velocity (degrees/s)")
    ax1.legend(["x","y","z"])
    ax2.plot(time,accX,c='r',linewidth=0.5)
    ax2.plot(time,accY,c='g',linewidth=0.5)
    ax2.plot(time,accZ,c='b',linewidth=0.5)
    ax2.set_title("accelerometer")
    ax2.set_xlabel("time (s)")
    ax2.set_ylabel("acceleration (g)")
    ax2.legend(["x","y","z"])
    plt.show(block=False)

    # Compute orientation
    quat  = np.zeros((time.size, 4), dtype=np.float64)
    
    # initial convergence
    initPeriod = 2
    indexSel = time<=time[0]+initPeriod
    gyr=np.zeros(3, dtype=np.float64)
    acc = np.array([np.mean(accX[indexSel]), np.mean(accY[indexSel]), np.mean(accZ[indexSel])])
    mahony = ahrs.filters.Mahony(Kp=1, Ki=0,KpInit=1, frequency=fs)
    q = np.array([1.0,0.0,0.0,0.0], dtype=np.float64)
    for i in range(0, 2000):
        q = mahony.updateIMU(q, gyr=gyr, acc=acc)
    
    # For all data
    for t in range(0,time.size):
        # if(stationary[t]):
        #     mahony.Kp = 0.5
        # else:
        #     mahony.Kp = 0
        mahony.Kp = 0
        gyr = np.array([gyrX[t],gyrY[t],gyrZ[t]])*np.pi/180
        acc = np.array([accX[t],accY[t],accZ[t]])
        quat[t,:]=mahony.updateIMU(q,gyr=gyr,acc=acc)
        
    sensordata['q0'] = quat[:,0]
    sensordata['q1'] = quat[:,1]
    sensordata['q2'] = quat[:,2]
    sensordata['q3'] = quat[:,3]
    
    euler = np.zeros((1,3))
    for i in range(0, len(sensordata['q0'])):
        r = R.from_quat(quat[i])
        euler = np.vstack((euler, r.as_euler('xyz', degrees=True)))
    euler = euler[1:,:]
    
    dife = np.diff(euler, axis=0)
    startneg = np.argwhere(dife[:,0] < -350).flatten()
    stopneg = np.argwhere(dife[:,0] > 350).flatten()
    for i in range(len(startneg)):
        try:
            euler[startneg[i]+1:stopneg[stopneg>startneg[i]][0]+1, 0] = euler[startneg[i]+1:stopneg[stopneg>startneg[i]][0]+1, 0]+360
        except:
            pass
    
    startneg = np.argwhere(dife[:,1] < -350).flatten()
    stopneg = np.argwhere(dife[:,1] > 350).flatten()
    for i in range(len(startneg)):
        try:
            euler[startneg[i]+1:stopneg[stopneg>startneg[i]][0]+1, 1] = euler[startneg[i]+1:stopneg[stopneg>startneg[i]][0]+1, 1]+360
        except:
            pass
        
    startneg = np.argwhere(dife[:,2] < -350).flatten()
    stopneg = np.argwhere(dife[:,2] > 350).flatten()
    for i in range(len(startneg)):
        try:
            euler[startneg[i]+1:stopneg[stopneg>startneg[i]][0]+1, 2] = euler[startneg[i]+1:stopneg[stopneg>startneg[i]][0]+1, 2]+360
        except:
            pass
        
    sensordata['ex'] = euler[:,0]
    sensordata['ey'] = euler[:,1]
    sensordata['ez'] = euler[:,2]
    
    return sensordata

sensor1 = orientationqsens(fs_qsense, sensor1)
sensor2 = orientationqsens(fs_qsense, sensor2)
sensor3 = orientationqsens(fs_qsense, sensor3)


fig, ax = plt.subplots(nrows=3, ncols=1)
ax[0].set_title('Euler orientations')
ax[0].plot(sensor1['ex'], label='x')
ax[1].plot(sensor1['ey'], label='y')
ax[2].plot(sensor1['ez'], label='z')

ax[0].legend()
ax[1].legend()
ax[2].legend()

