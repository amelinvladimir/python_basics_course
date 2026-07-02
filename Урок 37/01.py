# def inner():
#     print("Hello")

# inner()


# def outer():
#     def inner():
#         print("Hello")
#     inner()

# outer()

# def outer():
#     def inner():
#         print("Hello")
#     return inner

# i = outer()
# i()

def outer():
    cnt = 0
    def inner():
        nonlocal cnt
        cnt += 1
        print("Hello")
        print(f'cnt: {cnt}')
    return inner

i = outer()
i()
i()
i()