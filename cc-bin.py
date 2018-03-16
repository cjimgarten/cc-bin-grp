import pandas as pd

csv_file = pd.read_csv('cc-bin.csv')

cc_bin_combos = []
ccs = []
bins = []

for i, row in csv_file.iterrows():

	# get current cc and bin
	curr_cc = row['CC']
	curr_bin = row['Bin']
	
	# check if current row is unique
	if [curr_cc, curr_bin] in cc_bin_combos:
		
		# not unique
		print(i, " Not unique")
		
	else:
	
		# unique
		print(i, " Unique")
		cc_bin_combos.append([curr_cc, curr_bin])
		ccs.append(curr_cc)
		bins.append(curr_bin)
	
# write unique cc-bin combinations to csv file
df = pd.DataFrame(bins, ccs)
df.to_csv("unique-cc-bin-combos.csv")

print("Done!")
