import re

f = open('natarang-cards.xml', 'r')
photolist = []

for line in f.readlines():
	match = re.search(r'id="\d+"', line)
	if match:
		print 'searchfound'
		var = match.group()
		numpage = re.search(r'\d+',var)
		pho = numpage.group()+'.jpg\n'
		photolist.append(pho)
f.close()

g = open('photolist.txt','w')
g.writelines(photolist)
g.close()
		
