import re

f = open('natarang-cards.xml', 'r')
photolist = []

for line in f.readlines():
	match = re.search(r'entry id="\d+"', line)
	if match:
		print 'Search found ' + match.group()
		var = match.group().strip('\"')
		numpage = re.search(r'\d+$',var)
		pho = numpage.group() +'\n'
		photolist.append(pho)
		
	match2 = re.search(r'entry id="\d+\-\d+"', line)
	if match2:
		print 'Search found ' + match2.group()
		var2 = match2.group().strip('\"')
		numpage2 = re.search(r'\d+\-\d+$',var2)
		pho2 = numpage2.group() +'\n'
		photolist.append(pho2)
			
	
f.close()
photolist.sort()

g = open('photo_xml.txt','w')
g.writelines(photolist)
g.close()
		
f = open('photo.txt','r')
photolist = []
for line in f.readlines():
	var = line.strip('\n')
	var = var.strip('.jpg')
	var = var.strip('.tif')
	var = var.strip('.TIF')
	var = var + '\n'
	photolist.append(var)
f.close()
photolist.sort()

g = open('photo.txt','w')
g.writelines(photolist)
g.close()
