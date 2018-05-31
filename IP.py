#Python program to test if an address is a viable IP Adress

#accepts user input as a string
testIP = str(raw_input("Enter the address you'd like to test: "))
#splits user input at all '.' characters into a list splitIP
splitIP = testIP.split(".")

#int acts as a bool
isIP = 1;

#length of splitIP is found
lenIP = len(splitIP)

#tests to determine if IP is of valid length and comprised of integers
if lenIP  != 4:
    isIP = 0;
    print("Not long enough.")
else:
    for lenIP in range (0, 4):
        try:
            int(splitIP[lenIP])
            #print(splitIP[lenIP])
        except:
            isIP = 0;
            print("Not comprised of integers.")

x = 0;

#tests if tuples in splitIP are in range
for x in range (0, 3):
    if splitIP[x] > 256 and splitIP[x] < 0:
        print("Not in range.")
        isIP = 0

#prints result
if isIP == 1:
    print("This is a valid IP address.")
else:
    print("This is not a valid IP address.")
