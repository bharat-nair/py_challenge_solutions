from urllib import request
import re
number = '12345'
count = 0
numRegex = re.compile(r'and the next nothing is ?[0-9]?[0-9]?[0-9]?[0-9]?[0-9]')
for i in range(0,400):
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={num}'.format(num=number)
    f = request.urlopen(url)
    s = f.read().decode()

    if 'Divide by two' in s:
        count += 1
        number = int(number)/2
        print(str(s) + ' (' + str(count) + ')')
        continue
    
    try: match = numRegex.findall(s).pop()

    except:
        count += 1    
        print(str(s) + ' (' + str(count) + ')')
        break
    
    number = [x for x in match.split(' ') if x.isdigit()].pop()
    
    count += 1    
    print(str(s) + ' (' + str(count) + ')')


#66831
