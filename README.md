To start the API server, run:
```bash
uvicorn src.api.main:app --reload --port 8000 --reload-dir src 
```


To start the worker, run:
```bash
celery -A src.tasks.worker worker --loglevel=info  --autoreload
```

To monitor the worker, run:
```bash
celery -A src.tasks.worker flower
```
Then go to http://localhost:5555

# DevContainer Configuration

## 🐳 Vue d'ensemble

Le DevContainer permet de développer dans un environnement Docker standardisé. Il inclut :
- Python 3.11
- Redis
- PostgreSQL
- Les extensions VS Code recommandées ( rapidos )
- Les dépendances du projet

## 📁 Structure des fichiers

```
.devcontainer/
├── devcontainer.json    # Configuration principale
└── docker-compose.yml   # Services Docker (Redis, PostgreSQL)
```

## 🚀 Utilisation

1. Prérequis :
   - VS Code
   - Extension "Remote - Containers"
   - Docker Desktop

2. Démarrage :
   - Ouvrir le projet dans VS Code
   - Cliquer sur l'icône verte en bas à gauche
   - Sélectionner "Reopen in Container"

## 🔧 Services préconfigurés

- **Redis** : 
  - Port: 6379
  - Pas de mot de passe par défaut

- **PostgreSQL** :
  - Port: 5432
  - User: postgres
  - Password: postgres
  - Database: postgres

## 💡 Extensions VS Code incluses

- Python
- Pylance
- Ruff
- Docker
- Git
- etc.

## 🔄 Reconstruction

Si vous modifiez la configuration :
```bash
Ctrl/Cmd + Shift + P -> Remote-Containers: Rebuild Container
```

