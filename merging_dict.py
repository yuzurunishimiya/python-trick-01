dict1 = {
    "name": "Hanekawa Tsubasa",
    "meta": 50,
}

dict2 = {
    "friend": "Senjougahara Hitagi",
    "meta": 100
}

merged = {**dict1, **dict2}
print(merged)

# NOTE:
# If there are overlapping keys, the keys from the first dictionary will be overwritten.