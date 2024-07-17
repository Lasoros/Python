

while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break

#this loop is exactly the same as the one is while loops
#must be sure to ALWAYS HAVE A BREAK STATEMENT as this is an inf loop