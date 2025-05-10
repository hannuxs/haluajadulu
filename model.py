from transformers import AutoTokenizer, AutoModel

model_name = "indobenchmark/indobert-base-p1"

local_dir = "./indobert-base-p1"

print("Mengunduh tokenizer dan model...")
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

print(f"Menyimpan tokenizer dan model ke folder: {local_dir}")
tokenizer.save_pretrained(local_dir)
model.save_pretrained(local_dir)

print("✅ Model dan tokenizer berhasil disimpan secara lokal.")
