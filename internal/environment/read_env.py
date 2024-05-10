import os

env_file = ".env"

def read_env_file():
    if os.path.exists(env_file):
        with open(env_file) as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()
                print(f"Processing line {line_number}: {line}")
                if "=" in line:
                    key, value = line.split("=", 1)
                    os.environ[key] = value