import numpy as np

data = np.empty(8, dtype = object) # 8 range

def hash_function(string):
    return hash(string) % 8

class LinearMap:
    def __init__(self):
        self.items = list()

    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):
        data = list()
        for k, v in self.items:
            if key == k:
                data.append(v)
        return data

class BetterMap:
    def __init__(self, n = 100):
        self.maps = []
        for i in range(n):
            self.maps.append(LinearMap())

    def find_map(self, k):
        index = hash(k) % len(self.maps)
        return self.maps[index]

    def add(self, key, value):
        m = self.find_map(key) # LinearMap
        m.add(key, value)

    def get(self, key):
        m = self.find_map(key)
        return m.get(key)

class HashMap:
    def __init__(self):
        self.maps = BetterMap(2)
        self.num = 0

    def resize(self):
        new_maps = BetterMap(self.num * 2)
        for m in self.maps.maps:
            for k, v in m.items:
                new_maps.add(k,v)
        self.maps = new_maps

    def add(self, key, val):
        self.maps.add(key, val)
        
    def get(self, key):
        return self.maps.get(key)

hash_map = HashMap()
hash_map.add(1, 2)
hash_map.add(1, 3)
print(hash_map.get(1))