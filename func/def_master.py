#bin/python3_6



import math as M
import numpy as np 
    
    
def searchmaxima(maxima, distance, data, scale_vector=0):
    
    '''
    To find maxima in data, with option to give vecotr with scaling values for x-Axis
    
    Input:
    maxima    scalar        value of maxima to find
    distance  scalar        value for nearest next maxima to search for
    data      1-D array     numpy array of data 
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
    
    amp_values = np.zeros((np.shape(input_data)[1]))
    frequency_indices = np.zeros_like(amp_values)
    frequency_values = np.zeros_like(amp_values)
    
    
    max_array = np.zeros_like(input_data)
    for j in range(np.shape(input_data)[1]):
        win_average = np.mean(input_data.T[j])
        #if win_average < all_win_average:
        # not a good solution. deletes as well some instrument signal

        amp_values[j], frequency_indices[j], frequency_values[j] = searchmaxima(maxima=maxima, data=input_data.T[j],distance=distance, scale_vector=freq_vec)

        #print(any(frequency_value<freq_minimal_value))
        if any(frequency_values<freq_minimal_value) == True:
            #print((frequency_value))
            for i in range(len(frequency_indices)):


                if amp_values[i] > threshold:
                    max_array[int(frequency_indices[i]),j] = amp_values[i]
    return (max_array, amp_values, frequency_indices, frequency_values)