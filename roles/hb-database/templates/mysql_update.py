#!/usr/bin/python

import MySQLdb

db = MySQLdb.connect(host="localhost",
                     user="{{ mysql_users[0].name }}",
                     passwd="{{ mysql_users[0].password }}",
                     db="{{ mysql_databases[0].name }}")

cur = db.cursor()

cur.execute("UPDATE wp_site SET domain='http://{{ domain_name }}' WHERE id=1")
print int(cur.rowcount)

cur.execute("UPDATE wp_options SET option_value='http://{{ domain_name }}' WHERE option_id=1")
print int(cur.rowcount)

cur.execute("UPDATE wp_options SET option_value='http://{{ domain_name }}/' WHERE option_id=2")
print int(cur.rowcount)

cur.execute("UPDATE wp_blogs SET domain='{{ domain_name }}' WHERE domain='{{ old_domain_name }}'")
print int(cur.rowcount)

db.commit()
