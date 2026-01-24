import PyPDF2
import os
from pathlib import Path

def get_pdf_files_from_path(directory):
    """Get list of PDF files from a specific directory"""
    if not os.path.isdir(directory):
        print(f"❌ Directory not found: {directory}")
        return []
    
    pdf_files = [f for f in os.listdir(directory) if f.endswith(".pdf")]
    return sorted(pdf_files), directory

def main():
    print("📁 PDF Merger Tool\n")
    
    # Ask user where to find PDFs
    print("Choose an option:")
    print("  1. Search for PDFs in current directory")
    print("  2. Search for PDFs in a specific folder")
    print("  3. Enter PDF files manually (full path)")
    
    choice = input("\nYour choice (1-3): ").strip()
    
    selected_files = []
    
    if choice == "1":
        # Current directory
        pdf_files, directory = get_pdf_files_from_path(os.curdir)
        if not pdf_files:
            print("❌ No PDF files found in current directory.")
            return
        
        print(f"\n📄 PDF files in current directory:")
        for i, file in enumerate(pdf_files, 1):
            print(f"  {i}. {file}")
        
        # Ask user which PDFs to merge
        print("\n📝 Enter the numbers of PDFs you want to merge (e.g., 1,2,3 or 1-3):")
        user_input = input("Your choice: ").strip()
        
        try:
            selected_indices = parse_user_input(user_input, len(pdf_files))
            selected_files = [os.path.join(directory, pdf_files[i]) for i in selected_indices]
        except ValueError as e:
            print(f"❌ {str(e)}")
            return
    
    elif choice == "2":
        # Specific directory
        folder_path = input("\nEnter the folder path: ").strip()
        pdf_files, directory = get_pdf_files_from_path(folder_path)
        
        if not pdf_files:
            print(f"❌ No PDF files found in: {folder_path}")
            return
        
        print(f"\n📄 PDF files in {folder_path}:")
        for i, file in enumerate(pdf_files, 1):
            print(f"  {i}. {file}")
        
        # Ask user which PDFs to merge
        print("\n📝 Enter the numbers of PDFs you want to merge (e.g., 1,2,3 or 1-3):")
        user_input = input("Your choice: ").strip()
        
        try:
            selected_indices = parse_user_input(user_input, len(pdf_files))
            selected_files = [os.path.join(directory, pdf_files[i]) for i in selected_indices]
        except ValueError as e:
            print(f"❌ {str(e)}")
            return
    
    elif choice == "3":
        # Manual entry
        print("\n📝 Enter PDF file paths (one per line, empty line to finish):")
        while True:
            file_path = input("PDF path: ").strip()
            if not file_path:
                break
            if os.path.isfile(file_path) and file_path.endswith(".pdf"):
                selected_files.append(file_path)
                print(f"  ✓ Added: {file_path}")
            else:
                print(f"  ❌ File not found or not a PDF: {file_path}")
    
    else:
        print("❌ Invalid choice.")
        return
    
    # Merge PDFs
    if selected_files:
        try:
            print(f"\n🔄 Merging {len(selected_files)} PDF(s)...")
            print("Files to merge:")
            for file in selected_files:
                print(f"  ✓ {file}")
            
            output_name = input("\n💾 Enter output filename (default: combined.pdf): ").strip()
            if not output_name:
                output_name = "combined.pdf"
            
            if not output_name.endswith(".pdf"):
                output_name += ".pdf"
            
            merger = PyPDF2.PdfMerger()
            for file in selected_files:
                merger.append(file)
            
            merger.write(output_name)
            merger.close()
            
            print(f"✅ Successfully merged into: {output_name}")
        
        except Exception as e:
            print(f"❌ Error during merge: {str(e)}")
    else:
        print("❌ No PDF files selected.")

def parse_user_input(user_input, total_files):
    """Parse user input for file selection"""
    selected_indices = []
    
    # Handle range input (e.g., "1-3")
    if '-' in user_input:
        parts = user_input.split('-')
        start = int(parts[0].strip()) - 1
        end = int(parts[1].strip())
        selected_indices = list(range(start, end))
    else:
        # Handle comma-separated input (e.g., "1,2,3")
        selected_indices = [int(x.strip()) - 1 for x in user_input.split(',')]
    
    # Validate indices
    if not selected_indices or any(i < 0 or i >= total_files for i in selected_indices):
        raise ValueError("Invalid selection. Please enter valid numbers.")
    
    return selected_indices

if __name__ == "__main__":
    main()