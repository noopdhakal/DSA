
# anup * anup 9 

count = 1
def print_name(name):
    global count
    if count <= 10:
        print(name)
        count += 1
        print_name(name)

print_name("Anup")
