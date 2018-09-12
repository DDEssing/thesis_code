#bin/python3_6



import math as M
import numpy as np

def _nearest_pow_2(x):
    """
    copied from obspy specgram
    Find power of two nearest to x
    >>> _nearest_pow_2(3)
    2.0
    >>> _nearest_pow_2(15)
    16.0
    :type x: float
    :param x: Number
    :rtype: Int
    :return: Nearest power of 2 to x
    """
    a = M.pow(2, M.ceil(np.log2(x)))
    b = M.pow(2, M.floor(np.log2(x)))
    if abs(a - x) < abs(b - x):
        return a
    else:
        return b
    
    
    
    
    
def searchmaxima(maxima, data, distance, scale_vector=0):
    
    '''
    To find maxima in data, with option to give vecotr with scaling values for x-Axis
    
    Input:
    maxima    scalar        value of maxima to find
    data      1-D array     numpy array of data 
    distance  scalar        value for nearest next maxima to search for
    freqvec   1-D array     numpy array of data with values to scale x-Axis (optional)
    
    '''

    index_max = np.zeros(maxima)
    value_max_f = np.zeros(maxima)
    value_max = np.zeros(maxima)
    data1 = data.copy()
    
    if type(scale_vector) == int:
    
        for i in range(maxima):
            index_max[i] = np.argmax((data1))
            value_max[i] = np.max((data1))
            #index_max[i] = np.argmax(Pxx_sig1)
            #value_max_f[i] = freqvec[np.argmax(data1)]
            #value_max[i] = np.max(Pxx_sig1)

            minimal_value = np.min(data1)

            data1[int(index_max[i]-distance):int(index_max[i]+distance)] = minimal_value-100
        return(value_max, index_max)
    
    else:
        for i in range(maxima):
            index_max[i] = np.argmax((data1))
            value_max[i] = np.max((data1))
            value_max_f[i] = scale_vector[np.argmax(data1)]
            minimal_value = np.min(data1)
        
            data1[int(index_max[i]-distance):int(index_max[i]+distance)] = minimal_value-100
            
        return(value_max, index_max,value_max_f)
    
    
def sorting_out_peaks(input_data, freq_vec, maxima, distance ,threshold, freq_minimal_value):
    '''
    Calls searchmaxima and just hands maxima values which meet with two options:
            - there is a maximum below a certain frequency value (freq_minimal_value)
            - maximum amplitude value is higher then certain ampiltude (threshold) 
    
    
    '''
    
    
    max_array = np.zeros_like(input_data)
    for j in range(np.shape(input_data)[1]):
        win_average = np.mean(input_data.T[j])
        #if win_average < all_win_average:
        # not a good solution. deletes as well some instrument signal

        amp_value, frequency_index, frequency_value = searchmaxima(maxima=maxima, data=input_data.T[j],distance=distance, scale_vector=freq_vec)

        #print(any(frequency_value<freq_minimal_value))
        if any(frequency_value<freq_minimal_value) == True:
            #print((frequency_value))
            for i in range(len(frequency_index)):


                if amp_value[i] > threshold:
                    max_array[int(frequency_index[i]),j] = amp_value[i]
    return max_array