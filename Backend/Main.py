# main.py
from Backend.Buisiness.Scrape import Scrape
from Backend.utils.Paths import Paths


def main():
    print("Hello, World!")

if __name__ == "__main__":
    # Change this key search
    search = "Junior Full Stack"
    scrape = Scrape(key_search=search)
    # Wait for the user to press Enter
    input("Press Enter to continue...")

    # Continue with the rest of the code
    print("Collecting jobs...")
    scrape.get_jobs()

