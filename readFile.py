data = []
count = 0
strLen = 0
with open("reviews.txt", "r") as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))
print("File read completed! There are", len(data), "records in total!")

for record in data:
    strLen += len(record.strip())
averageLen = strLen/len(data)
print("The average length of reviews is", averageLen)