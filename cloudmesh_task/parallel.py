def Sequential (execution_array, f, **kwargs):
    result = {}
    print "ARGS", kwargs
    for element in execution_array:
        result[element] = f(element, **kwargs)
    return result
                
def Parallel (execution_array, f, **kwargs):
    result = {}
    for element in execution_array:
        result[element] = f.delay(element, **kwargs)

    for element in execution_array:        
        result[element].get(propagate=False)
    return result
