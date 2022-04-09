import time # a simple solution to the speed requirement in my objectives, I did not end up using this code as I assumed I would not, the exact location where one can control the speed was much simpler (although not implemented) but this code was useful for working out how I would have implemented it
class speed():
    while True:
        value = int(input("speed value?"))

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
            