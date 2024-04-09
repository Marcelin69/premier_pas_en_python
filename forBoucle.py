# list = [0,1,2,3,4,5,6,7,8,9,10]

# for i in list:
#     print(i ,i*i)

ma_list = range(21)

# print("Ma liste : ", ma_list)
for i in ma_list:
    print(i)
    if(i>=5):
        break
    

for i in ma_list:
    if(i<5):
        continue
    print(i)
    
