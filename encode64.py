ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def to_base_64(string):
    binarystr = ''
    encoded = []
    for ch in string:
        eightbits = str(bin(ord(ch)))[2:]
        eightbits = eightbits.rjust(8,'0')
        binarystr += eightbits

    if len(binarystr)%6 != 0:
        binarystr = binarystr + '0'*(6 - len(binarystr)%6)

    while len(binarystr) >= 6:
        encoded.append(binarystr[:6])
        binarystr = binarystr[6:]

    return ''.join([ALPH[int(x,2)] for x in encoded])


def from_base_64(string):
    binarystr = ''
    decoded = []
    for ch in string:
        # Look up in ALPH and convert to binary:
        sixbits = str(bin(ALPH.index(ch)))
        sixbits = sixbits[sixbits.index('b')+1:]
        sixbits = sixbits.rjust(6,'0')
        binarystr += sixbits

    while len(binarystr) >= 8:
        decoded.append(binarystr[:8])
        binarystr = binarystr[8:]

    return ''.join([unichr(int(x,2)) for x in decoded])

'''
from base64 import b64encode, b64decode

def to_base_64(string):
    return b64encode(string).replace("=", '')
    
def from_base_64(string):
    return b64decode(string + "==")
'''