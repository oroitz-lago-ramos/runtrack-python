alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Sur python le dernier élément d'une liste ou d'un string est accessible par -1, et ainsi de suite
for i in range(1, len(alphabet) + 1):
    print(alphabet[-i], end="")