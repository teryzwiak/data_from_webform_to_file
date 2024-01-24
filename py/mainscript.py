username = input("Enter username: ")

f = open("demofile.txt", "w")
f.write(username)
f.close()