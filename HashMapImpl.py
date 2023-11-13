class HashMap:

    # Total
    # Time complexity: O(n)
    # Space complexity: O(1)

    # Constructor function
    # Time complexity: O(1)
    # Space complexity: O(1)
    def __init__(self, init_cap=30):
        self.hashmap = []
        for i in range(init_cap):
            self.hashmap.append([])

    # Calculating hash number
    # Time complexity: O(1)
    # Space complexity: O(1)
    def get_hash(self, key):
        con = 0.35784
        hashnum = ((len(self.hashmap))*((int(key))*con % 1))//1
        return int(hashnum)

    # Insertion function for data
    # Time complexity: O(n)
    # Space complexity: O(1)
    def insert(self, key, value):
        key_hash = self.get_hash(key)
        key_pair = [key, value]

        if self.hashmap[key_hash] is None:
            self.hashmap[key_hash] = list([key_pair])
            return True
        else:
            for pair in self.hashmap[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.hashmap[key_hash].append(key_pair)
            return True

    # Update function for data
    # Time complexity: O(n)
    # Space complexity: O(1)
    def update(self, key, value):
        key_hash = self.get_hash(key)
        key_pair = [key, value]

        if self.hashmap[key_hash] is None:
            self.hashmap[key_hash] = list([key_pair])
            return True
        else:
            for pair in self.hashmap[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            print('No record found for update')

    # Retrieval function for data
    # Time complexity: O(n)
    # Space complexity: O(1)
    def get(self, key):
        key_hash = self.get_hash(key)
        if self.hashmap[key_hash] is not None:
            for pair in self.hashmap[key_hash]:
                if int(pair[0]) == key:
                    return pair[1]
        return None

    # Deletion function for data
    # Time complexity: O(n)
    # Space complexity: O(1)
    def delete(self, key):
        key_hash = self.get_hash(key)

        if self.hashmap[key_hash] is None:
            print("No record found")
            return False
        for i in range(len(self.hashmap[key_hash])):
            if self.hashmap[key_hash][i][0] == key:
                self.hashmap[key_hash].pop(i)
                print(key, "is deleted")
                return True
        return False
