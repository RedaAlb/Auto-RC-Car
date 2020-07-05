# Auto-RC-Car

This is my MSc Artificial Intelligence project.

This readme file is to be updated and refined as the projects evolves.


## To do next
- [x] Make camera connection extra robust/reliable and just amazingly fast.
- [x] Add and use multithreading for the sensor server.
- [x] Make a testing file for the camera connection for analysis, plots of e.g. FPS, delay, img bytes, etc.
    - [ ] I need to get more details about the frames lost in every second (how many lost frames in the 30 frames
    sent in the second), if that is substantial.
    - [ ] A way to see/find out when and how many frames are lost, is it usually 1 or are they lost consecutively.
- [x] Add testing folder to this readme file.
- [x] Close sensor server and thread more neatly and properly.
- [x] Look into multithreading options.
- [ ] Add the controller server.
    - [ ] Use multithreading for it.
- [ ] Make main loop in main.py into a class, and clean up main.py
    - Maybe make a CamHandler class to take care of it, and have instance var of frame that I can access
    in main.py
- [ ] Make another window for all stats/details, e.g. fps, num of bytes, delay, distance, etc.
- [ ] RC Car steering
- [ ] Add docstrings and document everything.


## Files and directories notes

`main.py` is the executable for this project. It combines everything together.

`/servers`, contains the server files for the camera, sensor, and controller connections between the computer and the Pi.

`/on_raspberrypi`, contains the files that are on the raspberry pi and that needs to be ran on the pi.

`/testing`, contains sub-directories to test and analyse different components of the project.


## To run

- [ ] Add hardware configuration here.
- [ ] I need to check if running from root or sub-directories makes a difference or not.

1. Run `main.py`
1. Run `cam_client.py` on the pi.
1. Run `sensor_client.py` on the pi.