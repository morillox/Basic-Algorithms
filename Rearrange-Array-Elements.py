

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    num1 = ""
    num2 = ""
    input_list = sorting_function(input_list)

    for index in range(0, len(input_list), 2):
        num1 = str(input_list[index]) + num1
        try:
            num2 = str(input_list[index+1]) + num2
        except Exception:
            return [int(num1), int(num2)]

    return [int(num1), int(num2)]


def sorting_function(array):
    if len(array) <= 1:
        return array

    midway = int(len(array)/2)
    left, right = sorting_function(array[:midway]), sorting_function(array[midway:])
    return merge_function(left, right)


def merge_function(left, right):
    result = []
    left_p = right_p = 0

    while left_p < len(left) and right_p < len(right):
        if left[left_p] < right[right_p]:
            result.append(left[left_p])
            left_p += 1
        else:
            result.append(right[right_p])
            right_p += 1

    result.extend(left[left_p:])
    result.extend(right[right_p:])

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
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]