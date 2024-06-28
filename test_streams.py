try:
    # Test printing to stdout
    print("Testing standard streams...")

    # Test opening a file using the 'open' function from 'builtins'
    with open("test_file.txt", "w") as f:
        f.write("This is a test file.")

    with open("test_file.txt", "r") as f:
        content = f.read()
        print("File content:", content)

    print("All tests passed successfully.")
except ImportError as e:
    print(f"ImportError: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
