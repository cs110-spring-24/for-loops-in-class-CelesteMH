
#prints every numer that is NOT a multiple of 6
for num in range(101):
    if num % 6 != 0:
        print(num)

len("hello")    #gives 5 as there are five numbers in the string

string = "hello"
# string[0] = "H" = string[-5]

for L in range(len(string)):
    print(string[L])
    # prints out...
    #   h
    #   e
    #   l
    #   l
    #   o
    
for A in range(len(string)): 
    print(string[A-2])
    # prints out
    #   l
    #   o
    #   h
    #   e
    #   l


#if we want every other letter...
word = input("Enter a Word: ")
for C in range(0, len(word), 2):
    print(word[C])


#if we want only the first half of that string...
newgirl = input("Enter a Word: ")
for Q in range(0, len(newgirl) // 2):
    print(newgirl[Q])

#the second half...
nick = input("Enter a Word: ")
for p in range(len(nick) // 2, len(nick)):
    print(nick[p])



#   string[start:stop+1:step] 
#   string[start:stop+1:]    reverts to 49      assumes step = 1
#   string[:stop+1:]         reverts to 49      assumes step = 1        assumes start = 0
#   string[:: step]          reverts to 49                              assumes start = 0       assumes stop = end of len

worddd = "Hello World"
worddd[0:3]     # --> "Hel"
worddd[0:len(worddd)//2]    #   --> "Hello"


string1 = "Hello World"
string2 = string1[::-1]
print(string2)



