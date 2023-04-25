names= "Advik,Akanksha"
#POSITIVE SLICING
print(names[0:5])    #first five characters { } is used for slicing.  #ADVIK,---(0123456)//(-7,-6,-5,-4,-3,-2,-1,0)
print(names[:4])                                                      
print(names[1:])
print(names[:])
print(names[0:6])
print(names[2::2])


#NEGATIVE SLICING
W="krishna"            #KRISHNA-----(0123456)//(-7,-6,-5,-4,-3,-2,-1)
print(W[0:-2])    
#print(W[-1:-6])       both will not give any output because 7-1:7-6=  6:1
#print(W[:-7])          7-0:7-7=  7:0
print(W[-5:-2])
print(W[-6:-2])