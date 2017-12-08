#
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

def printBucket(bucket, bucketName):
	if (len(bucket) == 0): # проверяем пустая ли корзина
		print('{} is empty'.format(bucketName))
		return
	print('In {}'.format(bucketName))
	for i in range(0, len(bucket)):
		itemOutput(bucket[i])
	message = 'end of bucket {}'.format(bucketName)
	print(message)
	
def analyseBucket(bucket, redBucket, blueBucket):
	for i in range(0, len(bucket)):
		item = bucket[i];
		if (item[color] == 'red'):
			redBucket.append(item)
		if ((item[color] == 'blue') and (item[weight] < 2)):
			blueBucket.append(item)

bucket = [
('red', 1, 1),
('blue', 1, 1),
('red', 2, 1),
('red', 1, 4),
('blue', 1, 2),
('red', 1, 1)
];

printBucket(bucket, "BaseBucket")

bucket1=[];
bucket2=[];
bucket3=[];
bucket4=[];


color = 0;
dimentions = 1;
weight = 2;



analyseBucket(bucket, bucket1, bucket2)
printBucket(bucket1, "Red bucket")
printBucket(bucket2, "Blue lite bucket")
printBucket(bucket3, "bucket3")
printBucket(bucket4, "bucket4")
