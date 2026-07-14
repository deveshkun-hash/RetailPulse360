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
    for i in range(1,ROW_COUNTS["customers"]+1):
        rows.append({"CustomerID":i,"Name":fake.name(),"Email":fake.email(),"City":fake.city(),"JoinDate":fake.date_between(start_date='-5y',end_date='today')})
    pd.DataFrame(rows).to_csv(out/'customers.csv',index=False)
