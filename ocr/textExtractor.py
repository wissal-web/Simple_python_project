import easyocr
import cv2
import os
from pathlib import Path

class OCRExtractor:
    def __init__(self, languages=['en']):
        """Initialize OCR reader"""
        print("🔄 Loading OCR model (first time may take a moment)...")
        self.reader = easyocr.Reader(languages)
        print("✅ OCR model loaded successfully")
    
    def extract_from_image(self, image_path, display_confidence=False):
        """Extract text from an image file"""
        if not os.path.isfile(image_path):
            print(f"❌ File not found: {image_path}")
            return None
        
        print(f"\n📸 Processing: {image_path}")
        
        # Read image
        image = cv2.imread(image_path)
        if image is None:
            print(f"❌ Could not read image: {image_path}")
            return None
        
        # Extract text
        results = self.reader.readtext(image)
        
        if not results:
            print("⚠️ No text found in the image")
            return ""
        
        # Combine text
        extracted_text = "\n".join([text[1] for text in results])
        
        # Show confidence if requested
        if display_confidence:
            print("\n📊 Text with confidence scores:")
            for (bbox, text, confidence) in results:
                print(f"  {text} ({confidence:.2%})")
        
        return extracted_text
    
    def extract_from_folder(self, folder_path, output_file=None, display_confidence=False):
        """Extract text from all images in a folder"""
        if not os.path.isdir(folder_path):
            print(f"❌ Folder not found: {folder_path}")
            return {}
        
        # Find image files
        image_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.gif'}
        image_files = [f for f in os.listdir(folder_path) 
                      if Path(f).suffix.lower() in image_extensions]
        
        if not image_files:
            print(f"❌ No image files found in: {folder_path}")
            return {}
        
        results = {}
        print(f"\n📁 Found {len(image_files)} image(s)")
        
        for image_file in sorted(image_files):
            image_path = os.path.join(folder_path, image_file)
            text = self.extract_from_image(image_path, display_confidence)
            results[image_file] = text
        
        # Save results if output file specified
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                for filename, text in results.items():
                    f.write(f"{'='*50}\n")
                    f.write(f"File: {filename}\n")
                    f.write(f"{'='*50}\n")
                    f.write(text)
                    f.write("\n\n")
            print(f"\n💾 Results saved to: {output_file}")
        
        return results

def main():
    print("🔤 OCR Text Extractor\n")
    
    # Ask for language
    print("Supported languages: en, fr, es, de, it, ar, zh, ja, ko, etc.")
    languages_input = input("Enter language codes (comma-separated, default: en): ").strip()
    languages = [lang.strip() for lang in languages_input.split(',')] if languages_input else ['en']
    
    # Initialize OCR
    ocr = OCRExtractor(languages=languages)
    
    # Ask for operation
    print("\n📋 Choose an option:")
    print("  1. Extract text from a single image")
    print("  2. Extract text from all images in a folder")
    
    choice = input("\nYour choice (1-2): ").strip()
    
    try:
        if choice == "1":
            # Single image
            image_path = input("\nEnter image file path: ").strip()
            text = ocr.extract_from_image(image_path, display_confidence=True)
            
            if text:
                print("\n📝 Extracted Text:")
                print("-" * 50)
                print(text)
                print("-" * 50)
                
                # Save option
                save = input("\nSave text to file? (y/n): ").strip().lower()
                if save == 'y':
                    output_file = input("Enter output filename (default: extracted_text.txt): ").strip()
                    if not output_file:
                        output_file = "extracted_text.txt"
                    
                    with open(output_file, 'w', encoding='utf-8') as f:
                        f.write(text)
                    print(f"✅ Text saved to: {output_file}")
        
        elif choice == "2":
            # Folder processing
            folder_path = input("\nEnter folder path: ").strip()
            
            save = input("Save results to file? (y/n): ").strip().lower()
            output_file = None
            if save == 'y':
                output_file = input("Enter output filename (default: ocr_results.txt): ").strip()
                if not output_file:
                    output_file = "ocr_results.txt"
            
            results = ocr.extract_from_folder(folder_path, output_file)
            
            if results:
                print(f"\n✅ Processed {len(results)} image(s)")
        
        else:
            print("❌ Invalid choice")
    
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    main()
