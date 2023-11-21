alphabet = "abcdefghijklmnopqrstuvwxyz" * 10
for i in range(0,len(alphabet),2):
    if i == 0:
        print(alphabet[0])
    else:
        print(alphabet[0:i + 1])