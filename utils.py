def save_output(text: str, out_path: str = "outputs\extracted_texts.txt"): 
    with open(out_path, "w", encoding="utf-8") as f: 
        f.write(text) 
    print(f"✅ OCR output saved at: {out_path}") 
