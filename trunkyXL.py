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
from scipy import stats
from scipy import signal
from sensor_analysis_functions import orientation_estimation, orientation_euler, relative_orientation
from dataimport_functions import correspondingfiles, importvicondata, importsensordata, resamplesensordata

folder = 'V:/research_reva_studies/807_TrunkyXL/II_Onderzoeksdata/Databestanden'

corresponding_files, foldersvicon, folderssensors = correspondingfiles(folder)

vicon = importvicondata (corresponding_files, foldersvicon)
sensors = importsensordata (corresponding_files, folderssensors)
sensors = resamplesensordata (sensors)

for trial in sensors:
    if sensors[trial]['Software'] != 'Corpus' and 'PP17' not in trial and len(sensors[trial]['Pelvis']['resampled']) >= 3:
        print('Orientation estimation of trial: ', trial)
        # Data captured with QSense Motion software
        sensors[trial]['Upper back']['resampled'] = orientation_estimation(sensors[trial]['Fs'], sensors[trial]['Upper back']['resampled'])
        sensors[trial]['Lower back']['resampled'] = orientation_estimation(sensors[trial]['Fs'], sensors[trial]['Lower back']['resampled'])
        sensors[trial]['Pelvis']['resampled'] = orientation_estimation(sensors[trial]['Fs'], sensors[trial]['Pelvis']['resampled'])

for trial in sensors:
    if len(sensors[trial]['Pelvis']['resampled']) >= 3:
        sensors[trial]['Upper back']['resampled'] = orientation_euler(sensors[trial]['Upper back']['resampled'])
        sensors[trial]['Lower back']['resampled'] = orientation_euler(sensors[trial]['Lower back']['resampled'])
        sensors[trial]['Pelvis']['resampled'] = orientation_euler(sensors[trial]['Pelvis']['resampled'])
        
        sensors[trial]['Lower back']['resampled'] = relative_orientation(sensors[trial]['Lower back']['resampled'], sensors[trial]['Pelvis']['resampled'], 'Pelvis')
        sensors[trial]['Upper back']['resampled'] = relative_orientation(sensors[trial]['Upper back']['resampled'], sensors[trial]['Lower back']['resampled'], 'Lower back')
        sensors[trial]['Upper back']['resampled'] = relative_orientation(sensors[trial]['Upper back']['resampled'], sensors[trial]['Pelvis']['resampled'], 'Pelvis')
        
        # vertical_q = pd.DataFrame(0, index=np.arange(len(sensors[trial]['Pelvis']['resampled'])), columns=['q0', 'q1', 'q2', 'q3'])
        # vertical_q['q3'] = 1
        # sensors[trial]['Lower back']['resampled'] = relative_orientation(sensors[trial]['Lower back']['resampled'], vertical_q, 'Vertical')
        # sensors[trial]['Upper back']['resampled'] = relative_orientation(sensors[trial]['Upper back']['resampled'], vertical_q, 'Vertical')
        # sensors[trial]['Upper back']['resampled'] = relative_orientation(sensors[trial]['Upper back']['resampled'], vertical_q, 'Vertical')
        
for trial in sensors:
    if sensors[trial]['Software'] == 'QSense Motion':
        try:
            fig, ax = plt.subplots(nrows=3, ncols=1)
            ax[0].set_title('Euler orientations '+trial[:-4])
            ax[0].plot(vicon[trial]['LSpineAngles'][:,0], label='x Spine') # Flexion extension
            ax[1].plot(vicon[trial]['LSpineAngles'][:,1], label='y Spine') # Latero flexion
            ax[2].plot(vicon[trial]['LSpineAngles'][:,2], label='z Spine') # Rotation
            
            # ax[0].plot(vicon[trial]['LThoraxAngles'][:,0], label='x Spine') # Flexion extension
            # ax[1].plot(vicon[trial]['LThoraxAngles'][:,1], label='y Spine') # Latero flexion
            # ax[2].plot(vicon[trial]['LThoraxAngles'][:,2], label='z Spine') # Rotation
            
            # ax[1].plot(sensors[trial]['Pelvis']['resampled']['ex'], label='x pelvis')
            # ax[0].plot(sensors[trial]['Pelvis']['resampled']['ey'], label='y pelvis')
            # ax[2].plot(sensors[trial]['Pelvis']['resampled']['ez'], label='z pelvis')
            
            # ax[0].plot(-1*sensors[trial]['Upper back']['resampled']['ex'], label='x upper back') # Rotation
            # ax[1].plot(sensors[trial]['Upper back']['resampled']['ey'], label='y upper back') # Flexion extension
            # ax[2].plot(sensors[trial]['Upper back']['resampled']['ez'], label='z upper back') # Latero flexion
            
            ax[1].plot(sensors[trial]['Upper back']['resampled']['ex relative to Pelvis'], label='x upper back relative')
            ax[0].plot(-1*sensors[trial]['Upper back']['resampled']['ey relative to Pelvis'], label='y upper back relative')
            ax[2].plot(sensors[trial]['Upper back']['resampled']['ez relative to Pelvis'], label='z upper back relative')
            
            ax[0].legend()
            ax[1].legend()
            ax[2].legend()
        except:
            print('Something went wrong in plotting trial: '+ trial)
    elif sensors[trial]['Software'] == 'Corpus':
        try:
            fig, ax = plt.subplots(nrows=3, ncols=1)
            ax[0].set_title('Euler orientations '+trial[:-4])
            ax[0].plot(vicon[trial]['LSpineAngles'][:,0], label='x Spine') # Flexion extension
            ax[1].plot(vicon[trial]['LSpineAngles'][:,1], label='y Spine') # Latero flexion
            ax[2].plot(vicon[trial]['LSpineAngles'][:,2], label='z Spine') # Rotation
            
            # ax[0].plot(vicon[trial]['LThoraxAngles'][:,0], label='x Spine') # Flexion extension
            # ax[1].plot(vicon[trial]['LThoraxAngles'][:,1], label='y Spine') # Latero flexion
            # ax[2].plot(vicon[trial]['LThoraxAngles'][:,2], label='z Spine') # Rotation
            
            # ax[1].plot(sensors[trial]['Pelvis']['resampled']['ex'], label='x pelvis')
            # ax[0].plot(sensors[trial]['Pelvis']['resampled']['ey'], label='y pelvis')
            # ax[2].plot(sensors[trial]['Pelvis']['resampled']['ez'], label='z pelvis')
            
            # ax[0].plot(-1*sensors[trial]['Upper back']['resampled']['ex'], label='x upper back') # Rotation
            # ax[1].plot(sensors[trial]['Upper back']['resampled']['ey'], label='y upper back') # Flexion extension
            # ax[2].plot(sensors[trial]['Upper back']['resampled']['ez'], label='z upper back') # Latero flexion
            
            ax[1].plot(-1*sensors[trial]['Upper back']['resampled']['ex relative to Pelvis'], label='x upper back relative')
            ax[2].plot(sensors[trial]['Upper back']['resampled']['ey relative to Pelvis'], label='y upper back relative')
            ax[0].plot(sensors[trial]['Upper back']['resampled']['ez relative to Pelvis'], label='z upper back relative')
            
            ax[0].legend()
            ax[1].legend()
            ax[2].legend()
        except:
            print('Something went wrong in plotting trial: '+ trial)

            
# Pearson correlation
pearson_rho = dict()
pearson_pval = dict()

for trial in sensors:
    if sensors[trial]['Software']=='QSense Motion':
        pearson_rho[trial]=np.zeros((1,3), dtype=float).flatten()
        pearson_pval[trial]=np.zeros((1,3), dtype=float).flatten()
        try:
            if len(sensors[trial]['Upper back']['resampled']['ey relative to Pelvis']) > len(vicon[trial]['LSpineAngles'][:,0]):
                sensor_pearson_FE = -1*sensors[trial]['Upper back']['resampled']['ey relative to Pelvis'][0:len(vicon[trial]['LSpineAngles'][:,0])]
                vicon_pearson_FE = vicon[trial]['LSpineAngles'][:,0]
                sensor_pearson_LF = sensors[trial]['Upper back']['resampled']['ex relative to Pelvis'][0:len(vicon[trial]['LSpineAngles'][:,1])]
                vicon_pearson_LF = vicon[trial]['LSpineAngles'][:,1]
                sensor_pearson_R = sensors[trial]['Upper back']['resampled']['ez relative to Pelvis'][0:len(vicon[trial]['LSpineAngles'][:,2])]
                vicon_pearson_R = vicon[trial]['LSpineAngles'][:,2]
            elif len(sensors[trial]['Upper back']['resampled']['ey relative to Pelvis']) < len(vicon[trial]['LSpineAngles'][:,0]):
                sensor_pearson_FE = -1*sensors[trial]['Upper back']['resampled']['ey relative to Pelvis']
                vicon_pearson_FE = vicon[trial]['LSpineAngles'][0:len(sensors[trial]['Upper back']['resampled']['ey relative to Pelvis']),0]
                sensor_pearson_LF = sensors[trial]['Upper back']['resampled']['ex relative to Pelvis']
                vicon_pearson_LF = vicon[trial]['LSpineAngles'][0:len(sensors[trial]['Upper back']['resampled']['ex relative to Pelvis']),1]
                sensor_pearson_R = sensors[trial]['Upper back']['resampled']['ez relative to Pelvis']
                vicon_pearson_R = vicon[trial]['LSpineAngles'][0:len(sensors[trial]['Upper back']['resampled']['ez relative to Pelvis']),2]
            pearson_rho[trial][0], pearson_pval[trial][0] = stats.pearsonr(sensor_pearson_FE, vicon_pearson_FE)
            pearson_rho[trial][1], pearson_pval[trial][1] = stats.pearsonr(sensor_pearson_LF, vicon_pearson_LF)
            pearson_rho[trial][2], pearson_pval[trial][2] = stats.pearsonr(sensor_pearson_R, vicon_pearson_R)
        except KeyError:
            pass
    if sensors[trial]['Software']=='Corpus':
        pearson_rho[trial]=np.zeros((1,3), dtype=float).flatten()
        pearson_pval[trial]=np.zeros((1,3), dtype=float).flatten()
        try:
            if len(sensors[trial]['Upper back']['resampled']['ey relative to Pelvis']) > len(vicon[trial]['LSpineAngles'][:,0]):
                sensor_pearson_FE = sensors[trial]['Upper back']['resampled']['ez relative to Pelvis'][0:len(vicon[trial]['LSpineAngles'][:,0])]
                vicon_pearson_FE = vicon[trial]['LSpineAngles'][:,0]
                sensor_pearson_LF = -1*sensors[trial]['Upper back']['resampled']['ex relative to Pelvis'][0:len(vicon[trial]['LSpineAngles'][:,1])]
                vicon_pearson_LF = vicon[trial]['LSpineAngles'][:,1]
                sensor_pearson_R = sensors[trial]['Upper back']['resampled']['ey relative to Pelvis'][0:len(vicon[trial]['LSpineAngles'][:,2])]
                vicon_pearson_R = vicon[trial]['LSpineAngles'][:,2]
            elif len(sensors[trial]['Upper back']['resampled']['ey relative to Pelvis']) < len(vicon[trial]['LSpineAngles'][:,0]):
                sensor_pearson_FE = sensors[trial]['Upper back']['resampled']['ez relative to Pelvis']
                vicon_pearson_FE = vicon[trial]['LSpineAngles'][0:len(sensors[trial]['Upper back']['resampled']['ez relative to Pelvis']),0]
                sensor_pearson_LF = -1*sensors[trial]['Upper back']['resampled']['ex relative to Pelvis']
                vicon_pearson_LF = vicon[trial]['LSpineAngles'][0:len(sensors[trial]['Upper back']['resampled']['ex relative to Pelvis']),1]
                sensor_pearson_R = sensors[trial]['Upper back']['resampled']['ey relative to Pelvis']
                vicon_pearson_R = vicon[trial]['LSpineAngles'][0:len(sensors[trial]['Upper back']['resampled']['ey relative to Pelvis']),2]
            pearson_rho[trial][0], pearson_pval[trial][0] = stats.pearsonr(sensor_pearson_FE, vicon_pearson_FE)
            pearson_rho[trial][1], pearson_pval[trial][1] = stats.pearsonr(sensor_pearson_LF, vicon_pearson_LF)
            pearson_rho[trial][2], pearson_pval[trial][2] = stats.pearsonr(sensor_pearson_R, vicon_pearson_R)
        except KeyError:
            pass

