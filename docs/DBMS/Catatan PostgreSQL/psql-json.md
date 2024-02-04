[This](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-json/) is the resoucerces of this catatan-pena section

### Create table for json type

```sql
CREATE TABLE mx (
	id serial NOT NULL PRIMARY KEY,
	info jsonmx NOT NULL
);
```


### insert value to table

```sql
insert into mx (jsonmx) values('{   "bkToCstmrStmt": {     "grpHdr": {       "msgId": "cmt053bizmsgidr-001",       "creDtTm": {         "year": 2020,         "month": 8,         "day": 4,         "timezone": 120,         "hour": 18,         "minute": 0,         "second": 0       }     },     "stmt": [       {         "id": "100-01-053053",         "stmtPgntn": {           "pgNb": "1",           "lastPgInd": true         },         "lglSeqNb": 1001,         "acct": {           "id": {             "othr": {               "id": "48751258"             }           },           "ccy": "EUR"         },         "bal": [           {             "tp": {               "cdOrPrtry": {                 "cd": "OPBD"               }             },             "amt": {               "value": 8547.25,               "ccy": "EUR"             },             "cdtDbtInd": "DBIT",             "dt": {               "dt": {                 "year": 2020,                 "month": 8,                 "day": 4,                 "timezone": -2147483648,                 "hour": -2147483648,                 "minute": -2147483648,                 "second": -2147483648               }             }           },           {             "tp": {               "cdOrPrtry": {                 "cd": "CLBD"               }             },             "amt": {               "value": 26452.75,               "ccy": "EUR"             },             "cdtDbtInd": "CRDT",             "dt": {               "dt": {                 "year": 2020,                 "month": 8,                 "day": 4,                 "timezone": -2147483648,                 "hour": -2147483648,                 "minute": -2147483648,                 "second": -2147483648               }             }           }         ],         "ntry": [           {             "amt": {               "value": 35000,               "ccy": "EUR"             },             "cdtDbtInd": "CRDT",             "sts": {               "cd": "BOOK"             },             "valDt": {               "dt": {                 "year": 2020,                 "month": 8,                 "day": 4,                 "timezone": -2147483648,                 "hour": -2147483648,                 "minute": -2147483648,                 "second": -2147483648               }             },             "acctSvcrRef": "ABKREF-125646",             "bkTxCd": {               "domn": {                 "cd": "PMNT",                 "fmly": {                   "cd": "RCDT",                   "subFmlyCd": "XBCT"                 }               }             },             "ntryDtls": [               {                 "txDtls": [                   {                     "refs": {                       "acctSvcrRef": "ABKREF-125646",                       "instrId": "asdfqwertest0003",                       "endToEndId": "pacs008EndToEndId-001",                       "uetr": "8a562c67-ca16-48ba-b074-65581be6f001"                     },                     "amt": {                       "value": 35000,                       "ccy": "EUR"                     },                     "cdtDbtInd": "CRDT"                   }                 ]               }             ]           },           {             "amt": {               "value": 35000,               "ccy": "EUR"             },             "cdtDbtInd": "CRDT",             "sts": {               "cd": "BOOK"             },             "valDt": {               "dt": {                 "year": 2020,                 "month": 8,                 "day": 4,                 "timezone": -2147483648,                 "hour": -2147483648,                 "minute": -2147483648,                 "second": -2147483648               }             },             "acctSvcrRef": "ABKREF-125646",             "bkTxCd": {               "domn": {                 "cd": "PMNT",                 "fmly": {                   "cd": "RCDT",                   "subFmlyCd": "XBCT"                 }               }             },             "ntryDtls": [               {                 "txDtls": [                   {                     "refs": {                       "acctSvcrRef": "ABKREF-125646",                       "instrId": "asdfqwertest0004",                       "endToEndId": "pacs008EndToEndId-001",                       "uetr": "8a562c67-ca16-48ba-b074-65581be6f001"                     },                     "amt": {                       "value": 35000,                       "ccy": "EUR"                     },                     "cdtDbtInd": "CRDT"                   }                 ]               }             ]           }         ]       }     ]   },   "appHdr": {     "fr": {       "fiId": {         "finInstnId": {           "bicfi": "BACALULLXXX"         }       }     },     "to": {       "fiId": {         "finInstnId": {           "bicfi": "BAERLULUXXX"         }       }     },     "bizMsgIdr": "cmt053bizmsgidr-001",     "msgDefIdr": "camt.053.001.08",     "bizSvc": "swift.cbprplus.02",     "creDt": {       "year": 2020,       "month": 8,       "day": 4,       "timezone": 120,       "hour": 18,       "minute": 0,       "second": 0     },     "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.02"   },   "type": "MX",   "@xmlns": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",   "identifier": "camt.053.001.08" }')
```

### Query json data
```sql
select * from mx;
-- return data
```

Postgre menyedikan dua operator native untuk meng-query data dalam bentuk JSON.

1. Operator `->` mengembalikan nilai dalam bentuk `object`
2. Operator `-->` mengembalikan nilai dalam bentuk `text`

Dibawah ini adalah contoh untuk mengambil data json Create Date Time dari pacs.008

```sql
select jsonmx-> 'bkToCstmrStmt'-> 'grpHdr' -> 'creDtTm' from mx

-- return object type
{ "year": 2020,"month": 8,"day": 4,"timezone": 120,"hour": 18,"minute": 0,"second": 0}
```

Sedangkan, contoh dibawah ini adalah mengambil message id dalam bentuk text

```sql
select jsonmx-> 'bkToCstmrStmt'-> 'grpHdr' ->> 'msgId' from mx

-- return
cmt053bizmsgidr-001
```

Bagaimana untuk mengambil array json ? kita dapat menggunakan nomor index

```sql
select jsonmx-> 'bkToCstmrStmt'-> 'stmt' -> 0 from mx
```

### PostgreSQL JSON functions

#### json_each
Function yang berguna untuk menampilkan JSON object terluar dalam bentuk pasangan _key_ dan _value_. Nilai kembalian fungsi ini adalah `object`. Jika lebih menginginkan `text` maka gunakan fungsi `json_each_text`

```sql
select json_each(jsonmx)  from mx
-- return
...
(type,"""MX""")
(identifier,"""camt.053.001.08""")
...
```

informasi lebih lanjut tentang fungsi json pada postgre sql dapat melihat di [sini](https://www.postgresql.org/docs/current/static/functions-json.html)

