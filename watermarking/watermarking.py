from PIL import Image, ImageDraw, ImageFont
import os
from pathlib import Path

class ImageWatermark:
    def __init__(self, text, position='bottom-right', opacity=0.7, font_size=40):
        self.text = text
        self.position = position
        self.opacity = opacity
        self.font_size = font_size
    
    def add_watermark(self, image_path, output_path=None):
        """Add watermark to a single image"""
        
        if not os.path.isfile(image_path):
            print(f"❌ File not found: {image_path}")
            return False
        
        try:
            # Open image
            img = Image.open(image_path).convert('RGBA')
            
            # Create watermark layer
            txt_layer = Image.new('RGBA', img.size, (255, 255, 255, 0))
            draw = ImageDraw.Draw(txt_layer)
            
            # Load font
            try:
                font = ImageFont.truetype("arial.ttf", self.font_size)
            except:
                font = ImageFont.load_default()
            
            # Get text size
            bbox = draw.textbbox((0, 0), self.text, font=font)
            txt_width = bbox[2] - bbox[0]
            txt_height = bbox[3] - bbox[1]
            
            # Calculate position
            margin = 10
            positions = {
                'top-left': (margin, margin),
                'top-right': (img.width - txt_width - margin, margin),
                'bottom-left': (margin, img.height - txt_height - margin),
                'bottom-right': (img.width - txt_width - margin, img.height - txt_height - margin),
                'center': ((img.width - txt_width) // 2, (img.height - txt_height) // 2),
            }
            
            pos = positions.get(self.position, positions['bottom-right'])
            
            # Draw text with opacity
            alpha = int(255 * self.opacity)
            draw.text(pos, self.text, font=font, fill=(255, 255, 255, alpha))
            
            # Composite images
            watermarked = Image.alpha_composite(img, txt_layer)
            watermarked = watermarked.convert('RGB')
            
            # Save
            if output_path is None:
                base = Path(image_path).stem
                ext = Path(image_path).suffix
                output_path = f"{base}_watermarked{ext}"
            
            watermarked.save(output_path)
            print(f"✅ Watermarked: {output_path}")
            return True
        
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            return False
    
    def batch_watermark(self, folder_path, output_folder='watermarked'):
        """Add watermark to all images in folder"""
        
        if not os.path.isdir(folder_path):
            print(f"❌ Folder not found: {folder_path}")
            return
        
        # Create output folder
        output_path = os.path.join(folder_path, output_folder)
        os.makedirs(output_path, exist_ok=True)
        
        # Find images
        image_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.gif'}
        images = [f for f in os.listdir(folder_path) 
                 if Path(f).suffix.lower() in image_extensions]
        
        if not images:
            print(f"❌ No images found in {folder_path}")
            return
        
        print(f"\n🎨 Watermarking {len(images)} image(s)...\n")
        
        for image in images:
            input_path = os.path.join(folder_path, image)
            output_file = os.path.join(output_path, f"watermarked_{image}")
            self.add_watermark(input_path, output_file)
        
        print(f"\n✅ Batch complete! Output: {output_path}")

def main():
    print("🎨 Image Watermarking Tool\n")
    
    # Get watermark text
    text = input("Enter watermark text: ").strip()
    
    # Get position
    print("\nPositions: top-left, top-right, bottom-left, bottom-right, center")
    position = input("Choose position (default: bottom-right): ").strip() or 'bottom-right'
    
    # Get opacity
    try:
        opacity = float(input("Enter opacity 0-1 (default: 0.7): ") or 0.7)
    except:
        opacity = 0.7
    
    watermark = ImageWatermark(text, position=position, opacity=opacity)
    
    # Choose mode
    print("\nMode:")
    print("  1. Single image")
    print("  2. Batch (all images in folder)")
    
    choice = input("\nYour choice (1-2): ").strip()
    
    if choice == "1":
        image_path = input("\nEnter image path: ").strip()
        watermark.add_watermark(image_path)
    elif choice == "2":
        folder_path = input("\nEnter folder path: ").strip()
        watermark.batch_watermark(folder_path)
    else:
        print("❌ Invalid choice")

if __name__ == "__main__":
    main()
