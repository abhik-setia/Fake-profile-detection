import csv

path = ''

fake_users_file=open( path +"fusers.csv", "r")
users_file=open( path +"users.csv", "r")
v=0
arff = open("fake_profile.arff", "w")
arff.write("@RELATION fake_profile\n")
arff.write("@ATTRIBUTE statuses_count  NUMERIC\n")
arff.write("@ATTRIBUTE followers_count  NUMERIC\n")
arff.write("@ATTRIBUTE friends_count  NUMERIC\n")
arff.write("@ATTRIBUTE favourites_count  NUMERIC\n")
arff.write("@ATTRIBUTE fake_profile {True,False}\n")
arff.write("@DATA\n")
reader = csv.reader(fake_users_file)
for line in reader:
    if (v!=0):
        buff=""
        values=line[3],line[4],line[5],line[6]
        buff+= (",".join([str(x) for x in values]) +', True' + "\n")
        arff.write(buff)
        print(v)
    v=v+1
v=0
reader = csv.reader(users_file)
for line in reader:
    if (v!=0):
        buff=""
        values=line[3],line[4],line[5],line[6]
        buff+= (",".join([str(x) for x in values]) +', False' + "\n")
        arff.write(buff)
        print(v)
    v=v+1

