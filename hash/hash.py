
def hash_func(key):
    """
    # modular based hash function
    index를 특정 range안으로 return해준다
    :param key:
    :return: index
    """
    return key % 10

hash_table = list([0 for i in range(10)])
def storage_data(hash_address, data):
    """
    :param hash_address: index
    :param data: key
    """
    hash_table[hash_address] = data

def get_data(key):
    return hash_table[hash_func(key)]

dial_code = dict()
dial_code[86] = 'China'
dial_code[91] = 'India'
address = hash_func(86)
storage_data(address, dial_code[86])
print (get_data(86))