import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
    means = np.array([])
    for col in range(data.shape[1]):
        mean = np.sum(data[: ,col]) / data.shape[0] 
        means = np.append(means, mean)    
    #print(means)
    
    diff = np.empty(data.shape)
    for col in range(data.shape[1]):
        for row in range(data.shape[0]):
            diff[row][col] = data[row][col] - means[col]
    #print(diff)
    std_dev = np.array([])
    for col in range(data.shape[1]):
        std_dev = np.append(std_dev, np.sqrt(np.sum(np.square(diff[: ,col])) / data.shape[0]))
    #print(std_dev)
     
    standardized_data = np.empty(data.shape)
    for col in range(data.shape[1]):
        for row in range(data.shape[0]):
            standardized_data[row][col] = (data[row][col] - means[col]) / std_dev[col]
    standardized_data = np.round(standardized_data, 4)
    #print(standardized_data)
    
    
    mins = np.array([])
    maxs = np.array([])
    
    for col in range(data.shape[1]):
        mins = np.append(mins, np.min(data[: ,col]))
        maxs = np.append(maxs, np.max(data[: ,col]))
        
    normalized_data = np.empty(data.shape)
    for col in range(data.shape[1]):
        for row in range(data.shape[0]):
            normalized_data[row][col] = (data[row][col] - mins[col]) / (maxs[col] - mins[col])
    normalized_data = np.round(normalized_data, 4)  
    #print(normalized_data)
    
    return standardized_data, normalized_data