import assignmentPart_2_pb2
from assignmentPart_2_pb2 import info,data_request
import json,os

dict_bench = {
    '1': 'DVD_testing.json',
    '2': 'DVD_training.json',
    '3': 'NDBench_testing.json',
    '4' : 'NDBench_training.json'
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


with open(dict_bench[benchmark_type], 'r') as file:
    data = file.read()

obj = json.loads(data)
my_list = []

for i in range(0,request_size):
    my_list.append(str(obj[i][dict_metric[workload_metric]]))

final = [my_list[i * int(batch_unit):(i + 1) * int(batch_unit)] for i in range((len(my_list) + int(batch_unit) - 1) // int(batch_unit))]

k = int(batch_id)
requested_batch = final[k]


test_obj = info()
test_obj.RFW_ID = int(rfw_id)
test_obj.last_batch_ID = int(batch_size)-1
test_obj.batch.extend(requested_batch)

out_dir = "proto_dump"
obj_new2 = data_request()

with open(os.path.join(out_dir, "assignment2.pb"), "wb") as f:
                 f.write(test_obj.SerializeToString())

with open(os.path.join(out_dir, "assignment2.protobuf"), "w") as f:
                 f.write(str(test_obj))


datarequest=info()
f = open('proto_dump/assignment2.pb','rb')
datarequest.ParseFromString(f.read())
print(datarequest)
f.close()



