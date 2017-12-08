from shapeslib import analyseBucket, getNewBucketItems, printBucket, loadBucketFromFile, saveBucketItems

bucket = loadBucketFromFile('shapes.data')
newItems = getNewBucketItems()

bucket = bucket + newItems

saveBucketItems('shapes.data', newItems)

redBucket = []
blueBucket = []

analyseBucket(bucket, redBucket, blueBucket)

printBucket(bucket, 'Origin')
printBucket(redBucket, 'Red')
printBucket(blueBucket, 'Blue')
