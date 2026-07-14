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
    for i in range(1,ROW_COUNTS["order_items"]+1):
        qty=random.randint(1,5)
        price=round(random.uniform(5,500),2)
        rows.append({"OrderItemID":i,"OrderID":random.randint(1,ROW_COUNTS["orders"]),"ProductID":random.randint(1,ROW_COUNTS["products"]),"Quantity":qty,"UnitPrice":price,"LineTotal":round(qty*price,2)})
    pd.DataFrame(rows).to_csv(out/'order_items.csv',index=False)
