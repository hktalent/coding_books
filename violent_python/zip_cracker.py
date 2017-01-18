import zipfile
import threading
import sys

def attempt_password(z_file, password):
	try:
		z_file.extractall(pwd=password)
		print '[+] Password Found: ' + password + '.\n'
	except:
		print '[-] Password not found.\n'

def start(zip_file, dict_file):
	try:
		password_file = open(dict_file)
		z_file = zipfile.ZipFile(zip_file)
	except:
		print 'Error opening zipfile or dictionary'
		sys.exit(0)

	for line in password_file.readlines():
		password = line.strip('\n')

		t = threading.Thread(target=attempt_password, args=(z_file, password))
		t.start() 
		
def main():
	zip_file = ''
	dict_file = ''

	try:
		zip_file = sys.argv[1]
		dict_file = sys.argv[2]
	except:
		print 'Usage: zip_cracker.py [zipfile] [dictionary file]'
		sys.exit(0)

	start(zip_file, dict_file)

