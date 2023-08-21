import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

#100 samples
simlen=int(1000)
i=0
#Probability of the event
prob = 0.5
desired_output=1/8
#Generating sample date using Bernoulli r.v.
data_bern = bernoulli.rvs(size=simlen,p=prob)
#Calculating the number of favourable outcomes
err_ind = np.nonzero(data_bern == 1)
#calculating the probability of no head on one toss 
err_n = round(np.size(err_ind)/simlen,1)
#calculating the probability of no head on three toss = prob no head on one toss x prob no head on one toss x prob no head on one toss
prob_0_head=err_n*err_n*err_n
if prob_0_head==desired_output:
    print('Probability of getting no head in three toss = '+str(prob_0_head))
      
