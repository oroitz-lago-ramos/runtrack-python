def distance_walked_per_week(steps, height):
    height_m = height / 100
    total_m = round(steps*height_m*5*2*7,2)
    print(f"Pour {steps} marches de {height} cm, le gardien parcourt {total_m} m par semaine.")
    
distance_walked_per_week(152,49)