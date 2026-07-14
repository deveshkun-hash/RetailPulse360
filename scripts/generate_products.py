import random
from faker import Faker
import pandas as pd
from pathlib import Path
from config import ROW_COUNTS, OUTPUT_DIR
fake=Faker()
out=(Path(__file__).parent/OUTPUT_DIR).resolve()
out.mkdir(parents=True,exist_ok=True)

cats=['Electronics','Fashion','Home','Sports','Beauty']
def run():
    rows=[]
    for i in range(1,ROW_COUNTS["products"]+1):
        price=round(random.uniform(5,500),2)
        rows.append({"ProductID":i,"ProductName":fake.word().title(),"Category":random.choice(cats),"Price":price})
    pd.DataFrame(rows).to_csv(out/'products.csv',index=False)
