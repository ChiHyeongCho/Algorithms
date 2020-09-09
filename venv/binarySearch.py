def binarySearch(array, target, left, right):

    middle_idx = (left+right)//2
    middle = array[middle_idx]

    if target == middle:

        print('answer {}'.format(middle_idx))

    elif middle > target:

        binarySearch(array, target,left,middle_idx-1)

    elif middle < target:
        binarySearch(array, target,middle_idx+1,right)
    else:
        return False

    import bisect