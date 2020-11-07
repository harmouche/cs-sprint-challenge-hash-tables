def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache_list = [1] * len(a)

    actual_cache = dict(zip(a, cache_list))

    hasNegatives = []
    for key in actual_cache:
        if key > 0:
            try:
                if actual_cache[key] is not None and actual_cache[-key] is not None:
                    hasNegatives.append(key)
            except:
                pass

    return hasNegatives


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
