# Hash Tables
Hash tables are a type of Dictionary that use a hash function on the key to determine where to place values in the array.
```java
key = "hi";
value = "val";

Hashmap h = new Hashmap();
h.put(key,value); //"hi".hashCode() = 3

//hashtable so far
//[ | | |"val" | | ]
```
# Hash Functions
## Properties of a good hash function include:
1. Easy to compute: It should be easy to compute and must not become an algorithm in itself.

2. Uniform distribution: It should provide a uniform distribution across the hash table and should not result in clustering.

3. Less collisions: Collisions occur when pairs of elements are mapped to the same hash value. These should be avoided.

## Cryptographic hash functions have other properties including: 
1. it is infeasible to generate a message from its hash value except by trying all possible messages
2. a small change to a message should change the hash value so extensively that the new hash value appears uncorrelated with the old hash value
3. it is infeasible to find two different messages with the same hash value

# Lab:
## Challenge one: (put answer in your comments)
* Which is a better hashfunction: 
  * x % n where n is a large number with several factors
  * x % n where n is a large prime number
Prove your answer with a simple example.

## Challenge two: (answer in comments)
Is char values summed % 599 a good hash function for strings? Why or why not?

## Challenge three: (answer in comments)
Take a look at Java's HashMap class and how it produces hashed values. (You may have to look at other classes to find the actual mathematical function! Follow the trail of breadcrumbs...)

## Challenge four: (code)
Implement a HashTable for Strings using arrays (caution python users) and a hash function you choose/design.
```java
//initializes an array of size capacity
public HashTable(int capacity)

//put hashes the key to an index in your array, and places the value there. Fails if there are collisions/repeat keys.  
public boolean put(String key, String value)

//get hashes the key to get the index, and returns that element. Returns null if key not found.
public String get(String key)

//returns the unique int in the range of the [0, array length)
private int hashCode(String key)
```
Write a driver to test all methods.

## Extra credit:+2 (code)
Design your own hash function (don't copy/pasta from another site) for your HashTable, and then write a driver that inputs random key value pairs and then analyses the 'quality' of the hash function (the number of collisions, uniformity of distribution or other useful metric).


