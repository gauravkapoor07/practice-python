import os

def print_directory_contents(path):
    try:
        # List all files and directories in the specified path
        with os.scandir(path) as entries:
            for entry in entries:
                print(entry.name)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access the directory '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
directory_path = '/Library'  # Current directory
print_directory_contents(directory_path)