with open("file1.txt") as f:
    content1 = f.read()
with open("file2.txt") as f:
    content2 = f.read()

if(content1 == content2):
    print("The Content is identical")
else:
    print("The Content is not identical")
