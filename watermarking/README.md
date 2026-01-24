# 🎨 Image Watermarking Tool

## Description
Ajoute un **filigrane** (texte) sur vos images pour les protéger ou les marquer.

## Caractéristiques
- ✅ Filigrane texte personnalisé
- ✅ 5 positions possibles (coins + centre)
- ✅ Contrôle d'opacité (0-1)
- ✅ Traitement individuel ou batch
- ✅ Supporte jpg, png, bmp, gif

## Positions disponibles
- `top-left` - Haut gauche
- `top-right` - Haut droit
- `bottom-left` - Bas gauche
- `bottom-right` - Bas droit (défaut)
- `center` - Centre

## Utilisation
```bash
python watermarking.py
```

## Exemple - Image unique
```
Enter watermark text: © 2025 MyName
Choose position: bottom-right
Enter opacity 0-1: 0.7

Mode:
  1. Single image
  2. Batch
Your choice: 1

Enter image path: photo.jpg
✅ Watermarked: photo_watermarked.jpg
```

## Exemple - Batch (tous les fichiers)
```
Mode:
  1. Single image
  2. Batch
Your choice: 2

Enter folder path: C:\Images
🎨 Watermarking 12 image(s)...
✅ Batch complete! Output: C:\Images\watermarked
```

## Notes
- Les images watermarkées sont sauvegardées avec le suffixe `_watermarked`
- Opacité 0 = transparent, 1 = opaque
- Les images originales ne sont pas modifiées
