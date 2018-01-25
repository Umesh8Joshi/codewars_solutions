'''
    codewars example to be done by following program
'''

def str_text(string):
    chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
    corr,err = 0,0
    x = list(string)
    for i in x:
        if i in chars:
            corr +=1
        else:
            err += 1
    print('error_printer(s) => "' + str(err) + '/' + str(corr) + '"' )