import glob

people = []
i = 0
for fn in glob.glob('apps/*')[:]:
	# print fn
	f = open(fn, 'r')
	# print f.readlines()
	name = [s for s in f.readlines() if 'name:' in s.lower()]
	print fn, name
	# email = [s for s in f.readlines() if 'email address:' in s.lower()]
	# print email
	# people.append((name,email))
	i += 1