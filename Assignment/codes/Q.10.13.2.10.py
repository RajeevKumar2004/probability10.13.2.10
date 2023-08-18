import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

#Let number of samples is 3000.
simlen=int(3000)

#Probability of the event 
prob = 1/2

#Generating sample data
data_bern = bernoulli.rvs(size=simlen,p=prob)
# let heads=1 and tails=0 
head_0_times=0
head_1_times=0
head_2_times=0
head_3_times=0
print("Samples generated:",data_bern)
# Converting list to group data in threes and count no. heads
for i in range (0,2998,3):
    add=0
    add=data_bern[i]+data_bern[i+1]+data_bern[i+2]
    if add == 0:
        head_0_times+=1
    elif add==1:
        head_1_times+=1
    elif add==2:
        head_2_times+=1   
    elif add==3:
        head_3_times+=1                      
print(f'Probability of head_0_times = {head_0_times/1000}')
print(f'Probability of head_1_times = {head_1_times/1000}')
print(f'Probability of head_2_times = {head_2_times/1000}')
print(f'Probability of head_3_times = {head_3_times/1000}')
# Equating given conclusion(head_0_times = 1/4) and rounding of our result for better evaluation
if round(head_0_times,2)==1/4:
    print("Given statement that no head = 1/4 is correct")
else:
    print ("Given statement that no head = 1/4 is incorrect")
