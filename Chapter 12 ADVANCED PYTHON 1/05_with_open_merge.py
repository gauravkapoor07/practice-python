with (
    open('file.txt') as f1,
    open('file1.txt') as f2
):
    content1 = f1.read()
    content2 = f2.read()

# You can now use multiple context managers in a single with statement more cleanly
# using the parenthesised context manager