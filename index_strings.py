s1 = "hello world!"
print(s1)
print(s1[0], s1[1], s1[2])
print(s1[4], s1[7]) #print both o-s
print(s1[11], s1[-1]) #print the last one
print(s1[-1])

## not happening bc 7.0 --> print(s1[14//2])

s1 = "hello"
s2 = "world"

print(s1+ " " + s2+ "!")

# if opeerations
if "bob": #bob is True!
    print("bob is")
else:
    print("non isn't")
if "":
    print("empty string is True")
else:
    print("Empty string is False")

s = "abcdefghijklmnop"
print(len(s))
#we can iterate over a sting and we get each character
for character in s:
    print(character, end=" ")
print()

i = -1 #the beginning index
while i < len(s):
    print(s[i], end=" ")
    i -=1

# slide is a fancy index
s = "0123456789"
print(s)
print(s[2:3]) # 2
print(s[4:6]) # 4 2
print(s[:3]) # 0 1 2
print(s[1:7:2]) #1 3 5
