import time
class speed():
    while True:
        value = int(input("value?"))

        if value == 1:
            for i in range(10):
                time.sleep(0)
                print(i)
        elif value == 2:
            for i in range(10):
                time.sleep(0.3)
                print(i)
        else:
            for i in range(10):
                wait = input("step to next square?")
                print(i)
            