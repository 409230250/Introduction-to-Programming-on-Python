
#  Michael Harris 29314351 and Junjie Lin 25792830.  ICS 31 Lab sec 5.  Lab asst 7.

# (e)
#e.1
def copy_file(s: str) -> None:
    '''User-driven function that copies one file to another'''
    infile_name = input("Please enter the name of the file to copy: ")
    infile = open(infile_name, 'r')
    outfile_name = input("Please enter the name of the new copy:  ")
    outfile = open(outfile_name, 'w')
#e.2
    if(s == 'line numbers'):
        i=0
        for line in infile:
            outfile.write('{:5}:'.format(i))
            outfile.write(line)
            i+=1
#e.3
    elif(s == 'Gutenberg trim'):
        file_list = []
        for line in infile:
            file_list.append(line)
        index = 0
        while(file_list[index][0:7] != '*** STA'):
            index += 1
        index += 1
        while(file_list[index][0:7] != '*** END'):
            outfile.write(file_list[index])
            index += 1
#e.4
    elif(s == 'statistics'):
        file_list = []
        for line in infile:
            if(line == '\n'):
                file_list.append('')
            else:
                file_list.append(line)
            outfile.write(line)
        line_count = len(file_list)
        empty_lines = file_list.count('')
        abs_average = len(str(file_list)) / len(file_list)
        if(file_list.count('') == 0):
            average_nonempty = 0
        else:
            average_nonempty = len(str(file_list)) / file_list.count('') 
        print('{:5}\t'.format(line_count), 'lines in the list\n',
              '{:4}\t'.format(empty_lines), 'empty lines\n',
              '{:6.1f}\t'.format(abs_average), 'average characters per line\n',
              '{:6.1f}\t'.format(average_nonempty), 'average characters per nonempty line\n')
    else:
        for line in infile:
            outfile.write(line)
    infile.close()
    outfile.close()
#copy_file('line numbers')      
#copy_file('Gutenberg trim')
copy_file('statistics')
