import os
from HW1gen import testset_path, slash

input_path = testset_path + 'input' + slash
output_path = testset_path + 'output' + slash

cnt = 0
for path in (input_path, output_path):
    for filename in os.listdir(path):
        if filename.startswith('custom'):
            os.remove(path + filename)
            cnt += 1

print("Removed {} custom testcase files.".format(cnt))
