# TrunkyXL

This code was generated for the VR4REHAB "TrunkyXL" project.

It uses accelerometer, gyroscoe and magnetometer data from inertial measurment units (IMUs) attached to the back (C8, T10, L4/5 regions), and estimates the relative orientation between these sensors to approximate the movements of the back.
These orientation estimations were compared to the gold standard, optical motion caputure (VICON), for movement analysis by Pearson correlation, root mean square error, and differences in calculated range of motion.

**TrunkyXL.py** is the main script, it requires:
- the **dataimport_functions.py** file, which contains functions to import all data used in this validation study in a structured way. It also describes which sensordata corresponds to which VICON data,
- the **sensor_analysis_functions.py** file, which contains functions to analyse the IMU data,
- the **readmarkerdata.py** file, which contains functions to analyse the VICON data.

The **data** folder structure is as follows:
 - folder per participant
    - Corpus *(sensordata during gameplay)*
        - *.csv files for each measurement*
        - ...
    - QSense *(sensordata during validation trials)*
        - *folders with sensordata for each measurement*
             - R
                 - Back
                     - *.csv files for each sensor in the string*
                     - ...
                 - Left Arm
                     - *.csv files for each sensor in the string*
                 - Right Arm
                     - *.csv files for each sensor in the string*
        - ...
    - Vicon *(VICON data druing validation trials and gameplay)*
        - *.c3d files for each measurement*
        - ...
 
