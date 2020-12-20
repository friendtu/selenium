from functools import wraps

def log(f):
    @wraps(f)
    def wrapper(*args,**kwds):
        print("Calling decorated funciton")
        f(*args,**kwds)
    return wrapper

@log
def example():
    print("called example function")

example()

