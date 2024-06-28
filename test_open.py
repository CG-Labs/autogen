# test_open.py
try:
    with open('test.txt', 'w') as f:
        f.write('Hello, world!')
    print('File written successfully.')
except Exception as e:
    print(f'Error: {e}')
