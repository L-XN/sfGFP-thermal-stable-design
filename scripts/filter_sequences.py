# 序列筛选脚本：去重 + 生色团校验
import pandas as pd
import os

# 确保 output 目录存在
os.makedirs("../output", exist_ok=True)

# 读取生成的序列
df = pd.read_csv("../output/final_sequences.csv")

# 1. 序列去重
df_unique = df.drop_duplicates(subset=["Sequence"])
print(f"✅ 去重完成，原始序列：{len(df)}，唯一序列：{len(df_unique)}")

# 2. 生色团完整性校验（必须保留 Ser65-Tyr66-Gly67，即 SYG）
def check_chromophore(seq):
    return "SYG" in seq[64:67]

df_valid = df_unique[df_unique["Sequence"].apply(check_chromophore)]
print(f"✅ 生色团校验完成，合格序列：{len(df_valid)}")

# 3. 保存筛选后的序列
df_valid.to_csv("../output/final_sequences_filtered.csv", index=False)
print("✅ 筛选完成！")
