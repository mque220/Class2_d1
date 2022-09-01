string = input()
result = []
while (string != "0 0 0"):
    array = string.split(" ")    
    first = int(array[0])
    second = int(array[1])
    third = int(array[2])

    maximum =  first if second <= first else second

    maximum = maximum if third <= maximum else third

    if maximum * maximum == first * first + second * second + third * third - maximum * maximum:
        result.append("right")
    else:
        result.append("wrong")
    string = input()

for answer in result:
    print(answer)