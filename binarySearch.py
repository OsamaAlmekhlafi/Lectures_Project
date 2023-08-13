
# *BY Osama Abdo Modhish*

def binary_search(list, target):
    left = 0
    right = len(list) - 1

    while left <= right:
        mid = (left + right) // 2

        if list[mid] == target:
            return mid
        elif list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


list = [7, 19, 88, 16, 54, 23]
target = input("Enter The number ")

result = binary_search(list, int(target))
if result != -1:
    print("Element is found in the List", result)
else:
    print("Element not found in the List")
