# -*- coding: utf-8 -*-
"""
Sint Maartenskliniek study ID: 807_TrunkyXL
    Script for validation of TrunkyXL sensordata against optical motion capture

Last update:
    05-04-2023: C.J. Ensink, improved version relative orientation
    22-09-2022: C.J. Ensink, c.ensink@maartenskliniek.nl
    
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy import signal
import os
from sensor_analysis_functions import orientation_estimation, orientation_euler, relative_orientation
from dataimport_functions import correspondingfiles, importvicondata, importsensordata, resamplesensordata

cwd = os.getcwd()
cwd = cwd.replace("\\", "/")
folder = cwd + '/data' 
# folder = 'V:/research_reva_studies/807_TrunkyXL/II_Onderzoeksdata/Databestanden'

# Define corresponding files
corresponding_files, foldersvicon, folderssensors = correspondingfiles(folder)
# Import data
vicon = importvicondata (corresponding_files, foldersvicon)
sensors = importsensordata (corresponding_files, folderssensors)
# Resample sensordata
sensors = resamplesensordata (sensors, vicon)

# Calculate orientation from IMU data (Madgwick AHRS filter)
for trial in sensors:
    if sensors[trial]['Software'] != 'Corpus' and 'PP17' not in trial and len(sensors[trial]['Pelvis']['resampled']) >= 3:
        print('Orientation estimation of trial: ', trial)
        # Data captured with QSense Motion software
        sensors[trial]['Upper back']['resampled'] = orientation_estimation(sensors[trial]['Fs'], sensors[trial]['Upper back']['resampled'])
        sensors[trial]['Lower back']['resampled'] = orientation_estimation(sensors[trial]['Fs'], sensors[trial]['Lower back']['resampled'])
        sensors[trial]['Pelvis']['resampled'] = orientation_estimation(sensors[trial]['Fs'], sensors[trial]['Pelvis']['resampled'])

# Describe orientation in Euler angles from quaternions
for trial in sensors:
    if len(sensors[trial]['Pelvis']['resampled']) >= 3:
        sensors[trial]['Upper back']['resampled'] = orientation_euler(sensors[trial]['Upper back']['resampled'])
        sensors[trial]['Lower back']['resampled'] = orientation_euler(sensors[trial]['Lower back']['resampled'])
        sensors[trial]['Pelvis']['resampled'] = orientation_euler(sensors[trial]['Pelvis']['resampled'])
# Calculate the orientation relative to another sensor
        # sensors[trial]['Lower back']['resampled'] = relative_orientation(sensors[trial]['Lower back']['resampled'], sensors[trial]['Pelvis']['resampled'], 'Pelvis')
        # sensors[trial]['Upper back']['resampled'] = relative_orientation(sensors[trial]['Upper back']['resampled'], sensors[trial]['Lower back']['resampled'], 'Lower back')
        sensors[trial]['Upper back']['resampled'] = relative_orientation(sensors[trial]['Upper back']['resampled'], sensors[trial]['Pelvis']['resampled'], 'Pelvis')


# Plots        
for trial in sensors:
    if sensors[trial]['Software'] == 'QSense Motion':
        try:
            lw = 1
            fig, ax = plt.subplots(nrows=3, ncols=1)
            ax[0].set_title('Euler orientations '+trial[:-4])
            ax[0].plot(vicon[trial]['LSpineAngles'][:,0], label='x Spine', linewidth=lw) # Flexion extension
            ax[1].plot(vicon[trial]['LSpineAngles'][:,1], label='y Spine', linewidth=lw) # Latero flexion
            ax[2].plot(vicon[trial]['LSpineAngles'][:,2], label='z Spine', linewidth=lw) # Rotation
            
            # ax[0].plot(vicon[trial]['LThoraxAngles'][:,0], label='x Spine') # Flexion extension
            # ax[1].plot(vicon[trial]['LThoraxAngles'][:,1], label='y Spine') # Latero flexion
            # ax[2].plot(vicon[trial]['LThoraxAngles'][:,2], label='z Spine') # Rotation
            
            # ax[1].plot(sensors[trial]['Pelvis']['resampled']['ex'], label='x pelvis')
            # ax[0].plot(sensors[trial]['Pelvis']['resampled']['ey'], label='y pelvis')
            # ax[2].plot(sensors[trial]['Pelvis']['resampled']['ez'], label='z pelvis')
            
            # ax[0].plot(-1*sensors[trial]['Upper back']['resampled']['ex'], label='x upper back') # Rotation
            # ax[1].plot(sensors[trial]['Upper back']['resampled']['ey'], label='y upper back') # Flexion extension
            # ax[2].plot(sensors[trial]['Upper back']['resampled']['ez'], label='z upper back') # Latero flexion
            
            ax[1].plot(sensors[trial]['Upper back']['resampled']['ex relative to Pelvis'], label='x upper back relative', linewidth=lw)
            ax[0].plot(-1*sensors[trial]['Upper back']['resampled']['ey relative to Pelvis'], label='y upper back relative', linewidth=lw)
            ax[2].plot(sensors[trial]['Upper back']['resampled']['ez relative to Pelvis'], label='z upper back relative', linewidth=lw)
            
            ax[0].legend()
            ax[1].legend()
            ax[2].legend()
        except:
            print('Something went wrong in plotting trial: '+ trial)
    elif sensors[trial]['Software'] == 'Corpus':
        try:
            fig, ax = plt.subplots(nrows=3, ncols=1)
            ax[0].set_title('Euler orientations '+trial[:-4])
            ax[0].plot(vicon[trial]['LSpineAngles'][:,0], label='x Spine', linewidth=lw) # Flexion extension
            ax[1].plot(vicon[trial]['LSpineAngles'][:,1], label='y Spine', linewidth=lw) # Latero flexion
            ax[2].plot(vicon[trial]['LSpineAngles'][:,2], label='z Spine', linewidth=lw) # Rotation
            
            # ax[0].plot(vicon[trial]['LThoraxAngles'][:,0], label='x Spine') # Flexion extension
            # ax[1].plot(vicon[trial]['LThoraxAngles'][:,1], label='y Spine') # Latero flexion
            # ax[2].plot(vicon[trial]['LThoraxAngles'][:,2], label='z Spine') # Rotation
            
            # ax[1].plot(sensors[trial]['Pelvis']['resampled']['ex'], label='x pelvis')
            # ax[0].plot(-1*sensors[trial]['Pelvis']['resampled']['ey'], label='y pelvis')
            # ax[2].plot(sensors[trial]['Pelvis']['resampled']['ez'], label='z pelvis')
            
            # ax[1].plot(sensors[trial]['Upper back']['resampled']['ex'], label='x upper back') # Rotation
            # ax[0].plot(-1*sensors[trial]['Upper back']['resampled']['ey'], label='y upper back') # Flexion extension
            # ax[2].plot(sensors[trial]['Upper back']['resampled']['ez'], label='z upper back') # Latero flexion
            
            ax[1].plot(-1*sensors[trial]['Upper back']['resampled']['ex relative to Pelvis'], label='x upper back relative', linewidth=lw)
            ax[2].plot(sensors[trial]['Upper back']['resampled']['ey relative to Pelvis'], label='y upper back relative', linewidth=lw)
            ax[0].plot(sensors[trial]['Upper back']['resampled']['ez relative to Pelvis'], label='z upper back relative', linewidth=lw)
            
            ax[0].legend()
            ax[1].legend()
            ax[2].legend()
        except:
            print('Something went wrong in plotting trial: '+ trial)

            
# Pearson correlation for each of the angles over time per person
# Delta Range Of Motion for each of the angles per person
# RMSE for each of the angles per person
pearson_rho = dict()
pearson_pval = dict()
ROM_delta_FE = dict()
ROM_delta_LF = dict()
ROM_delta_R = dict()
RMSE_FE = dict()
RMSE_LF = dict()
RMSE_R = dict()

pearson_rho['all'] = np.zeros((1,3), dtype=float).flatten()
pearson_pval['all'] = np.zeros((1,3), dtype=float).flatten()
# ROM_delta_FE['all'] = np.array([])
# ROM_delta_LF['all'] = np.array([])
# ROM_delta_R['all'] = np.array([])
RMSE_FE['all'] = np.array([])
RMSE_LF['all'] = np.array([])
RMSE_R['all'] = np.array([])

sensor_FE_all = np.array([])
sensor_LF_all = np.array([])
sensor_R_all = np.array([])
vicon_FE_all = np.array([])
vicon_LF_all = np.array([])
vicon_R_all = np.array([])
ROM_d_FE_all = np.array([])
ROM_d_LF_all = np.array([])
ROM_d_R_all = np.array([])
    
for person in corresponding_files:
    # Create empty matrix for Pearson rho and p-value to be filled per person for flexion-extension, lateroflexion and rotational correlation between systems
    pearson_rho[person]=np.zeros((1,3), dtype=float).flatten()
    pearson_pval[person]=np.zeros((1,3), dtype=float).flatten()
    # Create empty array per person for sensor and vicon based flexion-extension, lateroflexion and rotational movements (append with each trial)
    sensor_FE = np.array([])
    sensor_LF = np.array([])
    sensor_R = np.array([])
    vicon_FE = np.array([])
    vicon_LF = np.array([])
    vicon_R = np.array([])
    
    # Create empty array per person for delta flexion-extension, lateroflexion and rotation ROM between systems (array filled with delta per trial)
    ROM_d_FE = np.array([])
    ROM_d_LF = np.array([])
    ROM_d_R = np.array([])
    
    for trial in corresponding_files[person]:
        # if sensors[trial]['Software']=='QSense Motion':
            
        # Append angles over time for each of the systems in order to calculate a Pearson correlation and RMSE per person (for three trials)
        if len(sensors[trial]['Upper back']['resampled']['ey relative to Pelvis']) == len(vicon[trial]['LSpineAngles'][:,0]):
            sensor_FE = np.append(sensor_FE, -1*sensors[trial]['Upper back']['resampled']['ey relative to Pelvis'])
            vicon_FE = np.append(vicon_FE, vicon[trial]['LSpineAngles'][:,0])
            sensor_LF = np.append(sensor_LF, sensors[trial]['Upper back']['resampled']['ex relative to Pelvis'])
            vicon_LF = np.append(vicon_LF, vicon[trial]['LSpineAngles'][:,1])
            sensor_R = np.append(sensor_R, sensors[trial]['Upper back']['resampled']['ez relative to Pelvis'])
            vicon_R = np.append(vicon_R, vicon[trial]['LSpineAngles'][:,2])
            
            sensor_FE_all = np.append(sensor_FE_all, -1*sensors[trial]['Upper back']['resampled']['ey relative to Pelvis'])
            vicon_FE_all = np.append(vicon_FE_all, vicon[trial]['LSpineAngles'][:,0])
            sensor_LF_all = np.append(sensor_LF_all, sensors[trial]['Upper back']['resampled']['ex relative to Pelvis'])
            vicon_LF_all = np.append(vicon_LF_all, vicon[trial]['LSpineAngles'][:,1])
            sensor_R_all = np.append(sensor_R_all, sensors[trial]['Upper back']['resampled']['ez relative to Pelvis'])
            vicon_R_all = np.append(vicon_R_all, vicon[trial]['LSpineAngles'][:,2])
        
        elif len(sensors[trial]['Upper back']['resampled']['ey relative to Pelvis']) > len(vicon[trial]['LSpineAngles'][:,0]):
            sensor_FE = np.append(sensor_FE, -1*sensors[trial]['Upper back']['resampled']['ey relative to Pelvis'][0:len(vicon[trial]['LSpineAngles'][:,0])])
            vicon_FE = np.append(vicon_FE, vicon[trial]['LSpineAngles'][:,0])
            sensor_LF = np.append(sensor_LF, sensors[trial]['Upper back']['resampled']['ex relative to Pelvis'][0:len(vicon[trial]['LSpineAngles'][:,0])])
            vicon_LF = np.append(vicon_LF, vicon[trial]['LSpineAngles'][:,1])
            sensor_R = np.append(sensor_R, sensors[trial]['Upper back']['resampled']['ez relative to Pelvis'][0:len(vicon[trial]['LSpineAngles'][:,0])])
            vicon_R = np.append(vicon_R, vicon[trial]['LSpineAngles'][:,2])
            
            sensor_FE_all = np.append(sensor_FE_all, -1*sensors[trial]['Upper back']['resampled']['ey relative to Pelvis'][0:len(vicon[trial]['LSpineAngles'][:,0])])
            vicon_FE_all = np.append(vicon_FE_all, vicon[trial]['LSpineAngles'][:,0])
            sensor_LF_all = np.append(sensor_LF_all, sensors[trial]['Upper back']['resampled']['ex relative to Pelvis'][0:len(vicon[trial]['LSpineAngles'][:,0])])
            vicon_LF_all = np.append(vicon_LF_all, vicon[trial]['LSpineAngles'][:,1])
            sensor_R_all = np.append(sensor_R_all, sensors[trial]['Upper back']['resampled']['ez relative to Pelvis'][0:len(vicon[trial]['LSpineAngles'][:,0])])
            vicon_R_all = np.append(vicon_R_all, vicon[trial]['LSpineAngles'][:,2])
        
        elif len(sensors[trial]['Upper back']['resampled']['ey relative to Pelvis']) < len(vicon[trial]['LSpineAngles'][:,0]):
            sensor_FE = np.append(sensor_FE, -1*sensors[trial]['Upper back']['resampled']['ey relative to Pelvis'])
            vicon_FE = np.append(vicon_FE, vicon[trial]['LSpineAngles'][0:len(sensors[trial]['Upper back']['resampled']['ez relative to Pelvis']),0])
            sensor_LF = np.append(sensor_LF, sensors[trial]['Upper back']['resampled']['ex relative to Pelvis'])
            vicon_LF = np.append(vicon_LF, vicon[trial]['LSpineAngles'][0:len(sensors[trial]['Upper back']['resampled']['ez relative to Pelvis']),1])
            sensor_R = np.append(sensor_R, sensors[trial]['Upper back']['resampled']['ez relative to Pelvis'])
            vicon_R = np.append(vicon_R, vicon[trial]['LSpineAngles'][0:len(sensors[trial]['Upper back']['resampled']['ez relative to Pelvis']),2])
            
            sensor_FE_all = np.append(sensor_FE_all, -1*sensors[trial]['Upper back']['resampled']['ey relative to Pelvis'])
            vicon_FE_all = np.append(vicon_FE_all, vicon[trial]['LSpineAngles'][0:len(sensors[trial]['Upper back']['resampled']['ez relative to Pelvis']),0])
            sensor_LF_all = np.append(sensor_LF_all, sensors[trial]['Upper back']['resampled']['ex relative to Pelvis'])
            vicon_LF_all = np.append(vicon_LF_all, vicon[trial]['LSpineAngles'][0:len(sensors[trial]['Upper back']['resampled']['ez relative to Pelvis']),1])
            sensor_R_all = np.append(sensor_R_all, sensors[trial]['Upper back']['resampled']['ez relative to Pelvis'])
            vicon_R_all = np.append(vicon_R_all, vicon[trial]['LSpineAngles'][0:len(sensors[trial]['Upper back']['resampled']['ez relative to Pelvis']),2])
        
        # Calculate delta ROM between systems per angle, per person
        ROM_sensor_FE = np.diff([np.max(-1*sensors[trial]['Upper back']['resampled']['ey relative to Pelvis']), np.min(-1*sensors[trial]['Upper back']['resampled']['ey relative to Pelvis'])])
        ROM_vicon_FE = np.diff([np.max(vicon[trial]['LSpineAngles'][:,0]), np.min(vicon[trial]['LSpineAngles'][:,0])])
        ROM_d_FE = np.append(ROM_d_FE, (ROM_sensor_FE - ROM_vicon_FE))
        ROM_sensor_LF = np.diff([np.max(sensors[trial]['Upper back']['resampled']['ex relative to Pelvis']), np.min(sensors[trial]['Upper back']['resampled']['ex relative to Pelvis'])])
        ROM_vicon_LF = np.diff([np.max(vicon[trial]['LSpineAngles'][:,1]), np.min(vicon[trial]['LSpineAngles'][:,1])])
        ROM_d_LF = np.append(ROM_d_LF, (ROM_sensor_LF - ROM_vicon_LF))
        ROM_sensor_R = np.diff([np.max(sensors[trial]['Upper back']['resampled']['ez relative to Pelvis']), np.min(sensors[trial]['Upper back']['resampled']['ez relative to Pelvis'])])
        ROM_vicon_R = np.diff([np.max(vicon[trial]['LSpineAngles'][:,2]), np.min(vicon[trial]['LSpineAngles'][:,2])])
        ROM_d_R = np.append(ROM_d_R, (ROM_sensor_R - ROM_vicon_R))

    # Calculate Pearson correlation between systems, for each angle, per person
    pearson_rho[person][0], pearson_pval[person][0] = stats.pearsonr(sensor_FE, vicon_FE)
    pearson_rho[person][1], pearson_pval[person][1] = stats.pearsonr(sensor_LF, vicon_LF)
    pearson_rho[person][2], pearson_pval[person][2] = stats.pearsonr(sensor_R, vicon_R)
    
    # Calculate RMSE for each angle, per person
    RMSE_FE[person] = np.sqrt( np.sum((sensor_FE - vicon_FE)**2)/len(sensor_FE) )
    RMSE_LF[person] = np.sqrt( np.sum((sensor_LF - vicon_LF)**2)/len(sensor_LF) )
    RMSE_R[person]  = np.sqrt( np.sum((sensor_R  - vicon_R )**2)/len(sensor_R ) )
    
    # Calculate mean delta ROM between systems, for each angle, per person            
    ROM_delta_FE[person] = np.mean(ROM_d_FE)
    ROM_delta_LF[person] = np.mean(ROM_d_LF)
    ROM_delta_R[person] = np.mean(ROM_d_R)


# Calculate Pearson correlation between systems, for each angle, per person
pearson_rho['all'][0], pearson_pval['all'][0] = stats.pearsonr(sensor_FE_all, vicon_FE_all)
pearson_rho['all'][1], pearson_pval['all'][1] = stats.pearsonr(sensor_LF_all, vicon_LF_all)
pearson_rho['all'][2], pearson_pval['all'][2] = stats.pearsonr(sensor_R_all, vicon_R_all)

# Calculate RMSE for each angle, per person
RMSE_FE['all'] = np.sqrt( np.sum((sensor_FE_all - vicon_FE_all)**2)/len(sensor_FE_all) )
RMSE_LF['all'] = np.sqrt( np.sum((sensor_LF_all - vicon_LF_all)**2)/len(sensor_LF_all) )
RMSE_R['all']  = np.sqrt( np.sum((sensor_R_all  - vicon_R_all )**2)/len(sensor_R_all ) )

ROM_delta_FE_mean = sum(ROM_delta_FE.values()) / len(ROM_delta_FE)
ROM_delta_LF_mean = sum(ROM_delta_LF.values()) / len(ROM_delta_LF)
ROM_delta_R_mean = sum(ROM_delta_R.values()) / len(ROM_delta_R)
ROM_delta_FE_sd = np.nanstd(list(ROM_delta_FE.values()))
ROM_delta_LF_sd = np.nanstd(list(ROM_delta_LF.values()))
ROM_delta_R_sd = np.nanstd(list(ROM_delta_R.values()))
