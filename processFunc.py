

from defines import START_ROW
from processUtils import ProcessUtils


def addFields(utils: ProcessUtils, config: list[dict]):
    """
    config:
    [
        {
        fieldName : 'xxx',
        defalutValue : '' // 可选 默认为''
        },
        ...
    ]
    """
    ...
    fieldNames = []
    defalutValues = []
    for fieldInfo in config:
        fieldNames.append(fieldInfo['fieldName'])
        defalutValues.append(fieldInfo.get('defalutValue', ''))

    # 添加字段
    for rowId, row in utils.csvData.items():
        if rowId == START_ROW - 1:
            row.extend(fieldNames)
            for i in range(len(row)):
                utils.fieldIndex[row[i]] = i
        else:
            if rowId < START_ROW:
                continue
            row.extend(defalutValues)


def deleteFields(utils: ProcessUtils, config: list[str]):
    """
    config:
    [
        'fieldName',
        ...
    ]
    """
    ...


def replaceFields(utils: ProcessUtils, config: list[dict]):
    """
    config:
    [
        {
        fieldName : 'xxx',
        replaceValue : 'xxx'
        },
        ...
    ]
    """
    ...


def replaceValues(utils: ProcessUtils, config: list[dict]):
    """
    config:
    [
        {
        fieldName : 'xxx',
        targetValue : 'xxx',
        replaceValue : 'xxx'
        },
        ...
    ]
    """
    ...


def deleteRows(utils: ProcessUtils, config: list[dict]):
    """
    config:
    [
        {
        rowIndex : 'xxx',
        },
        {
        fieldName : 'xxx',
        targetValue : 'xxx'
        },
        ...
    ]
    """
    ...


PROCESS_CONFIG = {
    'addFields': addFields,
    'deleteFields': deleteFields,
    'replaceFields': replaceFields,
    'replaceValues': replaceValues,
    'deleteRows': deleteRows
}
