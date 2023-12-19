class UnifiedInterface:
    def __init__(self):
        # 初始化各种模块
        self.module1 = Module1()
        self.module2 = Module2()
        # 可以添加更多模块

    def process(self, input_data):
        """处理输入数据并返回结果"""
        # 使用模块1处理数据
        result1 = self.module1.process(input_data)

        # 使用模块2处理数据
        result2 = self.module2.process(input_data)

        # 根据需要添加更多模块的处理步骤

        # 返回所有模块的处理结果
        return result1, result2

# 示例模块类
class Module1:
    def process(self, data):
        # 模块1的处理逻辑
        return f"Module1 processed: {data}"

class Module2:
    def process(self, data):
        # 模块2的处理逻辑
        return f"Module2 processed: {data}"

# 使用统一接口
interface = UnifiedInterface()
input_data = "Some input data"
results = interface.process(input_data)
print(results)
