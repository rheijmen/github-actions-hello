import datetime
import os

def main():
    now = datetime.datetime.now()
    message = f"Hello, World! The time is: {now}"
    print(message)

    # Example of accessing an environment variable (optional)
    name = os.environ.get("NAME", "Stranger") # "Stranger" is the default if NAME is not set
    print(f"Hello, {name}!")

if __name__ == "__main__":
    main()
