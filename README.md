# 💣 Minesweeper Game

Un jeu de démineur moderne et personnalisable avec animations, thèmes colorés et système de classement.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Pygame](https://img.shields.io/badge/pygame-2.5.0+-green.svg)

## ✨ Fonctionnalités

- 🎮 **Jouabilité complète** - Toutes les règles classiques du démineur
- 🎨 **21 thèmes colorés** - Ocean, Forest, Sunset, Candy, Midnight, Neon, Retro, Aurora, Lava, Ice, Desert, Galaxy, Matrix, Cherry, Emerald, Copper, Lavender, Cyber, Jungle, Slate
- ✨ **Animations fluides** - Révélation des cellules, drapeaux, explosions avec effets visuels
- 📐 **Résolution adaptative** - S'adapte à toutes les tailles d'écran
- 🖥️ **Mode fenêtré et plein écran** - Basculez avec F11 ou via le bouton du menu
- ⚙️ **Personnalisation totale** - Taille du plateau (5x5 à 25x25) et nombre de mines
- 🏆 **Système de classement** - Scores séparés par configuration avec date et heure
- ⏱️ **Chronomètre** - Suivez votre temps de résolution
- 🎯 **Presets** - Débutant (9x9), Intermédiaire (16x16), Expert (22x22)

## 🚀 Installation

1. Clonez le dépôt :
```bash
git clone https://github.com/VOTRE_USERNAME/Demineur.git
cd Demineur
```

2. Installez les dépendances :
```bash
pip install -r requirements.txt
```

## 🎮 Utilisation

Lancez le jeu :
```bash
python minesweeper.py
```

### Contrôles

- **Clic gauche** - Révéler une case
- **Clic droit** - Placer/retirer un drapeau
- **F11** - Basculer entre mode fenêtré et plein écran
- **Bouton "Enter/Exit Fullscreen"** - Basculer le mode d'affichage depuis le menu
- **ESC** - Retour au menu / Quitter

### Règles du jeu

1. Le premier clic est toujours sûr
2. Les nombres indiquent combien de mines sont adjacentes
3. Placez des drapeaux sur les cases suspectées d'être des mines
4. Révélez toutes les cases sans mines pour gagner

## 📊 Classement

Les scores sont automatiquement sauvegardés dans le dossier `leaderboards/` avec un fichier séparé pour chaque configuration de jeu (taille du plateau + nombre de mines).

Format : `leaderboard_{taille}x{taille}_{mines}mines.txt`

## 🎨 Thèmes disponibles

Le jeu propose **21 thèmes** colorés avec des palettes uniques :

### Thèmes Originaux
1. **Ocean** - Tons bleus classiques
2. **Forest** - Thème nature vert
3. **Sunset** - Tons chauds rouge/rose
4. **Candy** - Violet/rose vif
5. **Midnight** - Mode sombre

### Thèmes Cyberpunk & Tech
6. **Neon** - Cyberpunk avec couleurs lumineuses
7. **Matrix** - Vert style Matrix avec cellules révélées sombres
8. **Cyber** - Bleu cyberpunk futuriste

### Thèmes Rétro & Classiques
9. **Retro** - Tons gris classiques
10. **Slate** - Ardoise gris-bleu avec cellules révélées colorées

### Thèmes Nature
11. **Aurora** - Gradient bleu/cyan aurore boréale
12. **Lava** - Thème volcanique orange/rouge
13. **Ice** - Thème glacé bleu/blanc
14. **Desert** - Tons sable/beige chaleureux
15. **Emerald** - Vert émeraude brillant
16. **Jungle** - Vert jungle luxuriant

### Thèmes Métalliques & Précieux
17. **Copper** - Cuivre/bronze avec cellules beiges
18. **Galaxy** - Violet spatial avec cellules mauves

### Thèmes Floraux & Doux
19. **Cherry** - Rose/rouge cerise
20. **Lavender** - Lavande doux

Chaque thème a été conçu avec des couleurs harmonieuses et des cellules révélées **non-blanches** pour une expérience visuelle unique !

## 🛠️ Technologies

- **Python 3.8+**
- **Pygame 2.5.0+**

## 📝 Structure du projet

```
Demineur/
├── minesweeper.py       # Code principal du jeu
├── requirements.txt     # Dépendances Python
├── leaderboards/        # Fichiers de classement (générés automatiquement)
└── README.md           # Ce fichier
```

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :

1. Fork le projet
2. Créer une branche (`git checkout -b feature/AmazingFeature`)
3. Commit vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push sur la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## 📜 Licence

Ce projet est libre d'utilisation.

## 👤 Auteur

Créé avec ❤️ pour les amateurs de démineur !

## 🎯 Améliorations futures possibles

- [ ] Mode multijoueur
- [ ] Statistiques de jeu détaillées
- [ ] Sons et musique
- [ ] Modes de jeu alternatifs (hexagonal, 3D)
- [ ] Système de succès/achievements
- [ ] Support de différentes langues

**Bon jeu ! 💣🎮**
