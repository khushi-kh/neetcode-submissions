class MyHashSet:

    def __init__(self):
        self.temp = [False] * 1000001 # because array size is fixed
        

    def add(self, key: int) -> None:
        self.temp[key] = True
        

    def remove(self, key: int) -> None:
        self.temp[key] = False
        

    def contains(self, key: int) -> bool:
        return self.temp[key]

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)