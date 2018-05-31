testIP = str(raw_input("Enter the address you'd like to test: "))

splitIP = testIP.split(".")

isIP = 1;

lenIP = len(splitIP)
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

for x in range (0, 3):
    if splitIP[x] > 256 and splitIP[x] < 0:
        print("Not in range.")
        isIP = 0

if isIP == 1:
    print("This is a valid IP address.")
else:
    print("This is not a valid IP address.")
