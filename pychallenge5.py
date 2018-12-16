import pickle
import urllib.request

p = 'rb'
pickled = pickle.load(urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p", p.encode('utf-8')))

for i in pickled:
	for j in i:
		print(j[0]*j[1],end='')

#You might want to adjust the size of your terminal window...
