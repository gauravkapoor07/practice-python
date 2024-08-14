def main():
    try:
        a = int(input("Hey, Enter a number:"))
        print(a)


    except Exception as e:
            print(e)

    finally:   #It can run with either try is executed or not
            print("hey, I am Inside of Fianlly")

main()