try:
    fr = open('sample.txt', "r")
    print("Reading file content:")
    i = 1
    for line in fr:
        print("Line {}: {}".format(i, line.strip()))
        i += 1
    fr.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
