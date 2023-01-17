# -*- coding: utf-8 -*-
"""
Check output TrunkyXL sensors vs xsens sensors

@author: ensinkc
"""

import numpy as np
import pandas as pd
import os

def loadxsensdata(datafolder):
    for (dirpath, dirnames, filenames) in os.walk(datafolder):
                break
            
    for j in range(0, len(filenames)):
        
        if 'MT_' in filenames[j]:
            
            sensortype = 'xsens'
            
            if '00B40AC5' in filenames[j] or '00B47787' in filenames[j]:
                left_foot = '/' + filenames[j]
                left_data_file = datafolder + left_foot
            elif '00B40A23' in filenames[j] or '00B47796' in filenames[j]:
                right_foot = '/' + filenames[j]
                right_data_file = datafolder + right_foot
            elif '00B40A8D' in filenames[j] or '00B4778F' in filenames[j]:
                lumbar = '/' + filenames[j]
                lumbar_data_file = datafolder + lumbar
            elif '00B40ACF' in filenames[j] or '00B47783' in filenames[j]:
                left_ankle = '/' + filenames[j]
                left_ankle_data_file = datafolder + left_ankle
            elif '00B40AC7' in filenames[j] or '00B47792' in filenames[j]:
                right_ankle = '/' + filenames[j]
                right_ankle_data_file = datafolder + right_ankle
            elif '00B40A40' in filenames[j] or '00B47781' in filenames[j]:
                sternum = '/'+ filenames[j]
                sternum_data_file = datafolder + sternum
                    
    filepaths = {}
    try:
        filepaths['LeftFoot'] = left_data_file
    except:
        filepaths['LeftFoot'] = []
        
    try:
        filepaths['RightFoot'] = right_data_file
    except:
        filepaths['RightFoot'] = []
    
    try:
        filepaths['RightAnkle'] = right_ankle_data_file
    except:
        filepaths['RightAnkle'] = []
        
    try:
        filepaths['LeftAnkle'] = left_ankle_data_file
    except:
        filepaths['LeftAnkle'] = []
    
    try:
        filepaths['Lumbar'] = lumbar_data_file
    except:
        filepaths['Lumbar'] = []
        
    try:
        filepaths['Sternum'] = sternum_data_file
    except:
        filepaths['Sternum'] = []
                    
    # Define Sample Frequency (Hz)
    # Default
    sample_frequency = 100
    
    try:
        dataleft = pd.read_csv(filepaths['LeftFoot'], delimiter='\t', engine='python', skiprows = 12)
    except ValueError:
        dataleft = pd.DataFrame(columns=(['PacketCounter', 'SampleTimeFine', 'Acc_X', 'Acc_Y', 'Acc_Z', 'FreeAcc_E', 'FreeAcc_N', 'FreeAcc_U', 'Gyr_X', 'Gyr_Y', 'Gyr_Z',
                                          'Mag_X', 'Mag_Y', 'Mag_Z', 'VelInc_X', 'VelInc_Y', 'VelInc_Z', 'Quat_q0', 'Quat_q1', 'Quat_q2', 'Quat_q3', 'Roll', 'Pitch', 'Yaw']))
    try:
        dataright = pd.read_csv(filepaths['RightFoot'], delimiter='\t', engine='python', skiprows = 12)
    except ValueError:
        dataright = pd.DataFrame(columns=(['PacketCounter', 'SampleTimeFine', 'Acc_X', 'Acc_Y', 'Acc_Z', 'FreeAcc_E', 'FreeAcc_N', 'FreeAcc_U', 'Gyr_X', 'Gyr_Y', 'Gyr_Z',
                                          'Mag_X', 'Mag_Y', 'Mag_Z', 'VelInc_X', 'VelInc_Y', 'VelInc_Z', 'Quat_q0', 'Quat_q1', 'Quat_q2', 'Quat_q3', 'Roll', 'Pitch', 'Yaw']))
    try:
        dataleftankle = pd.read_csv(filepaths['LeftAnkle'], delimiter='\t', engine='python', skiprows = 12)
    except ValueError:
        dataleftankle = pd.DataFrame(columns=(['PacketCounter', 'SampleTimeFine', 'Acc_X', 'Acc_Y', 'Acc_Z', 'FreeAcc_E', 'FreeAcc_N', 'FreeAcc_U', 'Gyr_X', 'Gyr_Y', 'Gyr_Z',
                                          'Mag_X', 'Mag_Y', 'Mag_Z', 'VelInc_X', 'VelInc_Y', 'VelInc_Z', 'Quat_q0', 'Quat_q1', 'Quat_q2', 'Quat_q3', 'Roll', 'Pitch', 'Yaw']))
    try:
        datarightankle = pd.read_csv(filepaths['RightAnkle'], delimiter='\t', engine='python', skiprows = 12)
    except ValueError:
        datarightankle = pd.DataFrame(columns=(['PacketCounter', 'SampleTimeFine', 'Acc_X', 'Acc_Y', 'Acc_Z', 'FreeAcc_E', 'FreeAcc_N', 'FreeAcc_U', 'Gyr_X', 'Gyr_Y', 'Gyr_Z',
                                          'Mag_X', 'Mag_Y', 'Mag_Z', 'VelInc_X', 'VelInc_Y', 'VelInc_Z', 'Quat_q0', 'Quat_q1', 'Quat_q2', 'Quat_q3', 'Roll', 'Pitch', 'Yaw']))
    try:
        datalumbar = pd.read_csv(filepaths['Lumbar'], delimiter='\t', engine='python', skiprows = 12)
    except ValueError:
        datalumbar = pd.DataFrame(columns=(['PacketCounter', 'SampleTimeFine', 'Acc_X', 'Acc_Y', 'Acc_Z', 'FreeAcc_E', 'FreeAcc_N', 'FreeAcc_U', 'Gyr_X', 'Gyr_Y', 'Gyr_Z',
                                          'Mag_X', 'Mag_Y', 'Mag_Z', 'VelInc_X', 'VelInc_Y', 'VelInc_Z', 'Quat_q0', 'Quat_q1', 'Quat_q2', 'Quat_q3', 'Roll', 'Pitch', 'Yaw']))
    except KeyError:
        datalumbar = pd.DataFrame(columns=(['PacketCounter', 'SampleTimeFine', 'Acc_X', 'Acc_Y', 'Acc_Z', 'FreeAcc_E', 'FreeAcc_N', 'FreeAcc_U', 'Gyr_X', 'Gyr_Y', 'Gyr_Z',
                                          'Mag_X', 'Mag_Y', 'Mag_Z', 'VelInc_X', 'VelInc_Y', 'VelInc_Z', 'Quat_q0', 'Quat_q1', 'Quat_q2', 'Quat_q3', 'Roll', 'Pitch', 'Yaw']))
    try:
        datasternum = pd.read_csv(filepaths['Sternum'], delimiter='\t', engine='python', skiprows = 12)
    except ValueError:
        datasternum = pd.DataFrame(columns=(['PacketCounter', 'SampleTimeFine', 'Acc_X', 'Acc_Y', 'Acc_Z', 'FreeAcc_E', 'FreeAcc_N', 'FreeAcc_U', 'Gyr_X', 'Gyr_Y', 'Gyr_Z',
                                          'Mag_X', 'Mag_Y', 'Mag_Z', 'VelInc_X', 'VelInc_Y', 'VelInc_Z', 'Quat_q0', 'Quat_q1', 'Quat_q2', 'Quat_q3', 'Roll', 'Pitch', 'Yaw']))
    except KeyError:
        datasternum = pd.DataFrame(columns=(['PacketCounter', 'SampleTimeFine', 'Acc_X', 'Acc_Y', 'Acc_Z', 'FreeAcc_E', 'FreeAcc_N', 'FreeAcc_U', 'Gyr_X', 'Gyr_Y', 'Gyr_Z',
                                          'Mag_X', 'Mag_Y', 'Mag_Z', 'VelInc_X', 'VelInc_Y', 'VelInc_Z', 'Quat_q0', 'Quat_q1', 'Quat_q2', 'Quat_q3', 'Roll', 'Pitch', 'Yaw']))
        
    # Check if all sensors contain data
    missingsensors = []
    if len(dataleft) == 0:
        print('No left foot data available')
        missingsensors.append('LeftFoot')
    if len(dataright) == 0:
        print('No right foot data available')
        missingsensors.append('RightFoot')
    if len(dataleftankle) == 0:
        print('No left ankle data available')
        missingsensors.append('LeftAnkle')
    if len(datarightankle) == 0:
        print('No right ankle data available')
        missingsensors.append('RightAnkle')
    if len(datalumbar) == 0:
        print('No lumbar data available')
        missingsensors.append('Lumbar')
    if len(datasternum) == 0:
        print('No sternum data available')
        missingsensors.append('Sternum')
    
    
    # Find missing packets
    # allpackets = np.hstack((np.hstack((dataleft['PacketCounter'].to_numpy(), dataright['PacketCounter'].to_numpy())), np.hstack((datalumbar['PacketCounter'].to_numpy(), datasternum['PacketCounter'].to_numpy() )) ))
    packets = pd.DataFrame()
    if 'LeftFoot' not in missingsensors:
        packets = pd.concat([packets, dataleft['PacketCounter']])
    if 'RightFoot' not in missingsensors:
        packets = pd.concat([packets, dataright['PacketCounter']])
    if 'LeftAnkle' not in missingsensors:
        packets = pd.concat([packets, dataleftankle['PacketCounter']])
    if 'RightAnkle' not in missingsensors:
        packets = pd.concat([packets, datarightankle['PacketCounter']])
    if 'Lumbar' not in missingsensors:
        packets = pd.concat([packets, datalumbar['PacketCounter']])
    if 'Sternum' not in missingsensors:
        packets = pd.concat([packets, datasternum['PacketCounter']])
    allpacketslist = list(packets[0])
    
    # allpackets = pd.concat([dataleft['PacketCounter'], dataright['PacketCounter'], datalumbar['PacketCounter'], datasternum['PacketCounter']]).to_numpy()
    
    # allpacketslist = list(allpackets)
    # Sort packets
    allpacketslist.sort()
    # Constants Declaration
    missingpackets = np.array([])
    prev = -1
    count = 0
    
    # Iterating
    unique, counts = np.unique(allpacketslist, return_counts=True)
    count = dict(zip(unique, counts))
    for key in count:
        if count[key] < 4-len(missingsensors):
            missingpackets = np.append(missingpackets, key)
    print("Measurement " + str(filepaths['LeftFoot'][77:96]) +" contains " + str(len(missingpackets)) + " missing packets in available sensordata")
    
    # Remove missing packets
    dataleft = dataleft[~dataleft['PacketCounter'].isin(missingpackets)]
    dataright = dataright[~dataright['PacketCounter'].isin(missingpackets)]
    dataleftankle = dataleftankle[~dataleftankle['PacketCounter'].isin(missingpackets)]
    datarightankle = datarightankle[~datarightankle['PacketCounter'].isin(missingpackets)]
    datalumbar = datalumbar[~datalumbar['PacketCounter'].isin(missingpackets)]
    datasternum = datasternum[~datasternum['PacketCounter'].isin(missingpackets)]
    
    # Define sensordata
    ACCEFleft = (dataleft.filter(['FreeAcc_E','FreeAcc_N','FreeAcc_U'])).to_numpy()
    quaternionorientationleft = (dataleft.filter(['Quat_q0','Quat_q1','Quat_q2','Quat_q3'])).to_numpy()
    eulerorientationleft = (dataleft.filter(['Roll','Pitch','Yaw'])).to_numpy()
    ACCSFleft = (dataleft.filter(['Acc_X','Acc_Y','Acc_Z'])).to_numpy()
    GYRleft = (dataleft.filter(['Gyr_X','Gyr_Y','Gyr_Z'])).to_numpy()
    MAGleft = (dataleft.filter(['Mag_X','Mag_Y','Mag_Z'])).to_numpy()
    
    ACCEFright = (dataright.filter(['FreeAcc_E','FreeAcc_N','FreeAcc_U'])).to_numpy()
    quaternionorientationright = (dataright.filter(['Quat_q0','Quat_q1','Quat_q2','Quat_q3'])).to_numpy()
    eulerorientationright = (dataright.filter(['Roll','Pitch','Yaw'])).to_numpy()
    ACCSFright = (dataright.filter(['Acc_X','Acc_Y','Acc_Z'])).to_numpy()
    GYRright = (dataright.filter(['Gyr_X','Gyr_Y','Gyr_Z'])).to_numpy()
    MAGright = (dataright.filter(['Mag_X','Mag_Y','Mag_Z'])).to_numpy()
    
    ACCEFleftA = (dataleftankle.filter(['FreeAcc_E','FreeAcc_N','FreeAcc_U'])).to_numpy()
    quaternionorientationleftA = (dataleftankle.filter(['Quat_q0','Quat_q1','Quat_q2','Quat_q3'])).to_numpy()
    eulerorientationleftA = (dataleftankle.filter(['Roll','Pitch','Yaw'])).to_numpy()
    ACCSFleftA = (dataleftankle.filter(['Acc_X','Acc_Y','Acc_Z'])).to_numpy()
    GYRleftA = (dataleftankle.filter(['Gyr_X','Gyr_Y','Gyr_Z'])).to_numpy()
    MAGleftA = (dataleftankle.filter(['Mag_X','Mag_Y','Mag_Z'])).to_numpy()
    
    ACCEFrightA = (datarightankle.filter(['FreeAcc_E','FreeAcc_N','FreeAcc_U'])).to_numpy()
    quaternionorientationrightA = (datarightankle.filter(['Quat_q0','Quat_q1','Quat_q2','Quat_q3'])).to_numpy()
    eulerorientationrightA = (datarightankle.filter(['Roll','Pitch','Yaw'])).to_numpy()
    ACCSFrightA = (datarightankle.filter(['Acc_X','Acc_Y','Acc_Z'])).to_numpy()
    GYRrightA = (datarightankle.filter(['Gyr_X','Gyr_Y','Gyr_Z'])).to_numpy()
    MAGrightA = (datarightankle.filter(['Mag_X','Mag_Y','Mag_Z'])).to_numpy()
    
    ACCEFlumbar = (datalumbar.filter(['FreeAcc_E','FreeAcc_N','FreeAcc_U'])).to_numpy()
    quaternionorientationlumbar = (datalumbar.filter(['Quat_q0','Quat_q1','Quat_q2','Quat_q3'])).to_numpy()
    eulerorientationlumbar = (datalumbar.filter(['Roll','Pitch','Yaw'])).to_numpy()
    ACCSFlumbar = (datalumbar.filter(['Acc_X','Acc_Y','Acc_Z'])).to_numpy()
    GYRlumbar = (datalumbar.filter(['Gyr_X','Gyr_Y','Gyr_Z'])).to_numpy()
    MAGlumbar = (datalumbar.filter(['Mag_X','Mag_Y','Mag_Z'])).to_numpy()
    
    ACCEFsternum = (datasternum.filter(['FreeAcc_E','FreeAcc_N','FreeAcc_U'])).to_numpy()
    quaternionorientationsternum = (datasternum.filter(['Quat_q0','Quat_q1','Quat_q2','Quat_q3'])).to_numpy()
    eulerorientationsternum = (datasternum.filter(['Roll','Pitch','Yaw'])).to_numpy()
    ACCSFsternum = (datasternum.filter(['Acc_X','Acc_Y','Acc_Z'])).to_numpy()
    GYRsternum = (datasternum.filter(['Gyr_X','Gyr_Y','Gyr_Z'])).to_numpy()
    MAGsternum = (datasternum.filter(['Mag_X','Mag_Y','Mag_Z'])).to_numpy()
    
    # Define timestamp
    timestamp = np.array([0])
    for i in range(1,len(dataleft)):
        timestamp = np.append(timestamp, (timestamp[i-1]+1/sample_frequency))
    
    # Export data in a structured dictionary
    dataxsens={}
    dataxsens['Missing Sensors'] = missingsensors
    dataxsens['Timestamp'] = timestamp
    dataxsens['Sample Frequency (Hz)'] = sample_frequency
    dataxsens['Left shoulder'] = dict()
    dataxsens['Left shoulder']['raw'] = dict()
    dataxsens['Left shoulder']['raw']['Accelerometer Earth Frame'] = ACCEFleft
    dataxsens['Left shoulder']['raw']['Orientation Quaternion'] = quaternionorientationleft
    dataxsens['Left shoulder']['raw']['Orientation Euler'] = eulerorientationleft
    dataxsens['Left shoulder']['raw']['Accelerometer Sensor Frame'] = ACCSFleft
    dataxsens['Left shoulder']['raw']['Gyroscope'] = GYRleft
    dataxsens['Left shoulder']['raw']['Magnetometer'] = MAGleft
    dataxsens['Right shoulder'] = dict()
    dataxsens['Right shoulder']['raw'] = dict()
    dataxsens['Right shoulder']['raw']['Accelerometer Earth Frame'] = ACCEFright
    dataxsens['Right shoulder']['raw']['Orientation Quaternion'] = quaternionorientationright
    dataxsens['Right shoulder']['raw']['Orientation Euler'] = eulerorientationright
    dataxsens['Right shoulder']['raw']['Accelerometer Sensor Frame'] = ACCSFright
    dataxsens['Right shoulder']['raw']['Gyroscope'] = GYRright
    dataxsens['Right shoulder']['raw']['Magnetometer'] = MAGright
    dataxsens['Lumbar'] = dict()
    dataxsens['Lumbar']['raw'] = dict()
    dataxsens['Lumbar']['raw']['Accelerometer Earth Frame'] = ACCEFrightA
    dataxsens['Lumbar']['raw']['Orientation Quaternion'] = quaternionorientationrightA
    dataxsens['Lumbar']['raw']['Orientation Euler'] = eulerorientationrightA
    dataxsens['Lumbar']['raw']['Accelerometer Sensor Frame'] = ACCSFrightA
    dataxsens['Lumbar']['raw']['Gyroscope'] = GYRrightA
    dataxsens['Lumbar']['raw']['Magnetometer'] = MAGrightA
    dataxsens['Lower back'] = dict()
    dataxsens['Lower back']['raw'] = dict()
    dataxsens['Lower back']['raw']['Accelerometer Earth Frame'] = ACCEFlumbar
    dataxsens['Lower back']['raw']['Orientation Quaternion'] = quaternionorientationlumbar
    dataxsens['Lower back']['raw']['Orientation Euler'] = eulerorientationlumbar
    dataxsens['Lower back']['raw']['Accelerometer Sensor Frame'] = ACCSFlumbar
    dataxsens['Lower back']['raw']['Gyroscope'] = GYRlumbar
    dataxsens['Lower back']['raw']['Magnetometer'] = MAGlumbar
    dataxsens['Upper back'] = dict()
    dataxsens['Upper back']['raw'] = dict()
    dataxsens['Upper back']['raw']['Accelerometer Earth Frame'] = ACCEFsternum
    dataxsens['Upper back']['raw']['Orientation Quaternion'] = quaternionorientationsternum
    dataxsens['Upper back']['raw']['Orientation Euler'] = eulerorientationsternum
    dataxsens['Upper back']['raw']['Accelerometer Sensor Frame'] = ACCSFsternum
    dataxsens['Upper back']['raw']['Gyroscope'] = GYRsternum
    dataxsens['Upper back']['raw']['Magnetometer'] = MAGsternum
    
    return dataxsens

datafolderxsens = 'V:/research_reva_studies/807_TrunkyXL/II_Onderzoeksdata/Databestanden/Pilot metingen/20210913 2M - Xsens/xsens/exported000'
datafolder2M = 'V:/research_reva_studies/807_TrunkyXL/II_Onderzoeksdata/Databestanden/Pilot metingen/20210913 2M - Xsens/nodes/VenH_210913132906'
filepathsNodes = {}
filepathsNodes['Upper back'] = datafolder2M + '/Q/T/Sensor1.csv'
filepathsNodes['Lower back'] = datafolder2M + '/Q/T/Sensor2.csv'
filepathsNodes['Lumbar'] = datafolder2M + '/Q/T/Sensor3.csv'
filepathsNodes['Left shoulder']  = datafolder2M + '/Q/U/Sensor1.csv'
filepathsNodes['Right shoulder']  = datafolder2M + '/Q/V/Sensor1.csv'

dataxsens = loadxsensdata(datafolderxsens)
datanodes ={}
datanodes['Upper back'] = {}
datanodes['Upper back']['Orientation Quaternion'] = pd.read_csv(filepathsNodes['Upper back'], delimiter='\t', decimal=',', engine='python', skiprows = 1)
datanodes['Lower back'] = {}
datanodes['Lower back']['Orientation Quaternion'] = pd.read_csv(filepathsNodes['Lower back'], delimiter='\t', decimal=',', engine='python', skiprows = 1)
datanodes['Lumbar'] = {}
datanodes['Lumbar']['Orientation Quaternion'] = pd.read_csv(filepathsNodes['Lumbar'], delimiter='\t', decimal=',', engine='python', skiprows = 1)
datanodes['Left shoulder'] = {}
datanodes['Left shoulder']['Orientation Quaternion'] = pd.read_csv(filepathsNodes['Left shoulder'], delimiter='\t', decimal=',', engine='python', skiprows = 1)
datanodes['Right shoulder'] = {}
datanodes['Right shoulder']['Orientation Quaternion'] = pd.read_csv(filepathsNodes['Right shoulder'], delimiter='\t', decimal=',', engine='python', skiprows = 1)

datanodes['Upper back']['Orientation Quaternion'] = datanodes['Upper back']['Orientation Quaternion'][datanodes['Upper back']['Orientation Quaternion'].columns[-4:]].to_numpy() #-4:
datanodes['Lower back']['Orientation Quaternion'] =datanodes['Lower back']['Orientation Quaternion'][datanodes['Lower back']['Orientation Quaternion'].columns[-4:]].to_numpy()
datanodes['Lumbar']['Orientation Quaternion'] = datanodes['Lumbar']['Orientation Quaternion'][datanodes['Lumbar']['Orientation Quaternion'].columns[-4:]].to_numpy()
datanodes['Left shoulder']['Orientation Quaternion'] = datanodes['Left shoulder']['Orientation Quaternion'][datanodes['Left shoulder']['Orientation Quaternion'].columns[-4:]].to_numpy()
datanodes['Right shoulder']['Orientation Quaternion'] = datanodes['Right shoulder']['Orientation Quaternion'][datanodes['Right shoulder']['Orientation Quaternion'].columns[-4:]].to_numpy()

timenodes = np.array([0])
for i in range(1,len(datanodes['Right shoulder']['Orientation Quaternion'])):
    timenodes = np.append(timenodes, (timenodes[i-1]+1/20))

import matplotlib.pyplot as plt
plt.figure()
plt.plot(timenodes, datanodes['Upper back']['Orientation Quaternion'], linestyle='-.', label='Nodes')
plt.plot(dataxsens['Timestamp'], dataxsens['Upper back']['raw']['Orientation Quaternion'], linestyle='-', label='xsens')

plt.figure()
plt.plot(timenodes, datanodes['Lower back']['Orientation Quaternion'], linestyle='-.', label='Nodes')
plt.plot(dataxsens['Timestamp'], dataxsens['Lower back']['raw']['Orientation Quaternion'], linestyle='-', label='xsens')

plt.figure()
plt.plot(timenodes, datanodes['Lumbar']['Orientation Quaternion'], linestyle='-.', label='Nodes')
plt.plot(dataxsens['Timestamp'], dataxsens['Lumbar']['raw']['Orientation Quaternion'], linestyle='-', label='xsens')

from scipy.spatial.transform import Rotation as R
datanodes['Upper back']['Orientation Euler'] = np.zeros((1,3))
for i in range(0, len(datanodes['Upper back']['Orientation Quaternion'])):
    r = R.from_quat(datanodes['Upper back']['Orientation Quaternion'][i,:])
    datanodes['Upper back']['Orientation Euler'] = np.vstack((datanodes['Upper back']['Orientation Euler'], r.as_euler('xyz', degrees=True)))
datanodes['Upper back']['Orientation Euler'] = datanodes['Upper back']['Orientation Euler'][1:,:]
datanodes['Lower back']['Orientation Euler'] = np.zeros((1,3))
for i in range(0, len(datanodes['Lower back']['Orientation Quaternion'])):
    r = R.from_quat(datanodes['Lower back']['Orientation Quaternion'][i,:])
    datanodes['Lower back']['Orientation Euler'] = np.vstack((datanodes['Lower back']['Orientation Euler'], r.as_euler('zyx', degrees=True)))
datanodes['Lower back']['Orientation Euler'] = datanodes['Upper back']['Orientation Euler'][1:,:]
datanodes['Lumbar']['Orientation Euler'] = np.zeros((1,3))
for i in range(0, len(datanodes['Lumbar']['Orientation Quaternion'])):
    r = R.from_quat(datanodes['Lumbar']['Orientation Quaternion'][i,:])
    datanodes['Lumbar']['Orientation Euler'] = np.vstack((datanodes['Lumbar']['Orientation Euler'], r.as_euler('zyx', degrees=True)))
datanodes['Lumbar']['Orientation Euler'] = datanodes['Lumbar']['Orientation Euler'][1:,:]
datanodes['Left shoulder']['Orientation Euler'] = np.zeros((1,3))
for i in range(0, len(datanodes['Left shoulder']['Orientation Quaternion'])):
    r = R.from_quat(datanodes['Left shoulder']['Orientation Quaternion'][i,:])
    datanodes['Left shoulder']['Orientation Euler'] = np.vstack((datanodes['Left shoulder']['Orientation Euler'], r.as_euler('zyx', degrees=True)))
datanodes['Left shoulder']['Orientation Euler'] = datanodes['Left shoulder']['Orientation Euler'][1:,:]
datanodes['Right shoulder']['Orientation Euler'] = np.zeros((1,3))
for i in range(0, len(datanodes['Right shoulder']['Orientation Quaternion'])):
    r = R.from_quat(datanodes['Right shoulder']['Orientation Quaternion'][i,:])
    datanodes['Right shoulder']['Orientation Euler'] = np.vstack((datanodes['Right shoulder']['Orientation Euler'], r.as_euler('zyx', degrees=True)))
datanodes['Right shoulder']['Orientation Euler'] = datanodes['Right shoulder']['Orientation Euler'][1:,:]



plt.figure()
plt.plot(timenodes, (datanodes['Upper back']['Orientation Euler'][:,0]), linestyle='-.', color='red', label='Nodes')
plt.plot(dataxsens['Timestamp'], (dataxsens['Upper back']['raw']['Orientation Euler'][:,0]), linestyle='-', color='red', label='xsens')
plt.plot(timenodes, (datanodes['Upper back']['Orientation Euler'][:,1]), linestyle='-.', color='blue', label='Nodes')
plt.plot(dataxsens['Timestamp'], (dataxsens['Upper back']['raw']['Orientation Euler'][:,1]), linestyle='-', color='blue', label='xsens')
plt.plot(timenodes, (datanodes['Upper back']['Orientation Euler'][:,2]), linestyle='-.', color='green', label='Nodes')
plt.plot(dataxsens['Timestamp'], (dataxsens['Upper back']['raw']['Orientation Euler'][:,2]), linestyle='-', color='green', label='xsens')
plt.legend()








