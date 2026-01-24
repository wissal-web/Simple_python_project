import os
import csv
import secrets
import string
import json
from pathlib import Path

class PasswordManager:
    def __init__(self, storage_file='passwords.json'):
        self.storage_file = storage_file
        self.passwords = self._load_passwords()
    
    def _load_passwords(self):
        """Load passwords from file"""
        if os.path.isfile(self.storage_file):
            try:
                with open(self.storage_file, 'r') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def _save_passwords(self):
        """Save passwords to file"""
        with open(self.storage_file, 'w') as f:
            json.dump(self.passwords, f, indent=2)
        print(f"💾 Saved to {self.storage_file}")
    
    def generate_password(self, length=16, use_special=True):
        """Generate a strong random password"""
        
        chars = string.ascii_letters + string.digits
        if use_special:
            chars += string.punctuation
        
        password = ''.join(secrets.choice(chars) for _ in range(length))
        return password
    
    def add_password(self, service, username, password=None):
        """Add a new password entry"""
        
        if service in self.passwords:
            overwrite = input(f"⚠️ {service} exists. Overwrite? (y/n): ").strip().lower()
            if overwrite != 'y':
                return
        
        if password is None:
            # Generate password
            print("\n🔐 Generate password?")
            print("  1. Generate random")
            print("  2. Enter manually")
            choice = input("Your choice (1-2): ").strip()
            
            if choice == "1":
                length = int(input("Password length (default: 16): ") or 16)
                password = self.generate_password(length)
                print(f"✅ Generated: {password}")
            else:
                password = input("Enter password: ").strip()
        
        self.passwords[service] = {
            'username': username,
            'password': password
        }
        
        self._save_passwords()
        print(f"✅ Added: {service}")
    
    def get_password(self, service):
        """Get password for a service"""
        
        if service not in self.passwords:
            print(f"❌ Not found: {service}")
            return None
        
        entry = self.passwords[service]
        print(f"\n🔐 {service}")
        print(f"  Username: {entry['username']}")
        print(f"  Password: {entry['password']}")
        
        # Copy to clipboard option
        copy = input("\nCopy password to clipboard? (y/n): ").strip().lower()
        if copy == 'y':
            try:
                import pyperclip
                pyperclip.copy(entry['password'])
                print("✅ Copied!")
            except:
                print("⚠️ pyperclip not installed. Use: pip install pyperclip")
    
    def list_services(self):
        """List all stored services"""
        
        if not self.passwords:
            print("ℹ️ No passwords stored")
            return
        
        print("\n🔐 Stored Services:\n")
        for i, service in enumerate(self.passwords.keys(), 1):
            print(f"  {i}. {service}")
    
    def delete_password(self, service):
        """Delete a password entry"""
        
        if service not in self.passwords:
            print(f"❌ Not found: {service}")
            return
        
        confirm = input(f"⚠️ Delete {service}? (y/n): ").strip().lower()
        if confirm == 'y':
            del self.passwords[service]
            self._save_passwords()
            print(f"✅ Deleted: {service}")
        else:
            print("❌ Cancelled")
    
    def export_csv(self, filename='passwords.csv'):
        """Export passwords to CSV (warning: not encrypted!)"""
        
        warn = input("⚠️ CSV is NOT encrypted! Continue? (y/n): ").strip().lower()
        if warn != 'y':
            return
        
        try:
            with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Service', 'Username', 'Password'])
                for service, entry in self.passwords.items():
                    writer.writerow([service, entry['username'], entry['password']])
            print(f"✅ Exported to {filename}")
        except Exception as e:
            print(f"❌ Error: {str(e)}")

def main():
    print("🔐 Password Manager\n")
    
    manager = PasswordManager()
    
    while True:
        print("\n📋 Options:")
        print("  1. Generate new password")
        print("  2. Add password")
        print("  3. Get password")
        print("  4. List all services")
        print("  5. Delete password")
        print("  6. Export to CSV")
        print("  7. Exit")
        
        choice = input("\nYour choice (1-7): ").strip()
        
        if choice == "1":
            length = int(input("Length (default: 16): ") or 16)
            pwd = manager.generate_password(length)
            print(f"\n✅ {pwd}")
        
        elif choice == "2":
            service = input("Service name: ").strip()
            username = input("Username: ").strip()
            manager.add_password(service, username)
        
        elif choice == "3":
            manager.list_services()
            service = input("\nEnter service name: ").strip()
            manager.get_password(service)
        
        elif choice == "4":
            manager.list_services()
        
        elif choice == "5":
            manager.list_services()
            service = input("\nEnter service to delete: ").strip()
            manager.delete_password(service)
        
        elif choice == "6":
            manager.export_csv()
        
        elif choice == "7":
            print("👋 Goodbye!")
            break
        
        else:
            print("❌ Invalid choice")

if __name__ == "__main__":
    main()
