# -*- coding: utf-8 -*-
"""
Sint Maartenskliniek study ID: 807_TrunkyXL
    Script for validation of TrunkyXL sensordata against optical motion capture

Last update:
    22-09-2022: C.J. Ensink, c.ensink@maartenskliniek.nl
    
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from sensor_analysis_functions import orientation_estimation, orientation_euler, relative_orientation
from dataimport_functions import correspondingfiles, importvicondata, importsensordata, resamplesensordata

folder = 'V:/research_reva_studies/807_TrunkyXL/II_Onderzoeksdata/Databestanden'
# folder = 'C:/Users/ensinkc.SMK/OneDrive - Sint Maartenskliniek/Documents/02. VR4REHAB/TrunkyXL/pp/807_pp00/Nodes/VenH_210406104317'

# data = dict()
# data['Upper back'] = pd.read_csv(folder+'/Q/T/Sensor1.csv', delimiter='\t', decimal=',', engine='python', skiprows = 2, header=0, names=['q0', 'q1', 'q2', 'q3', 'q0r', 'q1r', 'q2r', 'q3r'])
# data['Lower back'] = pd.read_csv(folder+'/Q/T/Sensor2.csv', delimiter='\t', decimal=',', engine='python', skiprows = 2, header=0, names=['q0', 'q1', 'q2', 'q3', 'q0r', 'q1r', 'q2r', 'q3r'])
# data['Pelvis'] = pd.read_csv(folder+'/Q/T/Sensor3.csv', delimiter='\t', decimal=',', engine='python', skiprows = 2, header=0, names=['q0', 'q1', 'q2', 'q3', 'q0r', 'q1r', 'q2r', 'q3r'])


corresponding_files, foldersvicon, folderssensors = correspondingfiles(folder)
# corresponding_files = dict()
# corresponding_files['807_pilot']=dict()
# corresponding_files['807_pilot']['Qsense01.c3d'] = 'QSM_20220929092537'
# corresponding_files['807_pilot']['Shape01.c3d'] = '20220929094618.csv'
# foldersvicon = list()
# foldersvicon.append('V:/research_reva_studies/807_TrunkyXL/II_Onderzoeksdata/Databestanden/Pilot metingen/807_pilot_20220929/Vicon/Pilot09/20220929')
# folderssensors = list()
# folderssensors.append('V:/research_reva_studies/807_TrunkyXL/II_Onderzoeksdata/Databestanden/Pilot metingen/807_pilot_20220929/QSense') #Corpus

vicon = importvicondata (corresponding_files, foldersvicon)
sensors = importsensordata (corresponding_files, folderssensors)
sensors = resamplesensordata (sensors)

for trial in sensors:
    if len(sensors[trial]['Pelvis']['resampled']) >= 3:
        # if '807_PP01' in trial or '807_PP02' in trial or '807_PP03' in trial or '807_PP04' in trial or '807_PP05' in trial or '807_PP06' in trial or '807_PP07' in trial:
        #     # Data captured with Nodes software
        #     # fs_nodes = 20 #?
        #     sensors[trial]['Pelvis']['resampled'] = orientation_euler(sensors[trial]['Pelvis']['resampled'])
        #     sensors[trial]['Lower back']['resampled'] = orientation_euler(sensors[trial]['Lower back']['resampled'])
        #     sensors[trial]['Upper back']['resampled'] = orientation_euler(sensors[trial]['Upper back']['resampled'])
        #     sensors[trial]['Lower back']['resampled'] = relative_orientation(sensors[trial]['Lower back']['resampled'], sensors[trial]['Pelvis']['resampled'], 'Pelvis')
        #     sensors[trial]['Upper back']['resampled'] = relative_orientation(sensors[trial]['Upper back']['resampled'], sensors[trial]['Lower back']['resampled'], 'Lower back')
        #     sensors[trial]['Upper back']['resampled'] = relative_orientation(sensors[trial]['Upper back']['resampled'], sensors[trial]['Pelvis']['resampled'], 'Pelvis')
        # else:
        # Data captured with QSense Motion software
        sensors[trial]['Upper back']['resampled'] = orientation_estimation(sensors[trial]['Fs'], sensors[trial]['Upper back']['resampled'])
        sensors[trial]['Lower back']['resampled'] = orientation_estimation(sensors[trial]['Fs'], sensors[trial]['Lower back']['resampled'])
        sensors[trial]['Pelvis']['resampled'] = orientation_estimation(sensors[trial]['Fs'], sensors[trial]['Pelvis']['resampled'])
        sensors[trial]['Pelvis']['resampled'] = orientation_euler(sensors[trial]['Pelvis']['resampled'])
        sensors[trial]['Lower back']['resampled'] = orientation_euler(sensors[trial]['Lower back']['resampled'])
        sensors[trial]['Upper back']['resampled'] = orientation_euler(sensors[trial]['Upper back']['resampled'])
        sensors[trial]['Lower back']['resampled'] = relative_orientation(sensors[trial]['Lower back']['resampled'], sensors[trial]['Pelvis']['resampled'], 'Pelvis')
        sensors[trial]['Upper back']['resampled'] = relative_orientation(sensors[trial]['Upper back']['resampled'], sensors[trial]['Lower back']['resampled'], 'Lower back')
        sensors[trial]['Upper back']['resampled'] = relative_orientation(sensors[trial]['Upper back']['resampled'], sensors[trial]['Pelvis']['resampled'], 'Pelvis')
        
# for trial in sensors:
#     lag = 0
#     try:
#         correlation = signal.correlate(sensors[trial]['Upper back']['resampled']['ez relative to Pelvis'], vicon[trial]['RSpineAngles'][:,1], mode='full')
#         lags = signal.correlation_lags(sensors[trial]['Upper back']['resampled']['ez relative to Pelvis'].size, vicon[trial]['RSpineAngles'][:,1].size, mode="full")
#         vicon[trial]['lag'] = lags[np.argmax(correlation)]
#     except:
#         pass

    

# trial = '807_PP02_M02.c3d' #'807_PP02_M03.c3d' #  '807_PP03_02.c3d' # '807_PP03_03.c3d'   # goede trials
trial = '807_PP02_M04.c3d' # 
# for trial in sensors:
strt = 0#vicon[trial]['lag']
try:
    fig, ax = plt.subplots(nrows=3, ncols=1)
    ax[0].set_title('Euler orientations')
    # ax[2].plot(sensors[trial]['Pelvis']['resampled']['ex'], label='x pelvis')
    # ax[0].plot(sensors[trial]['Pelvis']['resampled']['ey'], label='y pelvis')
    # ax[1].plot(sensors[trial]['Pelvis']['resampled']['ez'], label='z pelvis')
    # ax[2].plot(sensors[trial]['Lower back']['resampled']['ex'], label='x pelvis')
    # ax[0].plot(sensors[trial]['Lower back']['resampled']['ey'], label='y pelvis')
    # ax[1].plot(sensors[trial]['Lower back']['resampled']['ez'], label='z pelvis')
    ax[2].plot(sensors[trial]['Upper back']['resampled']['ex'], label='x upper back') # Rotation
    ax[0].plot(sensors[trial]['Upper back']['resampled']['ey'], label='y upper back') # Flexion extension
    ax[1].plot(sensors[trial]['Upper back']['resampled']['ez'], label='z upper back') # Latero flexion
    
    ax[2].plot(np.arange(0,len(sensors[trial]['Upper back']['resampled']['ex relative to Pelvis'])), sensors[trial]['Upper back']['resampled']['ex relative to Pelvis'][:], label='x upper back relative')
    ax[0].plot(np.arange(0,len(sensors[trial]['Upper back']['resampled']['ey relative to Pelvis'])), sensors[trial]['Upper back']['resampled']['ey relative to Pelvis'][:], label='y upper back relative')
    ax[1].plot(np.arange(0,len(sensors[trial]['Upper back']['resampled']['ez relative to Pelvis'])), sensors[trial]['Upper back']['resampled']['ez relative to Pelvis'][:], label='z upper back relative')
    
    ax[0].plot(vicon[trial]['RSpineAngles'][strt:,0], label='x Spine') # Flexion extension
    ax[1].plot(vicon[trial]['RSpineAngles'][strt:,1], label='y Spine') # Latero flexion
    ax[2].plot(vicon[trial]['RSpineAngles'][strt:,2], label='z Spine') # Rotation
    
    ax[0].legend()
    ax[1].legend()
    ax[2].legend()
except:
    print('Something went wrong in plotting trial: '+ trial)