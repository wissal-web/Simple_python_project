import os
import hashlib
from collections import defaultdict
from pathlib import Path

class DuplicateFinder:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.file_hashes = defaultdict(list)
        self.duplicates = {}
    
    def calculate_hash(self, file_path, chunk_size=8192):
        """Calculate SHA256 hash of file"""
        sha256_hash = hashlib.sha256()
        try:
            with open(file_path, "rb") as f:
                for byte_block in iter(lambda: f.read(chunk_size), b""):
                    sha256_hash.update(byte_block)
            return sha256_hash.hexdigest()
        except Exception as e:
            print(f"⚠️ Could not hash {file_path}: {str(e)}")
            return None
    
    def find_duplicates(self, recursive=True):
        """Find all duplicate files"""
        
        if not os.path.isdir(self.folder_path):
            print(f"❌ Folder not found: {self.folder_path}")
            return
        
        print(f"🔍 Scanning {self.folder_path}...")
        file_count = 0
        
        # Walk through files
        if recursive:
            for root, dirs, files in os.walk(self.folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    file_hash = self.calculate_hash(file_path)
                    if file_hash:
                        self.file_hashes[file_hash].append(file_path)
                        file_count += 1
        else:
            for file in os.listdir(self.folder_path):
                file_path = os.path.join(self.folder_path, file)
                if os.path.isfile(file_path):
                    file_hash = self.calculate_hash(file_path)
                    if file_hash:
                        self.file_hashes[file_hash].append(file_path)
                        file_count += 1
        
        # Find duplicates
        self.duplicates = {k: v for k, v in self.file_hashes.items() if len(v) > 1}
        
        print(f"\n📊 Results:")
        print(f"  Total files scanned: {file_count}")
        print(f"  Duplicate sets found: {len(self.duplicates)}")
        
        total_duplicates = sum(len(files) - 1 for files in self.duplicates.values())
        print(f"  Total duplicate files: {total_duplicates}")
        
        if self.duplicates:
            self._show_duplicates()
    
    def _show_duplicates(self):
        """Display duplicate files"""
        print(f"\n📁 Duplicates:\n")
        
        total_wasted = 0
        
        for i, (file_hash, files) in enumerate(self.duplicates.items(), 1):
            print(f"{i}. Group with {len(files)} copies:")
            
            for j, file_path in enumerate(files):
                size = os.path.getsize(file_path)
                size_mb = size / (1024 * 1024)
                print(f"   [{j+1}] {file_path} ({size_mb:.2f} MB)")
                if j > 0:  # Count duplicates (not the original)
                    total_wasted += size
            
            print()
        
        wasted_mb = total_wasted / (1024 * 1024)
        print(f"💾 Space wasted by duplicates: {wasted_mb:.2f} MB")
    
    def delete_duplicates(self, keep_first=True):
        """Delete duplicate files"""
        
        if not self.duplicates:
            print("✓ No duplicates found")
            return
        
        deleted_count = 0
        freed_space = 0
        
        for file_hash, files in self.duplicates.items():
            # Keep first file, delete others
            if keep_first:
                for file_path in files[1:]:
                    try:
                        size = os.path.getsize(file_path)
                        os.remove(file_path)
                        print(f"🗑️ Deleted: {file_path}")
                        deleted_count += 1
                        freed_space += size
                    except Exception as e:
                        print(f"❌ Could not delete {file_path}: {str(e)}")
        
        freed_mb = freed_space / (1024 * 1024)
        print(f"\n✅ Deleted {deleted_count} files, freed {freed_mb:.2f} MB")

def main():
    print("🔍 Duplicate File Finder\n")
    
    folder_path = input("Enter folder path: ").strip()
    
    recursive = input("Search recursively (all subfolders)? (y/n, default: y): ").strip().lower() != 'n'
    
    finder = DuplicateFinder(folder_path)
    finder.find_duplicates(recursive=recursive)
    
    if finder.duplicates:
        delete = input("\n🗑️ Delete duplicates? (y/n): ").strip().lower()
        if delete == 'y':
            confirm = input("⚠️ This cannot be undone. Confirm? (y/n): ").strip().lower()
            if confirm == 'y':
                finder.delete_duplicates()
            else:
                print("❌ Cancelled")
        else:
            print("✓ Duplicates preserved")

if __name__ == "__main__":
    main()
