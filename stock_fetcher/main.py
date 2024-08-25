import asyncio
import logging
from config import settings
from app.services.stock_service import periodic_stock_fetch
from app.services.rabbitmq_service import start_rabbitmq_listener

# 设置 pika 的日志级别为 WARNING 或更高，以隐藏调试和信息日志
logging.getLogger('pika').setLevel(logging.WARNING)
logging.basicConfig(level=getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO))
logger = logging.getLogger(__name__)

subscribed_stocks = set()

async def main():
    loop = asyncio.get_event_loop()
    
    # 启动RabbitMQ监听器
    loop.run_in_executor(None, start_rabbitmq_listener, subscribed_stocks)
    
    # 启动定时器获取股票数据
    await periodic_stock_fetch(subscribed_stocks)

if __name__ == "__main__":
    asyncio.run(main())
