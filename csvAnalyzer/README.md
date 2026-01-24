# 📊 CSV Data Analyzer

## Description
Analyse et explore vos **fichiers CSV** avec statistiques, filtrage et visualisation rapide.

## Caractéristiques
- ✅ Aperçu des données
- ✅ Statistiques détaillées (moyenne, médiane, std dev)
- ✅ Détection des valeurs manquantes
- ✅ Filtrage et tri par colonne
- ✅ Résumés par colonne
- ✅ Détection des doublons
- ✅ Export de données filtrées

## Utilisation
```bash
python analyzer.py
```

## Exemple
```
📊 CSV Data Analyzer

Enter CSV file path: data.csv
✅ Loaded: data.csv
  Rows: 1000, Columns: 5

📋 Options:
  1. Show info
  2. Preview data
  3. Show statistics
  ...

Your choice: 2
```

## Opérations disponibles

### 1. Show Info
Affiche forme, colonnes et taille du fichier

### 2. Preview Data
Affiche les premières N lignes

### 3. Show Statistics
Affiche min, max, moyenne, écart-type, etc.

```
📈 Statistics:
         Age      Salary
count  1000.00   1000.00
mean     42.35   65000.00
std      12.34   25000.00
min      18.00   20000.00
max      65.00  150000.00
```

### 4. Show Missing Values
Détecte les valeurs manquantes (NULL)

```
⚠️ Missing values:
  Age: 5 (0.5%)
  Email: 12 (1.2%)
```

### 5. Filter Data
Filtre par colonne = valeur

```
Column name: Department
Value to filter: Sales
🔍 Filtered Department = Sales
  Found 156 row(s)
```

### 6. Sort Data
Trie par une colonne

```
Column to sort by: Salary
Ascending? (y/n): n
📊 Sorted by Salary (descending):
```

### 7. Column Summary
Résumé détaillé d'une colonne

```
📊 Summary for 'Age':
  Count: 1000
  Mean: 42.35
  Median: 41.50
  Std Dev: 12.34
  Min: 18.00
  Max: 65.00
```

### 8. Find Duplicates
Trouve les lignes identiques

### 9. Export Filtered Data
Sauvegarde les données filtrées

## Format CSV
Structure attendue:
```
Name,Age,Email,Salary,Department
John,28,john@example.com,50000,IT
Jane,35,jane@example.com,65000,Sales
```

## Notes
- Supporte CSV standard (delimiter: virgule)
- Détecte automatiquement les types de données
- Idéal pour explorer rapidement de gros fichiers
- Pas besoin de connaître pandas pour l'utiliser
