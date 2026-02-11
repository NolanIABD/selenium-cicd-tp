# TP Selenium CI/CD – Calculatrice

## Objectif du TP
Créer une application web simple (calculatrice), automatiser des tests Selenium, et mettre en place une CI/CD avec GitHub Actions.

---

## Structure du projet
- src/
  - index.html
  - style.css
  - script.js
- tests/
  - requirements.txt
  - test_selenium.py
- .github/workflows/
  - ci-cd.yml

---

## Étapes réalisées

### 1) Création de l’application web
Création des fichiers dans `src/` :
- `index.html` : formulaire + affichage du résultat
- `style.css` : mise en forme simple
- `script.js` : calcul + gestion division par zéro

Test manuel dans le navigateur.

### 2) Mise en place Selenium + Pytest
Création d’un environnement virtuel :
    py -m venv .venv
Activation :
    .\.venv\Scripts\Activate.ps1
Installation dépendances :
    pip install -r tests/requirements.txt

Création des tests Selenium (Pytest) :
- test chargement page
- test addition
- test division par zéro
- test toutes opérations

Utilisation de `WebDriverWait` et `Select` (plus stable que `sleep`).

Génération d’un rapport HTML :
    pytest -v --html=report.html --self-contained-html

### 3) Mise en place CI/CD (GitHub Actions)
Création du workflow :
- installation Python
- installation Chrome sur Ubuntu
- installation dépendances
- exécution des tests en headless avec CI=true
- génération `test-report.html`
- upload artifact `selenium-report`

Déclenchement sur :
- push
- pull_request

### 4) Workflow Git
- création branche `develop`
- push de `develop`
- création Pull Request `develop -> main`
- validation CI verte
- merge

---

## Problèmes rencontrés et corrections

### 1) Activation du venv bloquée (PowerShell)
Problème : script `Activate.ps1` bloqué par ExecutionPolicy.  
Correction :
    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

### 2) Selenium WinError 193 (ChromeDriver)
Problème : `%1 n’est pas une application Win32 valide` avec webdriver-manager.  
Correction : suppression webdriver-manager et utilisation de Selenium Manager natif (webdriver.Chrome sans driver externe).

### 3) Repo Git non lié au remote
Problème : `No configured push destination`.  
Correction :
    git remote add origin <repo_url>
    git push -u origin main

### 4) __pycache__ commité
Problème : fichiers Python générés suivis par Git.  
Correction :
    ajout `.gitignore`
    git rm -r --cached __pycache__

---

## Questions finales du TP

### 1. Avantages observés

**Quels sont les avantages de l'automatisation des tests que vous avez constatés ?**  
Les tests se lancent automatiquement sans intervention manuelle.  
On gagne du temps et on détecte rapidement les erreurs après une modification.

**Comment le CI/CD améliore-t-il la qualité du code ?**  
Le pipeline vérifie automatiquement que les tests passent avant un merge.  
Cela évite d’intégrer du code cassé dans la branche principale.

### 2. Défis rencontrés

**Quelles difficultés avez-vous rencontrées avec Selenium ?**  
J’ai eu une erreur de driver Chrome (WinError 193).  
J’ai dû adapter la configuration pour l’exécution en CI.

**Comment pourriez-vous améliorer la stabilité des tests ?**  
Utiliser `WebDriverWait` au lieu de `time.sleep`.  
Garder une config headless propre pour la CI.  
Structurer mieux les tests (ex : Page Object Pattern).

### 3. Métriques

**Quelles métriques sont les plus importantes pour votre projet ?**  
Le nombre de tests réussis / échoués.  
Le temps d’exécution des tests.  
La stabilité du pipeline CI.

**Comment mesurer l'efficacité de votre pipeline CI/CD ?**  
Vérifier que les tests se lancent à chaque push/PR.  
Surveiller le taux de succès des runs.  
Vérifier que le rapport de test est généré et disponible en artifact.

