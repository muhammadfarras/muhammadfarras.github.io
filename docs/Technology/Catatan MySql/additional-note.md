# Additional-notes

## JSON Type
Source : 

* [Official Documentations](https://dev.mysql.com/doc/refman/8.0/en/json.html)

* [Pros about json data type](https://www.quora.com/What-has-been-your-experience-using-the-MySQL-JSON-format-What-advantages-does-it-offer-over-simply-storing-a-JSON-string-in-a-VARCHAR)


* [Conts about json data type](https://stackoverflow.com/questions/33660866/native-json-support-in-mysql-5-7-what-are-the-pros-and-cons-of-json-data-type)


Ada beberapa manfaat menggunakan JSON data type;

1. Validasi otomatis pada kolom dengan tipe data JSON. Akan menghasilkan error jika data yang dimasukan bukan dalam format json yang valid
   
2. Optimasi format penyimpanan. Data yang disimpan kedalam kolum JSON akan dikonversi menjadi format internal yang memungkian akses quick read kedalam data json tersebut. 

!!! warning
    Akan tetapi, besaran yang dibutuhkan oleh JSON sama seperti besaran peyimpanan dari LONGBLOB atau LONGTEXT. Serta, batas maksium data JSON yang disimpan didalam kolom JSON tidak boleh lebih dari max_allowed_packet system variable.

### Creating Json Type
JSON array berisikan daftar nilai yang dipisahkan dengan koma , dan dibuka ditutup dengan square bracket [].


``` json
["abc", 10, null, true, false]
```


JSON Object berisikan pasangan keys dan values yang dipisahkan dengan koma dan dibuka serta ditutup dengan curl brakcet {}.


``` json
{"k1": "value", "k2": 10}
```


Melihat contoh diatas, JSON Array dan Object dapat berisikan nilai skalar seperit string dan number, null, JSON bollean (true and false). Keys pada JSON Object harus strings. Temporal (date, time or datetime) juga tersedia.


```json
["12:18:29.000000", "2015-07-29", "2015-07-29 12:18:29.000000"]
```


JSON bersarang juga bisa disimpan didalam JSON kolom


```json
[99, {"id": "HK500", "cost": 75.99}, ["hot", "cold"]]
{"k1": "value", "k2": [10, 20]}
```

Work with JSON Value Columns

``` sql
CREATE TABLE T1 (jdoc JSON);

INSERT INTO t1 values ('{"key":"this is value"}');
--Query OK, 1 row affected (0.01 sec)

INSERT INTO t1 values ('[1,2,4,5,true,false]');
--OK, 1 row affected (0.00 sec)  

INSERT INTO t1 values ('{"key":"this is value"');
--3140 (22032): Invalid JSON text: "Missing a comma or '}' after an object member." at position 22 in value for column 't1.jdoc'. 
```



### Fungsi JSON_TYPE
Fungsin JSON_TYPE membutuhkan satu buah argumen berupa nilai JSON dengan nilai keluaran tipe JSON jika valid, dan error jika sebaliknya.


``` sql
mysql> SELECT JSON_TYPE('["a", "b", 1]');
+----------------------------+
| JSON_TYPE('["a", "b", 1]') |
+----------------------------+
| ARRAY                      |
+----------------------------+

mysql> SELECT JSON_TYPE('"hello"');
+----------------------+
| JSON_TYPE('"hello"') |
+----------------------+
| STRING               |
+----------------------+

mysql> SELECT JSON_TYPE('hello');
ERROR 3146 (22032): Invalid data type for JSON data in argument 1
to function json_type; a JSON string or JSON type is required.
```
More info you can visit the official documentation above.
