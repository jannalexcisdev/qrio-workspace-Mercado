                                                            #PYTHON INTRO
# def repeat(name,exclaim):
#     result = name*3
#     if exclaim:
#         result = result + '!!!'
#     return result

# def main():
#     print (repeat("Hello", True))
#     print (repeat("YaY", True))
#     print (repeat("WhO", False))
    

# if __name__ == '__main__':
#     main ()
    



                                                                #STRINGS
# raw = r'this\t\n and that'

#   # this\t\n and that
# print(raw)

# multi = """It was the best of times.
#   It was the worst of times."""

#   # It was the best of times.
#   #   It was the worst of times.
# print(multi)





# s = "Hello There, World!"
# ss = ['aaa', 'bbb', 'ccc']

# print(s.upper())    #uppercase
# print(s.lower())    #lowercase
# print(s.strip())            # bool removes spaces on start and on end
# print(sss.isalpha())            #bool checks if there are spaces and punctuations
# print(s.isdigit())          #bool checks if there is a digit
# print(sss.isspace())            #bool checks if the string contains only spaces
# print(s.startswith("Hello"),s.endswith("There"))            #bool checks the start and end of str
# print(s.find('There'))  #index kung pang ilan
# print(s.replace('World', "Universe"))   #changes the value of the first parameter
# print(s.split('delim')) #delimiter -> ["Hello There, World"]
# print(s.join(ss))   #aa -> aaaHello There, World!bbbHello There, World!





# value = 3.14159265
# print(f"The value of Pi is {value:.3}")

# car = {
#     "door":2,
#     'tires':4
# }
# print(f"car = {car}")

'''
address_book = [{'name':'N.X.', 'addr':'15 Jones St', 'bonus': 70},
      {'name':'J.P.', 'addr':'1005 5th St', 'bonus': 400},
      {'name':'A.A.', 'addr':'200001 Bdwy', 'bonus': 5},]

for person in address_book:
    print(f"{person["name"]:8} || {person['addr']:20} || {person["bonus"]:<5}")
    '''



                                                        #LISTS  
# colors = ['red', 'blue', 'green']
# a  = colors
# print(a)

# if "red" in colors:
#     print("Noice")


# i = 0
# a = "abcdefghijklmnopqrstuvwxyz"
# while i < len(a):
#     print(a[i])
#     i += 3


# list = ["Larry", "Curly", "Moe"]
# list.append("Jann")     #adds element to the last
# list.insert(1,"Juan")   #inserts elements in a given index
# list.extend(["aaa","bbb"])  #inserts elements in the end of the list
# print(list.index("Curly"))  #prints the index of curly
# list.pop()  #removes the last element
# print(list) 

# list = [1,2,3]
# list.append(4)
# print(list)

# list2 = []
# list2.append('a')
# list2.append('b')
# list2.append('c')
# list2.append('d')
# print(list2)
# print(list2[2:])
# list2[0:2] = 'z'    #replaces the index[0] and index [1] to z
# print (list2)





                                                        #SORTING
# a = [5,1,2,4,3]
# print(sorted(a))    #temporary sort
# print(a)

# strs = ['aaa',"BBBB",'z','CC']
# print(sorted(strs, reverse= True))  #temporary sort in reverse order. in sort, uppercase always comes first
# print(sorted(strs, key=len))        # to sort by number of length
# print(sorted(strs, key=str.lower))  #<- converted all strings to lower case before comparing then print the original
# print(sorted(strs))

# tuple = (1,2,"hi")
# print(len(tuple))
# print(tuple[2])
# print(tuple)

# tuple = (1,2,"bye")
# print(tuple)
# (x, y, z) = (42, 13, "hike")
# print(x)


# numbers = [1,2,3,4]
# output = [num * num for num in numbers]
# print(output)


# strs = ['hello', 'and', 'goodbye']
# shout = [s.upper() +"!" for s in strs]
# print(shout)

# nums = [2,8,1,6]
# small = [n for n in nums if n<=2]
# print(small)

# fruits = ['apple', 'cherry', 'banana', 'lemon']
# afruits = [s.upper() for s in fruits if 'a' in s]
# print(afruits)




                                                                #DICTS AND FILES 
# dict = {}
# dict ['a'] = 'alpha'
# dict['g'] = 'gamma'
# dict['o'] = 'omega'
# dict['a'] = 6
# #     ^key   ^value
# print(dict)

# if 'z' in dict: print (dict["z"])   #avoids key error
# print(dict.get('z'))                #returns none kesa error

# for key in dict:
#     print(key)
    
# print (dict.keys()) #<- prints dict keys
# print (dict.values())   #<- prints dict values
# print("\n")

# for key in sorted(dict.keys()):
#     print(key, dict[key])   #<key then call the dict[key]

# print(dict.items())     #prints all dict items
# print('\n')
# for k, v in dict.items(): print(k, '>', v)  #<k-key v-value so for ever key, value print k > v





# h = {}
# h['word'] = 'garfield'
# h['count'] = 42
# print(f"I want {h["count"]} copies of {h['word']}")






# var = 6 
# del var         #to delete var

# list = ['a','b','c','d']
# del list [0]    #delete first element
# del list [-2:]  #delete last 2 elements
# print (list)

# dict = {'a':1, 'b':2, 'c':3}
# del dict['b']   #deletes 'b':2
# print(dict)






f = open ('foo.txt', 'rt', encoding ='utf-8')   #<- to open and read the contents of foo.txt
for line  in f:
   print (line, end=' ')
    
    

# with open('foo.txt', 'rt', encoding='utf-8') as f:   
#   for line in f:                                        
#      print(line, end='')                                
#     # here line is a *unicode* string                            

# with open('write_test', encoding='utf-8', mode='wt') as f:       
#     f.write('\u20ACunicode\u20AC\n') #  €unicode€                  
#     # AKA print('\u20ACunicode\u20AC', file=f)  ## which auto-adds end='\n'      







                                                                #REGULAR EXPRESSIONS
# import re            #regular expression (pattern searching)

# text = 'an example word:cat!!'    #str na paghahanapan
# match = re.search(r'word:\w\w\w', text)     #<store sa match yung word na mahahanap sa variable na text

# if match:
#    print('found', match.group())     #store and print
# else:
#    print('did not find') 




# import re
# test_string = '123abc4567889acb123ABC'
# pattern = re.compile(r"abc")
# matches = pattern.finditer(test_string)
# for match in matches:
#     print(match)