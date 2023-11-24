def rectangle(width, height):
    for i in range(0, height):  
        if i == 0 or i == height - 1: 
            width_draw = ""
            for j in range(0,width):
                width_draw += '-'
            width_draw = "|" + width_draw + "|"
            print(width_draw)
        else:
            width_draw = ""
            for j in range(0,width):
                width_draw += ' '
            width_draw = "|" + width_draw + "|"
            print(width_draw)
            
def rectangle_simplifie(width, height):
    pass
rectangle(15, 5)