name =[]
data =[]

# empty list

# next page..........

about =["Kathmandu",123,True]
print(about)
print(about[1])

# answer
# ['Kathmandu', 123, True]
# 123

# next page..........

about =["Kathmandu",123,True]
about[2]=False
print(about)

# answer
# ['Kathmandu', 123, False]

# next page..........

about =["Kathmandu",123,True]
about.append(456)          # in append we can put only one argument
print(about)

# answer
# ['Kathmandu', 123, True, 456]

about =["Kathmandu",123,True]
about.append([456 ,789])          # we can do in this way but this is not good idea
print(about)

# answer
# ['Kathmandu', 123, True, [456, 789]]

# next page..........

data =[
    [20 ,40 ,60 ,80],
    ['ram','sita','shyam','hari']
]
print(data[1][1])

# answer
# sita

# next page..........

data =[
    [20 ,40 ,60 ,80 ,100],
    [11 ,22 ,33 ,[[[100]],200] ,44 ,55 ,66]
]
print(data[1][3][0][0][0])          # answer 100
print(data[1][3][1])          # answer 200

# next page..........

data =[20 ,40 ,60 ,80 ,100]
data.insert(2,500)
print(data)

# answer
# [20, 40, 500, 60, 80, 100]

data =[20 ,40 ,60 ,80 ,100]
data.pop(3)                    # If we don't indicate, then it removes the last one.
print(data)

# answer
# [20, 40, 60, 100]

data = [
    [10, 20, 30],
    [11, 22, 33]
]
data[0].pop(0)
data[1].pop(2)
print(data)

# answer
# [[20, 30], [11, 22]]

data = [
    [10, 20, 30],
    [11, 22, 33]
]

data[0].insert(2, 100)
data[1].insert(0, 500)
print(data)

# answer
# [[10, 20, 100, 30], [500, 11, 22, 33]]

# next page..........

about = ["Kathmandu", 123, True]
about[0] = about[0][:3] + 't' + about[0][4:]
print(about)

# answer
# ['Kathtmandu', 123, True]

about = ["Kathmandu", 123, True]
about[0] = about[0].replace('h', 't')
print(about)

# answer
# ['Kattmandu', 123, True]


