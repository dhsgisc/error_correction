def is_error(data, original):
    original_checksum = 0
    checksum = 0

    for i in range(0, len(original)):
        original_checksum += int(original[i])
        checksum += int(data[i])

    original_checksum %= 10
    checksum %= 10

    if original_checksum == checksum:
        weight = [1, 2, 3, 4, 5]

        original_checksum = 0
        checksum = 0

        for i in range(0, len(original)):
            original_checksum += int(original[i]) * weight[i]
            checksum += int(data[i]) * weight[i]

        original_checksum %= 10
        checksum %= 10

        if original_checksum != checksum:
            return False
    else:
        return False

    return True

original = "46756"
data = ["16756", "15756", "28756", "65756"]
for i in data:
    if(is_error(i, original)):
        print("Correct")
    else:
        print("Error")
