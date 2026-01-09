# 🎓 Analisis Sentimen Layanan KAI Access Menggunakan Fine-Tuned IndoBERTweet

Repositori ini berisi kode, dataset, dan dokumentasi pendukung untuk penelitian skripsi berjudul  
**“Analisis Sentimen terhadap Layanan Kereta Api Indonesia menggunakan Fine-Tuned IndoBERTweet”**.  
Penelitian ini disusun sebagai tugas akhir pada **Program Studi Teknik Informatika, Fakultas Ilmu Komputer, Universitas Brawijaya**.

---

## 📘 Deskripsi Singkat
Penelitian ini bertujuan untuk **menganalisis sentimen masyarakat terhadap layanan KAI Access** berdasarkan tweet berbahasa Indonesia.  
Pendekatan yang digunakan adalah **fine-tuning model IndoBERTweet**, yaitu model transformer yang dilatih khusus pada korpus Twitter bahasa Indonesia, untuk melakukan klasifikasi sentimen secara end-to-end ke dalam tiga kelas: **positif, netral, dan negatif**.

Penelitian ini juga mengevaluasi **pengaruh variasi preprocessing** serta **ketidakseimbangan distribusi data** terhadap kinerja model.

---

## 🧠 Metodologi
1. **Pengumpulan Data**
   - Data dikumpulkan dari platform **Twitter** menggunakan pustaka `snscrape`.
   - Kata kunci terkait layanan KAI dan KAI Access.
   - Rentang waktu data: **Desember 2022 – Desember 2024**.

2. **Preprocessing**
   - Case folding dan cleaning (URL, mention, simbol).
   - Tokenisasi menggunakan tokenizer bawaan IndoBERTweet.
   - Evaluasi beberapa skenario preprocessing:
     - Tanpa stopword removal dan stemming (baseline)
     - Dengan stopword removal
     - Dengan stemming
     - Kombinasi keduanya

3. **Fine-Tuning Model**
   - Model **IndoBERTweet** di-fine-tune secara end-to-end untuk tugas klasifikasi sentimen.
   - Optimasi hyperparameter meliputi learning rate, epoch, dan batch size.

4. **Penanganan Data Tidak Seimbang**
   - Eksplorasi beberapa teknik:
     - Random oversampling  
     - Class weighting  
     - Text augmentation (random deletion & random swap)  
     - Random undersampling  
   - Teknik diterapkan pada skenario preprocessing terbaik.

5. **Evaluasi**
   - Metrik evaluasi: **Accuracy, Precision, Recall, Macro F1-Score**, dan **Confusion Matrix**.

---

## ⚙️ Teknologi & Tools
| Kategori | Teknologi |
|--------|----------|
| Bahasa Pemrograman | Python 3.10+ |
| NLP Model | IndoBERTweet |
| Framework | PyTorch, HuggingFace Transformers |
| Data Crawling | snscrape |
| Data Processing | Pandas, NumPy |
| Evaluasi | Scikit-learn |
| Visualisasi | Matplotlib |
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

## 📊 Hasil & Temuan UTama

* Skenario tanpa stopword removal dan stemming menghasilkan performa terbaik.
* Model fine-tuned IndoBERTweet mencapai macro F1-score sebesar 0.7702 dan akurasi 0.8333.
* Kelas positif merupakan kelas minoritas dan menunjukkan performa terendah.
* Teknik penanganan data tidak seimbang belum mampu melampaui performa baseline, meskipun text augmentation menunjukkan stabilitas terbaik.
* Preprocessing yang terlalu agresif cenderung menurunkan kualitas representasi konteks pada data Twitter.
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
