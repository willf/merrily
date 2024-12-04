import sys
import os


def hello():
    return "Hello, world!"


if __name__ == "__main__":
    print(hello())
    print("This is the path to the script: ", os.path.realpath(__file__))
    print("This is the path to the interpreter: ", sys.executable)
    print("This is the path to the current working directory: ", os.getcwd())
    print("This is the name of the module: ", __name__)
