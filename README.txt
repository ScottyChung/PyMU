Hello. This is a IMU Filtering suite created for research and educational
purposes. While the marjority of this suite is designed to be largely
self explanitory, there is an example script located in the main directory.

This module expects an object to be initiated with a desired IMU filter
type defined. Then the object should be updated with a python list
consisting of gyro,accel, and magnetometer updates. Only the gyroscope
updates are required, but the other sensors will provide more accurate
results. The module will then return xyz euleur angles.


Author - Scotty Chung


