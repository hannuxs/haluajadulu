from transformers import AutoTokenizer, AutoModel

# Nama model IndoBERT dari Hugging Face
model_name = "indobenchmark/indobert-base-p1"

# Folder lokal tempat penyimpanan
local_dir = "./indobert-base-p1"

# Unduh tokenizer dan model dari Hugging Face
print("Mengunduh tokenizer dan model...")
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# Simpan ke folder lokal
print(f"Menyimpan tokenizer dan model ke folder: {local_dir}")
tokenizer.save_pretrained(local_dir)
model.save_pretrained(local_dir)

print("✅ Model dan tokenizer berhasil disimpan secara lokal.")
