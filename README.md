# 📚 Projet 1 : Outils de Synchronisation – Lecteurs & Rédacteurs

## 🎯 Objectif

Gérer l'accès concurrent à une base de données partagée entre **lecteurs** (lecture seule) et **rédacteurs** (écriture exclusive) en garantissant la cohérence des données grâce à l'utilisation de **sémaphores**.

---

## 📌 Contraintes

- ❌ Si un rédacteur écrit, aucun autre processus (lecteur ou rédacteur) ne peut accéder à la base.
- ✅ Plusieurs lecteurs peuvent lire simultanément si aucun rédacteur n'écrit.
- ⚠️ La variable partagée `readcount` doit être protégée par un sémaphore.

---

## 🧪 Cas étudiés

### ✅ Cas 1 : **Priorité aux Lecteurs**

#### 🔐 Sémaphores

- `mutex = 1` : protège `readcount`
- `lock_ecriture = 1` : bloque les rédacteurs quand un lecteur est actif

#### 🧠 Logique

- Si un lecteur lit, d'autres lecteurs peuvent entrer.
- Les rédacteurs attendent que tous les lecteurs terminent.

#### 📄 Code

```c
// Lecteur
p(mutex);
readcount++;
if (readcount == 1)
    p(lock_ecriture);
v(mutex);

Lecture();

p(mutex);
readcount--;
if (readcount == 0)
    v(lock_ecriture);
v(mutex);

// Rédacteur
p(lock_ecriture);
Écriture();
v(lock_ecriture);

### cas 2
