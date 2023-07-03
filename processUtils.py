

def addFields(utils, config):
    """
    config:
    [
        {
        fieldName : 'xxx',
        defalutValue : ''
        },
        ...
    ]
    """
    ...


def deleteFields(utils, config):
    """
    config:
    [
        'fieldName',
        ...
    ]
    """
    ...


def replaceFields(utils, config):
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


def replaceValues(utils, config):
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


def deleteRows(utils, config):
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


class ProcessUtils:
    """
    自定义处理文件工具类
    """

    def __init__(self, fileName, fieldIndex, csvData, config):
        self.fileName = fileName
        self.fieldIndex = fieldIndex
        self.csvData = csvData
        self.config = config

    def process(self):
        """
        自定义处理文件入口
        """
        self.processOnly()
        self.processAll()

    def processOnly(self):
        """
        处理only
        """
        if not self.fileName in self.config:
            return
        self.processConfig(self.config[self.fileName])

    def processAll(self):
        """
        处理all
        """
        if not 'all' in self.config:
            return
        self.processConfig(self.config['all'])

    def processConfig(self, config):
        for key, value in config.items():
            PROCESS_CONFIG[key](self, value)
