def max_of_three(n1, n2, n3):
        if n1>n2 and n1>n3:
            return n1
        elif n2>n3 and n2>n3:
            return n2
        else:
            return n3
        
if __name__ == '__main__':
    print(max_of_three(3, 6, 9))        

            