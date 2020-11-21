def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    dict = {}

    number_of_lists = len(arrays)
    for each_list in arrays:
        for each_item in each_list:
            if each_item in dict:
                dict[each_item] += 1
            else:
                dict[each_item] = 1

    intersection = []
    for key in dict:
        if dict[key] == number_of_lists:
            intersection.append(key)                

    return intersection


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

