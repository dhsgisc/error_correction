def most_common(data):
    result = {}
    highest_value = 0
    highest_key = 0
    
    for a in data:
        try:
            result[a] += 1
        except:
            result[a] = 1

    for key, value in result.iteritems():
        if value > highest_value:
            highest_key = key
            highest_value = value

    return highest_key

def corrected(data):
    result = []

    for i in range(0, len(str(data[0]))):
        a = []
        
        for j in range(0, len(data)):
            a.append(str(data[j])[i])

        result.append(most_common(a))
        
    return "".join(result)

data = [529375, 521375, 521311, 544375, 721875]
print(corrected(data))
