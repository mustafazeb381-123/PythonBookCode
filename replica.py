import os
man = []
other = []
os.getcwd()
os.chdir('D:\Windows')
os.getcwd()
try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == man:
                man.append(line_spoken)
            elif role == 'other man':
                other.append(line_spoken)

            print(role, end='')
            print('said:',end='')
            print(line_spoken, end='')
        except ValueError:
            pass
        #data.close()
except IOError:
    print('the data file is missing')
    try:
        data = open('missing.txt')
        print(data.readline(),end='')
        with open('man_data.txt','w') as man_file ,open('other_data.txt','w') as other_file:
            print(man,file=man_file)
            print(other,file=other_file)
        #man_file.close()
        #other_file.close()
    except IOError as err:
        print('File error' + str(err))
    finally:
        if 'man_file' in locals():
            man_file.close()
        #data.close()
        if 'other_file' in locals():
            other_file.close()
            #print(man)
            #print(other)
            '''in this code the  first try and second try runs when ANY
runtime error occurs within the code that
is being tried '''