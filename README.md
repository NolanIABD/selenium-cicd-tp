
## Branche develop utilisée pour la PR

---

# 8. Questions finales du TP

## 1. Avantages observés

### Quels sont les avantages de l'automatisation des tests que vous avez constatés ?

Les tests se lancent automatiquement sans intervention manuelle.  
On gagne du temps et on détecte rapidement les erreurs après une modification.

### Comment le CI/CD améliore-t-il la qualité du code ?

Le pipeline vérifie automatiquement que les tests passent avant un merge.  
Cela évite d’intégrer du code cassé dans la branche principale.

---

## 2. Défis rencontrés

### Quelles difficultés avez-vous rencontrées avec Selenium ?

J’ai rencontré une erreur liée au driver Chrome (WinError 193).  
Il y a aussi eu un problème d’exécution en environnement CI.

### Comment pourriez-vous améliorer la stabilité des tests ?

En utilisant WebDriverWait au lieu de time.sleep.  
En configurant correctement le mode headless pour la CI.  
En structurant mieux les tests.

---

## 3. Métriques

### Quelles métriques sont les plus importantes pour votre projet ?

Le nombre de tests réussis / échoués.  
Le temps d’exécution des tests.  
La stabilité du pipeline CI.

### Comment mesurer l'efficacité de votre pipeline CI/CD ?

En vérifiant que les tests s’exécutent automatiquement à chaque push.  
En surveillant le taux de succès des builds.  
En vérifiant que les rapports de tests sont générés correctement.
