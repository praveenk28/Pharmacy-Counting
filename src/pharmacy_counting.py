import sys
import csv

results = {}

input_file = open(sys.argv[1], 'r')

line = input_file.readline() #skip 1st line#

reader = csv.reader(input_file)

for row in reader:
    drugname = row[3]
    cost = float (row[4])
    prescriberid = row[0]
    if not drugname in results:
        results[drugname] = {'totalcost':cost, 'prescribers':set()}
        results[drugname]['prescribers'].add(prescriberid)
    else:
        entry = results[drugname]
        entry['totalcost'] += cost
        entry['prescribers'].add(prescriberid)

input_file.close()

output_file = open(sys.argv[2],'w')

output_file.write('drug_name,num_prescriber,total_cost\n')

writer = csv.writer(output_file)
sorted_keys = sorted(results.keys(),key = lambda drugname: (-int(results[drugname]['totalcost']), drugname))
for drugname in sorted_keys:
    writer.writerow( [drugname,len(results[drugname]['prescribers']),int(results[drugname]['totalcost'])] )
output_file.close()
    


    
