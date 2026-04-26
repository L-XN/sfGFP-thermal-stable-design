# 序列合规性校验工具
import pandas as pd

print("="*50)
print("sfGFP 提交序列最终校验工具")
print("="*50)

# 读取序列
df = pd.read_csv("../output/final_sequences.csv")
sequences = df["Sequence"].tolist()

# 校验1：无重复序列
if len(sequences) == len(set(sequences)):
    print("✅ 校验通过：6条序列完全无重复")
else:
    print("❌ 校验失败：存在重复序列")

# 校验2：生色团完整
all_chromophore_ok = True
for i, seq in enumerate(sequences):
    if "SYG" in seq[64:67]:
        print(f"✅ Seq{i+1} 生色团完整")
    else:
        print(f"❌ Seq{i+1} 生色团损坏！")
        all_chromophore_ok = False

# 校验3：序列长度正确（sfGFP 为 238 aa）
all_length_ok = True
for i, seq in enumerate(sequences):
    if len(seq) == 238:
        print(f"✅ Seq{i+1} 长度正确 (238 aa)")
    else:
        print(f"❌ Seq{i+1} 长度异常")
        all_length_ok = False

print("\n=== 校验总结 ===")
if len(sequences) == len(set(sequences)) and all_chromophore_ok and all_length_ok:
    print("✅ 所有校验通过，序列可安全提交！")
else:
    print("❌ 存在问题，请修正后再提交。")
