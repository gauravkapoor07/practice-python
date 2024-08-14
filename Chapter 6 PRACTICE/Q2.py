n1 = int(input("Enter the marks of subject 1:"))
n2 = int(input("Enter the marks of subject 2:"))
n3 = int(input("Enter the marks of subject 3:"))

# Check for total percentage
total_percentage = (100*(n1+n2+n3))/300

if(total_percentage>=40 and n1>=33 and n2>=33 and n3>=33):
    print("The Student has passed the test", total_percentage)

else:
    print("The Student has failed the test", total_percentage)






#if((n1+n2+n3)*100%100==40 or (n1+n2+n3)*100%100==33 ):#
   # print("The Student has passed the test")
#elif((n1+n2+n3)*100%200==100):#
    #print("The Student has passed the test")

#else:
   # print("The Student has Failed the test")
