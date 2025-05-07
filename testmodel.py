from transformers import AutoTokenizer, AutoModel

# Lokasi model lokal
local_dir = "./indobert-base-p1"

# Load model dan tokenizer dari lokal
tokenizer = AutoTokenizer.from_pretrained(local_dir)
model = AutoModel.from_pretrained(local_dir)

# Cek dengan inpu
text = "Saya suka belajar NLP menggunakan IndoBERT"
inputs = tokenizer(text, return_tensors="pt")
outputs = model(**inputs)

print(outputs.last_hidden_state)
