import pandas as pd

# Path file
file_a = r"D:\Code\skripsi_sentimen\02.Preprocessing\data\baru_preprocessed_A_stepwise_lengkap.csv"
file_c = r"D:\Code\skripsi_sentimen\02.Preprocessing\data\baru_preprocessed_C_stepwise__STEMwithoutStopword.csv"

# Load kedua file
df_a = pd.read_csv(file_a, encoding="utf-8-sig")
df_c = pd.read_csv(file_c, encoding="utf-8-sig")

print("Kolom A:", df_a.columns.tolist())
print("Kolom C:", df_c.columns.tolist())

# --- asumsi kunci gabung: id_str ---
# kalau mau lebih aman bisa pakai ["id_str", "full_text"] sebagai kunci

# Ambil hanya kolom yang dibutuhkan dari file C
cols_c = ["id_str", "text_stemmed_noSTOPWORD"]
df_c_small = df_c[cols_c].copy()

# Merge inner: hanya baris yang ada di kedua file
df_merged = pd.merge(
    df_a,
    df_c_small,
    on="id_str",
    how="inner",
    validate="one_to_one"  # kalau error, berarti ada duplikat
)

print("Rows A:", len(df_a))
print("Rows C:", len(df_c))
print("Rows merged:", len(df_merged))

out_path = r"D:\Code\skripsi_sentimen\02.Preprocessing\data\preprocessed_merged_stepwise.csv"
df_merged.to_csv(out_path, index=False, encoding="utf-8-sig")
print("✅ Saved to:", out_path)
