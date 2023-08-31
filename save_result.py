import csv
import asyncio

async def save_result(result):
    with open('test.csv','a+') as f:
        writer = csv.writer(f)
        writer.writerow([result])
    