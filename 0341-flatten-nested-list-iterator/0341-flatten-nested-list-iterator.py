# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList = []
        self.count = 0
        for nestedInteger in nestedList:
            self.helper(nestedInteger)
    
    def helper(self,nestedInteger:NestedInteger):
        if nestedInteger.isInteger():
            self.nestedList.append(nestedInteger.getInteger())
        else:
            for integer in nestedInteger.getList():
                self.helper(integer)
    def next(self) -> int:
         
        temp = self.nestedList[self.count]
        self.count += 1
        return temp
        
    
    def hasNext(self) -> bool:
        return self.count != len(self.nestedList)
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())