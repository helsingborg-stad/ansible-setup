Helsingborg deploy script
====

The script configures:
- two wordpress frontends
- one mariadb, nfs databaseserver
- one nginx loadbalancer

## Dependencies
- Ansible 1.9.x
- Vagrant 1.7.x
- Virtualbox 4.3.x

## Before startup
1. Make sure that you move the database to
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
- vagrant ssh-config >> ~/.ssh/config

## Ansible commands
```sh
cd /basepath/to/repository/ansible
```
1. You only need to do this command the first time after vagrant up.
```sh
ansible-playbook site.yml
```
2. Deploy changes to webbservers.
```sh
ansible-playbook webbservers.yml --tags="deploy"
```
3. Deploy/Reset changes to dbservers.
```sh
ansible-playbook dbservers.yml --tags="deploy"
```
