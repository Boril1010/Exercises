class HashMap:
    def __init__(self):
        self.size = 10
        self.buckets = [[] for _ in range(self.size)]
        self.items = 0

    def __len__(self):
        return self.items


    def _hash(self, key):
        keys = str(key)
        total = 0
        hash_key = 0

        if keys.isalpha():
            for char in key:
                total += ord(char)
                hash_key = total % self.size
            return hash_key

        elif keys.isdigit():
            hash_key = key % self.size
            return hash_key


    def rehash(self):
        old_buckets = self.buckets


        self.size *= 2
        self.buckets = [[] for _ in range(self.size)]

        for bucket in old_buckets:
            for item in bucket:

                total = 0
                position = 0

                key = str(item[0])

                if key.isalpha():
                    for char in key:
                        total += ord(char)
                    position = total % self.size
                    self.buckets[position].append(item)
                elif key.isdigit():
                    position = item[0] % self.size
                    self.buckets[position].append(item)


    def insert(self, key, value):


        #increase size
        if self.items >= self.size:
            self.rehash()

        position = self._hash(key)

        if (key, value) in self.buckets[position]:
            return print(f"{key}:{value} already exists")

        for index, item in enumerate(self.buckets[position]):
            if item[0] == key:
                self.buckets[position][index] = (key, value)
                return

        self.buckets[position].append((key, value))
        self.items += 1




    def get(self, key):
        position = self._hash(key)

        for item in self.buckets[position]:
            if item[0] == key:
                return item[1]

        return "key not found"


    def contains(self):
        for bucket in self.buckets:
            for item in bucket:
                print(f"{item[0]}:{item[1]}")



    def remove(self, key):
        position = hash(key)

        if len(self.buckets[position]) == 0:
            return "not found"

        for index, item in enumerate(self.buckets[position]):
            if item[0] == key:
                self.buckets[position].pop(index)
                self.items -= 1
                return print("removed")

        else:
            print("key does not exist")
            return None






# :) 
# :(
# :|



h = HashMap()

h.insert("cat", 10)
h.insert("tac", 20) #-- Collision 
h.insert(100, "hello")

print(h.get("cat"))
print(h.get("tac"))
print(h.get(100))

h.remove("cat")

print(h.get("cat"))

