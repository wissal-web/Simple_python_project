import pandas as pd
import numpy as np
from pathlib import Path

class CSVAnalyzer:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.df = None
        self._load_csv()
    
    def _load_csv(self):
        """Load CSV file"""
        try:
            self.df = pd.read_csv(self.csv_path)
            print(f"✅ Loaded: {self.csv_path}")
            print(f"  Rows: {len(self.df)}, Columns: {len(self.df.columns)}\n")
        except Exception as e:
            print(f"❌ Error loading CSV: {str(e)}")
            return False
        return True
    
    def show_info(self):
        """Show basic info"""
        print("\n📊 CSV Information:")
        print(f"  Shape: {self.df.shape[0]} rows × {self.df.shape[1]} columns")
        print(f"  Columns: {list(self.df.columns)}")
        print(f"  Memory usage: {self.df.memory_usage(deep=True).sum() / 1024:.2f} KB")
    
    def show_preview(self, rows=5):
        """Show preview"""
        print(f"\n📋 First {rows} rows:")
        print(self.df.head(rows).to_string())
    
    def show_statistics(self):
        """Show numerical statistics"""
        print("\n📈 Statistics:")
        print(self.df.describe().to_string())
    
    def show_missing(self):
        """Show missing values"""
        missing = self.df.isnull().sum()
        if missing.sum() == 0:
            print("\n✅ No missing values")
        else:
            print("\n⚠️ Missing values:")
            for col, count in missing[missing > 0].items():
                pct = (count / len(self.df)) * 100
                print(f"  {col}: {count} ({pct:.1f}%)")
    
    def filter_data(self, column, value):
        """Filter by column value"""
        try:
            filtered = self.df[self.df[column] == value]
            print(f"\n🔍 Filtered {column} = {value}")
            print(f"  Found {len(filtered)} row(s)")
            print(filtered.to_string())
        except Exception as e:
            print(f"❌ Error: {str(e)}")
    
    def sort_data(self, column, ascending=True):
        """Sort by column"""
        try:
            sorted_df = self.df.sort_values(by=column, ascending=ascending)
            order = "ascending" if ascending else "descending"
            print(f"\n📊 Sorted by {column} ({order}):")
            print(sorted_df.head(10).to_string())
        except Exception as e:
            print(f"❌ Error: {str(e)}")
    
    def get_summary(self, column):
        """Get column summary"""
        try:
            print(f"\n📊 Summary for '{column}':")
            if self.df[column].dtype in ['int64', 'float64']:
                print(f"  Count: {self.df[column].count()}")
                print(f"  Mean: {self.df[column].mean():.2f}")
                print(f"  Median: {self.df[column].median():.2f}")
                print(f"  Std Dev: {self.df[column].std():.2f}")
                print(f"  Min: {self.df[column].min():.2f}")
                print(f"  Max: {self.df[column].max():.2f}")
            else:
                print(f"  Unique values: {self.df[column].nunique()}")
                print(f"  Top values:")
                for val, count in self.df[column].value_counts().head(5).items():
                    pct = (count / len(self.df)) * 100
                    print(f"    {val}: {count} ({pct:.1f}%)")
        except Exception as e:
            print(f"❌ Error: {str(e)}")
    
    def export_filtered(self, column, value, output_file):
        """Export filtered data"""
        try:
            filtered = self.df[self.df[column] == value]
            filtered.to_csv(output_file, index=False)
            print(f"✅ Exported {len(filtered)} rows to {output_file}")
        except Exception as e:
            print(f"❌ Error: {str(e)}")
    
    def get_duplicates(self):
        """Show duplicate rows"""
        duplicates = self.df[self.df.duplicated(keep=False)]
        if len(duplicates) == 0:
            print("\n✅ No duplicate rows")
        else:
            print(f"\n⚠️ Found {len(duplicates)} duplicate rows:")
            print(duplicates.to_string())

def main():
    print("📊 CSV Data Analyzer\n")
    
    csv_path = input("Enter CSV file path: ").strip()
    
    analyzer = CSVAnalyzer(csv_path)
    if analyzer.df is None:
        return
    
    while True:
        print("\n📋 Options:")
        print("  1. Show info")
        print("  2. Preview data")
        print("  3. Show statistics")
        print("  4. Show missing values")
        print("  5. Filter data")
        print("  6. Sort data")
        print("  7. Column summary")
        print("  8. Find duplicates")
        print("  9. Export filtered data")
        print("  10. Exit")
        
        choice = input("\nYour choice (1-10): ").strip()
        
        if choice == "1":
            analyzer.show_info()
        
        elif choice == "2":
            rows = int(input("Number of rows to show (default: 5): ") or 5)
            analyzer.show_preview(rows)
        
        elif choice == "3":
            analyzer.show_statistics()
        
        elif choice == "4":
            analyzer.show_missing()
        
        elif choice == "5":
            column = input("Column name: ").strip()
            value = input("Value to filter: ").strip()
            analyzer.filter_data(column, value)
        
        elif choice == "6":
            column = input("Column to sort by: ").strip()
            order = input("Ascending? (y/n, default: y): ").strip().lower() != 'n'
            analyzer.sort_data(column, order)
        
        elif choice == "7":
            column = input("Column name: ").strip()
            analyzer.get_summary(column)
        
        elif choice == "8":
            analyzer.get_duplicates()
        
        elif choice == "9":
            column = input("Column name: ").strip()
            value = input("Value to filter: ").strip()
            output = input("Output filename: ").strip()
            analyzer.export_filtered(column, value, output)
        
        elif choice == "10":
            print("👋 Goodbye!")
            break
        
        else:
            print("❌ Invalid choice")

if __name__ == "__main__":
    main()
