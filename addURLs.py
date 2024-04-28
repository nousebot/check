import os

dir = os.path.dirname(os.path.realpath(__file__))
url = input("Enter the URL with {}: ")
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
open(os.path.join(dir, "sourceURLs.txt"), "w").write("")
for i in range(start, end):
    with open(os.path.join(dir, "sourceURLs.txt"), "a+") as f:
        f.write(url.format(i) + "\n")
        f.close()