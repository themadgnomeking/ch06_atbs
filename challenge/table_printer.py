#! python3

#write a function that takes a list of strings and displays it in a 
#well organized table with each column right-justified
#Assume that all the inner lists will contain the same number of strings

#Hint: your code will first have to find the longest string for each of the inner list so
#   that the whole column can be wide enough to fit al the strings.
#   You can store the maximum width of each column as a list of integers. 
#   The print_table() function can store the width of the longest string in table_data[0]
#   col_width[1] can store the width of the longest string in table_data[1], and so on
#   You can then find the largest value in the col_widths list to find out
#   what integer width to pass to the rjust() string method

table_data = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
    ]

def print_table(table_data):
    col_width = [0] * len(table_data)
    print(col_width)
    for list_data in table_data:
        
        print(len(max(list_data)))
        print(list_data)
    #TODO take the list and iterate 
    #TODO find the longest string
    #TODO store max width of each column as a list of int
    #TODO col_width[0] can store width of longest string in table_data[0], col_width[1] to table_data[1], and so on
    #TODO find the largest value in col_widths list to find what width to pass the rjust() method

print_table(table_data)