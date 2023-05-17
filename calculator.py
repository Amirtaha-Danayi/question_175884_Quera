def calculate_floor(string):
    floor = 0 
    list = []
    for i in string:
        list.append(i)
    
    for x in list:
        if x == 'U':
            floor+=1
        else:
            floor-=1
    return(floor)