fileName = input("Enter file name (include extension): ")
try:
    fr = open(fileName, "r")
    print("Reading file content:")
    i = 1
    for line in fr:
        print("Line {}: {}".format(i, line.strip()))
        i += 1
except FileNotFoundError:
    print("Error: The file '{}' was not found.".format(aa))
fr.close()
