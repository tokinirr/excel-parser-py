import pandas as pd
from filters import apply_filters
from utils import load_config


cfg = load_config("config/config.yaml")


df = pd.read_excel(cfg["input_file"])


results = apply_filters(df, cfg["filters"])


with pd.ExcelWriter(cfg["output_file"]) as writer:
for name, data in results.items():
data.to_excel(writer, sheet_name=name, index=False)


print("Traitement fini")
