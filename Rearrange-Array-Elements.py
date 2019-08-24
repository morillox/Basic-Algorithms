

def rearrange_digits(input_list):
    numONE = ""
    numTWO = ""
    input_list = sorting_function(input_list)

    for index in range(0, len(input_list), 2):
        numONE = str(input_list[index]) + numONE
        try:
            numTWO = str(input_list[index+1]) + numTWO
        except Exception:
            return [int(numONE), int(numTWO)]

    return [int(numONE), int(numTWO)]


def sorting_function(array):
    if len(array) <= 1:
        return array

    midway = int(len(array)/2)
    left, right = sorting_function(array[:midway]), sorting_function(array[midway:])
    return merge_function(left, right)


def merge_function(left, right):
    result = []
    leftPO = rightPO = 0

    while leftPO < len(left) and rightPO < len(right):
        if left[leftPO] < right[rightPO]:
            result.append(left[leftPO])
            leftPO += 1
        else:
            result.append(right[rightPO])
            rightPO += 1

    result.extend(left[leftPO:])
    result.extend(right[rightPO:])

    return result


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[2, 4, 3, 1, 5], [542, 31]])
