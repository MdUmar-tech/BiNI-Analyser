#!/usr/bin/env python3

import pandas as pd

# =====================
# INPUT FILES
# =====================
INPUT_CSV = "output_folder/bigslice_rank0_summary.csv"
OUTPUT_CSV = "output_folder/BiNI_result.csv"
THRESHOLD = 900

# =====================
# LOAD DATA
# =====================
df = pd.read_csv(INPUT_CSV)

# Number of BGCs (n)
n = len(df)

# BGCs with distance > threshold
novel_bgcs = df[df["distance"] > THRESHOLD]

# Sum of distances (Σd)
sum_d = novel_bgcs["distance"].sum()

# BiNI calculation
bini = sum_d / n if n > 0 else 0

# =====================
# SAVE RESULT
# =====================
result = pd.DataFrame([{
    "Total_BGCs (n)": n,
    "Novel_BGCs (distance > 900)": len(novel_bgcs),
    "Sum_of_Distances (Σd)": round(sum_d, 2),
    "BiNI": round(bini, 4)
}])

result.to_csv(OUTPUT_CSV, index=False)

print("✅ BiNI calculated successfully")
print(result)
