# Catatan-catatnan penting

Bismillah semoga bermanfaat

### JPA Cascade.REMOVE pada database
Jika kita menggunakan cascade.remove, Spring hanya menggunakan konfigurasi tersebut hanya pada level aplikasi Spring, bukan pada database. maka dari itu jika kita mendelete record dari table parent maka tidak akan berpengaruh pada record anak. Cara untuk memaksa cascde pada DDL adalah menggunakan fitur tambahan dari hibernate

```java
@OnDelete(action = OnDeleteAction.CASCADE)
```

!!! info
    In hibernate, you can use

    ```
        @OnDelete(action = OnDeleteAction.CASCADE)
    ```
    on your @OneToMany relationship. This tells hibernate to set ON DELETE CASCADE for the generated foreign key.

    Note that this is a hibernate extension and is not specified in the JPA standard.

    Use this with caution. When you let database cascade the deletes, these happen outside the control of hibernate so:

    Your second-level cache might become out of sync.
    You cant use on delete listeners on those entities.
    I think you should only use this if you have a large collection and performance consideration forces you to let database handles the delete instead of hibernate.

Sumber : [Stackover flow](https://stackoverflow.com/a/21155878/11021522)



### JPA membuat tipe data JSOB buat PSQL  
Sumber : [Stackoverflow](https://stackoverflow.com/questions/51276703/how-to-store-postgresql-jsonb-using-springboot-jpa)
