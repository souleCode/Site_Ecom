# 🛍️ Django E-Commerce

Bienvenue dans **Django E-Commerce**, une application web moderne et performante de boutique en ligne, développée avec **Django 4.2**.  
Ce projet illustre la création d’un site e-commerce complet, prêt à être déployé sur des plateformes cloud comme **Heroku**.

---

## 🚀 Fonctionnalités clés

- 🔐 Authentification sécurisée (inscription, connexion, gestion de profil utilisateur)
- 🛒 Gestion du panier d’achats en temps réel
- 📦 Gestion des produits (CRUD)
- 💳 Processus de commande fluide
- 📊 Tableau de bord administrateur pour gérer les produits et commandes
- 🌐 Déploiement optimisé avec **Heroku**, **Gunicorn** et **Whitenoise**
- 🗄️ Base de données **PostgreSQL** intégrée

---

## 🛠️ Technologies utilisées

- **Backend :** [Django 4.2](https://www.djangoproject.com/)  
- **Base de données :** PostgreSQL  
- **Serveur WSGI :** Gunicorn  
- **Déploiement :** Heroku  
- **Static files :** Whitenoise  

---

## 📂 Installation & Lancement

1. **Cloner le projet**
   ```bash
   git clone https://github.com/ton-utilisateur/django-ecommerce.git
   cd django-ecommerce
2. **Installer les independances**
 ````bash
   pip install -r requirements.txt

````
3. **Migrer la base de données**
   ````bash
   python manage.py migrate
   ````
4. **Lancer le server Django**
   ````bash
   python manage.py runserver
````

