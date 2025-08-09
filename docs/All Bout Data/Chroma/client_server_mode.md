# Client Side and Filtering in collection

Kali ini kita akan mencoba untuk mengakses chromadb melalui _http network_ menggunakan `#!python HttpClient`. Selain itu kita juga akan mencoba menggunakan filtering pada documents atau pada metadata.

Sumber pemebelajaran dan dokumentasi resmi `Chrome` dapat diakses di [https://www.trychroma.com/](https://www.trychroma.com/)

> Source code hands-on ada pada [https://github.com/muhammadfarras/Learn-Chroma](https://github.com/muhammadfarras/Learn-Chroma)

## Run Chroma in server Mode

Untuk menajalankan chroma sebagai server, kita dapat menggunakan syntax `chroma --run --path {path dari persistance db}` pada terminal atau CMD.

!!! info

    Gunakan `#!bash chroma --help` untuk melihat daftar parameter yang tersedia dan manfaatnya.

!!! question "Code"

    ```sh
    chroma run --port 9000 --path data_vector/persistance1


                    (((((((((    (((((####
                ((((((((((((((((((((((#########
            ((((((((((((((((((((((((###########
            ((((((((((((((((((((((((((############
            (((((((((((((((((((((((((((#############
            (((((((((((((((((((((((((((#############
            (((((((((((((((((((((((((##############
            ((((((((((((((((((((((((##############
            (((((((((((((((((((((#############
                ((((((((((((((((##############
                    (((((((((    #########

    Saving data to: data_vector/persistance1
    Connect to Chroma at: http://localhost:9000
    Getting started guide: https://docs.trychroma.com/docs/overview/getting-started

    OpenTelemetry is not enabled because it is missing from the config.
    Listening on localhost:9000
    ```

## Accsess Chroma on another server

Untuk terkoneksi ke chroma sever kita dapat menggunakan method `#!python HttpClient`. Method ini membutuhkan 2 parameter wajib, _path_ untuk menunjukan lokasi fisik vector database dan _port_ port chroma server berjalan. Selain kedua port tersebut ada satu lagi parameter yaitu _host_, namun jika parameter kosong nilai bawaan adalah _localhost_.

!!! question "Code"

    ```python
    # Persistance client
    persistance_client = chromadb.HttpClient(host='localhost', port=9000)

    # Mengambil collection yang seudah ada
    collection = persistance_client.get_collection(
        'Peraturan_ketiga',
        embedding_function=ef_googleAI
    )

    ## Mneampilkan objek collection
    pp(collection.get_model().metadata)
    print(f"\r\nQuery pertama",end="\r\n")

    ## {'creator': "Muhammad Farras Ma'ruf", 'at_place': 'Kebunsu Bogor'}
    ```

## Query menggunakan filter pada metadata

Saat meng-query sebuah collection kita juga dapat menggunakan filtering pada `documents` ataupun pada `metadata`. Ada beberapa operator yang dapat digunakan diantaranya;

<table>

<tr>
    <th>
        Operator
    </th>
    <th>
        Fungsi
    </th>
    <th>
        Contoh Penggunaan
    </th>
</tr>
<tr>
    <td>
        <code>$eq</code>
    </td>
    <td>Equal, untuk mencari kalimat yang sama persis</td>
    <td>

```json
{"field_metadata" : {"$eq" : "String yang dicari"}}
```
    </td>
</tr>

<tr>
    <td>
        <code>
            $or
        </code>
    </td>
    <td>
        Or, logika <b>atau</b>
    </td>
    <td>

```json
{
    "or": [
        {
            "pengarang": {
                "$eq": "Muhammad Farras"
            }
        },
        {
            "pengarang": {
                "$eq": "Farras Muhammad"
            }
        }
    ]
}
```

<p>Chroma akan mengembalikan document yang memiliki meta data <code>pengarang</code> dengan nilai <i>Muhammad Farras</i> atau <i>Farras Muhammad</i></p>
    </td>
</tr>

<tr>
<td><code>$and</code></td>
<td>Logak <b>dan</dan></td>
<td>

```json
{
    "and": [
        {
            "pengarang": {
                "$eq": "Muhammad Farras"
            }
        },
        {
            "pengarang": {
                "$eq": "Tania Dwi"
            }
        }
    ]
}
```

<p>
    Chroma akan mengembalikan document yang memiliki meta data <code>pengarang</code> <i>Muhammad Farras</i> dan <i>Tania Dwi</i>.
</p>

</td>
</tr>

<tr>
<td> <code>$in</code> atau <code>$nin</code></td>
<td>Operator inklusi, atau mengadung salah satu dari kalimat atau tidak mengadung salah satu dari nilai</td>
<td>

```json
"pengarang": {
    "$in": ["Muhammad Farras","Farras Muhammad"]
}
```

Chroma akan mengembalikan document yang nilai dari metadata <code>pengarang</code> mengadung nilai dari list yang diberikan.

```json
"pengarang": {
    "$nin": ["Muhammad Farras","Farras Muhammad"]
}
```

Chroma akan mengembalikan document yang nilai dari metadata <code>pengarang</code> tidak mengadung nilai dari list yang diberikan.

</td>
</tr>
</table>
