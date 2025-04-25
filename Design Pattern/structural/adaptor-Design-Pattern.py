'''
This pattern allow to interact two classes each other
'''

class XMLData:
    def __init__(self, data):
        self.data = data

    def get_data(self):
        return self.data

class DataAnalyticsTool:
    def __init__(self, json_data):
        self.json_data = json_data

    def analyze_data(self):
        print(f'Analyzing data: {self.json_data}')

class Adapter(DataAnalyticsTool):
    def __init__(self, xml_data: XMLData):
        json_data = {"data": xml_data.get_data()}
        print(f'Converting XML data to JSON data: {json_data}')
        super().__init__(json_data)

class Client:
    def __init__(self, tool: DataAnalyticsTool):
        self.tool = tool

    def process_data(self):
        self.tool.analyze_data()


xml_data = XMLData("hello xml data")
tool = Adapter(xml_data)
client = Client(tool)
client.process_data()




