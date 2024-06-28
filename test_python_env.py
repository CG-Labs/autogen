def test_python_environment():
    print("Testing Python environment...")

    # Attempt to open a file using the built-in 'open' function
    try:
        with open("test_file.txt", "w") as f:
            f.write("This is a test file.")
        print("File created and written successfully.")
    except Exception as e:
        print(f"Error occurred while opening/writing file: {e}")

    # Attempt to read the file
    try:
        with open("test_file.txt", "r") as f:
            content = f.read()
        print("File read successfully. Content:")
        print(content)
    except Exception as e:
        print(f"Error occurred while reading file: {e}")

if __name__ == "__main__":
    test_python_environment()
