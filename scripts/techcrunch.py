import requests

def getData():
    URL = "https://techcrunch-api-abhays-projects-bdb1b6d4.vercel.app/"
    response = requests.get(URL)
    data = response.json()
    return data


