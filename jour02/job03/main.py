# for i in range(0,101):
#     if (i != 26) and (i != 37) and (i != 88):
#         print(i)

ban_list= [26, 37, 88]     
for i in range(0,101):
    if i not in ban_list:
        print(i)