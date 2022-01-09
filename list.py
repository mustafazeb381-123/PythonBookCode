# movie = ['mustafa',1999,'touheed',2003,'gulalai',2011,'papa',1972,'mama',1973]
#movie.append("salwa")# append add item in the list
#movie.remove("touheed")#remove cut the one item from the list
#movie.extend(["mom","dad"])extand can extand the list mean add more than one item in the list
#movie.insert(1,"Grandmother")# in insert where you want to add item in the list
#print(movie[0])
#print(movie[1])
#for each_flick in movie:#it's als like each_item
#    print(each_flick)
#for each_item in movie:
 #   print(each_item)
#count = 0
#while count<len(movie):
#    print(movie[count])
#    count = count+1
"""so the movie is the list and we make the list in the lists and so on."""
import movies
# xuxaiii = ["The holy grail",1975,"Terry jhones & Terry Gillam",91,["Graham chapman",["Micheal palin","Jhone cleese","Eric idle","terry jhones",["mustafa","malaika","gulalaii"]]]]
names = ['jhon','eric',['cleese','idle'],'micheal',['palin']]
def print_lol(the_list,indent=False,level=0,): #in the fuction start i can print_lol to print_zebu so they doesn't matter.
    '''Call your argument
indent and set it initially to the value False—that is, do not switch on indentation by default.
In the body of your function, use the value of indent to control your indentation code.'''
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item,indent, level+1,)
        else:
            if indent:
             for tab_stop in range(level):
                print("\t"*level,end='',)
        print(each_item,)
print_lol(names)
#print_lol(names,True,4)
#print_lol(names,True)
'''so the upper code of print_lol names can print the value of list one by one in same line,
 and if you put the True the they can print in the zig zag from but one after next,
and if u put 4 with True the they will be also in the zig zag form but they will leave very high in space.'''
# movies.print_lol(xuxaiii,0)
# for each_item in movies: #in this lines we can make lists in lists in lists in lists so they are very long process so after that we can apply the fuction above this code.
#     if isinstance(each_item,list):
#         for nested_item in each_item:
#              if isinstance(nested_item,list):
#                  for depper_item in nested_item:
#                      if isinstance(depper_item,list):
#                          for deppest_item in depper_item:
#                              print(deppest_item)
#                      else:
#                         print(depper_item)
#              else:
#                 print(nested_item)
#     else:
#      print(each_item)
#for each_item in movies:# in this line we can print all item in vertically
#    print(each_item)
#print(movies[4][1][2])# in this lines we can make slicesor sclicing of list
#tdm = ["mustafa","gulalai"]
#isinstance(tdm,list)
#num_tdm = len(tdm)
#isinstance(num_tdm, list)
 # for each_item in movies:
 #       if isinstance(each_item,list):
 #           for nested_item in each_item:
 #             print(nested_item)
 #           else:
 #               print(each_item)