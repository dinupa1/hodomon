#!/usr/bin/python3

#
# plots for hodo channel monitoring
#

from hodomon import hodomon

# for now we use H4Y1L-l plane PMTs

hodo_name = "H4Y1R-l_"
pmt = []

for i in range(0, 16):
  pmt.append(hodo_name+str(i+1)+"_MV")
  
# print(pmt)

plots = []

for i in range(0, 16):
  plots.append(hodomon(pmt[i]))
  
for i in range(0, 16):
  plots[i].display()