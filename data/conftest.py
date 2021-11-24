# –*–coding:utf-8 –*–
# 2021-11-24 09:23
import pytest
import requests

def pytest_collect_file(parent, path):
    # 获取文件.yml 文件,匹配规则
    if path.ext == ".yml" and path.basename.startswith("test"):
        # print(path)
        # print(parent)
        return YamlFile(path, parent)



class YamlFile(pytest.File):
    # 读取文件内容
    def collect(self):
        import yaml
        raw = yaml.safe_load(self.fspath.open(encoding='utf-8'))
        for yaml_case in raw:
            name = yaml_case["test"]["name"]
            values = yaml_case["test"]
            yield YamlTest(name, self, values)


class YamlTest(pytest.Item):
    def __init__(self, name, parent, values):
        super(YamlTest, self).__init__(name, parent)
        self.name = name
        self.values = values
        self.request = self.values.get("request")
        self.validate = self.values.get("validate")
        self.s = requests.session()

    def runtest(self):
        # 运行用例
        request_data = self.values["request"]
        # print(request_data)
        response = self.s.request(**request_data)
        print("\n", response.text)
        # 断言
        self.assert_response(response, self.validate)

    def assert_response(self, response, validate):
        '''设置断言'''
        import jsonpath
        for i in validate:
            if "eq" in i.keys():
                yaml_result = i.get("eq")[0]
                actual_result = jsonpath.jsonpath(response.json(), yaml_result)
                expect_result = i.get("eq")[1]
                print("实际结果：%s" % actual_result)
                print("期望结果：%s" % expect_result)
                assert actual_result[0] == expect_result

if __name__ == '__main__':
    pytest.main()
