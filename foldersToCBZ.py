import zipfile 
import os

print([x[0] for x in os.walk('.')])

list = [x[0] for x in os.walk('.')]

with zipfile.ZipFile('full.zip', 'a', compression=zipfile.ZIP_STORED) as zf:
	for el in list:
		if el != '.' and el != '..':
			for page in os.listdir(el):
				print(str(el), ':', str(page))
				zf.write(el+'/'+page, str(el)+'-'+str(page))