import argparse 
from utils import save_output 
 
def main(): 
    parser = argparse.ArgumentParser(description="Bangla OCR Starter") 
    parser.add_argument("input_path", help="Path to image file") 
    args = parser.parse_args() 
 
    # Placeholder OCR action 
    text = f"OCR would run on: {args.input_path}" 
    print(text) 
    save_output(text) 
 
if __name__ == "__main__": 
    main() 
