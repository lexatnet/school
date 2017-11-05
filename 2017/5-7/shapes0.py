def itemOutput(item):
	color = 0;
	dimentions = 1;
	weight = 2;
	print('shape color={} dimentions={} weight={}'.format(
		item[color],
		item[dimentions],
		item[weight]
		)
	)


bucket = [
('red', 1, 1),
('blue', 1, 1),
('red', 2, 1),
('red', 1, 4),
('blue', 1, 2),
('red', 1, 1)
];

bucket1=[];
bucket2=[];
bucket3=[];
bucket4=[];


color = 0;
dimentions = 1;
weight = 2;


for i in range(0, len(bucket)):
	item = bucket[i];
	if (item[color] == 'red'):
		bucket1.append(item)
	if ((item[color] == 'blue') and (item[weight] < 2)):
		bucket2.append(item)
	itemOutput(bucket[i])

print('Red Bucket')
for i in range(0, len(bucket1)):
	itemOutput(bucket1[i])