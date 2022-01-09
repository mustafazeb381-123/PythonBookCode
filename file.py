import os
os.getcwd()
os.chdir('D:\Windows')
if os.path.exists('sketch.txt'):
    data = open('sketch.txt')

    for each_line in data:
        if not each_line.find(':') == -1:
            (role, line_spoken) = each_line.split(':',1)
            print(role, end='')
            print('said',end='')
            print(line_spoken,end='')
    data.close()
else:
    print('the data file is missing!')
'''this version uses extra logic to handle the i/o errors'''