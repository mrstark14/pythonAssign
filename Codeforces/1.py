a=input()
a=a.lower()
for x in a:
    if(x=='a' or x=='e' or x=='i' or x=='o' or x=='u' or x=='y'):
        continue
    else:
        print("."+x,end='')