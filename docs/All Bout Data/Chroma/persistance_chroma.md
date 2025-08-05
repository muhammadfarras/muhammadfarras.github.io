# Persistance Chroma

Pada catatan kali ini kita akan menggunakan beberapa fitur yang disediakan oleh chroma. Mirip seperti pada catatan sebelumnya, kita hanya akan sedikit memodifikasi fungsi bawaan, parameter tambahan dan lain lain guna mengetahui output hasil embeddings dan hasil pencarian, _query_. Salah satunya kita akan menggunakan `GoogleAIEmbedding function`.

Untuk itu, kita perlu menyediakan **API_KEY** yang didapatkan dari [https://aistudio.google.com/prompts/new_chat](https://aistudio.google.com/prompts/new_chat) sehingga kita dapat menggunakan `Gemini 2.5 Flash-Lite`. Sebelumnya, kita menggunakan `DefaultEmbendding function` denga model `ll-MiniLM-L6-v2`. Ji 

## Import library

!!! question "Code"

    ```python
    import chromadb
    import os
    from dotenv import dotenv_values as env
    from chromadb.utils import embedding_functions
    import pandas as pd
    from pprint import pp

    # Load env
    my_env = env(os.path.abspath(".env"))
    api = my_env.get("API_OPENAI")
    ```

Seperti contoh sebelumnya kita membutuhkan beberapa library terutama chromadb. Sedikit berbeda dengan catatan sebelumnya, saya juga meng-import dotenv untuk menyimpan API Google Gemini.

## Embedding function 

!!! question "Code"

    ```python
    # Membuat embeddings function
    ef_googleAI = embedding_functions.GoogleGenerativeAiEmbeddingFunction(
        api_key=api
    )

    # Persistance client
    persistance_client = chromadb.PersistentClient('data_vector/persistance1')

    # Membuat sebuah collection
    collection = persistance_client.get_or_create_collection(
        'Peraturan_kedua',
        embedding_function= ef_googleAI,
        metadata= {
            "creator":"Muhammad Farras Ma'ruf",
            "at_place" : "Kebunsu Bogor"
        }
    )
    ```

Selain `Default Embedding function` dan `GoogleAIEmbedding Function`, chorma juga dapat terintegrasi dengan beberapa embedding function, diantaranya; _**saat catatan ini dibuat berikut adalah daftar embedding function yang dapat integrasi dengan Chroma**_

| :----- |:---:|:---:|
Embedding function | Python | Typescript |
OpenAI |✓|✓|
Google Generative AI|✓| ✓|
Cohere|✓|✓|
Hugging Face|✓|-|
Instructor|✓|-|
Hugging Face Embedding Server|✓|✓|
Jina AI|✓|✓|
Cloudflare Workers AI|✓|✓|
Together AI|✓|✓|
Mistral|✓| ✓|


## Data yang awet, persistance Database

!!! question "Code"

    ```python
    # Persistance client
    persistance_client = chromadb.PersistentClient('data_vector/persistance1')

    # Membuat sebuah collection
    collection = persistance_client.get_or_create_collection(
        'Peraturan_kedua',
        embedding_function= ef_googleAI,
        metadata= {
            "creator":"Muhammad Farras Ma'ruf",
            "at_place" : "Kebunsu Bogor"
        }
    )
    ```


## Collection

Ada hal yang perlu diketauhi ketika memberikan document pada collection. Chroma menyediakan dua fungsi, yaitu `add` dan `upsert`, yang mana keduanya digunakan untuk mengkonversi documents menggunakan embedding function dari collection dan meyimpan-nya kedalam memory. Kasus ini, embeddings value akan disimpan kedalam memory fisik (Persistance). Pada catatan mengenai [collection](index.md#menambah-data-pada-collection), kita membutuhkan salah satunya parameter `ids` yang berisikan daftar id unik untuk setiap document. Perlakuan dalam meyimpan data fungsi `add` dan `upsert` terletak pada apakah eksistensi `id` pada collection.

Pada fungsi `add` jika id sudah terdaftar, maka akan penyimpanan diabaikan, sedangkan pada `upsert` jika id sudah terdaftar chorma akan melakukan operasi update pada id tersebut.

Kita akan menggunakan fungsi `upsert` agar data selalu diupdate seandainya id yang digunakan sama. Karena pasti dalam memahami, dan pembelajaran pada catata ini kita akan menjalankan kode ini berulang-ulang kali.


!!! query "Code"

    ```python
    # memuat berita dari resource tipe json
    df = pd.read_json(os.path.abspath("data/berita.json"))
    print(df.columns) # tampilkan nama kolom


    # Memberikan data pada persistance get 
    # Ini hanya jalan sekali saja (karena docoument yang kita berikan selalu sama, maka saya gunnakan upsert)
    collection.upsert(
        ids= [f"id_berita_ke_{a}" for a in range (len(df))],
        documents= df.isi.to_list(),
        metadatas= [{"judul":df.judul[a], "tanggal":df.tanggal[a], "lokasi":df.lokasi[a],"kategori":df.kategori[a],"sumber":df.sumber[a]} 
                    for a in range(len(df))] # type: ignore
    )

    # Giving question
    pertanyaan = ["Tradisi lomba perahu 'Pacu Jalur' dari Kabupaten Kuantan",
            "Berita tentang narkoba ?"]

    # Query the collection
    response = collection.query(
        query_texts=pertanyaan,
        n_results=1,
        include=["metadatas","documents","distances"]
    )
    ```