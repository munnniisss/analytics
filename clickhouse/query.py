import os

from dotenv import load_dotenv
from datetime import datetime

import time

from clickhouse.client import client

load_dotenv()

def insert_analytics_data_from_tips(data) -> bool:
    """
    Вставка данных в CLickhouse по схеме таблицы аналитики
    :param data: Данные аналитики
    :return:
    """

    columns = (
        'network_name', 'city_name', 'company_name', 'salon_name', 'manager_name',
        'deal_amount', 'from_status', 'external_id', 'to_status', 'created_at'
    )

    value = [
        data.get("network_name", ''),
        data.get("city_name", ''),
        data.get("company_name", ''),
        data.get("salon_name", ''),
        data.get("manager_name", ''),
        data.get("deal_amount", 0.0),
        data.get("from_status", 'EMPTY'),
        data.get("external_id", ''),
        data.get("to_status", ''),
        datetime.fromisoformat(data.get("created_at")) if data.get("created_at") else datetime.now(),

    ]

    query = f"INSERT INTO {os.getenv('CLICKHOUSE_DB')}.deals ({', '.join(columns)}) VALUES"

    result = client.execute(query, [tuple(value)])
    print("Заснул на конец")
    time.sleep(3)
    print("Проснулся под конец")

    return bool(result)
