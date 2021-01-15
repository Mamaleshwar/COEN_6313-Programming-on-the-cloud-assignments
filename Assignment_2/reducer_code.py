#!/usr/bin/env python
from operator import itemgetter
import sys
import statistics

# def cal_metrics(values):
#     metrics = {'Samples': 0, 'Max':0, 'Min': 0, 'Median':0, 'Standard Deviation': 0}
#     print(values)
#     for _ , mem in values.items():
#         metrics['Samples'] = len(mem)
#         metrics['Max'] = max(mem)
#         metrics['Min'] = min(mem)
#         metrics['Median'] = np.median(np.array(mem))
#         metrics['Standard Deviation'] = np.std(np.array(mem))
#         print( metrics)


samples = {0:[], 1:[],2:[], 3:[], 4:[],5:[], 6:[], 7:[], 8:[], 9:[]}

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    
    try:
        cpu, mem = line.split(' ', 1)
        print(cpu, mem)
        cpu = int(cpu)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    if -1 < int(cpu) < 11:
        samples[0].append(float(mem))
    if 10 < int(cpu) < 21:
        samples[1].append(float(mem))
    if 20 < int(cpu) < 31:
        samples[2].append(float(mem)) 
    if 30 < int(cpu) < 41:
        samples[3].append(float(mem)) 
    if 40 < int(cpu) < 51:
        samples[4].append(float(mem)) 
    if 50 < int(cpu) < 61:
        samples[5].append(float(mem)) 
    if 60 < int(cpu) < 71:
        samples[6].append(float(mem)) 
    if 70 < int(cpu) < 81:
        samples[7].append(float(mem)) 
    if 80 < int(cpu) < 91:
        samples[8].append(float(mem)) 
    if 90 < int(cpu) < 101:
        samples[9].append(float(mem)) 

metrics = {'Samples': 0, 'Max':0, 'Min': 0, 'Median':0, 'Standard Deviation': 0}
for _ , mem in samples.items():

    metrics['Samples'] = len(mem)
    metrics['Max'] = max(mem)
    metrics['Min'] = min(mem)
    metrics['Median'] = statistics.median(mem)
    metrics['Standard Deviation'] = statistics.stdev(mem)
    print(metrics)

