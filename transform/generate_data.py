with open('train.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

train_datas = []
temp_data = ''
for line in lines:

    if line != '\n':
        line = line.strip()
        temp_data += (line + '\t')
    else:
        train_datas.append(temp_data)
        temp_data = ''

train_datas = sorted(train_datas, key=lambda x: len(x))
new_train_datas = []
for train_data in train_datas:
    if len(train_data) < 300:
        new_train_datas.append(train_data)
new_train_datas = new_train_datas[::2]
with open('dataset.txt', 'w', encoding='utf-8') as f:
    for train_data in new_train_datas:
        f.write(train_data + '\n')
