import constants
from fetchData import fetch, params

constants.apiKey = "bb54d80a-6dfc-43a9-8771-aa0b09940240"

if __name__ == "__main__":
    php = fetch.Fetch()

    php.productions('php')
