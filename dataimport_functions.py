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
        if 'QSense' in os.listdir( folder + '/' + p):
            folderssensors.append( folder + '/' + p + '/' + 'QSense')
        # elif 'Nodes' in os.listdir( folder + '/' + p):
        #     folderssensors.append( folder + '/' + p + '/' + 'Nodes')
        if 'Corpus' in os.listdir( folder + '/' + p):
            folderssensors.append( folder + '/' + p + '/' + 'Corpus')
    
    # Set corresponding filenames
    corresponding_files = dict()
        
    # # 807_pp02
    # corresponding_files['807_pp02'] = dict()
    # # Validatie trial 1
    # corresponding_files['807_pp02']['807_PP02_M02.c3d'] = ''
    # # Validatie trial 2
    # corresponding_files['807_pp02']['807_PP02_M03.c3d'] = ''
    # # Validatie trial 3
    # corresponding_files['807_pp02']['807_PP02_M04.c3d'] = ''
    
    # 807_pp03
    corresponding_files['807_pp03'] = dict()
    # Validatie trial 1
    corresponding_files['807_pp03']['807_PP03_M02.c3d'] = 'QSM_20230116122258'
    # Validatie trial 2
    corresponding_files['807_pp03']['807_PP03_M03.c3d'] = 'QSM_20230116122428'
    # Validatie trial 3
    corresponding_files['807_pp03']['807_PP03_M04.c3d'] = 'QSM_20230116122532' 
    # # Manta snelheid normaal, gevoeligheid medium
    # corresponding_files['807_pp03']['807_PP03_M05.c3d'] = ''
    # # Manta snelheid normaal, gevoeligheid minimaal
    # corresponding_files['807_pp03']['807_PP03_M06.c3d'] = ''
    # # Shape sport rotatie
    # corresponding_files['807_pp03']['807_PP03_M07.c3d'] = ''
    # # Shape sport lateroflexie
    # corresponding_files['807_pp03']['807_PP03_M08.c3d'] = ''
            
    # # 807_pp04
    # corresponding_files['807_pp04'] = dict()
    # # Validatie trial 1
    # corresponding_files['807_pp04']['807_PP04M01.c3d'] = ''
    # # Validatie trial 2
    # corresponding_files['807_pp04']['807_PP04M02.c3d'] = ''
    # # Validatie trial 3
    # corresponding_files['807_pp04']['807_PP04M03.c3d'] = ''
    
    # 807_pp05
    corresponding_files['807_pp05'] = dict()
    # Validatie trial 1
    corresponding_files['807_pp05']['807_PP05_M01.c3d'] = 'QSM_20230116105902'
    # Validatie trial 2
    corresponding_files['807_pp05']['807_PP05_M02.c3d'] = 'QSM_20230116110402'
    # Validatie trial 3
    corresponding_files['807_pp05']['807_PP05_M03.c3d'] = 'QSM_20230116110514'
    # # Manta snelheid normaal, gevoeligheid medium
    # corresponding_files['807_pp03']['807_PP05_M04.c3d'] = ''
    # # Manta snelheid normaal, gevoeligheid minimaal
    # corresponding_files['807_pp03']['807_PP05_M05.c3d'] = ''
    # # Shape sport rotatie
    # corresponding_files['807_pp03']['807_PP05_M06.c3d'] = ''
    # # Shape sport lateroflexie
    # corresponding_files['807_pp03']['807_PP05_M07.c3d'] = ''
    
    # # 807_pp06
    # corresponding_files['807_pp06'] = dict()
    # # Validatie trial 1
    # corresponding_files['807_pp06']['807_PP06_M01.c3d'] = ''
    # # Validatie trial 2
    # corresponding_files['807_pp06']['807_PP06_M02.c3d'] = ''
    # # Validatie trial 3
    # corresponding_files['807_pp06']['807_PP06_M03.c3d'] = ''
    
    # # 807_pp07
    # corresponding_files['807_pp07'] = dict()
    # # Validatie trial 1
    # corresponding_files['807_pp07']['807_PP07_M01.c3d'] = ''
    # # Validatie trial 2
    # corresponding_files['807_pp07']['807_PP07_M02.c3d'] = ''
    # # Validatie trial 3
    # corresponding_files['807_pp07']['807_PP07_M03.c3d'] = ''
    
    # 807_pp10
    corresponding_files['807_pp10'] = dict()
    # Validatie trial 1
    corresponding_files['807_pp10']['807_PP10_M02.c3d'] = 'QSM_20230116084643' # Geen syncpulse!
    # Validatie trial 2
    corresponding_files['807_pp10']['807_PP10_M03.c3d'] = 'QSM_20230116084822' # Geen syncpulse!
    # Validatie trial 3
    corresponding_files['807_pp10']['807_PP10_M04.c3d'] = 'QSM_20230116084957' # Geen syncpulse!
    # # Manta snelheid normaal, gevoeligheid medium
    # corresponding_files['807_pp10']['807_PP10_M05.c3d'] = ''
    # # Manta snelheid normaal, gevoeligheid minimaal
    # corresponding_files['807_pp10']['807_PP10_M07.c3d'] = ''
    # # # Shape sport rotatie
    # # corresponding_files['807_pp10']['807_PP_M.c3d'] = ''
    # # # Shape sport lateroflexie
    # # corresponding_files['807_pp10']['807_PP_M.c3d'] = ''
    
    # 807_pp15
    corresponding_files['807_pp15'] = dict()
    # Validatie trial 1
    corresponding_files['807_pp15']['807_PP15_M01.c3d'] = 'QSM_20230116095507'
    # Validatie trial 2
    corresponding_files['807_pp15']['807_PP15_M02.c3d'] = 'QSM_20230116095612'
    # Validatie trial 3
    corresponding_files['807_pp15']['807_PP15_M03.c3d'] = 'QSM_20230116095745'
    # # Manta snelheid normaal, gevoeligheid medium
    # corresponding_files['807_pp15']['807_PP15_M04.c3d'] = ''
    # # Manta snelheid normaal, gevoeligheid minimaal
    # corresponding_files['807_pp15']['807_PP15_M05.c3d'] = ''
    # # # Shape sport rotatie
    # # corresponding_files['807_pp15']['807_PP_M.c3d'] = ''
    # # # Shape sport lateroflexie
    # # corresponding_files['807_pp15']['807_PP_M.c3d'] = ''
    
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
            
            
            if 'QSense' in sensortrialfolder:
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
            
            # elif 'Nodes' in sensortrialfolder:
            #     sensors[trial]['Software'] = 'Nodes'
            #     # Check if there is raw data
            #     try:
            #         print('Start import of sensor data of trial: ', trial)
            #         backstring = '/R/T'
            #         # Check outputformat Nodes raw data!
            #         sensors[trial]['Upper back']['raw'] = pd.read_csv(sensortrialfolder + backstring + '/Sensor1.csv', delimiter='\t', decimal=',', engine='python', skiprows = 2, header=0, names=['q0', 'q1', 'q2', 'q3', 'q0r', 'q1r', 'q2r', 'q3r'])
            #         sensors[trial]['Lower back']['raw'] = pd.read_csv(sensortrialfolder + backstring + '/Sensor2.csv', delimiter='\t', decimal=',', engine='python', skiprows = 2, header=0, names=['q0', 'q1', 'q2', 'q3', 'q0r', 'q1r', 'q2r', 'q3r'])
            #         sensors[trial]['Pelvis']['raw'] = pd.read_csv(sensortrialfolder + backstring + '/Sensor3.csv', delimiter='\t', decimal=',', engine='python', skiprows = 2, header=0, names=['q0', 'q1', 'q2', 'q3', 'q0r', 'q1r', 'q2r', 'q3r'])
            #     # Otherwise check if there is orientation data
            #     except:
            #         try:
            #             print('Start import of sensor data of trial: ', trial)
            #             backstring = '/Q/T'
            #             sensors[trial]['Upper back']['raw'] = pd.read_csv(sensortrialfolder + backstring + '/Sensor1.csv', delimiter='\t', decimal=',', engine='python', skiprows = 2, header=0, names=['q0', 'q1', 'q2', 'q3', 'q0r', 'q1r', 'q2r', 'q3r'])
            #             sensors[trial]['Lower back']['raw'] = pd.read_csv(sensortrialfolder + backstring + '/Sensor2.csv', delimiter='\t', decimal=',', engine='python', skiprows = 2, header=0, names=['q0', 'q1', 'q2', 'q3', 'q0r', 'q1r', 'q2r', 'q3r'])
            #             sensors[trial]['Pelvis']['raw'] = pd.read_csv(sensortrialfolder + backstring + '/Sensor3.csv', delimiter='\t', decimal=',', engine='python', skiprows = 2, header=0, names=['q0', 'q1', 'q2', 'q3', 'q0r', 'q1r', 'q2r', 'q3r'])
            #         except:
            #             print('Sensor data of trial ', trial, ' cannot be imported')
            #             sensors[trial]['Upper back']['raw'] = pd.DataFrame()
            #             sensors[trial]['Lower back']['raw'] = pd.DataFrame()
            #             sensors[trial]['Pelvis']['raw'] = pd.DataFrame()
                
            #     # Find sync pulses
            #     try:
            #         # find row of [1 1 1 1] = sync start
            #         syncstart = np.where([(sensors[trial]['Upper back']['q0'] ==1) & (sensors[trial]['Upper back']['q1'] ==1) & (sensors[trial]['Upper back']['q2'] ==1) & (sensors[trial]['Upper back']['q3']==1)][0] == True)[0]
            #         # find row of [0 0 0 0] = sync stop
            #         syncstop = np.where([(sensors[trial]['Upper back']['q0'] ==0) & (sensors[trial]['Upper back']['q1'] ==0) & (sensors[trial]['Upper back']['q2'] ==0) & (sensors[trial]['Upper back']['q3']==0)][0] == True)[0]
            #     except:
            #         syncstart = 0
            #         syncstop = len(sensors[trial]['Upper back']['raw'])
            #     sensors[trial]['sync start'] = syncstart
            #     sensors[trial]['sync stop'] = syncstop
    
    return sensors


def resamplesensordata (sensors):
    for trial in sensors:
        if sensors[trial]['Software'] == 'QSense Motion':
            sensors[trial]['Fs'] = 25

        # elif sensors[trial]['Software'] == 'Nodes':
        #     try:
        #         nviconsamples = len(vicon[trial]['LSpineAngles'])
        #         nsensorsamples = sensors[trial]['sync stop']-sensors[trial]['sync start']
        #         sensors[trial]['Fs'] = int(nsensorsamples/(nviconsamples/100))
        #     except:
        #         nviconsamples = 1
        #         sensors[trial]['Fs'] = 25 #?
            
        
    for trial in sensors:
        sensors[trial]['Upper back']['resampled'] = pd.DataFrame()
        sensors[trial]['Lower back']['resampled'] = pd.DataFrame()
        sensors[trial]['Pelvis']['resampled'] = pd.DataFrame()
        
        if sensors[trial]['Software'] == 'QSense Motion':
            columns = ['ax', 'ay', 'az', 'gx', 'gy', 'gz', 'mx', 'my', 'mz']
        elif sensors[trial]['Software'] == 'Corpus':
            columns = sensors[trial]['Pelvis']['raw'].columns.values #['', '', '', '', '', '']
        # elif sensors[trial]['Software'] == 'Nodes':
        #     columns = ['q0', 'q1', 'q2', 'q3', 'q0r', 'q1r', 'q2r', 'q3r']
            
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



