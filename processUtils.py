

class ProcessUtils:
    """
    自定义处理文件工具类
    """

    def __init__(self, fileName: str, fieldIndex: dict[str, int], csvData: dict[int, list[str]], config: dict[str, dict[str, any]]):
        self.fileName = fileName.replace('.csv', '')
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
        处理当前文件特定配置
        """
        if not self.fileName in self.config:
            return
        self.processConfig(self.config[self.fileName])

    def processAll(self):
        """
        处理所有文件都要执行的配置
        """
        if not 'all' in self.config:
            return
        self.processConfig(self.config['all'])

    def processConfig(self, config: dict[str, any]):
        from processFunc import PROCESS_CONFIG
        for key, value in config.items():
            PROCESS_CONFIG[key](self, value)
