"""
自定义 Tool 开发 - 构建天气查询工具
"""

from langchain.tools import tool, BaseTool
from pydantic import BaseModel, Field
from typing import Optional


# ============== 方式一：@tool 装饰器 ==============

@tool
def get_stock_price(symbol: str) -> str:
    """获取股票当前价格。
    
    Args:
        symbol: 股票代码，例如 AAPL, GOOGL, MSFT
    
    Returns:
        股票价格信息
    """
    # 模拟数据（实际项目中调用真实 API）
    stocks = {
        "AAPL": "$178.50",
        "GOOGL": "$140.25",
        "MSFT": "$378.90",
        "TSLA": "$245.60"
    }
    price = stocks.get(symbol.upper())
    if price:
        return f"{symbol} 当前价格: {price}"
    return f"未找到股票代码 {symbol}"


# ============== 方式二：BaseTool 类 ==============

class WeatherInput(BaseModel):
    city: str = Field(description="城市名称")
    unit: str = Field(default="celsius", description="温度单位: celsius 或 fahrenheit")


class WeatherTool(BaseTool):
    """天气查询工具"""
    name = "get_weather"
    description = "获取指定城市的天气信息，用于回答关于天气的问题。"
    
    args_schema = WeatherInput
    
    # 模拟天气数据
    _weather_db = {
        "北京": {"celsius": "25°C", "fahrenheit": "77°F", "condition": "晴天"},
        "上海": {"celsius": "28°C", "fahrenheit": "82°F", "condition": "多云"},
        "东京": {"celsius": "22°C", "fahrenheit": "72°F", "condition": "雨天"},
        "纽约": {"celsius": "20°C", "fahrenheit": "68°F", "condition": "晴"},
    }
    
    def _run(self, city: str, unit: str = "celsius") -> str:
        city_data = self._weather_db.get(city)
        if not city_data:
            return f"抱歉，暂无 {city} 的天气数据"
        
        temp = city_data.get(unit)
        condition = city_data.get("condition")
        return f"{city}今天{condition}，气温{temp}"


# ============== 使用示例 ==============

if __name__ == "__main__":
    # 测试装饰器工具
    print("=" * 50)
    print("股票工具测试:")
    print(get_stock_price.invoke({"symbol": "AAPL"}))
    
    # 测试 BaseTool 类
    print("\n" + "=" * 50)
    print("天气工具测试:")
    weather = WeatherTool()
    print(weather.run({"city": "北京", "unit": "celsius"}))
    print(weather.run({"city": "东京"}))
