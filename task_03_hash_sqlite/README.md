# Hash functions part #2 - SQLite

###

- [x] Zaprojektuj i zaimplementuj prosty własny sposób przechowywania haseł w bazie sqlite: użytkownik podaje hasło dwa razy, losujesz sól, hashujesz wszystko i zapisujesz hash oraz sól do bazy. Dodaj funkcję weryfikującą hasło.
- [x] Przerób pkt 1. aby używał pbkdf2_hmac. Zrób z tego porządny projekt (testy, docstringi, itp.)

## Usage:

#### Run with:

```cmd
    python task_03_hash_sqlite/src/users_manager_cli.py
```
#### from root directory, or:

```cmd
    python users_manager_cli.py
```
#### from 'task_03_hsh_sqlite/src' directory with command line.

Use with flags to invoke certain functions:

```cmd
    -a      add new user
    -d      delete user
    -s      show all users
    -l      log in      
    -h      help commands
```

All commands list:

#### add_user()

Add new user in the database. Has input validation implemented.

```cmd
python users_manager_cli.py -a
```

#### delete_user()

Deletes targeted user from database. 

```cmd
python users_manager_cli.py -d
```

#### show_users()

Displays all records from database: usernames, hashed passwords and salts.

```cmd
python users_manager_cli.py -s
```

#### log_in()

Simulates logging in operation: user is asked to provide username and password; credentials are validated and if they're correct, 
there is an 'success' information displayed.

```cmd
python users_manager_cli.py -l
```

#### help

Displays all available flags and their descriptions.

```cmd
python users_manager_cli.py -h
```