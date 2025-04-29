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
✅ Cas 2 : Priorité conditionnelle aux Lecteurs
🔐 Sémaphores
mutex = 1

database_access = 1

🧠 Logique
Si un lecteur est actif, il garde la priorité.

Sinon, rédacteur ou lecteur accède selon disponibilité.

📄 Code
c
Copier
Modifier
// Lecteur
p(mutex);
readcount++;
if (readcount == 1)
    p(database_access);
v(mutex);

Lecture();

p(mutex);
readcount--;
if (readcount == 0)
    v(database_access);
v(mutex);
c
Copier
Modifier
// Rédacteur
p(database_access);
Écriture();
v(database_access);
✅ Cas 3 : Priorité aux Rédacteurs
🔐 Sémaphores
mutex = 1

read_try = 1

database_access = 1

🧠 Logique
Dès qu’un rédacteur réclame la ressource, il est prioritaire.

Les lecteurs arrivés après un rédacteur doivent attendre.

📄 Code
c
Copier
Modifier
// Lecteur
p(read_try);
p(mutex);
readcount++;
if (readcount == 1)
    p(database_access);
v(mutex);
v(read_try);

Lecture();

p(mutex);
readcount--;
if (readcount == 0)
    v(database_access);
v(mutex);
c
Copier
Modifier
// Rédacteur
p(mutex);
p(read_try);
p(database_access);

Écriture();

v(database_access);
v(read_try);
v(mutex);
🛠️ Rôle des Sémaphores

Sémaphore	Description
mutex	Protège la section critique liée à readcount.
database_access	Garantit l’accès exclusif à la base pour l’écriture.
read_try	Bloque les nouveaux lecteurs si un rédacteur attend.
lock_ecriture	Empêche l’écriture si au moins un lecteur est actif (cas 1).
✅ Conclusion
Le problème des lecteurs et rédacteurs est un exemple fondamental de la synchronisation concurrente.
Le choix de la politique (priorité lecteur ou rédacteur) dépend du contexte système et des exigences de performance et d'équité.

go
Copier
Modifier

Souhaitez-vous que je crée un fichier `README.md` à télécharger ?






Vous avez dit :
je veux faire copier coller au readme.md


ChatGPT a dit :
Parfait ! Voici le contenu prêt à être copié-collé directement dans ton fichier README.md :

markdown
Copier
Modifier
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
c
Copier
Modifier
// Rédacteur
p(lock_ecriture);
Écriture();
v(lock_ecriture);
✅ Cas 2 : Priorité conditionnelle aux Lecteurs
🔐 Sémaphores
mutex = 1

database_access = 1

🧠 Logique
Si un lecteur est actif, il garde la priorité.

Sinon, rédacteur ou lecteur accède selon disponibilité.

📄 Code
c
Copier
Modifier
// Lecteur
p(mutex);
readcount++;
if (readcount == 1)
    p(database_access);
v(mutex);

Lecture();

p(mutex);
readcount--;
if (readcount == 0)
    v(database_access);
v(mutex);
c
Copier
Modifier
// Rédacteur
p(database_access);
Écriture();
v(database_access);
✅ Cas 3 : Priorité aux Rédacteurs
🔐 Sémaphores
mutex = 1

read_try = 1

database_access = 1

🧠 Logique
Dès qu’un rédacteur réclame la ressource, il est prioritaire.

Les lecteurs arrivés après un rédacteur doivent attendre.

📄 Code
c
Copier
Modifier
// Lecteur
p(read_try);
p(mutex);
readcount++;
if (readcount == 1)
    p(database_access);
v(mutex);
v(read_try);

Lecture();

p(mutex);
readcount--;
if (readcount == 0)
    v(database_access);
v(mutex);
c
Copier
Modifier
// Rédacteur
p(mutex);
p(read_try);
p(database_access);

Écriture();

v(database_access);
v(read_try);
v(mutex);
🛠️ Rôle des Sémaphores

Sémaphore	Description
mutex	Protège la section critique liée à readcount.
database_access	Garantit l’accès exclusif à la base pour l’écriture.
read_try	Bloque les nouveaux lecteurs si un rédacteur attend.
lock_ecriture	Empêche l’écriture si au moins un lecteur est actif (cas 1).
✅ Conclusion
Le problème des lecteurs et rédacteurs est un exemple fondamental de la synchronisation concurrente.
Le choix de la politique (priorité lecteur ou rédacteur) dépend du contexte système et des exigences de performance et d'équité.

yaml
Copier
Modifier

---

Tu peux maintenant coller ceci directement dans ton `README.md` – il sera bien structuré et prêt à être affiché correctement sur GitHub.  
Souhaites-tu aussi un diagramme visuel à intégrer ?
