methods = dir("hi")
useful_methods= []
for method in methods:
    if "__" in methods:
        continue
    useful_methods.append(method)
print(useful_methods)
print(help("hi".capitalize)) # get help for whatever method you want
print("cat".capitalize())
s = "i go to school every day"
print(s.capitalize())

print("I LIKE CAKE!!@@gmail.com".casefold()) #lower pretty much does the same thing

print("hello".center(30, "*") )
print("banannananannananananan".count("ana")) # count is useful

print("ana ana banana".find("ana",5)) # 0 bc the first ana is at position 0

words = ["i", "like", "to", "sing"]
print(" ".join(words))

s = "I like to go hiking!"
print(s.replace(" ", "! !"))
s = "I like to go hiking!"
# print(s.split())
print(s.replace("!", "").split())
print(s.upper())
punctuation= "!.?-/;',"
sentence= "How,are,you? I dont like this;"
for p in punctuation:
    sentence= sentence.replace(p,"")
print(sentence)

print("i like to go skiing".title())