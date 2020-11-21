def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    # create a dictionary to hold (weight, length)
    cache = {}
    for i in range(length):
        cache[weights[i]] = i
    # calculate the variance between weights and limit
    for i in range(length):
        var = limit - weights[i]
    # check if the variance match with any of the weights
    # return a tuple of weight , variance 
        if var in cache:
            return (max(i, cache[var]), min(i, cache[var]))

    return None


