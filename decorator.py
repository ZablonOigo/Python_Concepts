
"A function that takes another function (original function) as an argument and returns another function"

def currency(fn):
    def wrapper(*args,**kwargs):
        result=fn(*args,**kwargs)
        return f'${result}'
    return wrapper

net_price=currency(100,0.05)
print(net_price)