1. Quel est le rôle de chaque couche dans cette architecture ?

| Couche             | Rôle principal                                                               |
| ------------------ | ---------------------------------------------------------------------------- |
| **Présentation**   | Interface entre l’utilisateur et le système (ex. : pages HTML, formulaire).  |
| **Logique métier** | Gère les règles métier et la logique de traitement (ex. : ajout de tâche).   |
| **Données**        | Stocke et structure les données (ex. : liste en mémoire, plus tard une BDD). |

2. Comment pourriez-vous étendre cette application en une architecture 4-tiers ?
Pour étendre cette application en une architecture 4-tiers, vous pourriez ajouter une couche intermédiaire entre la couche de présentation et la couche de logique métier. Cette couche intermédiaire pourrait être un service web ou une API REST qui gère les requêtes et les réponses entre le client (côté présentation) et le serveur (côté logique métier). Voici comment cela pourrait être structuré :

| Couche                    | Rôle                                                               |
| ------------------------- | ------------------------------------------------------------------ |
| **Présentation (client)** | Affiche l’interface utilisateur, consomme une API via HTTP/JSON.   |
| **API (Flask-RESTful)**   | Fournit une interface REST pour accéder à la logique métier.       |
| **Logique métier**        | Gère les règles métier.                                            |
| **Données**               | Gère l’accès aux données, éventuellement dans une base de données. |

3. Quels sont les avantages de cette séparation des responsabilités ?
✅ Lisibilité du code : chaque partie a une fonction claire.

🔧 Facilité de maintenance : on peut modifier une couche sans impacter les autres.

🔄 Réutilisabilité : la logique métier peut être utilisée par plusieurs interfaces (ex. : web, mobile).

🧪 Testabilité : on peut tester chaque couche indépendamment.

🌐 Évolutivité : on peut remplacer une couche (ex. SQLite → PostgreSQL) facilement.