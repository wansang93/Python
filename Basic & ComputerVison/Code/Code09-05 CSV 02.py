import csv
import tkinter.filedialog

# file_name = tkinter.filedialog.askopenfilename(parent=None,
#             filetypes=(('csv file', '*.csv'), ('all file', '*.*')))

file_name = r'D:/☆☆☆멀캠생활/image/csv/supplier_data.csv'

# 참고 파일
"""
Supplier Name,Invoice Number,Part Number,Cost,Purchase Date
Supplier X,001-1001,2341,$500.00,1/20/14
Supplier X,001-1001,2341,$500.00,1/20/14
Supplier X,001-1001,5467,$750.00,1/20/14
Supplier X,001-1001,5467,$750.00,1/20/14
Supplier Y,50-9501,7009,$250.00,1/30/14
Supplier Y,50-9501,7009,$250.00,1/30/14
Supplier Y,50-9505,6650,$125.00,2/3/14
Supplier Y,50-9505,6650,$125.00,2/3/14
Supplier Z,920-4803,3321,$615.00,2/3/14
Supplier Z,920-4804,3321,$615.00,2/10/14
Supplier Z,920-4805,3321,$615.00,2/17/14
Supplier Z,920-4806,3321,$615.00,2/24/14
"""

# 파일을 읽어서 리스트로 저장
csv_list = []
with open(file_name) as rfp:
    reader = csv.reader(rfp)
    header_list = next(reader)
    for line in reader:
        csv_list.append(line)

# 가격 10% 인상시키기
header_list = [data.upper().strip() for data in header_list]
pos = header_list.index('COST')

for i in range(len(csv_list)):
    cost = float(csv_list[i][pos][1:])
    cost *= 1.1
    cost_str = f'{cost:.2f}'
    csv_list[i][pos] = cost_str
print(csv_list)

# 결과 저장하기
save_fp = tkinter.filedialog.asksaveasfile(
    parent=None,
    mode='wt',
    defaultextension='*.csv',
    filetypes=(('csv file', '*.csv'), ('all file', '*.*'))
    )

with open(save_fp.name, mode='w', newline='') as wfp:
    writer = csv.writer(wfp)
    writer.writerow(tuple(header_list))
    for row in csv_list:
        writer.writerow(row)
