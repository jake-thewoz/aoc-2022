import data_getter
import os

if (os.path.exists("data_day_5.txt")):
    with open("data_day_5.txt", "r") as f:
        data = f.read()
else:
    data = data_getter.get_data(5)
    with open("data_day_5.txt", "r") as f:
        data = f.read()

data = data.splitlines()
print(data)