#!/usr/bin/env python
class TestCase:

    def helloWorld(self):
        print 'Hello World'

    def hashStr(self, str):
        hashTable = {}

        # hash each char in the str
        for item in str:
            hashTable[item] = True

        return hashTable

    def remove(self, str1, str2):
        hashTable = self.hashStr(str2)

        newStr = ''
        for item in str1:
            if item not in hashTable:
                newStr += item

        return newStr

testCase = TestCase()
print testCase.remove('abcdddghkdffeayweisfxxxdds', 'abcdefaaidasbkd')
