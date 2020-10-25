import numpy

def mid_rule(n, interval, my_func):
    '''Approximates the area between a given curve f(x) and the line x=0 within a closed interval [a,b] using the Midpiont Rule '''

    delta_x = (interval[1] - interval[0])/n

    endpoints = []
    for i in numpy.arange(interval[0]+delta_x, interval[1]+delta_x, delta_x):
        endpoints.append( 1./2 * ( (i-delta_x) + i))

    endpoints = my_func(endpoints)
    result = sum(endpoints)
    result *= delta_x
    
    return result

def trap_rule(n, interval, my_func):
    '''Approximates the area between a given curve f(x) and the line x=0 within a closed interval [a,b] using the Trapezoidal Rule '''

    delta_x = (interval[1] - interval[0])/n
    endpoints = [] 
    for i in numpy.arange(interval[0], interval[1]+delta_x, delta_x):
        endpoints.append(i)

    endpoints = my_func(endpoints)

    # the first and last term stay unchanged. This is why the for loop only goes through indices 1 to (and including) len(endpoints)-2 
    for i in range(1,len(endpoints)-1):
        endpoints[i] = endpoints[i]*2
    
    result = sum(endpoints)
    result *= (delta_x/2)

    return result

def simpsons_rule(n, interval, my_func):
    '''Approximates the area between a given curve f(x) and the line x=0 within a closed interval [a,b] using Simpson's Rule '''

    delta_x = (interval[1] - interval[0])/n
    endpoints = [] 
    for i in numpy.arange(interval[0], interval[1]+delta_x, delta_x):
        endpoints.append(i)

    endpoints = my_func(endpoints)
    # the first and last term stay unchanged. This is why the for loop only goes through indices 1 to endpoints-2
    for i in range(1,len(endpoints)-1):
        
        # if my index is odd, multiply by four, otherwise multiply by two.
        if (i%2)==1:
            endpoints[i] = endpoints[i]*4
        else:
            endpoints[i] = endpoints[i]*2

    result = sum(endpoints)
    result *= (delta_x/3)

    return result