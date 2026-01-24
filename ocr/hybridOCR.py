import easyocr
import cv2
import numpy as np
import os
from pathlib import Path
import pytesseract

# Configure Tesseract path (adjust if needed based on your installation)
try:
    pytesseract.pytesseract.pytesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
except:
    pass

class HybridOCRExtractor:
    def __init__(self, languages=['en'], use_tesseract=False):
        """Initialize OCR readers"""
        print("🔄 Loading OCR models...")
        self.reader_easy = easyocr.Reader(languages)
        self.use_tesseract = use_tesseract
        
        if use_tesseract:
            try:
                # Test if Tesseract is available
                pytesseract.pytesseract.get_tesseract_version()
                self.has_tesseract = True
                print("✅ Tesseract OCR available")
            except:
                self.has_tesseract = False
                print("⚠️ Tesseract not found - using EasyOCR only")
        
        print("✅ OCR models loaded successfully")
    
    def preprocess_image(self, image, enhance_type='handwriting'):
        """Enhance image specifically for handwritten text"""
        
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Denoise
        denoised = cv2.fastNlMeansDenoising(gray, h=15)
        
        # Increase contrast with CLAHE
        clahe = cv2.createCLAHE(clipLimit=4.0, tileGridSize=(8, 8))
        enhanced = clahe.apply(denoised)
        
        # Bilateral filter for edge preservation
        bilateral = cv2.bilateralFilter(enhanced, 9, 75, 75)
        
        # Dilation to connect broken characters
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
        dilated = cv2.dilate(bilateral, kernel, iterations=1)
        
        # Adaptive threshold for better binary image
        thresh = cv2.adaptiveThreshold(dilated, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                      cv2.THRESH_BINARY, 15, 2)
        
        return thresh, enhanced
    
    def extract_with_easyocr(self, processed_image, display_confidence=False):
        """Extract text using EasyOCR"""
        results = self.reader_easy.readtext(processed_image)
        
        if not results:
            return ""
        
        text = "\n".join([text[1] for text in results])
        
        if display_confidence:
            print("\n📊 EasyOCR Confidence Scores:")
            for (bbox, txt, confidence) in results:
                print(f"  {txt} ({confidence:.2%})")
        
        return text
    
    def extract_with_tesseract(self, processed_image, display_confidence=False):
        """Extract text using Tesseract"""
        if not self.has_tesseract:
            return ""
        
        text = pytesseract.image_to_string(processed_image, lang='fra+eng')
        
        return text
    
    def extract_from_image(self, image_path, display_confidence=False):
        """Extract text using both OCR engines and combine results"""
        
        if not os.path.isfile(image_path):
            print(f"❌ File not found: {image_path}")
            return None
        
        print(f"\n📸 Processing: {image_path}")
        
        # Read image
        image = cv2.imread(image_path)
        if image is None:
            print(f"❌ Could not read image: {image_path}")
            return None
        
        # Preprocess
        print("🔄 Preprocessing image for handwriting...")
        processed, enhanced = self.preprocess_image(image)
        
        # Save preprocessed images
        base_name = image_path.rsplit('.', 1)[0]
        cv2.imwrite(f"{base_name}_processed.png", processed)
        cv2.imwrite(f"{base_name}_enhanced.png", enhanced)
        print(f"💾 Saved: {base_name}_processed.png")
        
        # Extract with EasyOCR
        print("\n🔤 Extracting with EasyOCR...")
        text_easy = self.extract_with_easyocr(processed, display_confidence=True)
        
        # Extract with Tesseract if available
        text_tesseract = ""
        if self.has_tesseract:
            print("\n🔤 Extracting with Tesseract...")
            text_tesseract = self.extract_with_tesseract(processed)
        
        # Combine or show both
        print("\n" + "="*60)
        print("📝 EASYOCR RESULT:")
        print("="*60)
        print(text_easy if text_easy else "[No text detected]")
        
        if text_tesseract:
            print("\n" + "="*60)
            print("📝 TESSERACT RESULT:")
            print("="*60)
            print(text_tesseract)
            
            # For now, return EasyOCR result
            return text_easy if text_easy else text_tesseract
        
        return text_easy

def main():
    print("🔤 Hybrid OCR for Handwritten Text\n")
    
    # Initialize OCR with Tesseract option
    ocr = HybridOCRExtractor(languages=['en', 'fr'], use_tesseract=True)
    
    # Single image processing
    image_path = input("\nEnter image file path: ").strip()
    text = ocr.extract_from_image(image_path, display_confidence=True)
    
    if text:
        # Save option
        save = input("\nSave text to file? (y/n): ").strip().lower()
        if save == 'y':
            output_file = input("Enter output filename (default: extracted_text.txt): ").strip()
            if not output_file:
                output_file = "extracted_text.txt"
            
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f"✅ Text saved to: {output_file}")

if __name__ == "__main__":
    main()
