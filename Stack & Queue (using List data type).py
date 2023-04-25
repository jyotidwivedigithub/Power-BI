# STACK.....is a linear data structure..
   # Stores items in a Last-In/First-Out(LIFO) or First-in/Last-Out(FILO) manner.
   #Stack Operations                                      STACK
      #Push=> Inserting an Element                         4
      #Pop=> Deleting an Element (Last Element)            3-2-top
      #Peek=> Display the Last Element                     2-9
      #Display=> Display List                              1-6
      #Exit=>exit the list                                 0-5

l=[]
while True:
     c=int(input('''
       1 Push Elements
       2 Pop Elements
       3 Peek Elements
       4 Display Stack 
       5 Exit

       '''))
     if c==1:                  #push element ..inserting element
        n=input("Enter the Value");
        l.append(n)
        print(l)
 
     elif c==2:                #pop element..delete element
       if len(l)==0:
        print("Empty Stack")
       else:
        p=l.pop()
        print(p)
        print(l)

     elif c==3:                #peek element..last element
      if len(l)==0:
        print("Empaty Stack")
      else:
        print("Last Stack Value",l[-1])

     elif c==4:                #display element
        print("DisplaynStack",l)

     elif c==5:                #exit list
        break;
     


#QUEUE....is a linear data structure..
    # Stores itemsin First in First Out (FIFO) manner..
    #Queue Operations                                                 QUEUE
       #Enqueue:Adds an item to the queue
       #Dequeue:Remove an item from the queue                      7-6-5-4-3-2-  >1
       #Front:Get the front item from the queue                    ^            ^
       #Rear:Get the last item from queue                         Rear         Front


 
l=[]
while True:
     c=int(input('''
       1 Push Elements
       2 Pop first Elements
       3 Front Elements
       4 Last Elements
       5 Display Stack 
       6 Exit

       '''))
     if c==1:                  #Enqueue element ..inserting element
        n=input("Enter the Value");
        l.append(n)
        print(l)
 
     elif c==2:                #Dequeue element..delete element
       if len(l)==0:
        print("Empty Queue")
       else:
        del l[0]
       print(l)

     elif c==3:                # Front..get front element
      if len(l)==0:
        print("Empaty Queue")
      else:
        print("First Queue Value:-",l[0])

     elif c==4:                #Rear...last element
      if len(l)==0:
        print("Empaty Queue")
      else:
        print("Last Queue Value:-",l[-1])

     elif c==5:                #display element
        print("Display Queue:- ",l)

     elif c==6:                #exit list
        break;
      