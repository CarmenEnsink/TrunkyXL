# -*- coding: utf-8 -*-
"""
Trunky data, Nodes application

Author: CJ Ensink

"""
import pandas as pd
from VICON_functions.readmarkerdata import readmarkerdata
import matplotlib.pyplot as plt
import numpy as np
import samplerate

sensor1 = pd.read_csv('C:/Users/ensinkc.SMK/OneDrive - Sint Maartenskliniek/Documents/02. VR4REHAB/TrunkyXL/pp/807_pp00/Nodes/VenH_210406104317/Q/T/Sensor1.csv', delimiter='\t', decimal=',', engine='python', skiprows = 2, header=0, names=['q0', 'q1', 'q2', 'q3', 'q0r', 'q1r', 'q2r', 'q3r'])
sensor2 = pd.read_csv('C:/Users/ensinkc.SMK/OneDrive - Sint Maartenskliniek/Documents/02. VR4REHAB/TrunkyXL/pp/807_pp00/Nodes/VenH_210406104317/Q/T/Sensor2.csv', delimiter='\t', decimal=',', engine='python', skiprows = 2, header=0, names=['q0', 'q1', 'q2', 'q3', 'q0r', 'q1r', 'q2r', 'q3r'])
sensor3 = pd.read_csv('C:/Users/ensinkc.SMK/OneDrive - Sint Maartenskliniek/Documents/02. VR4REHAB/TrunkyXL/pp/807_pp00/Nodes/VenH_210406104317/Q/T/Sensor3.csv', delimiter='\t', decimal=',', engine='python', skiprows = 2, header=0, names=['q0', 'q1', 'q2', 'q3', 'q0r', 'q1r', 'q2r', 'q3r'])

# find row of [1 1 1 1] = sync start
syncstart = np.where([(sensor1['q0'] ==1) & (sensor1['q1'] ==1) & (sensor1['q2'] ==1) & (sensor1['q3']==1)][0] == True)[0]
# find row of [0 0 0 0] = sync stop
syncstop = np.where([(sensor1['q0'] ==0) & (sensor1['q1'] ==0) & (sensor1['q2'] ==0) & (sensor1['q3']==0)][0] == True)[0]
nsensorsamples = syncstop-syncstart

datavicon, ParameterGroup, VideoFrameRate = readmarkerdata( 'C:/Users/ensinkc.SMK/OneDrive - Sint Maartenskliniek/Documents/02. VR4REHAB/TrunkyXL/pp/807_pp00/Vicon/807_PP00_Trial2_01.c3d' )
nviconsamples = len(datavicon['LSpineAngles'])


sensor1resamp = pd.DataFrame(columns=(['q0', 'q1', 'q2', 'q3', 'q0r', 'q1r', 'q2r', 'q3r']))
sensor2resamp = pd.DataFrame(columns=(['q0', 'q1', 'q2', 'q3', 'q0r', 'q1r', 'q2r', 'q3r']))
sensor3resamp = pd.DataFrame(columns=(['q0', 'q1', 'q2', 'q3', 'q0r', 'q1r', 'q2r', 'q3r']))

wrongfs = int(nsensorsamples/(nviconsamples/100))
for key in sensor1:
    sensor1resamp[key] = samplerate.resample(sensor1[key][syncstart[0]:syncstop[0]], 100/wrongfs, 'sinc_best')
for key in sensor2:
    sensor2resamp[key] = samplerate.resample(sensor2[key][syncstart[0]:syncstop[0]], 100/wrongfs, 'sinc_best') 
for key in sensor3:
    sensor3resamp[key] = samplerate.resample(sensor3[key][syncstart[0]:syncstop[0]], 100/wrongfs, 'sinc_best') 
    
from scipy.spatial.transform import Rotation as R
eulersensor1 = np.zeros((1,3))
for i in range(0, len(sensor1resamp)):
    r = R.from_quat([sensor1resamp['q0'][i],sensor1resamp['q1'][i],sensor1resamp['q2'][i],sensor1resamp['q3'][i]])
    eulersensor1 = np.vstack((eulersensor1, r.as_euler('xyz', degrees=True)))
eulersensor1 = eulersensor1[1:,:]


fig, ax = plt.subplots(nrows=3, ncols=1)
# plt.plot(sensor1resamp['q0'])
# plt.plot(sensor1resamp['q1'])
# plt.plot(sensor1resamp['q2'])
# plt.plot(sensor1resamp['q3'])

ax[0].plot(np.unwrap(eulersensor1[:,0]) - np.mean(np.unwrap(eulersensor1[:,0])), label='x')
ax[1].plot(np.unwrap(eulersensor1[:,1]) - np.mean(np.unwrap(eulersensor1[:,1])), label='y')
ax[2].plot(np.unwrap(eulersensor1[:,2]) - np.mean(np.unwrap(eulersensor1[:,2])), label='z')

ax[0].plot(datavicon['LSpineAngles'][:,0], label='vicon x')
ax[1].plot(datavicon['LSpineAngles'][:,1], label='vicon y')
ax[2].plot(datavicon['LSpineAngles'][:,2], label='vicon z')

ax[0].legend()
ax[1].legend()
ax[2].legend()

