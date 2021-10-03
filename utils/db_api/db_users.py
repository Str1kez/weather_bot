import asyncpg
import asyncio

from data.config import PG_USER, PG_PASSWORD, PG_DB, PG_HOST, PG_PORT


class DataBase:
    def __init__(self, loop: asyncio.AbstractEventLoop):
        self.pool = loop.run_until_complete(
            asyncpg.create_pool(
                database=PG_DB,
                user=PG_USER,
                password=PG_PASSWORD,
                host=PG_HOST,
                port=PG_PORT
            )
        )

    async def drop_user_table(self):
        cmd = """
        DROP TABLE Users"""
        await self.pool.execute(cmd)

    async def create_user_table(self):
        cmd = """
        CREATE TABLE IF NOT EXISTS Users (
            request_id SERIAL PRIMARY KEY,
            user_id BIGINT NOT NULL,
            name_city VARCHAR(20) NOT NULL
        )
        """
        await self.pool.execute(cmd)

    async def insert_user(self, id, city):
        cmd = """
        INSERT INTO Users (user_id, name_city) VALUES ($1, $2)
        """
        await self.pool.execute(cmd, id, city)

    async def select_three_cities(self, id):
        cmd = """
        SELECT name_city FROM Users WHERE user_id = $1 ORDER BY request_id DESC LIMIT 3
        """
        cities = map(dict, await self.pool.fetch(cmd, id))
        return [d[city] for d in cities for city in d]

    async def user_reduction(self, id):
        cmd = """
        DELETE FROM Users WHERE request_id NOT IN
        (SELECT request_id FROM Users WHERE user_id = $1 ORDER BY request_id DESC LIMIT 3)
        AND user_id = $1
        """
        await self.pool.execute(cmd, id)
