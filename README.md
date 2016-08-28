# Colias-Scratch-Interface
Dissertation Artifact; Interface to allow the Colias robot to communicate with Scratch in real time.

--Setup Instructions---

1.Install Scratch and Scratchpy

$ sudo apt-get install scratch
$ sudo apt-get install python-pip
$ sudo pip install scratchpy
Open Colias project in Scratch

2.Install pyserial

Download pyserial @ https://pypi.python.org/pypi/pyserial
navigate to tar eg. $ cd ~/Desktop/
$ tar -xzf pyserial-3.0.1.tar.gz
navigate into folder eg. $ cd~/Desktop/pyserial_3.0.1
$ sudo python setup.py install

3.Setup Colias
dmesg | egrep tty
Connect Colias, check serial port and make adjustments

4.Run interface
Download Script and navigate to folder eg. $ cd ~/Desktop/
https://drive.google.com/open?id=0B0de_mzPYmMreGFoWHZNSEV6N0U
execute script
$sudo python colias.py
