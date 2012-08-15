original = "4837543622563997"
transmission = "4837543627563997"
result = list(transmission)

# 0 = vertical
# 1 = horizontal
correct_checksum = [[0 for i in range(4)] for i in range(4)]
checksum = [[0 for i in range(4)] for i in range(4)]

# loop through rows
for i in range(0, 4):
    # loop through columns
    for j in range(0, 4):
        for k in range(0, 2):
            correct_checksum[k][i] += int(original[i * 4 + j])
            checksum[k][i] += int(transmission[i * 4 + j])
    
    for k in range(0, 2):
        correct_checksum[k][i] %= 10
        checksum[k][i] %= 10

coords = []

for i in range(0, len(checksum[0])):
    if correct_checksum[0][i] - checksum[0][i] != 0:
        for j in range(0, len(checksum[1])):
            if correct_checksum[1][j] - checksum[1][j] != 0:
                result[i * 4 + j] = str(int(result[i * 4 + j]) - (abs(correct_checksum[1][j] - checksum[1][j])))
    
print("Corrected: " + "".join(result))
            
