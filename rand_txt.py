import random
in_file = 'in.txt'
out_file = 'out.txt'

data = [x.strip() for x in open(in_file)]
random.shuffle(data)
with open(out_file, 'w') as f:
    f.write('\n'.join(data))
