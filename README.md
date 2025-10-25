# 🎓 Analisis Sentimen Layanan KAI Access Menggunakan IndoBERTweet dan Algoritma Random Forest

Repositori ini berisi kode, dataset, dan dokumentasi pendukung untuk penelitian skripsi berjudul **"Analisis Sentimen Layanan KAI Access Menggunakan IndoBERTweet dan Algoritma Random Forest"**.  
Penelitian ini dilakukan sebagai bagian dari tugas akhir **Program Studi Teknik Informatika, Fakultas Ilmu Komputer, Universitas Brawijaya**.

---

## 📘 Deskripsi Singkat
Penelitian ini bertujuan untuk **mengidentifikasi dan menganalisis sentimen masyarakat terhadap layanan KAI Access** berdasarkan data tweet berbahasa Indonesia.  
Model utama yang digunakan adalah **IndoBERTweet** untuk ekstraksi fitur berbasis bahasa alami (embedding), yang kemudian diklasifikasikan menggunakan algoritma **Random Forest** guna memperoleh hasil analisis yang akurat dan interpretatif.

---

## 🧠 Metodologi
1. **Pengumpulan Data**
   - Data diambil dari platform **Twitter** menggunakan pustaka `snscrape`.
   - Kata kunci pencarian: `"KAI Access"`, `"KAIACCESS"`, `"KAI"`, dan variasinya.
   - Rentang waktu: Desember 2022 – Desember 2023.

2. **Preprocessing**
   - Case folding, tokenisasi, penghapusan tanda baca, URL, mention, dan stopword.
   - Normalisasi teks informal ke bentuk baku.

3. **Feature Extraction**
   - Representasi vektor menggunakan **IndoBERTweet** pretrained model dari HuggingFace.

4. **Klasifikasi**
   - Model **Random Forest** digunakan untuk klasifikasi sentimen (`positif`, `netral`, `negatif`).

5. **Evaluasi**
   - Menggunakan metrik **Accuracy**, **Precision**, **Recall**, dan **F1-Score**.

---

## ⚙️ Teknologi & Tools
| Kategori | Teknologi |
|-----------|------------|
| Bahasa Pemrograman | Python 3.10+ |
| NLP Model | IndoBERTweet |
| Machine Learning | Random Forest (Scikit-Learn) |
| Data Crawling | snscrape |
| Data Processing | Pandas, NumPy, Regex |
| Visualization | Matplotlib, Seaborn |
| Environment | Jupyter Notebook / VS Code |

---

## 📂 Struktur Folder
```

📦 skripsi_sentimen
├── data/
│   ├── raw/                # Dataset mentah hasil crawling
│   ├── processed/          # Dataset setelah preprocessing
│   └── labeled/            # Dataset hasil labeling manual
├── models/
│   ├── indobertweet_finetuned/
│   └── random_forest.pkl
├── notebooks/
│   ├── 01_crawling.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_finetuning_indoBERT.ipynb
│   ├── 04_random_forest.ipynb
│   └── 05_evaluation.ipynb
├── requirements.txt
├── README.md
└── main.py

````

---

## 🚀 Cara Menjalankan Proyek
### 1️⃣ Kloning repositori
```bash
git clone https://github.com/ahmdzzzki/skripsi_sentimen.git
cd skripsi_sentimen
````

### 2️⃣ Buat virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate   # macOS / Linux
# atau
.venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Jalankan Notebook

```bash
jupyter notebook
```

---

## 📊 Hasil & Temuan

* Model **IndoBERTweet + Random Forest** memberikan **akurasi tertinggi mencapai ±0.84**.
* Sentimen **positif** mendominasi, terutama terkait kemudahan transaksi dan fitur digital KAI Access.
* Sentimen **negatif** sering muncul pada isu *error system*, *delay update*, dan *kendala login akun*.

---

## 📜 Lisensi

Proyek ini dibuat untuk keperluan akademik dan penelitian.
Hak cipta © 2025 **Ahmad Zaki**, Universitas Brawijaya.

---

## 📫 Kontak

**Ahmad Zaki**
📍 Fakultas Ilmu Komputer, Universitas Brawijaya
💼 [LinkedIn](https://linkedin.com/in/ahmdzki)
🌐 [ahmdzki.vercel.app](https://ahmdzki.vercel.app)
📧 [ahmadzaki12@student.ub.ac.id](mailto:ahmadzaki12@student.ub.ac.id)

---

> *"Technology is best when it brings people closer."* – Matt Mullenweg
