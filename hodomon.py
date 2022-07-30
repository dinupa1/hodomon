#!/usr/bin/python3

#
# base class for hodo channel monitoring
#

import os
import glob
import csv
import time
import datetime
import numpy as np
import matplotlib.pyplot as plt

class hodomon(object):
  "read the voltages from slow crontrols and plot the voltage with time"
  def __init__(self, pmt):
    super(hodomon, self).__init__()
    self.channel = pmt
    
    cwd=os.getcwd()
    
    directories=glob.glob("/data2/e1039_data/slowcontrol_data/*")
    self.directory=max(directories, key=os.path.getctime)
    # self.directory="/data2/e1039_data/slowcontrol_data/slowcontrol_2022_07_26/"
    
    
    self.files = []
    
    os.chdir(self.directory)
    
    for file in glob.glob("*_HodoHv.tsv"):
      self.files.append(os.path.join(self.directory, file))
    
    os.chdir(cwd)
    
    self.files.sort(key=lambda x: os.path.getmtime(x))
    
    # H1YL_1_MV	1658937447	-1545	0
    
    self.date_time = []
    self.voltage = []
    self.x = []
    
    for i in range(len(self.files)):
      with open(self.files[i]) as data:
        tsv_file = csv.reader(data, delimiter="\t")
        for line in tsv_file:
          if(line[0]==self.channel and len(line[2]) > 0):
            # print(self.files[i])
            time_form = time.ctime(os.path.getctime(self.files[i]))
            self.date_time.append(time_form)
            self.x.append(i)
            self.voltage.append(float(line[2]))
    
    # print(self.voltage)
    
    # self.date_time = np.array(self.date_time)
    # self.voltage = np.array(self.voltage)
    # self.x = np.array(self.x)
  
  def display(self):
    fig, ax = plt.subplots(1, figsize=(8, 6))
    ax.plot(self.x, self.voltage, "go")
    plt.text(5, 5, self.directory)
    # plt.xticks(self.x, self.date_time)
    # plt.ylim(-1950, -1850)
    plt.title(self.channel)
    plt.xlabel("time")
    plt.ylabel("voltage (V)")
    # plt.tight_layout()
    fig.show()
    # print(type(self.date_time), type(self.voltage))
    
# A = hodomon("H4Y1L-l_3_MV")
# A.display()