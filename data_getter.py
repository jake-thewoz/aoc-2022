import requests
import json
import os

def get_data(day):
    if (os.path.exists(f"data_day_{day}.txt")):
        with open(f"data_day_{day}.txt", "r") as f:
            data = f.read()
        return data
    else:

        with open('defaults.json','r') as f:
            defaults = json.load(f)

        URL = "https://adventofcode.com/2022/day/" + str(day) + "/input"
        USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
        token = defaults["token"]

        headers = {'User-Agent': USER_AGENT}
        cookies = {"session": token}

        page = requests.get(URL, cookies=cookies, headers=headers)

        page_lines = page.text.splitlines()
        data = []
        for line in page_lines:
            data.append(line)

        with open("data_day_" + str(day) + ".txt", "w") as f:
            for line in data:
                f.write(line + "\n")
        return data