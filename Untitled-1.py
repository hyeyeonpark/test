
def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i       
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i

    return result

result = add_mul('add',1,2,3,45,5)

print(result)


def say_myself(name, old, man = True):
    print("나의 이름은 %s 입니다" % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다")

    else:
        print("여자입니다.")

say_myself("박응용",23)
say_myself("박응선",26,False)

a = 1

def vartest(a):
    a = a + 1

vartest(a)
print(a)

def vartest(a):
    a = a + 1

vartest(3)
print(a)

#지역변수(함수 내)와 전역변수(함수 외) 구분 -!

a = 1

def vartest(a):
    a = a + 1
    return a

a = vartest(a)
print(a)

add = lambda a, b : a + b

result = add(3,4)

print(result)


def factorial(n):
     if n == 0:
         return 1

    else:
        return n * factorial(n-1)



def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(5))
