def decor(fun):
    def fun2(x):
        rez = fun(x)+10
        print(rez)
    return fun2

@decor
def test(z):
    res = z+5
    return(res)




def main():
    test(5)

if __name__ == "__main__":
    main()