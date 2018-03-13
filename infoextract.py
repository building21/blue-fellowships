import glob

people = []
emails = []
for fn in glob.glob('newapps/*')[:]:
	# print fn
	f = open(fn, 'r')
	lines = f.readlines()
	name = lines[0][6:-2]
	email = lines[2][15:-2]
	# app = fn[5:-4] #apps
	app = fn[8:-4] #newapps
	enroll = lines[4][15:-2]
	date = lines[-1:][0]
	people.append([app,name,email,enroll,date])
	emails.append((email,app))

#find duplicates
dups = [[],[]]
for e,app in emails:
	check = [1 for s in emails if e in s]
	if sum(check) > 1:
		if e in dups[0]:
			pass
		else:
			#find dups
			dups[1].append([app for s,app in emails if e in s])
			dups[0].append(e)

for i in range(len(dups[0])):
	print dups[0][i], dups[1][i]

import csv
with open('apps.csv', 'wb') as csvfile:
	w = csv.writer(csvfile)
	w.writerow(['Application Number', 'Name', 'Email', 'Faculty/Year', 'Date'])
	for person in people:
		w.writerow(person)