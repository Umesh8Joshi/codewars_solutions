'''
    codewars 4 kyu kata solution
    Function that validates the play schedule for golfers
'''

def valid(a):
    '''
    function to validate list
    :param a: list contains sublist of golfers playing
    :return: True if satisfies all needs else False
    '''

    #create set of all golfers
    golfers = set(''.join(''.join(x) for x in a))
    #mapping of each golfer playing with each other
    each = dict((x, golfers-{x}) for x in golfers)
    arrlen = sum(len(x) for x in a)/len(a)

    for arr in a:
        '''
            exactly once a day and len checks
        '''
        day = ''.join(arr)
        if set(day) != golfers or len(arr) != arrlen:
            return False
        for j in day:
            if day.count(j) > 1:
                return False
        '''
            once with each other at most
        '''
        for group in arr:
            for golfer in group:
                out = [x for x in group if x != golfer]
                derp = each[golfer]
                for j in out:
                    try:
                        derp.remove(j)
                    except KeyError:
                        return False
                each[golfer] = derp
    return True




if __name__ == '__main__':
    a = [   ['ABCD', 'EFGH', 'IJKL', 'MNOP', 'QRST'],
            ['AEIM', 'BJOQ', 'CHNT', 'DGLS', 'FKPR'],
            ['AGKO', 'BIPT', 'CFMS', 'DHJR', 'ELNQ'],
            ['AHLP', 'BKNS', 'CEOR', 'DFIQ', 'GJMT'],
            ['AFJN', 'BLMR', 'CGPQ', 'DEKT', 'HIOS']    ]
    print(valid(a))