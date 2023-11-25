def distance_walked_per_week(steps, height):
    height_m = height / 100
    print(f"Pour {steps} marches de {height} cm, le gardien parcourt {steps*height_m*5*2*7} m par semaine.")
    
distance_walked_per_week(87,20)