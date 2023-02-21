# -*- coding: utf-8 -*-
"""
Sint Maartenskliniek study ID: 807_TrunkyXL
    Functions for analysis of 2M sensor data (Nodes or QSense Motion)

Last update:
    02-02-2023: C.J. Ensink, update orientation estimation (Mahony AHRS filter)
    21-09-2022: C.J. Ensink, c.ensink@maartenskliniek.nl
    
"""

import numpy as np
import matplotlib.pyplot as plt
from ahrs.filters import Mahony, Madgwick
from scipy.spatial.transform import Rotation as R

import pyquaternion as pyq
import math

def orientation_estimation (fs, sensordata):
    # This function uses the Mahony AHRS filter to estimate orientation (quaternion) from accelerometer and gyroscope data.
    # Mahony was chosen in favor of Madgwick, as the LEC of the Sint Maartenskliniek has a lot of metal that might interfere on the magnetometer, therefore orientation estimations including the magnetometer signal (Madgwick) might drift quite a lot.
    # Euler angles were calculated from the estimated quaternion orientation.
    
    time = (np.zeros(shape=(len(sensordata),1))).flatten()
    for i in range(1,len(time)):
        time[i] = time[i-1]+1/fs
    gyrX = sensordata['gx'].to_numpy()
    gyrY = sensordata['gy'].to_numpy()
    gyrZ = sensordata['gz'].to_numpy()
    accX = sensordata['ax'].to_numpy()
    accY = sensordata['ay'].to_numpy()
    accZ = sensordata['az'].to_numpy()
    magX = sensordata['mx'].to_numpy()
    magY = sensordata['my'].to_numpy()
    magZ = sensordata['mz'].to_numpy()
    
    # Compute orientation
    # orientation = Mahony()
    orientation = Madgwick()
    Q = np.tile([1., 0., 0., 0.], (time.size, 1)) # Allocate for quaternions
    for t in range(1,time.size):
        gyr_data = np.array([gyrX[t],gyrY[t],gyrZ[t]])*np.pi/180 # In radians/s
        acc_data = np.array([accX[t],accY[t],accZ[t]])*9.81 # In m/s^2 g
        mag_data = np.array([magX[t],magY[t],magZ[t]])
        Q[t] = orientation.updateMARG(Q[t-1], gyr=gyr_data, acc=acc_data, mag=mag_data)
        
    sensordata['q0'] = Q[:,0]
    sensordata['q1'] = Q[:,1]
    sensordata['q2'] = Q[:,2]
    sensordata['q3'] = Q[:,3]
    
    # Debug plot - angular velocity and acceleration
    # fig = plt.figure(figsize=(10, 5))
    # ax1 = fig.add_subplot(2,1,1)
    # ax2 = fig.add_subplot(2,1,2)
    # ax1.plot(time,gyrX,c='r',linewidth=0.5)
    # ax1.plot(time,gyrY,c='g',linewidth=0.5)
    # ax1.plot(time,gyrZ,c='b',linewidth=0.5)
    # ax1.set_title("gyroscope")
    # ax1.set_xlabel("time (s)")
    # ax1.set_ylabel("angular velocity (degrees/s)")
    # ax1.legend(["x","y","z"])
    # ax2.plot(time,accX,c='r',linewidth=0.5)
    # ax2.plot(time,accY,c='g',linewidth=0.5)
    # ax2.plot(time,accZ,c='b',linewidth=0.5)
    # ax2.set_title("accelerometer")
    # ax2.set_xlabel("time (s)")
    # ax2.set_ylabel("acceleration (g)")
    # ax2.legend(["x","y","z"])
    # plt.show(block=False)
  
    return sensordata



def orientation_euler(sensordata):
    
    quat = np.array([sensordata[f'q{i}'] for i in range(4)]).T
    euler = np.zeros((1,3))
    for i in range(len(sensordata['q0'])):
        try:
            r = R.from_quat(quat[i])
            euler = np.vstack((euler, r.as_euler('xyz', degrees=True)))
        except:
            euler = np.vstack((euler, np.array([0,0,0])))   
    euler = euler[1:,:]
    
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
        qd = q_relative * q_fixed.conjugate
        qd = qd.normalised
    
        # Calculate Euler angles from this difference quaternion
        phi[j]   = np.rad2deg( math.atan2( 2 * (qd.w * qd.x + qd.y * qd.z), 1 - 2 * (qd.x**2 + qd.y**2) ) )
        theta[j] = np.rad2deg( math.asin ( 2 * (qd.w * qd.y - qd.z * qd.x) ) )
        psi[j]   = np.rad2deg( math.atan2( 2 * (qd.w * qd.z + qd.x * qd.y), 1 - 2 * (qd.y**2 + qd.z**2) ) )
    phi = phi.flatten()
    theta = theta.flatten()
    psi = psi.flatten()
    
    diffs_pos = np.argwhere(np.diff(phi)>90).flatten()
    diffs_neg = np.argwhere(np.diff(phi)<-90).flatten()
    if len(diffs_pos)>0 and len(diffs_neg)>0:
        if diffs_pos[0] < diffs_neg[0]:
            for i in range(len(diffs_pos)):
                try:
                    phi[diffs_pos[i]+1:diffs_neg[diffs_neg>diffs_pos[i]][0]+1] = phi[diffs_pos[i]+1:diffs_neg[diffs_neg>diffs_pos[i]][0]+1]-180
                except IndexError:
                    phi[diffs_pos[i]+1:] = phi[diffs_pos[i]+1:]-180
        elif diffs_neg[0] < diffs_pos[0]:
            for i in range(len(diffs_neg)):
                try:
                    phi[diffs_neg[i]+1:diffs_pos[diffs_pos>diffs_neg[i]][0]+1] = phi[diffs_neg[i]+1:diffs_pos[diffs_pos>diffs_neg[i]][0]+1]+180
                except IndexError:
                    phi[diffs_neg[i]+1:] = phi[diffs_neg[i]+1:]+180
    diffs_pos = np.argwhere(np.diff(phi)>90).flatten()
    diffs_neg = np.argwhere(np.diff(phi)<-90).flatten()
    if len(diffs_pos)>0 and len(diffs_neg)>0:
        if diffs_pos[0] < diffs_neg[0]:
            for i in range(len(diffs_pos)):
                try:
                    phi[diffs_pos[i]+1:diffs_neg[diffs_neg>diffs_pos[i]][0]+1] = phi[diffs_pos[i]+1:diffs_neg[diffs_neg>diffs_pos[i]][0]+1]-180
                except IndexError:
                    phi[diffs_pos[i]+1:] = phi[diffs_pos[i]+1:]-180
        elif diffs_neg[0] < diffs_pos[0]:
            for i in range(len(diffs_neg)):
                try:
                    phi[diffs_neg[i]+1:diffs_pos[diffs_pos>diffs_neg[i]][0]+1] = phi[diffs_neg[i]+1:diffs_pos[diffs_pos>diffs_neg[i]][0]+1]+180
                except IndexError:
                    phi[diffs_neg[i]+1:] = phi[diffs_neg[i]+1:]+180
    
    diffs_pos = np.argwhere(np.diff(theta)>90).flatten()
    diffs_neg = np.argwhere(np.diff(theta)<-90).flatten()
    if len(diffs_pos)>0 and len(diffs_neg)>0:
        if diffs_pos[0] < diffs_neg[0]:
            for i in range(len(diffs_pos)):
                try:
                    theta[diffs_pos[i]+1:diffs_neg[diffs_neg>diffs_pos[i]][0]+1] = theta[diffs_pos[i]+1:diffs_neg[diffs_neg>diffs_pos[i]][0]+1]-180
                except IndexError:
                    theta[diffs_pos[i]+1:] = theta[diffs_pos[i]+1:]-180
        elif diffs_neg[0] < diffs_pos[0]:
            for i in range(len(diffs_neg)):
                try:
                    theta[diffs_neg[i]+1:diffs_pos[diffs_pos>diffs_neg[i]][0]+1] = theta[diffs_neg[i]+1:diffs_pos[diffs_pos>diffs_neg[i]][0]+1]+180
                except IndexError:
                    theta[diffs_neg[i]+1:] = theta[diffs_neg[i]+1:]+180
    diffs_pos = np.argwhere(np.diff(theta)>90).flatten()
    diffs_neg = np.argwhere(np.diff(theta)<-90).flatten()
    if len(diffs_pos)>0 and len(diffs_neg)>0:
        if diffs_pos[0] < diffs_neg[0]:
            for i in range(len(diffs_pos)):
                try:
                    theta[diffs_pos[i]+1:diffs_neg[diffs_neg>diffs_pos[i]][0]+1] = theta[diffs_pos[i]+1:diffs_neg[diffs_neg>diffs_pos[i]][0]+1]-180
                except IndexError:
                    theta[diffs_pos[i]+1:] = theta[diffs_pos[i]+1:]-180
        elif diffs_neg[0] < diffs_pos[0]:
            for i in range(len(diffs_neg)):
                try:
                    theta[diffs_neg[i]+1:diffs_pos[diffs_pos>diffs_neg[i]][0]+1] = theta[diffs_neg[i]+1:diffs_pos[diffs_pos>diffs_neg[i]][0]+1]+180
                except IndexError:
                    theta[diffs_neg[i]+1:] = theta[diffs_neg[i]+1:]+180
    diffs_pos = np.argwhere(np.diff(psi)>90).flatten()
    diffs_neg = np.argwhere(np.diff(psi)<-90).flatten()
    if len(diffs_pos)>0 and len(diffs_neg)>0:
        if diffs_pos[0] < diffs_neg[0]:
            for i in range(len(diffs_pos)):
                try:
                    psi[diffs_pos[i]+1:diffs_neg[diffs_neg>diffs_pos[i]][0]+1] = psi[diffs_pos[i]+1:diffs_neg[diffs_neg>diffs_pos[i]][0]+1]-180
                except IndexError:
                    psi[diffs_pos[i]+1:] = psi[diffs_pos[i]+1:]-180
        elif diffs_neg[0] < diffs_pos[0]:
            for i in range(len(diffs_neg)):
                try:
                    psi[diffs_neg[i]+1:diffs_pos[diffs_pos>diffs_neg[i]][0]+1] = psi[diffs_neg[i]+1:diffs_pos[diffs_pos>diffs_neg[i]][0]+1]+180
                except IndexError:
                    psi[diffs_neg[i]+1:] = psi[diffs_neg[i]+1:]+180
    diffs_pos = np.argwhere(np.diff(psi)>90).flatten()
    diffs_neg = np.argwhere(np.diff(psi)<-90).flatten()
    if len(diffs_pos)>0 and len(diffs_neg)>0:
        if diffs_pos[0] < diffs_neg[0]:
            for i in range(len(diffs_pos)):
                try:
                    psi[diffs_pos[i]+1:diffs_neg[diffs_neg>diffs_pos[i]][0]+1] = psi[diffs_pos[i]+1:diffs_neg[diffs_neg>diffs_pos[i]][0]+1]-180
                except IndexError:
                    psi[diffs_pos[i]+1:] = psi[diffs_pos[i]+1:]-180
        elif diffs_neg[0] < diffs_pos[0]:
            for i in range(len(diffs_neg)):
                try:
                    psi[diffs_neg[i]+1:diffs_pos[diffs_pos>diffs_neg[i]][0]+1] = psi[diffs_neg[i]+1:diffs_pos[diffs_pos>diffs_neg[i]][0]+1]+180
                except IndexError:
                    psi[diffs_neg[i]+1:] = psi[diffs_neg[i]+1:]+180
    
    if np.mean(phi) < -150:
        phi = phi + 180
    if np.mean(theta) < -150:
        theta = theta + 180
    if np.mean(psi) < -150:
        psi = psi + 180
    if np.mean(phi) > 150:
        phi = phi - 180
    if np.mean(theta) > 150:
        theta = theta - 180
    if np.mean(psi) > 150:
        psi = psi - 180
        
    eulerx_relative_to = 'ex relative to '+ relative_to
    eulery_relative_to = 'ey relative to '+ relative_to
    eulerz_relative_to = 'ez relative to '+ relative_to
        
    sensorRelative[eulerx_relative_to] = phi
    sensorRelative[eulery_relative_to] = theta
    sensorRelative[eulerz_relative_to] = psi
    
    return sensorRelative