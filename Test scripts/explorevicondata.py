# -*- coding: utf-8 -*-
"""
Explore VICON data.

Versions
    2021-05-11 - C.J. Ensink
    
"""

from VICON_functions.readmarkerdata import readmarkerdata

import matplotlib.pyplot as plt
from scipy import interpolate
import numpy as np

filepath_metgaps = 'V:/research_reva_studies/807_TrunkyXL/II_Onderzoeksdata/Databestanden/807_pp03/Vicon/807_PP03_20230116/C3D_MetGaps_MetKinematica/807_PP03_M02.c3d'
filepath_zondergaps = 'V:/research_reva_studies/807_TrunkyXL/II_Onderzoeksdata/Databestanden/807_pp03/Vicon/807_PP03_20230116/C3D_ZonderGaps_MetKinematica/807_PP03_M02.c3d'

# Read the markerdata from the full filepath (from the dialog window)
datavicon_met, VideoFrameRate = readmarkerdata( filepath_metgaps )
datavicon_zonder, VideoFrameRate = readmarkerdata( filepath_zondergaps )
# # Identify missing values for each marker
# missingvalues={}
# nonmissingvalues={}
# for key in datavicon:
#     missingvalues[key] = np.unique(np.where(datavicon[key] == 0)[0])
#     # datavicon[key][missingvalues[key]] = np.nan
#     nonmissingvalues[key] = np.unique(np.where(datavicon[key] != 0)[0])


# # Plot x-y trajectory markers
# figaxis1 = 0
# figaxis2 = 1
# fig, (ax1, ax2) = plt.subplots(2,1, sharex=True)
# ax1.set_title('Left')
# ax1.plot(datavicon['LASI'][:,figaxis1], datavicon['LASI'][:,figaxis2], 'k', label='LASI')
# # ax1.plot(datavicon['LASI'][missingvalues['LASI'],figaxis1], datavicon['LASI'][missingvalues['LASI'],figaxis2], 'r.', markersize = 2, label='')

# ax1.plot(datavicon['LPSI'][:,figaxis1], datavicon['LPSI'][:,figaxis2], 'm', label='LPSI')
# # ax1.plot(datavicon['LPSI'][missingvalues['LPSI'],figaxis1], datavicon['LPSI'][missingvalues['LPSI'],figaxis2], 'r.', markersize = 2, label='')

# # ax1.plot(datavicon['LANK'][:,figaxis1], datavicon['LANK'][:,figaxis2], 'b', label='LANK')
# # ax1.plot(datavicon['LANK'][missingvalues['LANK'],figaxis1], datavicon['LANK'][missingvalues['LANK'],figaxis2], 'r.', markersize = 2, label='')

# ax1.set_ylabel('Position y-direction (mm)')
# ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# ax2.set_title('Right')
# ax2.plot(datavicon['RASI'][:,figaxis1], datavicon['RASI'][:,figaxis2], 'k', label='RASI')
# # ax2.plot(datavicon['RASI'][missingvalues['RASI'],figaxis1], datavicon['RASI'][missingvalues['RASI'],figaxis2], 'r.', markersize = 2, label='')

# ax2.plot(datavicon['RPSI'][:,figaxis1], datavicon['RPSI'][:,figaxis2], 'm', label='RPSI')
# # ax2.plot(datavicon['RPSI'][missingvalues['RPSI'],figaxis1], datavicon['RPSI'][missingvalues['RPSI'],figaxis2], 'r.', markersize = 2, label='')

# # ax2.plot(datavicon['RANK'][:,figaxis1], datavicon['RANK'][:,figaxis2], 'b', label='RANK')
# # ax2.plot(datavicon['RANK'][missingvalues['RANK'],figaxis1],datavicon['RANK'][missingvalues['RANK'],figaxis2], 'r.', markersize = 2, label='')

# ax2.set_xlabel('Position x-direction (mm)')
# ax2.set_ylabel('Position y-direction (mm)')
# ax2.legend(loc='center left', bbox_to_anchor=(1, 0.5))


# # Plot markers
# figaxis1 = 0

# fig, (ax1, ax2) = plt.subplots(2,1, sharex=True)
# ax1.set_title('Left')
# ax1.plot(datavicon['LASI'][:,figaxis1], 'k', label='LASI')
# ax1.plot(missingvalues['LASI'], datavicon['LASI'][missingvalues['LASI'],figaxis1], 'r.', markersize = 2, label='')

# ax1.plot(datavicon['LPSI'][:,figaxis1], 'm', label='LPSI')
# ax1.plot(missingvalues['LPSI'], datavicon['LPSI'][missingvalues['LPSI'],figaxis1], 'r.', markersize = 2, label='')


# ax1.set_ylabel('Position x-direction (mm)')
# ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# ax2.set_title('Right')
# ax2.plot(datavicon['RASI'][:,figaxis1], 'k', label='RASI')
# ax2.plot(missingvalues['RASI'], datavicon['RASI'][missingvalues['RASI'],figaxis1], 'r.', markersize = 2, label='')

# ax2.plot(datavicon['RPSI'][:,figaxis1], 'm', label='RPSI')
# ax2.plot(missingvalues['RPSI'], datavicon['RPSI'][missingvalues['RPSI'],figaxis1], 'r.', markersize = 2, label='')

# ax2.set_xlabel('Time (samples)')
# ax2.set_ylabel('Position x-direction (mm)')
# ax2.legend(loc='center left', bbox_to_anchor=(1, 0.5))


# # # Interpolate missing values
# dataviconinterpolated=datavicon
# interpkeys = ['STRN', 'C7', 'T10', 'LSpineAngles', 'LThoraxAngles', 'LPelvisAngles', 'LPSI', 'RPSI', 'LASI', 'RASI']
# for key in interpkeys:
#     if key in datavicon.keys():
#         x = nonmissingvalues[key]
#         cols = np.shape(datavicon[key])[1]
#         for i in range(0,cols):
#             y = datavicon[key][nonmissingvalues[key],i]
#             f = interpolate.interp1d(x, y, kind = 'quadratic') # second order spline interpolation
#             xnew = np.arange(min(x), len(datavicon[key]), 1)
#             xnew = xnew[ (xnew <= np.max(x)) ]
#             ynew = f(xnew)   # use interpolation function returned by `interp1d`
#             dataviconinterpolated[key][xnew,i] = ynew
#         fig = plt.figure()
#         plt.title(key)
#         plt.plot(nonmissingvalues[key], datavicon[key][nonmissingvalues[key]], 'o', dataviconinterpolated[key], '-')
#         plt.show()

# for key in datavicon:
#     datavicon[key][missingvalues[key],0] = np.interp(missingvalues[key], nonmissingvalues[key], datavicon[key][nonmissingvalues[key],0])
#     datavicon[key][missingvalues[key],1] = np.interp(missingvalues[key], nonmissingvalues[key], datavicon[key][nonmissingvalues[key],1])
#     datavicon[key][missingvalues[key],2] = np.interp(missingvalues[key], nonmissingvalues[key], datavicon[key][nonmissingvalues[key],2])



# timeinsec = np.arange(0,len(dataviconinterpolated['LThoraxAngles'])/100,0.01)
# # Plot thorax angles
# fig, (ax1) = plt.subplots(1,1, sharex=True)
# ax1.set_title('Thorax angles')

# ax1.plot(timeinsec, dataviconinterpolated['LThoraxAngles'][:,0], 'b', label='Flexion-extension')
# ax1.plot(timeinsec, dataviconinterpolated['LThoraxAngles'][:,1], 'r', label='Latero flexion')
# ax1.plot(timeinsec, dataviconinterpolated['LThoraxAngles'][:,2], 'g', label='Rotation')

# ax1.set_ylabel('Angle (deg)')
# ax1.set_xlabel('Time (seconds)')
# ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5))



# timeinsec = np.arange(0,len(dataviconinterpolated['LSpineAngles'])/100,0.01)
# # Plot spine angles
# fig, (ax1) = plt.subplots(1,1, sharex=True)
# ax1.set_title('Spine angles')

# ax1.plot(timeinsec, dataviconinterpolated['LSpineAngles'][:,0], 'b', label='Flexion-extension')
# ax1.plot(timeinsec, dataviconinterpolated['LSpineAngles'][:,1], 'r', label='Latero flexion')
# ax1.plot(timeinsec, dataviconinterpolated['LSpineAngles'][:,2], 'g', label='Rotation')

# ax1.set_ylabel('Angle (deg)')
# ax1.set_xlabel('Time (seconds)')
# ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5))




def bland_altman_plot(data1, data2, *args, **kwargs):
    data1     = np.asarray(data1)
    data2     = np.asarray(data2)
    mean      = np.mean([data1, data2], axis=0)
    diff      = data1 - data2                   # Difference between data1 and data2
    md        = np.mean(diff)                   # Mean of the difference
    md_string = 'mean of the difference: ' + round(md, 3).astype(str)
    sd        = np.std(diff, axis=0)            # Standard deviation of the difference
    ub_string = '+ 1.96*SD: ' + round(md + 1.96*sd, 3).astype(str)
    lb_string = '- 1.96*SD: ' + round(md - 1.96*sd, 3).astype(str)
    
    fig = plt.subplots()
    plt.title('Bland-Altman Plot ')
    plt.scatter(mean, diff, *args, **kwargs)
    plt.axhline(md,           color='gray', linestyle='--')
    plt.text(data1[-1], md, md_string, fontsize=10)
    plt.axhline(md + 1.96*sd, color='gray', linestyle='--')
    plt.text(data1[-1], md + 1.96*sd, ub_string, fontsize=10)
    plt.axhline(md - 1.96*sd, color='gray', linestyle='--')
    plt.text(data1[-1], md - 1.96*sd, lb_string, fontsize=10)
    plt.xlabel("Average of 2 measures")
    plt.ylabel("Difference between 2 measures")





def checkevents (data1, data2):
    # Compare right datapoint with eachother
    # Bland altman plot needs same length of data, keep only datapoints that are within 'window' frames of each other in rightdata1 and rightdata2
    # assumed that datapoint that do not have a matching event are false detected or missed events. These are saved in wrongdata1 and wrongdata2

    window = 40
    rightdata1 = np.array([], dtype = int)
    rightdata2 = np.array([], dtype = int)
    wrongdata1 = np.array([], dtype = int)
    wrongdata2 = np.array([], dtype = int)
    
    #Identify gait events within window of frames with a matching event in the other dataset
    for i in range(0, len(data1)):
        windowvaluesdata1 = np.array(range(data1[i]-window, data1[i]+window))
        for j in range(0,len(windowvaluesdata1)):
            if windowvaluesdata1[j] in data2:
                rightdata1 = np.append(rightdata1, data1[i])
                okayvaluedata2 = np.argwhere(data2 == windowvaluesdata1[j])
                rightdata2 = np.append(rightdata2, data2[okayvaluedata2])
    # Identify wich gait events do not have a matching event in the other dataset
    for i in range(0, len(data1)):
        if data1[i] not in rightdata1:
            wrongdata1 = np.append(wrongdata1, data1[i])
    for i in range(0, len(data2)):
        if data2[i] not in rightdata2:
            wrongdata2 = np.append(wrongdata2, data2[i])
            
    return rightdata1, rightdata2, wrongdata1, wrongdata2