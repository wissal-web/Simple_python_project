import os
import shutil
from pathlib import Path
from collections import defaultdict

class FileOrganizer:
    # Define file categories by extension
    CATEGORIES = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.ico'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.xls', '.ppt', '.pptx'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv'],
        'Audio': ['.mp3', '.wav', '.flac', '.aac', '.m4a', '.wma'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
        'Code': ['.py', '.js', '.java', '.cpp', '.c', '.html', '.css', '.php'],
        'Executables': ['.exe', '.msi', '.apk', '.app'],
    }
    
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.stats = defaultdict(int)
    
    def organize(self, simulate=True):
        """Organize files in folder by category"""
        
        if not os.path.isdir(self.folder_path):
            print(f"❌ Folder not found: {self.folder_path}")
            return
        
        print(f"📁 Organizing: {self.folder_path}")
        print(f"🔍 Scanning files..." + (" (SIMULATION MODE)" if simulate else ""))
        
        files = [f for f in os.listdir(self.folder_path) 
                if os.path.isfile(os.path.join(self.folder_path, f))]
        
        if not files:
            print("✓ Folder is empty")
            return
        
        # Get file category
        for file in files:
            ext = Path(file).suffix.lower()
            category = self._get_category(ext)
            self.stats[category] += 1
            
            src = os.path.join(self.folder_path, file)
            dest_folder = os.path.join(self.folder_path, category)
            
            if not simulate:
                # Create category folder
                if not os.path.exists(dest_folder):
                    os.makedirs(dest_folder)
                
                # Move file
                dest = os.path.join(dest_folder, file)
                shutil.move(src, dest)
                print(f"  ✓ {file} → {category}/")
            else:
                print(f"  → {file} → {category}/")
        
        # Print summary
        print(f"\n📊 Summary:")
        for category, count in sorted(self.stats.items()):
            print(f"  {category}: {count} file(s)")
        
        if simulate:
            print("\n✓ Simulation complete. Run with confirm to apply changes.")
    
    def _get_category(self, extension):
        """Find category for file extension"""
        for category, extensions in self.CATEGORIES.items():
            if extension in extensions:
                return category
        return 'Other'

def main():
    print("📁 File Organizer\n")
    
    folder_path = input("Enter folder path to organize: ").strip()
    
    organizer = FileOrganizer(folder_path)
    
    # First simulate
    print("\n🔍 Running simulation...\n")
    organizer.organize(simulate=True)
    
    # Ask for confirmation
    confirm = input("\n✓ Apply changes? (y/n): ").strip().lower()
    if confirm == 'y':
        print("\n⚙️ Applying changes...\n")
        organizer2 = FileOrganizer(folder_path)
        organizer2.organize(simulate=False)
        print("\n✅ Files organized successfully!")
    else:
        print("❌ Cancelled")

if __name__ == "__main__":
    main()
