#x = float(input("What is x? "))
#y = float(input("What is y? "))

#z = round(x + y)

#print(f"{z:,}")

#z = x / y

#print(f"{z:.2f}")

#int is for normal number 
# float is for decimal


def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n + n

if __name__=="__main__":
    main( )


