import os

from pathlib import Path
from dotenv import load_dotenv

from clickhouse_driver import Client
from clickhouse_migrations.clickhouse_cluster import ClickhouseCluster

load_dotenv()


def migrate_db() -> None:
    """
    Функция для миграции БД и применения всех изменений к ней
    :return:
    """

    cluster = ClickhouseCluster(
        db_host=os.getenv("CLICKHOUSE_HOST"),
        db_port="9000",
        db_user=os.getenv("CLICKHOUSE_USER"),
        db_password=os.getenv("CLICKHOUSE_PASSWORD"),
    )

    migration_path = Path(__file__).parent / "migrations"

    migrations = cluster.migrate(
        db_name=os.getenv("CLICKHOUSE_DB"), create_db_if_no_exists=True, migration_path=migration_path
    )


def setup_client() -> Client:
    """
    Функция для создания клиента ClickHouse и применения миграций к нему
    :return:
    """
    clickhouse_driver = Client(
        host=f"{os.getenv('CLICKHOUSE_HOST')}",
        port="9000",
        user=os.getenv("CLICKHOUSE_USER"),
        password=os.getenv("CLICKHOUSE_PASSWORD"),
        database=os.getenv("CLICKHOUSE_DB"),
    )

    migrate_db()

    return clickhouse_driver


client = setup_client()
