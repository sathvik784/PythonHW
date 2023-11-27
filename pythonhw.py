import requests
import json

class Cats:

    def __init__(self):
        self.base_url = "https://catfact.ninja/breeds"
    
    def get_n_fact(self, n):
        response = requests.get(self.base_url)

        if response.status_code == 200:
            data = response.json()

            if 0 <= n < len(data['data']):
                return data['data'][n]['breed']
            else:
                return f"Invalid value for n"
        else:
            return f"Could not retrieve data"


catfacts = Cats()
n = catfacts.get_n_fact(5)
print(n)