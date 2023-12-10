## Create engine mssql and pyodbc
The file-based DSN string is being interpreted by SQLAlchemy as server name = `c`, database name = `users`.

I prefer connecting without using DSNs, it's one less configuration task to deal with during code migrations.

This syntax works using Windows Authentication:

    engine = sa.create_engine('mssql+pyodbc://server/database')

Or with SQL Authentication:

    engine = sa.create_engine('mssql+pyodbc://user:password@server/database')

SQLAlchemy has a thorough explanation of the different connection string options [here][1].


  [1]: http://docs.sqlalchemy.org/en/latest/dialects/mssql.html#module-sqlalchemy.dialects.mssql.pyodbc

## Execuqtion Method
SQL Alchemy session objects have their own `execute` method:

```
result = db.session.execute('SELECT * FROM my_table WHERE my_column = :val', {'val': 5})
```

**All** your application queries should be going through a session object, whether they're raw SQL or not. This ensures that the queries are properly [managed by a transaction](https://docs.sqlalchemy.org/en/latest/orm/session_transaction.html), which allows multiple queries in the same request to be committed or rolled back as a single unit. Going outside the transaction using the [engine](https://stackoverflow.com/a/17987782/1394393) or the [connection](https://stackoverflow.com/a/18808942/1394393) puts you at much greater risk of subtle, possibly hard to detect bugs that can leave you with corrupted data. Each request should be associated with only one transaction, and using `db.session` will ensure this is the case for your application.

Also take note that `execute` is designed for [parameterized queries](https://stackoverflow.com/a/4712113/1394393). Use parameters, like `:val` in the example, for any inputs to the query to protect yourself from SQL injection attacks. You can provide the value for these parameters by passing a `dict` as the second argument, where each key is the name of the parameter as it appears in the query. The exact syntax of the parameter itself may be different depending on your database, but all of the major relational databases support them in some form.

Assuming it's a `SELECT` query, this will return [an iterable](https://docs.sqlalchemy.org/en/latest/core/connections.html?highlight=resultproxy#sqlalchemy.engine.ResultProxy) of [`RowProxy`](https://docs.sqlalchemy.org/en/latest/core/connections.html?highlight=rowproxy#sqlalchemy.engine.RowProxy) objects.

You can access individual columns with a variety of techniques:

```
for r in result:
    print(r[0]) # Access by positional index
    print(r['my_column']) # Access by column name as a string
    r_dict = dict(r.items()) # convert to dict keyed by column names
```

Personally, I prefer to convert the results into `namedtuple`s:

```
from collections import namedtuple

Record = namedtuple('Record', result.keys())
records = [Record(*r) for r in result.fetchall()]
for r in records:
    print(r.my_column)
    print(r)
```

<hr>

If you're not using the Flask-SQLAlchemy extension, you can still easily use a session:

```
import sqlalchemy
from sqlalchemy.orm import sessionmaker, scoped_session

engine = sqlalchemy.create_engine('my connection string')
Session = scoped_session(sessionmaker(bind=engine))

s = Session()
result = s.execute('SELECT * FROM my_table WHERE my_column = :val', {'val': 5})
```