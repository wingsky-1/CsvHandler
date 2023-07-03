import csv
import os
import json


from defines import START_ROW
from processUtils import ProcessUtils


def main():
    # 从./config.json中读取配置文件
    config = {}
    with open('./config.json', 'r', encoding='utf-8') as file:
        config = json.load(file)

    # 遍历指定目录下的csv文件
    for root, dirs, files in os.walk('./data'):
        print(root, dirs, files)
        for file in files:
            if not '.csv' in file:
                continue
            processFile(root, file, config)


def processFile(root, file, config):
    """
    自定义处理文件入口
    """

    # 如果配置文件中没有all或者当前文件不在配置文件中则跳过
    if not 'all' in config and not file in config:
        return

    filePath = os.path.join(root, file)
    # TODO 文件格式修复，验证当前逻辑下修改的文件是否能够导入
    with open(filePath, 'r+', newline='') as f:
        fieldIndex, csvData = readCsv(f)
        print(fieldIndex, csvData)
        ProcessUtils(file, fieldIndex, csvData, config).process()
        wirteCsv(f, csvData)


def readCsv(file):
    """
    读取csv文件
    """

    fieldIndex = {}
    csvData = {}

    reader = csv.reader(file)
    for row in reader:
        if (reader.line_num == START_ROW - 1):
            # 将row转为字典 value为index
            for i in range(len(row)):
                fieldIndex[row[i]] = i
        rowId = reader.line_num
        csvData[rowId] = row

    return fieldIndex, csvData


def wirteCsv(file, csvData):
    """
    写入csv文件
    """

    file.seek(0)
    writer = csv.writer(file)
    writer.writerows(csvData.values())


if __name__ == '__main__':
    # test
    main()
