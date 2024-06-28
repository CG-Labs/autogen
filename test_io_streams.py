from autogen.io import IOStream, InputStream, OutputStream

try:
    # Test custom IOStream
    class CustomIOStream(IOStream):
        def print(self, *objects: Any, sep: str = " ", end: str = "\n", flush: bool = False) -> None:
            print(*objects, sep=sep, end=end, flush=flush)

        def input(self, prompt: str = "", *, password: bool = False) -> str:
            return input(prompt)

    # Set the custom IOStream as the default
    IOStream.set_global_default(CustomIOStream())

    # Test printing to stdout using custom IOStream
    default_stream = IOStream.get_default()
    default_stream.print("Testing custom IOStream...")

    # Test reading input using custom IOStream
    user_input = default_stream.input("Enter some text: ")
    default_stream.print("You entered:", user_input)

    print("All tests passed successfully.")
except ImportError as e:
    print(f"ImportError: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
