# 🔍 Duplicate File Finder

## Description
Trouve et supprime les **fichiers en doublon** dans vos dossiers en comparant leur contenu (hash SHA256).

## Caractéristiques
- ✅ Détection par hash (fichiers identiques)
- ✅ Recherche récursive (sous-dossiers)
- ✅ Affiche l'espace disque gaspillé
- ✅ Suppression sécurisée avec confirmation
- ✅ Support de tous les types de fichiers

## Utilisation
```bash
python finder.py
```

## Exemple
```
🔍 Duplicate File Finder

Enter folder path: C:\Documents
Search recursively? (y/n, default: y): y

🔍 Scanning C:\Documents...

📊 Results:
  Total files scanned: 256
  Duplicate sets found: 8
  Total duplicate files: 15

📁 Duplicates:

1. Group with 3 copies:
   [1] C:\Documents\photo.jpg (2.50 MB)
   [2] C:\Documents\Backup\photo.jpg (2.50 MB)
   [3] C:\Documents\Archive\photo.jpg (2.50 MB)

💾 Space wasted by duplicates: 125.50 MB

🗑️ Delete duplicates? (y/n): y
⚠️ This cannot be undone. Confirm? (y/n): y

🗑️ Deleted: C:\Documents\Backup\photo.jpg
🗑️ Deleted: C:\Documents\Archive\photo.jpg
✅ Deleted 15 files, freed 125.50 MB
```

## Notes
- Utilise SHA256 pour comparer le contenu exact
- Le premier fichier de chaque groupe est conservé
- Les autres copies sont supprimées
- ⚠️ La suppression ne peut pas être annulée - soyez prudent !
- Idéal pour libérer de l'espace disque
