m1=int(input("Enter the marks in 1st IA"))
m2=int(input("Enter the marks in 2nd IA"))
m3=int(input("Enter the marks in 3rd IA"))
if(m1==m2 and m1==m3):
    avg=(m1+m2)/2
    print("the marks are equal\n avg:",avg)
elif(m1<=m2 and m1<=m3):
    avg=(m2+m3)/2  
    print("the avg of m2 and m3:",avg)
elif(m2<=m1 and m2<=m3):
    avg=(m1+m3)/2   
    print("the avg of m1 and m3:",avg)
else:
    avg=(m2+m1)/2 
    print("the avg of m1 and m2 :",avg)
        
    
            

