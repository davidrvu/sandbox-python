from multiprocessing import Process

def func1(param1):
    print('func1: starting')
    print("param1 = " + str(param1))
    for i in range(300000):
        print("func1 i = " + str(i) + "     ", end='\r')
    print("\n")
    print('func1: finishing')

def func2():
    print('func2: starting')
    for i in range(300000):
        print("func2 i = " + str(i) + "     ", end='\r')
    print("\n")    
    print('func2: finishing')

if __name__ == '__main__':
    print("Process(target=func1(param1))")
    param1 = 42
    p1 = Process(target=func1, args=(param1,))
    p1.start()



    print("Process(target=func2)")
    p2 = Process(target=func2)
    p2.start()



    print("p1.join()")
    p1.join()




    print("p2.join()")
    p2.join()