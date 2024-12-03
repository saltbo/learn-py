# time: O(n), space: O(n)
# def moveElementToEnd(array, toMove):
#     notToMove = []
#     toMoveItems = []
#     for idx in range(len(array)):
#         if array[idx] != toMove:
#             notToMove.append(array[idx])
#         else:
#             toMoveItems.append(toMove)
#     return notToMove + toMoveItems

# time: O(n^2), space: O(1)
# def moveElementToEnd(array, toMove):
#     idx = 0
#     count = 0
#     while idx + count < len(array):
#         if array[idx] == toMove:
#            num = array.pop(idx)
#            array.append(num)
#            count+=1
#         else:
#            idx+=1
#     return array

# time: O(n), space: O(1)
def moveElementToEnd(array, toMove):
    left = 0
    right = len(array) - 1
    while left < right:
        if array[left] == toMove and array[right] != toMove:
            array[left], array[right] = array[right], array[left]
        elif array[left] == toMove and array[right] == toMove:
            right -= 1
        else:
            left += 1
                
    return array

array = [2, 1, 2, 2, 2, 3, 4, 21] 
toMove = 2
print(moveElementToEnd(array, toMove))