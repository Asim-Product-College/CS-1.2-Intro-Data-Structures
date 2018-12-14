#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]
        self.number_of_entries = 0

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    # Lucia get and set function ideas.
    def __getitem__(self, key):
        #get an item with subscripting syntax
        self.get(key)

    def __setitem__(self, key):
        #get an item with subscripting syntax
        self.set(key, value)

    def __len__(self):
        return self.number_of_entries

    def __iter__(self):
        return self.generator();

    # yeild - when you call the function, the code you have written in the function body does not run.
    # The function only returns the generator object.
    def generator(self):
        for bucket in self.buckets:
            for entry in bucket:
                yield entry

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(n^2) Loops through all the buckets and key value pairs in a nested for loop."""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys #returns list of all keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(nk) Loops through all the buckets and key value pairs in a nested for loop.
        k reps the items in the bucket."""
        # TODO: Loop through all buckets
        # TODO: Collect all values in each bucket
        print("McDonalds $1 VALUE MENU")
        mcdonalds_dollar_value_menu = []
        for bucket in self.buckets:
            for key,value in bucket.items():
                mcdonalds_dollar_value_menu.append(value)
        return mcdonalds_dollar_value_menu
            

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(n) aka O(b*l) always iterates through the hash table in a for loop"""
        # Collect all pairs of key-value entries in each bucket.
        # u gottsta access all item in the array and then make space for em.
        all_items = []
        for bucket in self.buckets: # b times.
            all_items.extend(bucket.items()) #ur not calling extend or item a bunch of times so you don't times em. they're sequential so it's just l + l.
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(nk) always iterates thhough the hash table in a nested for loop"""
        # TODO: Loop through all buckets
        # TODO: Count number of key-value entries in each bucket    
        total_kv_entries = 0 # count the length with this var.
        for bucket in self.buckets: #for every key:value pair in the hashmap
            total_kv_entries += bucket.length() #add for every key val pair in the bucket
        return total_kv_entries

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Running time: O(n) - not sure why though.
        n is linear.
        n reps size of inputs (# of key val entries
        this code is broken!
        O(n) reps worst case scenario, n in hashmap is the # of nodes u traverse.
        but in linkedlist n reps the number of items in the linkedlist.
        argu is a thing u give to a func
        param is the thing u recieve. most ppl in industry don't even know this.

        ll find methods worst case O(n) - num of nodes in ll, length aka items
        in this context we have a different n.
        O(l) is length of one linkedlist bucket.
        so how do we get l? Move to get method.
        Best case O(1) is what we're looking for is at the head.
        """
        # Find bucket where given key belongs
        bucket_index = self._bucket_index(key)
        found = False
        bucket = self.buckets[bucket_index]
        
        # lambda function will return True if items key == item, else False... maybe not actually.
        item = bucket.find(lambda item: item[0] == key)
        if item is not None:
            found = True
        return found

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(l) as I loop through the array adn get each item in the bucket.
        2 constant steps with l at the end.
        l = # of entries / # of buckets 
        n = # of entries
        b = # of buckets
        l = n / b
        b is given in our linked list.
        l will be the aprox average bc hash is usually really good at distributing things.
        entry = bucket.find
        return entry[1]
        """
        # Find bucket where given key belongs
        # Check if key-value entry exists in bucket
        # If found, return value associated with given key
        # Otherwise, raise error to tell user get failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        bucket_index = self._bucket_index(key)
        bucket = self.buckets[bucket_index]
        item = bucket.find(lambda item: item[0] == key)

        if item is None:
            raise KeyError('Key not found: {}'.format(key))
        return key_value[1]

        # instead - use find here!
        
        # get each item in the bucket. - another operation. rewrite this bc it could be worse, and using more memory.
        for ikey,value in bucket.items():
            if ikey == key:
                return value
        raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        Running time: O(n)
        drop the constants and lower levels"""
        # Find bucket where given key belongs
        bucket_index = self._bucket_index(key)
        bucket = self.buckets[bucket_index]
        # cost of running bucket find: O(l)
        # python idimaticlaly prefers peopel to try catch and fail fast cuz error handling has been v slow in python
        # ask for forgiveness not permission
        node_data = bucket.find(lambda item: item[0] == (key)) #we're only checking the key against it.
        # If found, update value associated with given key
        if (node_data != None): #if the val is not null.
            bucket.delete(node_data) #remove the whole tuple here and insert brand new one later.
        # might need an else here?
        # Otherwise, insert given key-value entry into bucket
        tuple = (key, value)
        bucket.append(tuple)
        self.number_of_entries+=1


    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(l) for every item in the the bucket items, check it's keys"""
        bucket_index = self._bucket_index(key)
        bucket = self.buckets[bucket_index]
        # bucket.find(key)
        # if item:
        #     bucket delete
        # else;
        #     raiseError
        for node_data in bucket.items():
            if node_data[0] == key:
                bucket.delete(node_data)
                self.number_of_entries-=1
                return
        # Find bucket where given key belongs
        # Check if key-value entry exists in bucket
        # If found, delete entry associated with given key
        # Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        raise KeyError('Key not found: {}'.format(key))

    def length(self):
        # l is going to happen b times.
        # so run time O(n) or O(b*l)
        length = 0 #const time 
        for bucket in self.buckets: #O(b) - exact num of iterations.
            length += bucket.length() # += constant time, method.length is O(l)

        

def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))
    ht.values()

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))
    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
