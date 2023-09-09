# str = "aaabbchaadjjha"
# print(str.count("a"))
# print(str.count("ab"))

# str = "Pruthvi"
# print(str[::-1])

# str = "zxddsaasf"
# print(sorted(str))

# str = "Pruthviraj is bad boy"
# str2 = str.replace("bad", "good")
# print(str2)

# str = "Pruthviraj is a good boy"
# print(str.upper())
# print(str.lower())
# print(str.count(" "))

# ls = str.split(" ")
# print(ls)


# mobile = int(input("Enter Mobile: "))
# mobStr = str(mobile)
# if( mobStr.isdigit() and len(mobStr)==12 and mobStr.startswith("91")):
#     print("Accepted")
# else:
#     print("Not Accepted")


# name = "Pruthviraj"
# rev = ""
# for i in name:
#     rev = i + rev
# print(rev)

# name  = "madam"
# i = 0
# j = len(name)-1
# flag = 1

# while(i<j):
#     if(name[i] != name[j]):
#         print("Not Palindrome")
#         flag = 0
#         break
#     else:
#         i+=1
#         j-=1

# if flag : print("Palindrome")

# REVERSE THE WORDS IN STRING
myStr = "India will be called Bharat Now"
ls = []
temp = ""
ans = ""

# for i in myStr:
#     if i != " ":
#         temp += i
#     else:
#         ls.append(temp)
#         temp = ""
# ls.append(temp)
# ls.reverse()
# ans = " ".join(ls)
# print(ls)      
      
for i in myStr:
    if i != " ":
        temp += i
    else:
        ans = temp + " " + ans
        temp = ""

ans = temp + " " + ans
print(ans)            
