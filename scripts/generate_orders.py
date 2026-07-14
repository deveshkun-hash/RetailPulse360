import random
from faker import Faker
import pandas as pd
from pathlib import Path
from config import ROW_COUNTS, OUTPUT_DIR
fake=Faker()
out=(Path(__file__).parent/OUTPUT_DIR).resolve()
out.mkdir(parents=True,exist_ok=True)

def run():
    rows=[]
    for i in range(1,ROW_COUNTS["orders"]+1):
        rows.append({"OrderID":i,"CustomerID":random.randint(1,ROW_COUNTS["customers"]),"StoreID":random.randint(1,ROW_COUNTS["stores"]),"OrderDate":fake.date_between(start_date='-2y',end_date='today')})
    pd.DataFrame(rows).to_csv(out/'orders.csv',index=False)
