# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 16:27:06 2017

This is the code to tackle the problem in 5_word2vec.ipynb in the Deep Learning 
free course by Google on UdaCity.

The problem is to use Continuous Bag of Word (CBOW) to train the latent vectors 
of words. This is different from Skip-Gram algorithm.

In Skip-Gram algorithm, the label word is the context words that are surrounding the central
word in each skipping window, i.e., we are using the central word to predict the surrounding 
context words.

In contract, in CBOW algorithm, the label word is the central word in each skipping window,
and we are using the context words to predict the label word. 

The function generate_batch_cbow(batch_size, num_skips, skip_window) is a revision
from https://github.com/wangz10/tensorflow-playground/blob/master/word2vec.py

@author: hangzh
"""

import numpy as np
import collections
import random

def generate_batch_cbow(batch_size, num_skips, skip_window):

    '''
    Batch generator for CBOW (Continuous Bag of Words).
    batch should be a shape of (batch_size, num_skips)

    Parameters
    ----------
    data: list of index of words
    batch_size: number of words in each mini-batch
    num_skips: number of surrounding words on both direction (2: one word ahead and one word following)
    skip_window: number of words at both ends of a sentence to skip (1: skip the first and last word of a sentence)
    '''

    global data_index
    assert batch_size % num_skips == 0
    assert num_skips <= 2 * skip_window
    batch = np.ndarray(shape=(batch_size), dtype=np.int32)
    labels = np.ndarray(shape=(batch_size, 1), dtype=np.int32)
    span = 2 * skip_window + 1 # [ skip_window target skip_window ]
    buffer = collections.deque(maxlen=span) # used for collecting data[data_index] in the sliding window
    # collect the first window of words
    for _ in range(span):
        buffer.append(data[data_index])
        data_index = (data_index + 1) % len(data)
        
    # move the sliding window  
    for i in range(batch_size // num_skips):
        #mask = [1] * span
        #mask[skip_window] = 0 
        #batch[i, :] = list(compress(buffer, mask)) # all surrounding words
        #labels[i, 0] = buffer[skip_window] # the word at the center 
        #buffer.append(data[data_index])
        #data_index = (data_index + 1) % len(data)
        target = skip_window  # target label at the center of the buffer
        targets_to_avoid = [ skip_window ]
        for j in range(num_skips):
            while target in targets_to_avoid:
                target = random.randint(0, span - 1)
            targets_to_avoid.append(target)
            batch[i * num_skips + j] = buffer[target]
            labels[i * num_skips + j, 0] = buffer[skip_window]
        buffer.append(data[data_index])
        data_index = (data_index + 1) % len(data)
    return batch, labels

# To test this function, try the following lines in the context of 5_word2vec.ipynb
print('data:', [reverse_dictionary[di] for di in data[:8]])

for num_skips, skip_window in [(2, 1), (4, 2)]:
    data_index = 0
    batch, labels = generate_batch_cbow(batch_size=8, num_skips=num_skips, skip_window=skip_window)
    print('\nwith num_skips = %d and skip_window = %d:' % (num_skips, skip_window))
    print('    batch:', [reverse_dictionary[bi] for bi in batch])
    print('    labels:', [reverse_dictionary[li] for li in labels.reshape(8)])