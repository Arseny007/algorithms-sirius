

def insertion_sort(array):
    for i in range(len(array)):
        item_to_insert = array[i]
        j = i

        while j > 0 and item_to_insert < array[j-1]:
            array[j] = array[j-1]
            j -= 1

        array[j] = item_to_insert
        print(f'step {i}, sorted {i+1} elements: {array}')

#first_array = [2, 9, 11, 7, 1]
#print(insertion_sort(first_array))

digit_length = [4, 4, 3, 3, 6, 4, 5, 4, 6, 6]

def key(index):
    return digit_length[index]

def insertion_sort(array):
    for i in range(len(array)):
        item_to_insert = array[i]
        j = i

        while j > 0 and key(item_to_insert) < key(array[j-1]):
            array[j] = array[j-1]
            j -= 1

        array[j] = item_to_insert
        print(f'step {i}, sorted {i+1} elements: {array}')


second_array = [7, 9, 4, 8, 2]

#def less(card_1, card_2):  # функция-компаратор
#    return digit_lengths[card_1] < digit_lengths[card_2]

def less(a, b):
    if [digit_length[a], a] < [digit_length[b], b]: return True

    return False

def insert_sort_by_comporator(array, comporator):
    for i in range(len(array)):
        # print(f'i: {i}, value: {array[i]}')
        
        item_to_insert = array[i]
        j = i
        
        while j > 0 and comporator(item_to_insert, array[j-1]):
            array[j] = array[j-1]
            j -= 1
            
        array[j] = item_to_insert
        print(f'step {i}, sorted {i+1} elements: {array}')

insert_sort_by_comporator([9, 7, 2, 4, 8, 3], less)
