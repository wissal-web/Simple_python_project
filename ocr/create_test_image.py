from PIL import Image, ImageDraw, ImageFont
import os

def create_handwritten_test_image():
    """Create a test image with handwritten-style text"""
    
    # Create image
    width, height = 800, 600
    image = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(image)
    
    # Try to use a font that looks handwritten
    try:
        # Try to find a nice font
        font_size = 40
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        # Fallback to default font
        font = ImageFont.load_default()
    
    # Add some text
    text_lines = [
        "Bonjour et bienvenue!",
        "",
        "Ceci est un texte de test",
        "pour vérifier l'OCR.",
        "",
        "123 ABC XYZ",
        "Texte avec chiffres: 2025"
    ]
    
    y_position = 50
    for line in text_lines:
        draw.text((50, y_position), line, fill='black', font=font)
        y_position += 60
    
    # Save image
    output_path = "test_image.png"
    image.save(output_path)
    print(f"✅ Test image created: {output_path}")
    return output_path

if __name__ == "__main__":
    create_handwritten_test_image()
