# import movies
# cast = ['mustafa','malaika','gulalai','mom']
# movies.print_lol(cast)
# for num in range(10):
#     print(num)
import os
os.getcwd()#what's the current working directory?
os.chdir("D:\Windows")#in this line we can add path where we can take the documents
os.getcwd()#confirm that you are in right place
data = open('sketch.txt')#Open a named file and assign the file to a file object called “data”.
print(data.readline(), end='')
'''Use the “readline()” method to grab a
line from the file, then use the “print()”
BIF to display it on screen.'''
data.seek(0)
for each_line in data:
 try:
    if not each_line.find(":") == -1: # the if codition can remove the error which they can give  before the if condition

        (role, line_spoken) = each_line.split(':',1)#Process the data, extracting each part from each line and displaying each part on screen.
        print(role, end='')
        '''this code b/w try and except are protected from run time error'''
        print('said: ', end='')
        print(line_spoken, end='')
        print(each_line,end='')
        data.close()  # so if u r sure that u wanna to close the file then data.close will close the file
 except:#If a runtime error occurs, this code is executed.
    pass
 '''this version uses another "try" statement to handle file i/o errors'''