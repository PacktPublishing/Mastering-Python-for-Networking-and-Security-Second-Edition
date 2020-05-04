def printExceptionsTree(ExceptionClass, level = 0):
    if level > 1:
        print("   |" * (level - 1), end="")
    if level > 0:
        print("   +---", end="")
 
    print(ExceptionClass.__name__)
    for subclass in ExceptionClass.__subclasses__():
        printExceptionsTree(subclass, level+1)
 
printExceptionsTree(BaseException)
