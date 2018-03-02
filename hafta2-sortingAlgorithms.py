import random

def bubleSort(arr):
    n = len(arr)
    comparison = 0

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            comparison += 1
    return comparison


def insertionSort(arr):
    n = len(arr)

    comprasion = 0
    for i in range(1, n):

        temp = arr[i]
        j = i - 1

        while j >= 0 and temp < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            comprasion += 1

        arr[j+1] = temp
    return comprasion


def createRandomArrayBySize(size, limit):
    tempArray = []
    for i in range(size):
        tempArray.append(random.randint(0, limit))

    return tempArray


def square(arr):

    n = len(arr)
    comprasion = 0

    for i in range(n):
        arr[i] *= arr[i]
        comprasion += 1

    return comprasion

size = int(input("Enter size of Array: "))
lim = int(input("Enter top limit of numbers: "))
arr1 = createRandomArrayBySize(size, lim)
# bubleSort(arr1)
# insertionSort(arr1)
comprasion_sqaure= square(arr1)
comprasion_insertionSort = insertionSort(arr1)
comprasion_bubleSort = bubleSort(arr1)

print("Buble Sort number of comprasion: {}".format(comprasion_bubleSort))
print("Insertion Sort number of comprasion: {}".format(comprasion_insertionSort))
print("Square number of comprasion: {}".format(comprasion_sqaure))
