def sorter (my_list):
    for srt in range (len(my_list)-1):
        for i in range(len(my_list)-1-srt):
            if my_list[i]>my_list[i+1]:
                my_list[i],my_list[i+1]=my_list[i+1],my_list[i]
    return my_list
my_list=[1,6,8,3,2,45,76,35,0]
sorter(my_list)
print(my_list)