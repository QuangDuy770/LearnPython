ask=input(">")
while ask!=False:
    if ask=='help':
        print('start- to start the card')
        print('stop- to stop the card')
        print('quit- to exit')
        break
    else:
        print("I dont understand")    
        break


while ask=='help':
    yeu_cau_1=input(">")
    if yeu_cau_1=='start':
        a=('car stared')
        print(a)
        while a == a:
            yeu_cau_1=input(">")
            if yeu_cau_1=='start':
                print("fuck")
                break
    elif yeu_cau_1=="stop":
        b=('car stopped')
        print(b)
        while b == b:
            yeu_cau_1=input(">")
            if yeu_cau_1=='stop':
                print("fuck")
                break
    elif yeu_cau_1=='exit':
        break
    else:
        print('I dont understand2')
        



