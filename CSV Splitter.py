import math as m
row_size = 500000
source_location = 'D:/csvfilepathgoeshere.csv'
destination_location = 'D:/outputnamegoeshere_'
# will output as outputnamegoeshere_number.csv

def write_rows(part, lines):
    with open(destination_location + str(part) + '.csv', 'w') as f_out:
        f_out.write(header)
        f_out.writelines(lines)
        print('Writing file ' + str(part) + ' of ' + str(total_files))

def count_rows():
   f = open(source_location,'r')
   line_count = len(f.readlines())
   return line_count
        
with open(source_location, 'r') as f:
    ## Display file info
    total_lines = count_rows()
    print('Csv file lines: ' +  str("{:,}".format(total_lines)))
    total_files = m.ceil(total_lines/row_size)
    print('Process will output ' + str("{:,}".format(total_files)) + ' files')

    ## Split out the file    
    count = 0
    header = f.readline()
    lines = []
    for line in f:
        count += 1
        lines.append(line)
        if count % row_size == 0:
            write_rows(count // row_size, lines)
            lines = []
    ## write remainder
    if len(lines) > 0:
        write_rows((count // row_size) + 1, lines)
