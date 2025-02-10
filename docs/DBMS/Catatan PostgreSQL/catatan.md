### Login to PSQL CMD

```bash
psql -u 'your user name'
# after this you have to type your password
```


### Display Databases
Untuk menampilkan data base gunakan perintah `\dt`

```sql
\dt
postgres=# \dt
        List of relations
 Schema | Name | Type  |  Owner
--------+------+-------+----------
 public | mx   | table | postgres
```

### Choosing database
Untuk memilih database gunakan perintah `\c [database name]`

```sql
postgres=# \c DBCM-BBA
You are now connected to database "DBCM-BBA" as user "postgres".
```


### Display informatio about table
Untuk menampilkan informasi mengenai sebuah table seperti tipe data, nama kolom, primary key serta index dan constraint gunakan `\d [table name]`

```sql
DBCM-BBA=# \d mx
                            Table "public.mx"
 Column |  Type   | Collation | Nullable |            Default
--------+---------+-----------+----------+--------------------------------
 id     | integer |           | not null | nextval('mx_id_seq'::regclass)
 jsonmx | json    |           | not null |
Indexes:
    "mx_pkey" PRIMARY KEY, btree (id)
```

More information about table definition you can visit [here](https://www.commandprompt.com/education/how-to-describe-a-table-in-postgresql/)

### Backup dan restore

```sql
pg_dump -U postgres -d DBCM -h 192.168.220.241 > dbcm_muamalat
```

Backup database `DBCM` pada host `192.168.220.241` dan taruh file output `dbcm_muamalat`

```sql
psql -U postgres -d "DBCM-Muamalat" -h localhost < dbcm_muamalat
```

Restore `dbcm_muamalat` pada database `DBCM-Muamalat` pada localhost