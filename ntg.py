from sets import Set

def read_file(inp):
	f = open(inp, 'r')
	var = []
	for line in f.readlines():
		var.append(line)
	f.close()
	return var
	
def write_file(out, var):
	f = open(out, 'w')
	f.writelines(var)
	f.close()


DVDPhotos = read_file('photos.txt')
XMLPhotos = read_file('photos_xml.txt')

dvd = Set(DVDPhotos)
xml = Set(XMLPhotos)

extras = dvd - xml
needed = xml - dvd

write_file('needed.txt', needed)
write_file('extras.txt', extras)
