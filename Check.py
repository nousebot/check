import os
import requests
import concurrent.futures

dir = os.path.dirname(os.path.abspath(__file__))

url_list = []
try:
    with open(os.path.join(dir, "sourceURLs.txt"), "r") as f:
        for line in f.readlines():
            url_list.append(line.strip())
        f.close()
except FileNotFoundError:
    print("sourceURLs.txt not found !")
    exit(1)

def check_url(url):
    try:
        response = requests.head(url)
        if response.status_code == 200:
            #print(f"Valid URL: {url} ! Status Code: {response.status_code}")
            print(url)
            with open(os.path.join(dir, "outputs.txt"), "a") as f:
                f.write(url + "\n")
                f.close()
        #else:
            #print(f"Invaild URL: {url} ! Status Code: {response.status_code}")
    except requests.RequestException:
        print(f"An error occur in checking URL: {url}")

with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
    executor.map(check_url, url_list)

