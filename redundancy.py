import difflib

def corrected(a):
    encoding = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,\
                'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    result = []
    similarity = [0] * len(a)

    for i in range(0, len(a)):
        for key, value in encoding.items():
            similarity_ratio = difflib.SequenceMatcher(None, key, a[i]).ratio()
            
            if similarity_ratio > similarity[i]:
                similarity[i] = similarity_ratio
                try:
                    result[i] = value
                except:
                    result.append(value)

    return result

data = ['fiqe', 'kwo', 'one', 'thrxp', 'sivpn', 'fivq']
print(corrected(data))
