from HashMapImpl import HashMap

lookup_hashmap = HashMap()


def set_lookup_log(key, value):
    lookup_hashmap.insert(key, value)


def get_lookup_log():
    return lookup_hashmap
