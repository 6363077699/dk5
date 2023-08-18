[200~x =lambda x,y,z:x+y+z
        print(x(6,9,5))

        lst=[10,1,2,3,5]
        l=list (filter(lambda x:x%2,lst))
        print(l)

        x=lambda x,y:x if (x>y) else y
        print(x(5,7))

        x=lambda x,y:x if (x<y) else y
        print(x(5,7))

        a=(2,4,5,6)
        z=list(map(lambda x:x+8,a))
        print(z)

        from functools import reduce
        p=reduce (lambda x,y:x+y,lst)
        print(p)
