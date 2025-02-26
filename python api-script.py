import requests
from functools import wraps
import time

# Decorator to log function execution
def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Starting '{func.__name__}' function execution.")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Finished '{func.__name__}' function execution in {end_time - start_time:.2f} seconds.")
        return result
    return wrapper

# Function to fetch a random joke from an API
@log_execution
def fetch_random_joke():
    url = "https://github.com/guillou73/assignment10.git"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        joke = response.json()
        print(f"Here's a joke for you: {joke['setup']} - {joke['punchline']}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Main entry point
if __name__ == "__main__":
    fetch_random_joke()
