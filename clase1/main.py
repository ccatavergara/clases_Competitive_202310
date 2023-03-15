

def main():
    print("Hello world!")
    
    #list comprehension
    even = [2*i for i in range(10)]
    print(even)
    
    odd = [(2*i)+1 for i in range(10)]
    print(odd)
    
    
    
if __name__ == "__main__":
    main()