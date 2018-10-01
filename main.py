#Ulysses Atkeson, 9/30/18, implement a HashTable
#EC DONE!
#Q1: Primes are better, take 1260 (has a lot of factors) vs 1259 (prime). any mutiple of 10 will end in 0 if moded by 1260. NOT GOOD it is somewhat predicatble. but that is not the case with 1259
#Q2: No, that means you can only have 599 unique hashes and abc is the same as cba or acb...
#Q3: I looked into Python's hash function and did some online reasearch into java's

import random, unittest, string, statistics

def randomword(length):
    #random.seed()
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

class HashTable:
    def __init__(self, capacity):
        self.cap = capacity
        self.arr = [None]*self.cap
    def put(self, key, value):
        if self.arr[self.hashCode(key)] == None:
            self.arr[self.hashCode(key)] = value
        else:
            print("ERROR: Collision at " + str(self.hashCode(key)))
    def get(self, key):
        return self.arr[self.hashCode(key)]
    def hashCode(self, key): #this is EC
        modKey = self.cap #this will change on array size
        retValue = 0
        random.seed(5280) #same start every time very import!!
        #this is sudo random by controlling the seed we can make it work the same every time
        colValue = 0 # to prevent fips form being the same ex eh an he
        pow = 5
        for i, x in enumerate(key): #will loop through the chars in the string
            if (len(key)/2 + len(key)%2) > i:# if you have not gone 1/2 way thought the string
                colValue = ord(x)^pow + ord(key[random.randint(0, len(key)-1)])#the ^5 is to prevent fips form being the same ex eh an he
                if colValue == 0:
                    colValue = 1
                random.seed(colValue)# change seed to col value

                retValue = (retValue + (ord(x)*ord(key[len(key)-i-1]))/colValue%modKey)%modKey #multiply the two char values equal distance from the middle mod by modkey
        return retValue
    def defaultHashCode(self, key): #this is EC
        return hash(key)%self.cap

class TestMethods(unittest.TestCase):
    def test_init(self):#idk about this one
        print("running init test")
        h = HashTable(1000)
        self.assertEqual(h.get("0"), None)
        print("init test complete")
        print

    def test_put_and_get(self):
        print("running put and get test")
        h = HashTable(1000)
        self.assertEqual(h.get("test"), None)
        h.put("test", "ing")
        h.put("do", "thing")
        self.assertEqual(h.get("test"), "ing")
        self.assertEqual(h.get("do"), "thing")
        self.assertEqual(h.get("idk"), None)
        print("put and get test complete")
        print

    def test_distro_small(self):
        print("running small distribution test")
        tableSize = 10
        testSize = 100000
        ideal = testSize/tableSize
        h = HashTable(tableSize)
        sumArr = [0]*tableSize
        defaultSumArr = [0]*tableSize
        hashArr = []
        random.seed()
        for x in range(0, testSize):#huge speed bennfits b/c of random.seed()
            hashArr.append(randomword(random.randint(1, 10)))
        for x in range(0, testSize):
            temp = h.hashCode(hashArr[x])
            defaultTemp = h.defaultHashCode(hashArr[x])
            sumArr[temp] = sumArr[temp] + 1
            defaultSumArr[defaultTemp] = defaultSumArr[defaultTemp] + 1
        self.assertEqual(sum(sumArr), testSize)
        print("small distribution test complete")
        print
        print("put " + str(testSize) + " key pairs into a size " + str(tableSize) + " dict ideal number is " + str(ideal) + " for all")
        print
        print("my distribution: " + str(sumArr))
        print("default distribution: " + str(defaultSumArr))
        print
        print("my min value : " + str(min(sumArr)) + ", default min value : " + str(min(defaultSumArr)))
        print("my max value : " + str(max(sumArr)) + ", default max value : " + str(max(defaultSumArr)))
        print
        myIdeal = statistics.stdev(sumArr)
        defaultIdeal = statistics.stdev(defaultSumArr)
        print("my standard deviation : " + str(myIdeal) + ", default standard deviation : " + str(defaultIdeal))
        print
        if myIdeal < defaultIdeal:
            print("based on standard deviation my hash is " + str(abs(myIdeal-defaultIdeal)/defaultIdeal*100) + " % closer to equaly distibuted")
        else:
            print("based on standard deviation my hash is " + str(abs(myIdeal-defaultIdeal)/defaultIdeal*100) + " % farther from equaly distibuted")
        print

    def test_distro_big(self):
        print("running big distribution test")
        tableSize = 100
        testSize = 100000
        ideal = testSize/tableSize
        h = HashTable(tableSize)
        sumArr = [0]*tableSize
        defaultSumArr = [0]*tableSize
        hashArr = []
        random.seed()
        for x in range(0, testSize):#huge speed bennfits b/c of random.seed()
            hashArr.append(randomword(random.randint(1, 10)))
        for x in range(0, testSize):
            temp = h.hashCode(hashArr[x])
            defaultTemp = h.defaultHashCode(hashArr[x])
            sumArr[temp] = sumArr[temp] + 1
            defaultSumArr[defaultTemp] = defaultSumArr[defaultTemp] + 1
        self.assertEqual(sum(sumArr), testSize)
        print("big distribution test complete")
        print
        print("put " + str(testSize) + " key pairs into a size " + str(tableSize) + " dict ideal number is " + str(ideal) + " for all")
        print
        print("my min value : " + str(min(sumArr)) + ", default min value : " + str(min(defaultSumArr)))
        print("my max value : " + str(max(sumArr)) + ", default max value : " + str(max(defaultSumArr)))
        print
        myIdeal = statistics.stdev(sumArr)
        defaultIdeal = statistics.stdev(defaultSumArr)
        print("my standard deviation : " + str(myIdeal) + ", default standard deviation : " + str(defaultIdeal))
        print
        if myIdeal < defaultIdeal:
            print("based on standard deviation my hash is " + str(abs(myIdeal-defaultIdeal)/defaultIdeal*100) + " % closer to equaly distibuted")
        else:
            print("based on standard deviation my hash is " + str(abs(myIdeal-defaultIdeal)/defaultIdeal*100) + " % farther from equaly distibuted")
        print


if __name__ == '__main__':
    #unittest.main()
    1259
    for x in range()
