import numpy as np
from math import log, sqrt, exp
import scipy.stats
import matplotlib.pyplot as plt

def log_likelihood(n1, n2, a, W):
    # this function takes a numpy array for n1, n2, and the accuracy (0/1), whether they answerd correctly
    # as well as W, the hypothesis
    # and returns the *log* likelihood of the responses, log P(acc | n1, n2, W)

    assert(len(n1) == len(n2) == len(a))

    p = 1.0-scipy.stats.norm.cdf(0, loc=np.abs(n1-n2), scale=W*np.sqrt(n1**2 + n2**2)) # the probability of answering correctly
    return np.sum(np.where(a, np.log(p), np.log(1.0-p)))

def log_prior(W):
    if W<0:
        return 0
    else:
        return log(exp(-W))

def log_posterior(W):
    return log_prior(W) + log_likelihood(data['n1'], data['n2'], data['correct'], W)

import pandas as pd
data = pd.read_csv("Metropolis-data.csv")

log_likelihood(data['n1'], data['n2'], data['correct'], 0.9)

hypothesis_list = []
posterior_score = []
hypothesis_list.append(np.random.rand())

w_current = hypothesis_list[-1]
w_next = hypothesis_list[-1] + np.random.normal(0, 0.1)
rand = np.random.uniform(0,1)

def metropolis(sample_size):
    for i in range(0, sample_size) :
        w_current = hypothesis_list[-1]
        #print("W is : ", w_current)
        w_next = hypothesis_list[-1] + np.random.normal(0, 0.1)
        #print("W' is : ", w_next)

        if exp((log_posterior(w_next))-(log_posterior(w_current))) > 1:
            hypothesis_list.append(w_next)
            posterior_score.append(log_posterior(w_next))
        else :
            rand = np.random.uniform(0,1)
            ratio = exp((log_posterior(w_next))-(log_posterior(w_current)))
            if ratio > rand :
                hypothesis_list.append(w_next)
                posterior_score.append(log_posterior(w_next))
            else :
                hypothesis_list.append(w_current)
                posterior_score.append(log_posterior(w_current))
    return hypothesis_list, posterior_score

sample300 = metropolis(300)
plt.title('(4a) Posterior scores over 300 samples')
plt.xlabel('# of samples')
plt.ylabel('Posterior score of W')
plt.plot(np.arange(300),sample300[1])
plt.show()

plt.title('(4b) W values over 300 samples')
plt.xlabel('# of samples')
plt.ylabel('W value')
plt.plot(np.arange(300),sample300[0][1:])
plt.show()

burn_in = metropolis(1000)
sample10000 = metropolis(10000)

plt.title('(4c) W values over 10,000 samples')
plt.xlabel('value of W')
plt.ylabel('# of samples')
plt.hist(sample10000[0][1000:])
plt.show()

w_in_interval = np.sum([1 if i>.2 and i<.3 else 0 for i in sample10000[0]])/len(sample10000[0])
