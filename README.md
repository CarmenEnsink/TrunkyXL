# TrunkyXL

This code was generated for the VR4REHAB "TrunkyXL" project.

It uses accelerometer, gyroscoe and magnetometer data from inertial measurment units (IMUs) attached to the back (C8, T10, L4/5 regions), and estimates the relative orientation between these sensors to approximate the movements of the back.
These orientation estimations were compared to the gold standard, optical motion caputure (VICON), for movement analysis by Pearson correlation, root mean square error, and differences in calculated range of motion.

**TrunkyXL.py** is the main script, it requires:
- the **dataimport_functions.py** file, which contains functions to import all data used in this validation study in a structured way,
- the **sensor_analysis_functions.py** file, which contains functions to analyse the IMU data,
- the **readmarkerdata.py** file, which contains functions to analyse the VICON data.
