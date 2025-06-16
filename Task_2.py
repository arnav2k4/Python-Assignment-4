userWrite = input("Enter text to write in the file: ")

outWrite = open("output.txt", "w")

outWrite.write(userWrite)
outWrite.write("\n")
print("Data successfully written to output.txt.")
print()

outWrite.close()

userAppend = input("Enter data to append in the file: ")

outAppendRead = open("output.txt", "a+")
outAppendRead.write(userAppend)
print("Data successfully appended.")
print()

print("Final content of output.txt")
outAppendRead.seek(0)
print(outAppendRead.read())

outAppendRead.close()
