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

from readmarkerdata import readmarkerdata


def correspondingfiles(folder):
    participants = os.listdir(folder)
    participants = [f for f in participants if ('807_pp' in f and 'ppxx' not in f)]
    
    foldersvicon = list()
    folderssensors = list()
    
    # Set subfolder for vicon data
    for p in participants:
        if "V:/research_reva_studies" in folder:
            sub = os.listdir( folder + '/' + p + '/' + 'Vicon')
            for s in sub:
                if os.path.isdir( folder + '/' + p + '/' + 'Vicon' + '/' + s) and (s.startswith("807") or s.startswith("PP")):
                    foldersvicon.append( folder + '/' + p + '/' + 'Vicon' + '/' + s + '/C3D_ZonderGaps_MetKinematica')
        else:
            foldersvicon.append( folder + '/' + p + '/' + 'Vicon')
    # Set subfolder for sensor data
    for p in participants:
        if 'QSense' in os.listdir( folder + '/' + p):
            folderssensors.append( folder + '/' + p + '/' + 'QSense')
        if 'Corpus' in os.listdir( folder + '/' + p):
            folderssensors.append( folder + '/' + p + '/' + 'Corpus')
    
    # Set corresponding filenames
    corresponding_files = dict()
        
    # 807_pp02
    corresponding_files['807_pp02'] = dict()
    # Validatie trial 1
    corresponding_files['807_pp02']['807_PP02M02.c3d'] = 'QSM_20230125165354'
    # Validatie trial 2
    corresponding_files['807_pp02']['807_PP02M03.c3d'] = 'QSM_20230125165508'
    # Validatie trial 3
    corresponding_files['807_pp02']['807_PP02M04.c3d'] = 'QSM_20230125165552'
    # # Manta snelheid normaal, gevoeligheid medium
    # corresponding_files['807_pp02']['807_PP02M05.c3d'] = '20230125170111'
    # # Manta snelheid normaal, gevoeligheid minimaal
    # corresponding_files['807_pp02']['807_PP02M06.c3d'] = '20230125170249'
    # # Shape sport rotatie
    # corresponding_files['807_pp02']['807_PP02M07.c3d'] = '20230125171120'
    # # Shape sport lateroflexie
    # corresponding_files['807_pp02']['807_PP02M08.c3d'] = '20230125171428'
    
    # 807_pp03
    corresponding_files['807_pp03'] = dict()
    # Validatie trial 1
    # corresponding_files['807_pp03']['807_PP03_M02.c3d'] = 'QSM_20230116122258' # Gimbal lock in senosrdata
    # Validatie trial 2
    # corresponding_files['807_pp03']['807_PP03_M03.c3d'] = 'QSM_20230116122428' # Gimbal lock in senosrdata
    # Validatie trial 3
    corresponding_files['807_pp03']['807_PP03_M04.c3d'] = 'QSM_20230116122532' 
    # # Manta snelheid normaal, gevoeligheid medium
    # corresponding_files['807_pp03']['807_PP03_M05.c3d'] = '20230116123321'
    # # Manta snelheid normaal, gevoeligheid minimaal
    # corresponding_files['807_pp03']['807_PP03_M06.c3d'] = '20230116123525'
    # # Shape sport rotatie
    # corresponding_files['807_pp03']['807_PP03_M07.c3d'] = '20230116124532'
    # # Shape sport lateroflexie
    # corresponding_files['807_pp03']['807_PP03_M08.c3d'] = '20230116124734'
            
    # 807_pp05
    corresponding_files['807_pp05'] = dict()
    # Validatie trial 1
    corresponding_files['807_pp05']['807_PP05_M01.c3d'] = 'QSM_20230116105902'
    # Validatie trial 2
    corresponding_files['807_pp05']['807_PP05_M02.c3d'] = 'QSM_20230116110402'
    # Validatie trial 3
    corresponding_files['807_pp05']['807_PP05_M03.c3d'] = 'QSM_20230116110514'
    # # Manta snelheid normaal, gevoeligheid medium
    # corresponding_files['807_pp05']['807_PP05_M04.c3d'] = '20230116111248'
    # # Manta snelheid normaal, gevoeligheid minimaal
    # corresponding_files['807_pp05']['807_PP05_M05.c3d'] = '20230116111448'
    # # Shape sport rotatie
    # corresponding_files['807_pp05']['807_PP05_M06.c3d'] = '20230116112309'
    # # Shape sport lateroflexie
    # corresponding_files['807_pp05']['807_PP05_M07.c3d'] = '20230116112409'
    
    # 807_pp06
    corresponding_files['807_pp06'] = dict()
    # Validatie trial 1
    corresponding_files['807_pp06']['807_PP06M01.c3d'] = 'QSM_20230201134952' # Sensordata bevat heel veel drift
    # # Validatie trial 2
    # corresponding_files['807_pp06']['807_PP06M02.c3d'] = 'QSM_20230201135053' # Sensordata bevat heel veel drift en een gimbal lock
    # Validatie trial 3
    corresponding_files['807_pp06']['807_PP06M03.c3d'] = 'QSM_20230201135221' # Sensordata bevat heel veel drift
    # # # Manta snelheid normaal, gevoeligheid medium
    # # corresponding_files['807_pp06']['807_PP06M04.c3d'] = '20230201140133' # Niet bruikbaar (Bericht webex Lise Wilders 10-3-2023)
    # # Manta snelheid normaal, gevoeligheid minimaal
    # corresponding_files['807_pp06']['807_PP06M05.c3d'] = '20230201140436'
    # # Shape sport rotatie
    # corresponding_files['807_pp06']['807_PP06M06.c3d'] = '20230201140943'
    # # Shape sport lateroflexie
    # corresponding_files['807_pp06']['807_PP06M07.c3d'] = '20230201141224'
    
    # 807_pp07
    corresponding_files['807_pp07'] = dict()
    # Validatie trial 1
    corresponding_files['807_pp07']['807_PP07M01.c3d'] = 'QSM_20230125152230'
    # Validatie trial 2
    corresponding_files['807_pp07']['807_PP07M02.c3d'] = 'QSM_20230125152352'
    # Validatie trial 3
    corresponding_files['807_pp07']['807_PP07M03.c3d'] = 'QSM_20230125152457'
    # # Manta snelheid normaal, gevoeligheid medium
    # corresponding_files['807_pp07']['807_PP07M04.c3d'] = '20230125153306'
    # # Manta snelheid normaal, gevoeligheid minimaal
    # corresponding_files['807_pp07']['807_PP07M05.c3d'] = '20230125153536'
    # # Shape sport rotatie
    # corresponding_files['807_pp07']['807_PP07M06.c3d'] = '20230125154047'
    # # Shape sport lateroflexie
    # corresponding_files['807_pp07']['807_PP07M07.c3d'] = '20230125154256'
    
    # 807_pp08
    corresponding_files['807_pp08'] = dict()
    # Validatie trial 1
    corresponding_files['807_pp08']['807_PP08M01.c3d'] = 'QSM_20230131104830'
    # Validatie trial 2
    corresponding_files['807_pp08']['807_PP08M02.c3d'] = 'QSM_20230131104933'
    # Validatie trial 3
    corresponding_files['807_pp08']['807_PP08M03.c3d'] = 'QSM_20230131105018'
    # # Manta snelheid normaal, gevoeligheid medium
    # corresponding_files['807_pp08']['807_PP08M04.c3d'] = '20230131105605'
    # # Manta snelheid normaal, gevoeligheid minimaal
    # corresponding_files['807_pp08']['807_PP08M05.c3d'] = '20230131105857'
    # # Manta snelheid normaal, gevoeligheid minimaal
    # corresponding_files['807_pp08']['807_PP08M06.c3d'] = '20230131110019'
    # # Shape sport rotatie
    # corresponding_files['807_pp08']['807_PP08M07.c3d'] = '20230131110621'
    # # Shape sport lateroflexie
    # corresponding_files['807_pp08']['807_PP08M08.c3d'] = '20230131110910'
    
    # NO DATA, NO SYNC PULSE
    # # 807_pp10
    # corresponding_files['807_pp10'] = dict()
    # # Validatie trial 1
    # corresponding_files['807_pp10']['807_PP10_M02.c3d'] = 'QSM_20230116084643' # Geen syncpulse!
    # # Validatie trial 2
    # corresponding_files['807_pp10']['807_PP10_M03.c3d'] = 'QSM_20230116084822' # Geen syncpulse!
    # # Validatie trial 3
    # corresponding_files['807_pp10']['807_PP10_M04.c3d'] = 'QSM_20230116084957' # Geen syncpulse!
    # # Manta snelheid normaal, gevoeligheid medium
    # corresponding_files['807_pp10']['807_PP10_M05.c3d'] = '20230116085944'
    # # Manta snelheid normaal, gevoeligheid minimaal
    # corresponding_files['807_pp10']['807_PP10_M07.c3d'] = '20230116090252'
    # # # Shape sport rotatie
    # # corresponding_files['807_pp10']['807_PP_M.c3d'] = '20230116090749'
    # # # Shape sport lateroflexie
    # # corresponding_files['807_pp10']['807_PP_M.c3d'] = '20230116091400'
    
    # 807_pp11
    corresponding_files['807_pp11'] = dict()
    # Validatie trial 1
    corresponding_files['807_pp11']['807_PP11_M01.c3d'] = 'QSM_20230131084952'
    # Validatie trial 2
    corresponding_files['807_pp11']['807_PP11_M02.c3d'] = 'QSM_20230131085242'
    # Validatie trial 3
    corresponding_files['807_pp11']['807_PP11_M03.c3d'] = 'QSM_20230131085350'
    # # Manta snelheid normaal, gevoeligheid medium
    # corresponding_files['807_pp11']['807_PP11_M04.c3d'] = '20230131090302'
    # # Manta snelheid normaal, gevoeligheid minimaal
    # corresponding_files['807_pp11']['807_PP11_M05.c3d'] = '20230131090605'
    # # Shape sport rotatie
    # corresponding_files['807_pp11']['807_PP11_M06.c3d'] = '20230131091255'
    # # Shape sport lateroflexie
    # corresponding_files['807_pp11']['807_PP11_M07.c3d'] = '20230131091511'
    
    # 807_pp12
    corresponding_files['807_pp12'] = dict()
    # Validatie trial 1
    corresponding_files['807_pp12']['807_PP12M01.c3d'] = 'QSM_20230125134809'
    # Validatie trial 2
    corresponding_files['807_pp12']['807_PP12M02.c3d'] = 'QSM_20230125134929'
    # Validatie trial 3
    corresponding_files['807_pp12']['807_PP12M03.c3d'] = 'QSM_20230125135023'
    # # Manta snelheid normaal, gevoeligheid medium
    # corresponding_files['807_pp12']['807_PP12M04.c3d'] = '20230125140230'
    # # Manta snelheid normaal, gevoeligheid minimaal
    # corresponding_files['807_pp12']['807_PP12M05.c3d'] = '20230125140447'
    # # Shape sport rotatie
    # corresponding_files['807_pp12']['807_PP12M06.c3d'] = '20230125141700'
    # # Shape sport lateroflexie
    # corresponding_files['807_pp12']['807_PP12M07.c3d'] = '20230125141927'
    
    # 807_pp13
    corresponding_files['807_pp13'] = dict()
    # Validatie trial 1
    corresponding_files['807_pp13']['807_PP13_M02.c3d'] = 'QSM_20230131094733'
    # Validatie trial 2
    corresponding_files['807_pp13']['807_PP13_M03.c3d'] = 'QSM_20230131094819'
    # Validatie trial 3
    corresponding_files['807_pp13']['807_PP13_M09.c3d'] = 'QSM_20230131101114'
    # # Manta snelheid normaal, gevoeligheid medium
    # corresponding_files['807_pp13']['807_PP13_M04.c3d'] = '20230131095838'
    # # Manta snelheid normaal, gevoeligheid minimaal
    # corresponding_files['807_pp13']['807_PP13_M05.c3d'] = '20230131100140'
    # # Manta snelheid normaal, gevoeligheid minimaal
    # corresponding_files['807_pp13']['807_PP13_M06.c3d'] = '20230131100308'
    # # Shape sport rotatie
    # corresponding_files['807_pp13']['807_PP13_M07.c3d'] = '20230131100612'
    # # Shape sport lateroflexie
    # corresponding_files['807_pp13']['807_PP13_M08.c3d'] = '20230131100810'
    
    # 807_pp14
    corresponding_files['807_pp14'] = dict()
    # Validatie trial 1
    corresponding_files['807_pp14']['807PP14_M02.c3d'] = 'QSM_20230125122243'
    # Validatie trial 2
    corresponding_files['807_pp14']['807PP14_M03.c3d'] = 'QSM_20230125122342'
    # Validatie trial 3
    # corresponding_files['807_pp14']['807PP14_M04.c3d'] = 'QSM_20230125122446' # Missing packets?
    # # Manta snelheid normaal, gevoeligheid medium
    # corresponding_files['807_pp14']['807PP14_M05.c3d'] = '20230125123150'
    # # Manta snelheid normaal, gevoeligheid minimaal
    # corresponding_files['807_pp14']['807PP14_M07.c3d'] = '20230125123609'
    # # Shape sport rotatie
    # corresponding_files['807_pp14']['807PP14_M08.c3d'] = '20230125124507'
    # # Shape sport lateroflexie
    # corresponding_files['807_pp14']['807PP14_M09.c3d'] = '20230125124702'
    
    # 807_pp15
    corresponding_files['807_pp15'] = dict()
    # Validatie trial 1
    # corresponding_files['807_pp15']['807_PP15_M01.c3d'] = 'QSM_20230116095507' # Missing packets?
    # Validatie trial 2
    # corresponding_files['807_pp15']['807_PP15_M02.c3d'] = 'QSM_20230116095612' # Missing packets?
    # Validatie trial 3
    corresponding_files['807_pp15']['807_PP15_M03.c3d'] = 'QSM_20230116095745'
    # # Manta snelheid normaal, gevoeligheid medium
    # corresponding_files['807_pp15']['807_PP15_M0.c3d'] = '20230116100603' # Niet bruikbaar
    # # Manta snelheid normaal, gevoeligheid minimaal
    # corresponding_files['807_pp15']['807_PP15_M0.c3d'] = '20230116100820' # Niet bruikbaar
    # # # Shape sport rotatie
    # # corresponding_files['807_pp15']['807_PP_M.c3d'] = '' # Niet bruikbaar
    # # # Shape sport lateroflexie
    # # corresponding_files['807_pp15']['807_PP_M.c3d'] = '' # Niet bruikbaar
    
    # 807_pp16
    corresponding_files['807_pp16'] = dict()
    # Validatie trial 1
    corresponding_files['807_pp16']['807_PP16M02.c3d'] = 'QSM_20230201122308' # Sensordata bevat heel veel drift
    # Validatie trial 2
    corresponding_files['807_pp16']['807_PP16M03.c3d'] = 'QSM_20230201122429' # Sensordata bevat heel veel drift
    # Validatie trial 3
    corresponding_files['807_pp16']['807_PP16M04.c3d'] = 'QSM_20230201122541' # Sensordata bevat heel veel drift
    # # Manta snelheid normaal, gevoeligheid medium
    # corresponding_files['807_pp16']['807_PP16M05.c3d'] = '20230201123301'
    # # Manta snelheid normaal, gevoeligheid minimaal
    # corresponding_files['807_pp16']['807_PP16M06.c3d'] = '20230201123721'
    # # Shape sport rotatie
    # corresponding_files['807_pp16']['807_PP16M07.c3d'] = '20230201124128'
    # # Shape sport lateroflexie
    # corresponding_files['807_pp16']['807_PP16M08.c3d'] = '20230201124344'
    
    # 807_pp17
    corresponding_files['807_pp17'] = dict()
    # Validatie trial 1
    corresponding_files['807_pp17']['807_PP17M01.c3d'] = 'QSM_20230201144642'
    # Validatie trial 2
    corresponding_files['807_pp17']['807_PP17M02.c3d'] = 'QSM_20230201144742'
    # Validatie trial 3
    corresponding_files['807_pp17']['807_PP17M03.c3d'] = 'QSM_20230201144835'
    # # Manta snelheid normaal, gevoeligheid medium
    # corresponding_files['807_pp17']['807_PP17M04.c3d'] = '20230201145502' # Niet bruikbaar
    # # Manta snelheid normaal, gevoeligheid minimaal
    # corresponding_files['807_pp17']['807_PP17M05.c3d'] = '20230201145749' # Niet bruikbaar
    # # Shape sport rotatie
    # corresponding_files['807_pp17']['807_PP17M06.c3d'] = '20230201150257'
    # # Shape sport lateroflexie
    # corresponding_files['807_pp17']['807_PP17M07.c3d'] = '20230201150549'    
    
    return corresponding_files, foldersvicon, folderssensors
    



def importvicondata (corresponding_files, foldersvicon):
    
    # Prepare datastructure
    vicon = dict()
    viconpath = list() 
    # Read markerdata vicon        
    for person in corresponding_files:
        for trial in corresponding_files[person]:
            try:
                p =[i for i in foldersvicon if person in i]
                if len(p)>0:
                    viconpath.append(p[0] + '/' + trial )
                print('Start import of vicon data of trial: ', trial)
                datavicon, VideoFrameRate, analog_data = readmarkerdata( viconpath[-1], analogdata=False )
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
            sensors[trial] = dict()
            sensors[trial]['Upper back'] = dict()
            sensors[trial]['Lower back'] = dict()
            sensors[trial]['Pelvis'] = dict()
            sensors[trial]['Software'] = ''
            
            
            if 'QSM_' in corresponding_files[person][trial]:
                tempfolder = [i for i in folderssensors if person in i and 'QSense' in i]
                sensortrialfolder = tempfolder[0] + '/' + corresponding_files[person][trial]
                sensors[trial]['Software'] = 'QSense Motion'
                backstring = '/R/Back'
                try:
                    print('Start import of sensor raw data of trial: ', trial)
                    sensors[trial]['Upper back']['raw'] = pd.read_csv(sensortrialfolder + backstring + '/Sensor 1.csv', delimiter='\t', decimal=',', engine='python', skiprows = 6, names=['ax','ay','az','gx','gy','gz','mx','my','mz','Reference'])
                    sensors[trial]['Lower back']['raw'] = pd.read_csv(sensortrialfolder + backstring + '/Sensor 2.csv', delimiter='\t', decimal=',', engine='python', skiprows = 6, names=['ax','ay','az','gx','gy','gz','mx','my','mz','Reference'])
                    sensors[trial]['Pelvis']['raw'] = pd.read_csv(sensortrialfolder + backstring + '/Sensor 3.csv', delimiter='\t', decimal=',', engine='python', skiprows = 6, names=['ax','ay','az','gx','gy','gz','mx','my','mz','Reference'])
                except:
                    # print('Sensor data of trial ', trial, ' cannot be imported')
                    try:
                        print('Start import of sensor quaternion data of trial: ', trial)
                        backstring = '/Q/Back'
                        sensors[trial]['Upper back']['raw'] = pd.read_csv(sensortrialfolder + backstring + '/Sensor 1.csv', delimiter='\t', decimal=',', engine='python', skiprows = 6, names=['q0', 'q1', 'q2', 'q3', 'Interference', 'Reference'])
                        sensors[trial]['Lower back']['raw'] = pd.read_csv(sensortrialfolder + backstring + '/Sensor 2.csv', delimiter='\t', decimal=',', engine='python', skiprows = 6, names=['q0', 'q1', 'q2', 'q3', 'Interference', 'Reference'])
                        sensors[trial]['Pelvis']['raw'] = pd.read_csv(sensortrialfolder + backstring + '/Sensor 3.csv', delimiter='\t', decimal=',', engine='python', skiprows = 6, names=['q0', 'q1', 'q2', 'q3', 'Interference', 'Reference'])
                    except:
                        print('Sensor data of trial ', trial, ' cannot be imported')
            
                sensors[trial]['sync start'] = 0
                sensors[trial]['sync stop'] = len(sensors[trial]['Upper back']['raw'])
            
            elif corresponding_files[person][trial].startswith('2023'):
                tempfolder = [i for i in folderssensors if person in i and 'Corpus' in i]
                sensortrialfolder = tempfolder[0] + '/' + corresponding_files[person][trial]
                print('Start import of sensor raw data of trial: ', trial)
                sensors[trial]['Software'] = 'Corpus'
                corpus = pd.read_csv(sensortrialfolder+'.csv', delimiter=',', decimal='.', engine='python', skiprows = 1, names=['Time','Body Part','Quaternion (x)','Quaternion (y)','Quaternion (z)','Quaternion (w)','Angles (x)','Angles (y)','Angles (z)'])
                # corpus_time = corpus['Time'][corpus['Time'].notnull()].reset_index(drop=True)
                corpus_head = corpus[corpus['Body Part'] == 'Head'].reset_index(drop=True)
                # corpus_head['Time'] = corpus_time
                corpus_head = corpus_head.rename({'Quaternion (x)': 'q0', 'Quaternion (y)': 'q1','Quaternion (z)': 'q2', 'Quaternion (w)': 'q3', 'Angles (x)': 'ex', 'Angles (y)': 'ey', 'Angles (z)': 'ez'}, axis='columns')
                corpus_UB = corpus[corpus['Body Part'] == 'UpperTrunk'].reset_index(drop=True)
                # corpus_UB['Time'] = corpus_time
                corpus_UB = corpus_UB.rename({'Quaternion (x)': 'q0', 'Quaternion (y)': 'q1','Quaternion (z)': 'q2', 'Quaternion (w)': 'q3', 'Angles (x)': 'ex', 'Angles (y)': 'ey', 'Angles (z)': 'ez'}, axis='columns')
                corpus_LB = corpus[corpus['Body Part'] == 'LowerTrunk'].reset_index(drop=True)
                # corpus_LB['Time'] = corpus_time
                corpus_LB = corpus_LB.rename({'Quaternion (x)': 'q0', 'Quaternion (y)': 'q1','Quaternion (z)': 'q2', 'Quaternion (w)': 'q3', 'Angles (x)': 'ex', 'Angles (y)': 'ey', 'Angles (z)': 'ez'}, axis='columns')
                corpus_P = corpus[corpus['Body Part'] == 'Hips'].reset_index(drop=True)
                # corpus_P['Time'] = corpus_time
                corpus_P = corpus_P.rename({'Quaternion (x)': 'q0', 'Quaternion (y)': 'q1','Quaternion (z)': 'q2', 'Quaternion (w)': 'q3', 'Angles (x)': 'ex', 'Angles (y)': 'ey', 'Angles (z)': 'ez'}, axis='columns')
                                
                sensors[trial]['Head'] = dict()
                sensors[trial]['Head']['raw'] = corpus_head.drop(columns=['Time', 'Body Part'])
                sensors[trial]['Upper back']['raw'] = corpus_UB.drop(columns=['Time', 'Body Part'])
                sensors[trial]['Lower back']['raw'] = corpus_LB.drop(columns=['Time', 'Body Part'])
                sensors[trial]['Pelvis']['raw'] = corpus_P.drop(columns=['Time', 'Body Part'])
                
                sensors[trial]['sync start'] = 0
                sensors[trial]['sync stop'] = len(sensors[trial]['Upper back']['raw'])
            else:
                print('Sensor data of trial ', trial, ' cannot be imported')
                
    return sensors



def resamplesensordata (sensors, vicon):
    # Define sample frequency
    for trial in sensors:
        if sensors[trial]['Software'] == 'QSense Motion':
            nviconsamples = len(vicon[trial]['LSpineAngles'])
            nsensorsamples = len(sensors[trial]['Upper back']['raw'])
            sensors[trial]['Fs'] = int(round(nsensorsamples/(nviconsamples/100),0))
        if sensors[trial]['Software'] == 'Corpus':
            nviconsamples = len(vicon[trial]['LSpineAngles'])
            nsensorsamples = len(sensors[trial]['Upper back']['raw'])
            sensors[trial]['Fs'] = 28 #25 #30
            
    # Create initial dataframe
    for trial in sensors:
        sensors[trial]['Upper back']['resampled'] = pd.DataFrame()
        sensors[trial]['Lower back']['resampled'] = pd.DataFrame()
        sensors[trial]['Pelvis']['resampled'] = pd.DataFrame()
        
        # Resample QSense Motion data
        if sensors[trial]['Software'] == 'QSense Motion':
            columns = ['ax', 'ay', 'az', 'gx', 'gy', 'gz', 'mx', 'my', 'mz']
            if 'PP17' in trial:
                columns = ['q0', 'q1', 'q2', 'q3']
            
            nviconsamples = len(vicon[trial]['LSpineAngles'])
            nsensorsamples = len(sensors[trial]['Upper back']['raw'])
            
            for col in columns:
                sensors[trial]['Upper back']['resampled'][col] = samplerate.resample(input_data=sensors[trial]['Upper back']['raw'][col][sensors[trial]['sync start']:sensors[trial]['sync stop']], ratio=(nviconsamples/nsensorsamples), converter_type='sinc_best') #100/sensors[trial]['Fs'], 'sinc_best')
            for col in columns:
                sensors[trial]['Lower back']['resampled'][col] = samplerate.resample(input_data=sensors[trial]['Lower back']['raw'][col][sensors[trial]['sync start']:sensors[trial]['sync stop']], ratio=(nviconsamples/nsensorsamples), converter_type='sinc_best') #100/sensors[trial]['Fs'], 'sinc_best')
            for col in columns: #sensors[trial]['Pelvis']['raw'].columns.values
                sensors[trial]['Pelvis']['resampled'][col] = samplerate.resample(input_data=sensors[trial]['Pelvis']['raw'][col][sensors[trial]['sync start']:sensors[trial]['sync stop']], ratio=(nviconsamples/nsensorsamples), converter_type='sinc_best') #100/sensors[trial]['Fs'], 'sinc_best')
            

            
        # Resample Corpus data
        elif sensors[trial]['Software'] == 'Corpus':
            columns = sensors[trial]['Pelvis']['raw'].columns.values #['', '', '', '', '', '']
        
            # try:
            for col in columns:
                sensors[trial]['Upper back']['resampled'][col] = samplerate.resample(input_data=sensors[trial]['Upper back']['raw'][col][sensors[trial]['sync start']:sensors[trial]['sync stop']], ratio=100/sensors[trial]['Fs'], converter_type='sinc_best')
            for col in columns:
                sensors[trial]['Lower back']['resampled'][col] = samplerate.resample(input_data=sensors[trial]['Lower back']['raw'][col][sensors[trial]['sync start']:sensors[trial]['sync stop']], ratio=100/sensors[trial]['Fs'], converter_type='sinc_best')
            for col in columns: #sensors[trial]['Pelvis']['raw'].columns.values
                sensors[trial]['Pelvis']['resampled'][col] = samplerate.resample(input_data=sensors[trial]['Pelvis']['raw'][col][sensors[trial]['sync start']:sensors[trial]['sync stop']], ratio=100/sensors[trial]['Fs'], converter_type='sinc_best')
            # except:
            #     pass
        
    return sensors



