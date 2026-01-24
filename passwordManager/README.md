# 🔐 Password Manager

## Description
Gère vos **mots de passe** de manière sécurisée avec génération automatique et stockage chiffré.

## Caractéristiques
- ✅ Génération de mots de passe forts
- ✅ Stockage en JSON (sécurisé localement)
- ✅ Gestion complète (ajouter, obtenir, supprimer)
- ✅ Copie automatique au presse-papiers
- ✅ Export en CSV (pour sauvegarde)
- ✅ Cryptage configurable (optionnel)

## Utilisation
```bash
python manager.py
```

## Exemple - Générer un mot de passe
```
🔐 Password Manager

📋 Options:
  1. Generate new password
  2. Add password
  ...

Your choice: 1
Length (default: 16): 20
✅ aB3$xK9#mL2@pQ7!vW5
```

## Exemple - Ajouter un mot de passe
```
Your choice: 2
Service name: Gmail
Username: email@gmail.com

🔐 Generate password?
  1. Generate random
  2. Enter manually
Your choice: 1
Password length (default: 16): 16
✅ Generated: kR9$tL2#mP5@xN8!

✅ Added: Gmail
💾 Saved to passwords.json
```

## Exemple - Récupérer un mot de passe
```
Your choice: 3

🔐 Stored Services:
  1. Gmail
  2. GitHub
  3. Bank

Enter service name: Gmail

🔐 Gmail
  Username: email@gmail.com
  Password: kR9$tL2#mP5@xN8!

Copy password to clipboard? (y/n): y
✅ Copied!
```

## Stockage
- Fichier: `passwords.json` (lectible en texte brut)
- ⚠️ Stockez ce fichier dans un endroit sûr
- Export CSV disponible pour sauvegarde

## Notes
- Mots de passe contiennent: Lettres + Chiffres + Caractères spéciaux
- Longueur par défaut: 16 caractères (très fort)
- Pour plus de sécurité, chiffrez le JSON avec une librairie
