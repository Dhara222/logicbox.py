print("Welcome to the Pattern Generator and Number Analyzer!")

while True:
    print("\n Select an option: ")
    print("\n1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")
    
    choice=int(input("Enter your choice: "))
    
    if choice == 1:
        
      i=int(input("Enter the number of rows for the pattern: "))

      print("\n Pattern:")

      for i in range(1,i+1):
         for j in range(i):
             print("*", end="")
         print()

    elif choice == 2:
    
       A=int(input("Enter the start of the range: "))
       B=int(input("Enter the end of the range: "))

       for i in range(A,B+1):

         if i%2==0:
             print("Number",i,"is even")
         else:
             print("Number",i,"is odd")

       i=A
       total=0

       while i<=B:
         total=total+i
         i=i+1

       print("Sum of all numbers from",A,"to",B,"is:",total)

    elif choice == 3:
          print("Exiting the program. Goodbye!")
          break

    else:
         print("Invalid choice. Please enter 1,2 or 3.")
          
