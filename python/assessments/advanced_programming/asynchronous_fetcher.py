# https://www.programmingexpert.io/advanced-programming/assessment/5

import asyncio

class BatchFetcher:
    # The `database` has an `async_fetch` method
    # that you should use in your code. This method
    # takes in a record id and returns a record.
    def __init__(self, database):
        self.database = database

    # Write your code here.
    async def fetch_records(self, record_ids):
        operations = []
        for id in record_ids:
            task = self.database.async_fetch(id)
            operations.append(task)

        records = await asyncio.gather(*operations)
        return records