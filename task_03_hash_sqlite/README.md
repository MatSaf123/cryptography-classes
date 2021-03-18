# Hash functions part #2 - SQLite

###

- [x] Zaprojektuj i zaimplementuj prosty własny sposób przechowywania haseł w bazie sqlite: użytkownik podaje hasło dwa razy, losujesz sól, hashujesz wszystko i zapisujesz hash oraz sól do bazy. Dodaj funkcję weryfikującą hasło.
- [x] Przerób pkt 1. aby używał pbkdf2_hmac. Zrób z tego porządny projekt (testy, docstringi, itp.)

### Usage:

#### Run with:

```cmd
    python task_03_hash_sqlite/src/accounts_manager_cli.py
```
#### from root directory, or:

```cmd
    python accounts_manager_cli.py
```
#### from 'task_03_hsh_sqlite/src' directory.

### Importing module:

```python
from task_03_hash_sqlite.src.database_controller import DatabaseController as dm
```

#### register_user()

Used for adding new user to database. Has input validation implemented.

- params: None
- return: None
```python
dm.register_user()
```

#### display_users()

Displays all records from database: usernames, hashed passwords and salts.

- params: None
- return: None
```python
dm.display_users()
```

#### log_in()

Simulates logging in operation: user is asked to provide username and password; credentials are validated and if they're correct, 
there is an 'success' information displayed.

- params: None
- return: None
```python
dm.log_in()
```

####

Rest of documentation (database_controller.py, utility.py) — soon.