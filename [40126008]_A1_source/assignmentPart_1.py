import pandas as pd
import json


dict_bench = {
    '1': 'DVD_testing.csv',
    '2': 'DVD_training.csv',
    '3': 'NDBench_testing.csv',
    '4' : 'NDBench_training.csv'
}

dict_metric = {
    '1': 'CPUUtilization_Average',
    '2': 'NetworkIn_Average',
    '3': 'NetworkOut_Average',
    '4': 'MemoryUtilization_Average',
    '5': 'Final_Target'
}


rfw_id = input("Enter the RFW ID\n")
benchmark_type = input('What is the benchmark type you require? Choose from the following:\n 1: DVD testing \n 2: DVD training\n 3: NDBench testing\n 4: NDBench training\n ')
workload_metric = input("What is the workload metric you require? Choose from the following:\n 1: Cpu utilization average\n 2: Network in average\n 3: Network out average\n 4: Memory utilization average\n 5: Final target \n")
batch_unit = input('How many units do you want in one batch?\n')
batch_size = input('How many batches do you require?\n')
batch_id = input('Which batch of data do you want? (Batch IDs start from 0)\n')

request_size = int(batch_unit)*int(batch_size)
try:
    df = pd.read_csv(dict_bench[benchmark_type])
    requested_data = df[dict_metric[workload_metric]][0:request_size]
except:
    print("Enter a valid key please!")
    quit()

list = []
for line in requested_data:
    list.append(line)

final = [list[i * int(batch_unit):(i + 1) * int(batch_unit)] for i in range((len(list) + int(batch_unit) - 1) // int(batch_unit))]
k = int(batch_id)
try:
    requested_batch = final[k]
except:
    print("Enter a valid batch please!")
    quit()

dict_request = {
   'RFW ID':" ",
   'Last batch ID' : " ",
   'Requested data': " "
}
dict_request['RFW ID'] = rfw_id
dict_request['Last batch ID'] = int(batch_size)-1
dict_request['Requested data']= requested_batch


json_format = json.dumps(dict_request)

with open('app.json', 'w') as f:
   json.dump(json_format, f)

with open('app.json') as file:
   data = json.load(file)

print(data)









