# 🔤 OCR Text Extractor

## Description
Extrait du **texte à partir d'images** (reconnaissance optique de caractères / OCR).

## Caractéristiques
- ✅ Support de 50+ langues
- ✅ Extraction de texte automatique
- ✅ 3 moteurs OCR (EasyOCR, Tesseract, Hybrid)
- ✅ Traitement batch (dossier entier)
- ✅ Affichage des scores de confiance
- ✅ Prétraitement d'images pour meilleurs résultats

## Fichiers disponibles

### 1. **textExtractor.py** (Basique)
OCR simple avec EasyOCR uniquement

```bash
python textExtractor.py
```

### 2. **advancedTextExtractor.py** (Recommandé)
Version améliorée avec prétraitement d'images
- Meilleur pour le texte manuscrit
- Détection de valeurs manquantes
- Sauvegarde des images prétraitées

```bash
python advancedTextExtractor.py
```

### 3. **hybridOCR.py** (Professionnel)
Combine EasyOCR + Tesseract pour résultats optimaux
- Nécessite Tesseract installé
- Meilleur pour manuscrit

```bash
python hybridOCR.py
```

### 4. **create_test_image.py**
Crée une image de test pour vérifier l'OCR

```bash
python create_test_image.py
```

## Exemple d'utilisation

```
🔤 OCR Text Extractor

Enter language codes: en,fr
Choose an option:
  1. Extract text from a single image
  2. Extract text from all images in a folder

Your choice: 1
Enter image file path: photo.jpg

📸 Processing: photo.jpg
📊 Text with confidence scores:
  Hello (95.23%)
  World (94.87%)

📝 Extracted Text:
Hello
World
```

## Langues supportées
- **Européennes**: en, fr, de, es, it, pt, nl
- **Asiatiques**: zh, ja, ko, ar, hi
- **Et 40+ autres langues**

## Notes
- **EasyOCR**: Fonctionne bien avec texte imprimé
- **Tesseract**: Meilleur pour manuscrit (doit être installé)
- **Hybrid**: Combine les deux pour meilleurs résultats
- Les images prétraitées sont sauvegardées avec suffixe `_processed` et `_enhanced`
