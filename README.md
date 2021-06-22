# Simulation of free falling cylindrical object using overset method

This test-case is able to reproduce the dynamic of a solid object (cylinder) falling first through air, impacting through water 
all the way on the bottom of the cuboid domain. Numerical Method used is OVERSET

**Installation**\
\


Download this repository into a RUN folder of OpenFOAM run path version v2012

**Execution**\
\

For domain features please see BACKGROUND folder
For object features please see FLOATINGBODY folder: shape and orientation in TOPOSETDICT (to set particular lenght and orientation please refer to Python file Angle_Length_topoSetDict.py), whereas for dynamic features check path background/constant/dynamicMeshDict. Remember to change to Allrun and Allclean according to your directory path

---> SEE REPORT FOR MORE DETAILS
