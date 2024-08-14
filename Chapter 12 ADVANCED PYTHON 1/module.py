def myFunc():
    print("Hello World")

if __name__ == "__main__": # Due to this, the below written code will only execute if it is run from module and will not work if this is imported
    # If the code is directly executed by running the file its present in
    print("We are directly running the code")
    myFunc()
    print(__name__)


# IT tells that if the code is run from original source then it shows(__main__)
# Otherwise if this code run by another program by importing then it shows the name of the file the source code is present in.