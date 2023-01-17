"""
Validation study - TrunkyXL project
Sint Maartenskliniek study ID: 0900_Smarten_the_Clinic_V2

Author:         C.J. Ensink, c.ensink@maartenskliniek.nl
Last update:    10-01-2023

Functions for running the scripts for the validation study.
This file:
    - correspondingfiles
    - importvicondata
    - importsensordata
    - resamplesensordata

"""
# Import dependencies
import pandas as pd
import numpy as np
import os # Scan directories
import samplerate

from VICON_functions.readmarkerdata import readmarkerdata


def correspondingfiles(folder):
    participants = os.listdir(folder)
    participants = [f for f in participants if ('807_pp' in f and 'ppxx' not in f)]
    
    foldersvicon = list()
    folderssensors = list()
    
    # Set subfolder for vicon data
    for p in participants:
        sub = os.listdir( folder + '/' + p + '/' + 'Vicon')
        for s in sub:
            if os.path.isdir( folder + '/' + p + '/' + 'Vicon' + '/' + s):
                foldersvicon.append( folder + '/' + p + '/' + 'Vicon' + '/' + s )
    # Set subfolder for sensor data
    for p in participants:
        if 'Nodes' in os.listdir( folder + '/' + p):
            folderssensors.append( folder + '/' + p + '/' + 'Nodes')
        elif 'QSense' in os.listdir( folder + '/' + p):
            folderssensors.append( folder + '/' + p + '/' + 'QSense')
        if 'Corpus' in os.listdir( folder + '/' + p):
            folderssensors.append( folder + '/' + p + '/' + 'Corpus')
    
    # Set corresponding filenames
    corresponding_files = dict()
    # 807_pp01
    corresponding_files['807_pp01'] = dict()
    # Validatie trial 1
    corresponding_files['807_pp01']['807_PP01_01.c3d'] = 'VenH_210420094704'
    # Validatie trial 2
    corresponding_files['807_pp01']['807_PP01_02.c3d'] = 'VenH_210420095002'
    # Validatie trial 3
    corresponding_files['807_pp01']['807_PP01_03.c3d'] = 'VenH_210420095201'
    
    # 807_pp02
    corresponding_files['807_pp02'] = dict()
    # Validatie trial 1
    corresponding_files['807_pp02']['807_PP02_M02.c3d'] = 'VenH_210428161813'
    # Validatie trial 2
    corresponding_files['807_pp02']['807_PP02_M03.c3d'] = 'VenH_210428161911'
    # Validatie trial 3
    corresponding_files['807_pp02']['807_PP02_M04.c3d'] = 'VenH_210428162118'
    
    # 807_pp03
    corresponding_files['807_pp03'] = dict()
    # Validatie trial 1
    corresponding_files['807_pp03']['807_PP03_01.c3d'] = 'VenH_210512123445'
    # Validatie trial 2
    corresponding_files['807_pp03']['807_PP03_02.c3d'] = 'VenH_210512123652'
    # Validatie trial 3
    corresponding_files['807_pp03']['807_PP03_03.c3d'] = 'VenH_210512123830' 
    
    # 807_pp04
    corresponding_files['807_pp04'] = dict()
    # Validatie trial 1
    corresponding_files['807_pp04']['807_PP04M02.c3d'] = 'VenH_210602155343'
    # Validatie trial 2
    corresponding_files['807_pp04']['807_PP04M03.c3d'] = 'VenH_210602155526'
    # Validatie trial 3
    corresponding_files['807_pp04']['807_PP04M04.c3d'] = 'VenH_210602155721'
    # Validatie trial 4
    corresponding_files['807_pp04']['807_PP04M05.c3d'] = 'VenH_210602155832'
    # Validatie trial 5
    corresponding_files['807_pp04']['807_PP04M06.c3d'] = 'VenH_210602155923'
    # Validatie trial 6
    corresponding_files['807_pp04']['807_PP04M07.c3d'] = 'VenH_210602160113'
    # Validatie trial 7
    corresponding_files['807_pp04']['807_PP04M08.c3d'] = 'VenH_210602160344'
    # Validatie trial 8
    corresponding_files['807_pp04']['807_PP04M09.c3d'] = 'VenH_21060216045'
    # Validatie trial 9
    corresponding_files['807_pp04']['807_PP04M10.c3d'] = 'VenH_210602160600'
    # Validatie trial 10
    corresponding_files['807_pp04']['807_PP04M11.c3d'] = 'VenH_210602160652'
    
    # 807_pp05
    corresponding_files['807_pp05'] = dict()
    # Validatie trial 1
    corresponding_files['807_pp05']['807_PP05_M01.c3d'] = 'VenH_210621120344'
    # Validatie trial 2
    corresponding_files['807_pp05']['807_PP05_M02.c3d'] = 'VenH_210621120505'
    # Validatie trial 3
    corresponding_files['807_pp05']['807_PP05_M03.c3d'] = 'VenH_210621120721'
    
    # 807_pp06
    corresponding_files['807_pp06'] = dict()
    # Validatie trial 1
    corresponding_files['807_pp06']['807_PP06_M01.c3d'] = 'VenH_210623104645'
    # Validatie trial 2
    corresponding_files['807_pp06']['807_PP06_M02.c3d'] = 'VenH_210623104822'
    # Validatie trial 3
    corresponding_files['807_pp06']['807_PP06_M03.c3d'] = 'VenH_210623104914'
    
    # 807_pp07
    corresponding_files['807_pp07'] = dict()
    # Validatie trial 1
    corresponding_files['807_pp07']['807_PP07_M01.c3d'] = 'VenH_210702164038'
    # Validatie trial 2
    corresponding_files['807_pp07']['807_PP07_M03.c3d'] = 'VenH_210702164331'
    # Validatie trial 3
    corresponding_files['807_pp07']['807_PP07_M04.c3d'] = 'VenH_210702164758'
    
    return corresponding_files, foldersvicon, folderssensors
    



def importvicondata (corresponding_files, foldersvicon):
    
    # Prepare datastructure
    vicon = dict()
    viconpath = list() 
    # Read markerdata vicon        
    for person in corresponding_files:
        for trial in corresponding_files[person]:
            viconpath.append( [i for i in foldersvicon if person in i][0] + '/' + trial )
            try:
                print('Start import of vicon data of trial: ', trial)
                datavicon, VideoFrameRate = readmarkerdata( viconpath[-1], analogdata=False )
            except:
                print('Vicon data of trial ', trial, ' cannot be imported')
                datavicon = {}
    
            # Check the markernames
            for key in datavicon:
                if 'LASI' in key:
                    datavicon['LASI'] = datavicon[key]
                elif 'RASI' in key:
                    datavicon['RASI'] = datavicon[key]
                elif 'LPSI' in key:
                    datavicon['LPSI'] = datavicon[key]
                elif 'RPSI' in key:
                    datavicon['RPSI'] = datavicon[key]
                elif 'LPelvisAngles' in key:
                    datavicon['LPelvisAngles'] = datavicon[key]
                elif 'RPelvisAngles' in key:
                    datavicon['RPelvisAngles'] = datavicon[key]
                elif 'LSpineAngles' in key:
                    datavicon['LSpineAngles'] = datavicon[key]
                elif 'RSpineAngles' in key:
                    datavicon['RSpineAngles'] = datavicon[key]
                elif 'LThoraxAngles' in key:
                    datavicon['LThoraxAngles'] = datavicon[key]
                elif 'RThoraxAngles' in key:
                    datavicon['RThoraxAngles'] = datavicon[key]          
            
            vicon[trial] = datavicon
        
    return vicon
    
    


def importsensordata (corresponding_files, folderssensors):    
    
    # Prepare datastructure
    sensors = dict()
    
    for person in corresponding_files:
        for trial in corresponding_files[person]:
            sensortrialfolder = [i for i in folderssensors if person in i][0] + '/' + corresponding_files[person][trial]
            sensors[trial] = dict()
            sensors[trial]['Upper back'] = dict()
            sensors[trial]['Lower back'] = dict()
            sensors[trial]['Pelvis'] = dict()
            sensors[trial]['Software'] = ''
            
            
            if 'Nodes' in sensortrialfolder:
                sensors[trial]['Software'] = 'Nodes'
                # Check if there is raw data
                try:
                    print('Start import of sensor data of trial: ', trial)
                    backstring = '/R/T'
                    # Check outputformat Nodes raw data!
                    sensors[trial]['Upper back']['raw'] = pd.read_csv(sensortrialfolder + backstring + '/Sensor1.csv', delimiter='\t', decimal=',', engine='python', skiprows = 2, header=0, names=['q0', 'q1', 'q2', 'q3', 'q0r', 'q1r', 'q2r', 'q3r'])
                    sensors[trial]['Lower back']['raw'] = pd.read_csv(sensortrialfolder + backstring + '/Sensor2.csv', delimiter='\t', decimal=',', engine='python', skiprows = 2, header=0, names=['q0', 'q1', 'q2', 'q3', 'q0r', 'q1r', 'q2r', 'q3r'])
                    sensors[trial]['Pelvis']['raw'] = pd.read_csv(sensortrialfolder + backstring + '/Sensor3.csv', delimiter='\t', decimal=',', engine='python', skiprows = 2, header=0, names=['q0', 'q1', 'q2', 'q3', 'q0r', 'q1r', 'q2r', 'q3r'])
                # Otherwise check if there is orientation data
                except:
                    try:
                        print('Start import of sensor data of trial: ', trial)
                        backstring = '/Q/T'
                        sensors[trial]['Upper back']['raw'] = pd.read_csv(sensortrialfolder + backstring + '/Sensor1.csv', delimiter='\t', decimal=',', engine='python', skiprows = 2, header=0, names=['q0', 'q1', 'q2', 'q3', 'q0r', 'q1r', 'q2r', 'q3r'])
                        sensors[trial]['Lower back']['raw'] = pd.read_csv(sensortrialfolder + backstring + '/Sensor2.csv', delimiter='\t', decimal=',', engine='python', skiprows = 2, header=0, names=['q0', 'q1', 'q2', 'q3', 'q0r', 'q1r', 'q2r', 'q3r'])
                        sensors[trial]['Pelvis']['raw'] = pd.read_csv(sensortrialfolder + backstring + '/Sensor3.csv', delimiter='\t', decimal=',', engine='python', skiprows = 2, header=0, names=['q0', 'q1', 'q2', 'q3', 'q0r', 'q1r', 'q2r', 'q3r'])
                    except:
                        print('Sensor data of trial ', trial, ' cannot be imported')
                        sensors[trial]['Upper back']['raw'] = pd.DataFrame()
                        sensors[trial]['Lower back']['raw'] = pd.DataFrame()
                        sensors[trial]['Pelvis']['raw'] = pd.DataFrame()
                
                # Find sync pulses
                try:
                    # find row of [1 1 1 1] = sync start
                    syncstart = np.where([(sensors[trial]['Upper back']['q0'] ==1) & (sensors[trial]['Upper back']['q1'] ==1) & (sensors[trial]['Upper back']['q2'] ==1) & (sensors[trial]['Upper back']['q3']==1)][0] == True)[0]
                    # find row of [0 0 0 0] = sync stop
                    syncstop = np.where([(sensors[trial]['Upper back']['q0'] ==0) & (sensors[trial]['Upper back']['q1'] ==0) & (sensors[trial]['Upper back']['q2'] ==0) & (sensors[trial]['Upper back']['q3']==0)][0] == True)[0]
                except:
                    syncstart = 0
                    syncstop = len(sensors[trial]['Upper back']['raw'])
                sensors[trial]['sync start'] = syncstart
                sensors[trial]['sync stop'] = syncstop
                
            
            elif 'QSense' in sensortrialfolder:
                sensors[trial]['Software'] = 'QSense Motion'
                backstring = '/R/Back'
                try:
                    print('Start import of sensor data of trial: ', trial)
                    sensors[trial]['Upper back']['raw'] = pd.read_csv(sensortrialfolder + backstring + '/Sensor 1.csv', delimiter='\t', decimal=',', engine='python', skiprows = 6, names=['ax','ay','az','gx','gy','gz','mx','my','mz','Reference'])
                    sensors[trial]['Lower back']['raw'] = pd.read_csv(sensortrialfolder + backstring + '/Sensor 2.csv', delimiter='\t', decimal=',', engine='python', skiprows = 6, names=['ax','ay','az','gx','gy','gz','mx','my','mz','Reference'])
                    sensors[trial]['Pelvis']['raw'] = pd.read_csv(sensortrialfolder + backstring + '/Sensor 3.csv', delimiter='\t', decimal=',', engine='python', skiprows = 6, names=['ax','ay','az','gx','gy','gz','mx','my','mz','Reference'])
                except:
                    print('Sensor data of trial ', trial, ' cannot be imported')
            
                sensors[trial]['sync start'] = 0
                sensors[trial]['sync stop'] = len(sensors[trial]['Upper back']['raw'])
            
            elif 'Corpus' in sensortrialfolder:
                sensors[trial]['Software'] = 'Corpus'
                sensors[trial] = pd.read_csv(sensortrialfolder, delimiter=',', decimal='.', engine='python', skiprows = 1, names=['Time','Body Part','Quaternion (x)','Quaternion (y)','Quaternion (z)','Quaternion (w)','Angles (x)','Angles (y)','Angles (z)'])
    
    return sensors


def resamplesensordata (sensors, vicon):
    for trial in sensors:
        if sensors[trial]['Software'] == 'QSense Motion':
            sensors[trial]['Fs'] = 25

        elif sensors[trial]['Software'] == 'Nodes':
            try:
                nviconsamples = len(vicon[trial]['LSpineAngles'])
                nsensorsamples = sensors[trial]['sync stop']-sensors[trial]['sync start']
                sensors[trial]['Fs'] = int(nsensorsamples/(nviconsamples/100))
            except:
                nviconsamples = 1
                sensors[trial]['Fs'] = 25 #?
            
        
    for trial in sensors:
        sensors[trial]['Upper back']['resampled'] = pd.DataFrame()
        sensors[trial]['Lower back']['resampled'] = pd.DataFrame()
        sensors[trial]['Pelvis']['resampled'] = pd.DataFrame()
        if sensors[trial]['Software'] == 'Nodes':
            columns = ['q0', 'q1', 'q2', 'q3', 'q0r', 'q1r', 'q2r', 'q3r']
        elif sensors[trial]['Software'] == 'QSense':
            columns = ['ax', 'ay', 'az', 'gx', 'gy', 'gz', 'mx', 'my', 'mz']
        elif sensors[trial]['Software'] == 'Corpus':
            columns = sensors[trial]['Pelvis']['raw'].columns.values #['', '', '', '', '', '']
        
        try:
            for col in columns:
                sensors[trial]['Upper back']['resampled'][col] = samplerate.resample(sensors[trial]['Upper back']['raw'][col][sensors[trial]['sync start']:sensors[trial]['sync stop']], 100/sensors[trial]['Fs'], 'sinc_best')
            for col in columns:
                sensors[trial]['Lower back']['resampled'][col] = samplerate.resample(sensors[trial]['Lower back']['raw'][col][sensors[trial]['sync start']:sensors[trial]['sync stop']], 100/sensors[trial]['Fs'], 'sinc_best')
            for col in columns: #sensors[trial]['Pelvis']['raw'].columns.values
                sensors[trial]['Pelvis']['resampled'][col] = samplerate.resample(sensors[trial]['Pelvis']['raw'][col][sensors[trial]['sync start']:sensors[trial]['sync stop']], 100/sensors[trial]['Fs'], 'sinc_best')
        except:
            pass
    
    return sensors



