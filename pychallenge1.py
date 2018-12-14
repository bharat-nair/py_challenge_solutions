import string

text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"

trans = str.maketrans('{|','ab')

for letter in text:
    if letter in string.ascii_lowercase:
        letter = ord(letter) + 2
        outtext = ''.join(chr(letter))
    else:
        outtext = ''.join(letter)
    print(outtext.translate(trans),end='')

print('\n')
    
for letter in 'map':
    if letter in string.ascii_lowercase:
        letter = ord(letter) + 2
        outtext = ''.join(chr(letter))
    else:
        outtext = ''.join(letter)
    print(outtext.translate(trans),end='')
    
