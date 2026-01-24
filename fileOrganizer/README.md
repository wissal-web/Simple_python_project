# 📁 File Organizer

## Description
Organise automatiquement les fichiers d'un dossier par **catégorie** (Images, Documents, Vidéos, Audio, etc.).

## Caractéristiques
- ✅ Crée automatiquement des dossiers par type de fichier
- ✅ Mode simulation avant d'appliquer les changements
- ✅ Récursif (traite aussi les sous-dossiers)
- ✅ Support de 7 catégories principales

## Catégories supportées
- **Images**: jpg, jpeg, png, gif, bmp, svg, ico
- **Documents**: pdf, doc, docx, txt, xlsx, xls, ppt, pptx
- **Vidéos**: mp4, avi, mkv, mov, wmv, flv
- **Audio**: mp3, wav, flac, aac, m4a, wma
- **Archives**: zip, rar, 7z, tar, gz
- **Code**: py, js, java, cpp, c, html, css, php
- **Executables**: exe, msi, apk, app
- **Other**: tous les autres types

## Utilisation
```bash
python organizer.py
```

## Exemple
```
📁 Organizing: C:\Users\Downloads
🔍 Scanning files... (SIMULATION MODE)

  → photo1.jpg → Images/
  → document.pdf → Documents/
  → video.mp4 → Videos/

📊 Summary:
  Images: 5 file(s)
  Documents: 3 file(s)
  Videos: 2 file(s)

✓ Simulation complete. Run with confirm to apply changes.
✓ Apply changes? (y/n): y
```

## Notes
- Les fichiers sans extension vont dans "Other"
- Le script crée un dossier pour chaque catégorie trouvée
- Préférez toujours tester en simulation d'abord
