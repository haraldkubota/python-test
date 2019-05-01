# map, reduce, filter and lambda

from functools import reduce

def doubleMe(n: int) -> int:
    return n * 2

def isEven(x: int) -> bool:
    if x%2 == 0:
        return True
    else:
        return False

def sumMe(x: int, y: int) -> int:
    return x+y

print(doubleMe(10))
print(sumMe(10, 11))

# map
def doMapThing():
    myList=[1, 2, 3, 4, 5, 6, 7]

    # myDoubleList=map(doubleMe, myList)
    # myDoubleList=list(map(doubleMe, myList))
    myDoubleList=list(map(lambda x: x*2, myList))

    print(f'myList={myList}, myDoubleList={myDoubleList}')

# reduce
def doReduceThing():
    myList=[1, 2, 3, 4, 5, 6, 7]

    mySum=reduce(sumMe, myList)
    # mySum=reduce((lambda x, y: x+y), myList)
    print(f'myList={myList}, mySum={mySum}')

# filter
def doFilterThing():
    myList=[1, 2, 3, 4, 5, 6, 7]
    myFilteredList = list(filter(isEven, myList))
    # myFilteredList=list(filter(lambda x: x%2==0, myList))

    print(f'myList={myList}, myFilteresList={myFilteredList}')

doMapThing()
doReduceThing()
doFilterThing()

