from pip._vendor.pygments.console import x

try:
    print(x)
except NameError:
    print("x hasn't been defined yet.")