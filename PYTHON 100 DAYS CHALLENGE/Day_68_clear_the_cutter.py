import os

files = os.listdir('Day_68_code_test')
i = 1
for file in files:
    if file.endswith('.JPG'):
        print(file)
        os.rename(f"clutteredFolder/{file}", f"Day_68_code_test/{i}.png")
        i = i+1
    