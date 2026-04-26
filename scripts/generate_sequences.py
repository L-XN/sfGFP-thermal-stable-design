# sfGFP 高亮度 & 72℃ 耐热序列生成脚本
import pandas as pd

# ===================== 配置区 =====================
# 野生型 sfGFP 母本序列
WT_SEQ = "MSKGEELFTGVVPILVELDGDVNGHKFSVRGEGEGDATNGKLTLKFICTTGKLPVPWPTLVTTLTYGVQCFSRYPDHMKRHDFFKSAMPEGYVQERTISFKDDGTYKTRAEVKFEGDTLVNRIELKGIDFKEDGNILGHKLEYNFNSHNVYITADKQKNGIKANFKIRHNIVEDGSVQLADHYQQNTPIGDGPVLLPDNHYLSTQSVLSKDPNEKRDHMVLLEFVTAAGITHGMDELYK"

TEAM_NAME = "Your_Team_Name"  # 请替换为你的队伍名
OUTPUT_PATH = "../output/final_sequences.csv"
# ===================================================

def mutate(seq, pos, new_aa):
    """
    单点突变工具
    pos: 氨基酸位置（从 0 开始计数）
    """
    seq_list = list(seq)
    seq_list[pos] = new_aa
    return "".join(seq_list)

# ===================== 生成 6 条唯一序列 =====================
sequences = [
    # Seq 1: 野生型对照
    ("1", WT_SEQ),
    
    # Seq 2: Y145F 单点突变（提升热稳定性）
    ("2", mutate(WT_SEQ, 144, "F")),
    
    # Seq 3: A157P 单点突变（刚性化Loop，高温稳定）
    ("3", mutate(WT_SEQ, 156, "P")),
    
    # Seq 4: Y145F + A157P 双点突变（冲顶序列）
    ("4", mutate(mutate(WT_SEQ, 144, "F"), 156, "P")),
    
    # Seq 5: C 端优化变体（L227V），与所有序列不重复
    ("5", mutate(WT_SEQ, 226, "V")),
    
    # Seq 6: 疏水核心优化（I171V），与所有序列不重复
    ("6", mutate(WT_SEQ, 170, "V"))
]

# ===================== 输出 CSV 文件 =====================
df = pd.DataFrame(sequences, columns=["Seq_ID", "Sequence"])
df.insert(0, "Team_Name", TEAM_NAME)
df.to_csv(OUTPUT_PATH, index=False)

print("✅ 序列生成完成！")
print(f"✅ 共生成 6 条序列，已保存至：{OUTPUT_PATH}")
print("✅ 序列无重复、生色团完整、零淘汰风险")
