# -*- coding: utf-8 -*-
"""
Sint Maartenskliniek study ID: 807_TrunkyXL
    Functions for analysis of 2M sensor data (Nodes or QSense Motion)

Last update:
    21-09-2022: C.J. Ensink, c.ensink@maartenskliniek.nl
    
"""

import numpy as np
import matplotlib.pyplot as plt
import ahrs
from scipy.spatial.transform import Rotation as R

import pyquaternion as pyq
import math

def orientation_estimation (fs, sensordata):
    # This function uses the Mahony AHRS filter to estimate orientation (quaternion) from accelerometer and gyroscope data.
    # Mahony was chosen in favor of Madgwick, as the LEC of the Sint Maartenskliniek has a lot of metal that might interfere on the magnetometer, therefore orientation estimations including the magnetometer signal (Madgwick) might drift quite a lot.
    # Euler angles were calculated from the estimated quaternion orientation.
    
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
    
    return sensordata



def orientation_euler(sensordata):
    
    quat = np.swapaxes(np.array((sensordata['q0'],sensordata['q1'],sensordata['q2'],sensordata['q3'])), 0,1)
    euler = np.zeros((1,3))
    for i in range(0, len(sensordata['q0'])):
        try:
            r = R.from_quat(quat[i])
            euler = np.vstack((euler, r.as_euler('xyz', degrees=True)))
        except:
            euler = np.vstack((euler, np.array([0,0,0])))   
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




def relative_orientation(sensorRelative, sensorFixed, relative_to):
    # sensorRelative should include the orientation of the sensor relative to the orientation of another sensor over time.
    # sensorFixed should include the orientation of the sensor to which another sensor's orientation should be calculated over time.
    quat_sensorRelative = np.swapaxes(np.array([sensorRelative['q0'],sensorRelative['q1'],sensorRelative['q2'],sensorRelative['q3']]), 0, 1)
    quat_sensorFixed = np.swapaxes(np.array([sensorFixed['q0'],sensorFixed['q1'],sensorFixed['q2'],sensorFixed['q3']]), 0, 1)

    phi = np.zeros((len(quat_sensorRelative), 1))
    theta = np.zeros((len(quat_sensorRelative), 1))
    psi = np.zeros((len(quat_sensorRelative), 1))
    
    for j in range(len(quat_sensorFixed)):
        q_fixed = pyq.Quaternion( quat_sensorFixed[j,:] )
        q_relative = pyq.Quaternion( quat_sensorRelative[j,:] )
        
        # Get the 3D difference between these two orientations
        qd = q_fixed.conjugate * q_relative
        qd = qd.normalised
    
        # Calculate Euler angles from this difference quaternion
        phi[j]   = np.rad2deg( math.atan2( 2 * (qd.w * qd.x + qd.y * qd.z), 1 - 2 * (qd.x**2 + qd.y**2) ) )
        theta[j] = np.rad2deg( math.asin ( 2 * (qd.w * qd.y - qd.z * qd.x) ) )
        psi[j]   = np.rad2deg( math.atan2( 2 * (qd.w * qd.z + qd.x * qd.y), 1 - 2 * (qd.y**2 + qd.z**2) ) )
    
    eulerx_relative_to = 'ex relative to '+ relative_to
    eulery_relative_to = 'ey relative to '+ relative_to
    eulerz_relative_to = 'ez relative to '+ relative_to
    sensorRelative[eulerx_relative_to] = phi
    sensorRelative[eulery_relative_to] = theta
    sensorRelative[eulerz_relative_to] = psi
    
    return sensorRelative