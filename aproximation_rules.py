import numpy as np
from math import *

def f_of_x(func_str, endpoints):
    ''' User-entered Function

    Takes a mathematical expression as string and computes its result

    Args:
        func_str (string)     : the function to be analized [f(x)]
        endpoints (float list): coordinates of the partitions
    
    Returns:
        A new list of endpoints
    '''
    
    #result = [ (pow(1+(cos(i)), 1./3)) for i in endpoints]
    result = [ eval(func_str) for x in endpoints]

    return result

def mid_rule(interval, delta_x, f_of_x, func_str):
    ''' Midpoint Rule of Integration

    Approximates the area between a given curve f(x) and the line x=0 within a closed interval [a,b] using the Midpiont Rule
    
    Args:
        interval (int list): [a,b]
        my_func (function) : the function to integrate
        delta_x (float)    : length of partitions
    
    Returns:
        Approximate are under f(x) within the interval [a,b]
    
    '''
    endpoints = [ (.5* ( (i-delta_x) + i)) for i in np.arange(interval[0]+delta_x, interval[1]+delta_x, delta_x)]

    endpoints = f_of_x(func_str, endpoints)
    result = np.sum(endpoints)
    result *= delta_x
    
    return result

def trap_rule(interval, delta_x, endpoints):
    ''' Trapezoidal Rule of Integration

    Approximates the area between a given curve f(x) and the line x=0 within a closed interval [a,b] using the Trapezoidal Rule
    
    Args:
        interval  (int list): [a,b]
        my_func   (function): the function to integrate
        delta_x   (float): length of partitions
        endpoints (float list): enpoints of the partitions
    
    Returns:
        Approximate are under f(x) within the interval [a,b]
    
    '''
    
    # the first and last term stay unchanged. This is why the for loop only goes through indices 1 to (and including) len(endpoints)-2 
    for i in range(1,len(endpoints)-1):
        endpoints[i] = endpoints[i]*2

    #endpoints = [endpoints[i]*2 for i in range(1,len(endpoints)-1)]
    
    result = np.sum(endpoints)
    result *= (delta_x/2)

    return result

def simpsons_rule(interval, delta_x, endpoints):
    ''' Simpson's Rule of Integration

    Approximates the area between a given curve f(x) and the line x=0 within a closed interval [a,b] using Simpson's Rule
    
    Args:
        interval  (int list): [a,b]
        my_func   (function): the function to integrate
        delta_x   (float): length of partitions
        endpoints (float list): enpoints of the partitions
    
    Returns:
        Approximate are under f(x) within the interval [a,b]
    
    '''

    # the first and last terms stay unchanged. This is why the for loop only goes through indices 1 to endpoints-2
    for i in range(1,len(endpoints)-1):
        
        # if my index is odd, multiply by four, otherwise multiply by two.
        if (i%2)==1:
            endpoints[i] = endpoints[i]*4
        else:
            endpoints[i] = endpoints[i]*2

    result = sum(endpoints)
    result *= (delta_x/3)

    return result

def compute(n, interval, func_str):
    ''' Main function

    Controls the flow of information on the file; helps minimize redundant functionalities.

    Args:
        n (int)            : number of partitions
        interval (int list): [a,b]
        func_str (str)     : string version of the formula entered by the user.
    
    Returns:
        The area under the cruve and within the interval using all three methods of approximate integration
    '''

    delta_x = (interval[1] - interval[0])/n
    
    # Bescause two different rules use the same set on endpoints, delegate this computation, so it only happens once.
    endpts = [ i for i in np.arange(interval[0], interval[1] + delta_x, delta_x)]

    #enpoints_max = fofx2(my_func, endpts)
    endpts = f_of_x(func_str, endpts)
    endpts_copy = endpts.copy()

    by_midpoint = round(mid_rule(interval, delta_x, f_of_x, func_str), 6)
    by_trapezoidal = round(trap_rule(interval, delta_x, endpts), 6)
    by_simpsons = round(simpsons_rule(interval, delta_x, endpts_copy), 6)   

    return by_midpoint, by_trapezoidal, by_simpsons
