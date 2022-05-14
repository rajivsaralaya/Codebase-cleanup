




from statistics import pvariance


def to_usd(my_price):




#price = input("Please choose a price like 4.9999")

#print(to_usd(float(price)))

if __name__ == "__main__":
    
    #nesting code in main coneitional will allow other scripts to import functions from this file
    #if code is in global scope
    #of file trying to import
    #it will throw errors 
    
    price = input("Please choose a price like 4.9999")
    
    print(to_usd(float(price)))