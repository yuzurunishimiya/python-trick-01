def count_duplicated(dataset):
    result = {}
    for data in dataset:
        result.setdefault(data, 0)
        result[data] += 1
    
    return result

data = ["hitagi", "tsubasa", "shinobu", "hachikuji", "koyomin", "hitagi", "hitagi", "koyomin", "shinobu"]

result = count_duplicated(data)
print(result)
