from prompt_toolkit.shortcuts.utils import clear
from lib import analyseBucket, getNewBucketItems, printBucket, loadBucketFromFile, saveBucketItems

from prompt_toolkit.shortcuts.dialogs import input_dialog

shapes_db_name = input_dialog(
        title='Open DB',
        text='Please enter shapes DB name:')

bucket = loadBucketFromFile(shapes_db_name)
newItems = getNewBucketItems()

bucket = bucket + newItems

saveBucketItems(shapes_db_name, newItems)

redBucket = []
blueBucket = []

analyseBucket(bucket, redBucket, blueBucket)


printBucket(bucket, 'Origin')
printBucket(redBucket, 'Red')
printBucket(blueBucket, 'Blue')
