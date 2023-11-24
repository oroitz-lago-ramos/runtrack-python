def draw_carpet(n):
    print("+" + "-" * (n + 1) +"+")
    for i in range(n ,-1,-1):
        carpet_list = ["#"] * (n + 1)
        carpet_list[i] = ' '
        carpet = "".join(carpet_list)
        print("|" + carpet + "|")
    print("+" + "-" * (n + 1) +"+")
    
draw_carpet(15)