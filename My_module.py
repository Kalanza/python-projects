print('Imported My module...')

test = 'Test String'

def find_index(to_search, target):
    '''Find the index of a value in a text'''
    for i,value in enumerate(to_search):
        if value == target:
            return i
    return -1