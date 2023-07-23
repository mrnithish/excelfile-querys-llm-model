import torch
from transformers import pipeline
import pandas as pd
tqa = pipeline(task="table-question-answering",model="google/tapas-base-finetuned-wtq")
table=pd.read_csv("data.csv")
table = table.astype(str)
# table

query = "Who has secured the highest sgpa?"
print(tqa(table=table,query=query)["answer"])
          