def announce(A):
    def wrapper():
        print("About to run the function...")
        A()
        print("Done with the funcition")
    return wrapper

@announce
def hello():
    print("Hello, world!")

hello()