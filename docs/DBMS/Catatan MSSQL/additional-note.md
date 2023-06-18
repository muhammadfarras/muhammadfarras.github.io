## How to install MSSQL and Transact SQL
Follow this steps, from [official documentation](https://learn.microsoft.com/en-us/sql/linux/quickstart-install-connect-ubuntu?view=sql-server-ver16)

## How to restore `.bak` files
Follow this step, from [official documentation](https://learn.microsoft.com/en-us/sql/t-sql/statements/restore-statements-transact-sql?view=sql-server-ver16)


karena saya menggunakan docker, maka pastikan bak filenya di copy kedalam container yang sedang berjalan. Gunakan perintah `docker cp`.



Pastikan file backup ditaru di repository 
```
/var/opt/mssql/data/backup_filename.bak
```

Selanjutnya masuk kedalam mysql menggunakan sqlcmd
```
/opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P <password-here>
```

Pasti akan ada error yang menyatakan baha mdf dan ldf tidak ditemukan.Anda haris mengemovenya mengikuti logicalnamenya masing2

```
RESTORE DATABASE ADMSCRAPSCALE_UAT
FROM DISK = '/var/opt/mssql/backup/ADMSCRAPSCALE_LIVE_20220209.bak'
WITH MOVE 'ADMSCRAPSCALE_UAT' TO '/var/opt/mssql/data/ADMSCRAPSCALE_UAT.mdf',
MOVE 'ADMSCRAPSCALE_UAT_log' TO '/var/opt/mssql/data/ADMSCRAPSCALE_UAT_log.ldf'
GO
```

Untuk melihat logicalname gunakan query dibawha ini

```
RESTORE FILELISTONLY
FROM DISK = '/var/opt/mssql/backup/ADMSCRAPSCALE_LIVE_20220209.bak'
```


