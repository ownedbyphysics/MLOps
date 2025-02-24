import pickle
import re
from pathlib import Path

__version__ = "0.1.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent

with open(f"{BASE_DIR}/pipeline-{__version__}.pkl", "rb") as f:
    model = pickle.load(f)
    
with open(f"{BASE_DIR}/encoder-{__version__}.pkl", "rb") as l:
    le = pickle.load(l)
    
    
def predict_pipeline(text):
    text = re.sub(r'[!@#$(),\n"%^*?\:;~`0-9]', ' ', text)
    text = re.sub(r'[[]]', ' ', text)
    text = text.lower()
    pred = model.predict([text])
    print(le.inverse_transform(pred)[0])
    return le.inverse_transform(pred)[0]  #classes[pred[0]]