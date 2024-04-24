README
======

THINGS YOU NEED TO DO FIRST TO RUN THIS WEBAPP
----------------------------------------------

You need to create ``virtual environment`` for Django:

    python -m venv venv

Activate your venv:
---
PowerShell: 
    
    .\venv\Scripts\activate

--------------------------------
    
cmd: 

    venv\Scripts\activate

---------------------------------

gitbash terminal: 

    source venv\Scripts\activate

----------------------------------

Linux:
    
    source venv/bin/activate

---

Install the packages in ``requirements.txt`` file:

    pip install -r requirements.txt

---

# API ENDPOINTS

### MENU ITEMS
```
    http://127.0.0.1:8000/api/menu-items
    http://127.0.0.1:8000/api/menu-items/{int:id}
```
### BOOKING TABLES
```
    http://127.0.0.1:8000/api/tables
    http://127.0.0.1:8000/api/tables/{int:id}
```
### USER MANAGEMENT
```
    http://127.0.0.1:8000/api/users
    http://127.0.0.1:8000/api/users/{int:id}
```
### DJOSER
```
    http://127.0.0.1:8000/auth/...
```
### OBTAIN TOKEN
```
    http://127.0.0.1:8000/api/auth-token
```