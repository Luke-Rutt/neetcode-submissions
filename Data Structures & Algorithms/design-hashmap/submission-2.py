class MyHashMap:

    def __init__(self):
        self.my_key = []
        self.my_value = []

    def put(self, key: int, value: int) -> None:
        if key not in self.my_key:
            self.my_key.append(key)
            self.my_value.append(value)
        
        else:
            idx = self.my_key.index(key)
            self.my_value[idx] = value

    def get(self, key: int) -> int:
        if key not in self.my_key:
            return -1
        else:
            idx = self.my_key.index(key)
            return self.my_value[idx]

    def remove(self, key: int) -> None:
        if key in self.my_key:
            idx = self.my_key.index(key)
            self.my_key.remove(key)
            self.my_value.pop(idx)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)