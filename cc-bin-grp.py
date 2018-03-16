import pandas as pd

combos = pd.read_csv('unique-cc-bin-combos.csv')
cc_bin_grp = pd.read_csv('cc-bin-grp.csv')

for i, combos_row in combos.iterrows():
	combos_cc = combos_row['CC']
	combos_bin = combos_row['Bin']
	
	grps_list = []
	for j, row in cc_bin_grp.iterrows():
		cc = row['CC']
		bin = row['Bin']
		grp = row['Group No']
		
		if combos_cc == cc and combos_bin == bin:
		
			# match found
			grps_list.append(grp)
			
	grps_str = ','.join(grps_list)
	final_row = [combos_cc, combos_bin, grps_str]
	print(final_row)

print("Done!")
