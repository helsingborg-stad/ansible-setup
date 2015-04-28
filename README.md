Helsingborg deploy script
====

The script configures:
- two wordpress frontends
- one mariadb, nfs databaseserver
- one nginx loadbalancer

## Dependencies
- Ansible 1.8.x
- Vagrant 1.7.x
- Virtualbox 4.3.x

## Before startup
1. Make sure that you move the live database to
```sh
/ansible/roles/hb-database/files/XXXXXX.sql
```
2. Then change the constant, according to the mysql dump filename, "sql_backup_file" in
```sh
/ansible/group_vars/db
```

## Start
- cd /basepath/to/repository
- vagrant up
