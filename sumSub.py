arr = [1,2,3]
t = 3

def countThis(arr,t):
    count = 0
    for start in range(len(arr)):
        for end in range(start, len(arr)):
            if sum(arr[start:end +1]) == t:
                count += 1
    return count

print(countThis(arr,t))
