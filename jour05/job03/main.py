def draw_triangle(height):
    print(" " * (height - 1) + "/\\")
    for i in range(1, height):
        if i == height - 1:
            print("/" + "_" * (i*2) + "\\")
        else:
            print(" " * (height-i -1) + "/" + " " * (i*2) + "\\")
draw_triangle(20)