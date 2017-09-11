import numpy as np
import pandas as pd

def read_csv():
	users_path="data/users.csv"
	fusers_path="data/fusers.csv"

	u_data=pd.read_csv(users_path)
	f_data=pd.read_csv(fusers_path)

	feature_columns_to_use = ['statuses_count','followers_count',
	'friends_count','favourites_count','listed_count','sex_code',
	'lang_code']

	arff_file=open('train.arff',"w")

	RELATION_NAME="Fake_profile"
	arff_file.write("@RELATION " + RELATION_NAME + "\n")
	
	for feature in feature_columns_to_use:
		if feature=="sex_code" or feature=="lang_code":
			arff_file.write("@ATTRIBUTE "+feature +" string \n")
		else:
			arff_file.write("@ATTRIBUTE "+feature +" real \n")

if __name__=="__main__":
	read_csv()