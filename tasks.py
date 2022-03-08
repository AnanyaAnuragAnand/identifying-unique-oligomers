import pandas as pd 

df = pd.read_csv('C:/Users/anany/Desktop/COMP.BIO._PYTHON_SCRIPTS/proteins.fasta', delimiter='\t')

data_list, end_data, = [], [],
for index, row in df.iterrows():
    pass

for i in range(index):
    if ">gi" not in str(df.iloc[i, 0]):
        a_string = str(df.iloc[i, 0])
        for index in range(0, len(a_string), 10):
            data_list.append(a_string[index: index + 10])

for rec in data_list:
	if len(rec) == 10:
		end_data.append(rec)

data_set = set(end_data)
count_data = []
for res in data_set:
	count=0
	for data in end_data:
    		if data == res: 
        		count += 1 
	print(res, count)
	count_data.append(count)

count_data2 = count_data
count_data = list(set(count_data))
count_data.sort()
if not len(count_data)%2:
	start = len(count_data) // 2
	end = start + 1
	median = (count_data[start] + count_data[end]) / 2

else:
	median = count_data[start] // 2 

sum_total = 0
for record in count_data2:
	sum_total += record
mean = sum_total / len(count_data2)


print("min:", count_data[0])
print("max:", count_data[len(count_data)-1])
print("median:", median)
print("mean:", mean)
variance_total = 0
for re in count_data2:
	variance_total += (re - mean) * (re - mean)
print("variance:", variance_total / len(count_data2))


