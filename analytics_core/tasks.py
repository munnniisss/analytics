from analytics.celery import app
from clickhouse.query import insert_analytics_data_from_tips


@app.task
def create_analytics_row_task(data):
    print(f"Полученные данные: {data}")
    try:
        result = insert_analytics_data_from_tips(data=data)
        print(f"Результат вставки: {result}")
    except Exception as e:
        print(f"Ошибка: {e}")
