# Ch.5 Hash Tables

## Hash functions

- A hash function is a function that maps strings to numbers.
- The number can be associated to the index of an array, in which the index stores the return value (number, string, etc)
- The hash function knows how big your array is and only returns valid indexes.
- Has many names, depending on language: hash maps, maps, dictionaries, and associative arrays

### Checking duplicates

In Python, the dictionary object has the `get()` function which returns a value if the key is in the hash table.  If not, it will return `None`.

Since it doesn't have to check every item in a list like an array, ideally it will have _constant time_, ie. it has a call stack height of `O(1)` where the time taken to perform an operation stays the same, regardless of how big the hash table is.

Simplified example of how caching works:

```py
def get_page(url):
  if cache.get(url):
    return cache[url]
  else:
    data = get_data_from_server(url)
    cache[url] = data
    return data
```

### Recap

Hash tables are good for:
- Modeling relationships from one thing to another thing
- Filtering out duplicates
- Caching/memorizing data instead of making your server do work

## Collisions and Performance

- Ideally, your hash function should map keys evenly all over the hash. When it doesn't and map keys to the same hash, it's called a _collision_. To get around this, a simple workaround is to use a _linked list_.
- A poor hash function could map all keys to a single slot and create one long _linked list_ (i.e. a key with an value that maps to another key and so forth).  This would be as slow as putting all the items in a list.
- To avoid collisions, you need 1) a low load factor (number of items in a hash table / total number of slots) and 2) a good hash function.


## Recap

- You can make a hash table by combining a hash function with an array.
- Collisions are bad. You need a hash function that minimizes collisions.
- Hash tables have really fast search, insert, and delete.
- Hash tables are good for modeling relationships from one item to another item.
- Once your load factor is greater than 0.7, it’s time to resize your hash table.
- Hash tables are used for caching data (for example, with a web server).
- Hash tables are great for catching duplicates.

