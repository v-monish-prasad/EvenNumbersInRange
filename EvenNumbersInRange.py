def evenNumbersInRange(array, length, queries):
    if not array:
        return "Empty Array."

    prefixEvenCount = [1 if array[0] % 2 == 0 else 0]
    result = []

    for i in range(1, length):
        if array[i] % 2 == 0:
            prefixEvenCount.append(prefixEvenCount[i - 1] + 1)
        else:
            prefixEvenCount.append(prefixEvenCount[i - 1])

    for query in queries:
        if query[0] != 0:
            result.append(prefixEvenCount[query[1]] - prefixEvenCount[query[0] - 1])
        else:
            result.append(prefixEvenCount[query[1]])

    return result


if __name__ == "__main__":
    array = list(map(int, input().strip('[').strip(']').split(',')))
    length = len(array)
    Q = int(input())
    queries = []
    for i in range(Q):
        queries.append(list(map(int, input().strip('[').strip(']').split(','))))
    print(evenNumbersInRange(array, length, queries))
