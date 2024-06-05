import matplotlib.pyplot as plt

# Sorts list containing numeric numbers in-place and in ascending order using a mergesort algorithm
def merge_sort(number_list):
    
    number_list_length = len(number_list)
    
    if (not (number_list_length > 1)):     # If length equals one we have a sorted list
        return

    # Splits the list in the middle
    middle_index = number_list_length // 2
    left_list = number_list[:middle_index]
    right_list = number_list[middle_index:]
    
    merge_sort(left_list)
    merge_sort(right_list)
    
    # Indices for each list
    left_index = 0
    right_index = 0
    target_index = 0
    
    # Lenghts of the lists
    left_length = len(left_list)
    right_length = len(right_list)
    
    # Merges the left and right list by comparing the current values of the left and right lists and then storing them sorted in the orignial list
    while left_index < left_length and right_index < right_length :
        if left_list[left_index] <= right_list[right_index]:
            number_list[target_index] = left_list[left_index]
            left_index += 1
        else:
            number_list[target_index] = right_list[right_index]
            right_index += 1
        target_index += 1
    
    # In case that the left and the right list have diffrent lengths these loops append the remaining values to our original list
    while left_index < left_length:
        number_list[target_index] = left_list[left_index]
        left_index += 1
        target_index += 1
    
    while right_index < right_length:
        number_list[target_index] = right_list[right_index]
        right_index += 1
        target_index += 1


my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
my_list_length = len(my_list)
x_coordinates = range(my_list_length)
plt.plot(x_coordinates, my_list)
plt.show()
merge_sort(my_list)
x_coordinates = range(my_list_length)
plt.plot(x_coordinates, my_list)
plt.show()
