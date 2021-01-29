def duplicate(words):
    result = []
    [result.append(word) for word in words if word not in result]
    return result

def loop():
    term = ""
    collection = []
    while term != "quit":
        term = input()
        collection.append(term)
    return collection
