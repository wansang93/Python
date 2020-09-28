import csv
## 우리회사 연봉 평균은?

file_path = r'D:\☆☆☆멀캠생활\Image\csv\emp.csv'

with open(file_path) as rfp:
    # 방법2
    reader = csv.reader(rfp)
    header_list = next(reader)
    sum = 0
    count = 0
    for cList in reader:
        sum += int(cList[3])
        count += 1
    avg = sum // count
    print('평균연봉:', avg)

    # 방법1
    sum = 0
    line = rfp.readline()
    count = 0
    while True:
        line = rfp.readline()
        if not line:
            break
        count += 1
        line_list = line.split(',')
        sum += int(line_list[3])
    avg = sum // count
    print(avg)


