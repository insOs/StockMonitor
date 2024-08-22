import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

def analyze_stock_data(stock_code: str, stock_data: Dict[str, Any]) -> Dict[str, Any]:
    """分析股票数据并作出策略决策"""
    if stock_data.get('market_status') == "交易中":
        fluctuation = detect_price_fluctuation(stock_data)
        if fluctuation and abs(fluctuation) > 1.0:  # 价格波动大于1%
            logger.info(f"Significant price change detected for {stock_code}: {fluctuation}%")
            return fluctuation
    return "0"

def detect_price_fluctuation(stock_data: Dict[str, Any]) -> float:
    """检测价格波动"""
    price_info = stock_data.get('price_info', [])
    if len(price_info) >= 2:
        price_now = float(price_info[-1]["price"])
        price_old = float(price_info[-2]["price"])
        return round(((price_now - price_old) / price_old) * 100, 2)
    return 0.0
