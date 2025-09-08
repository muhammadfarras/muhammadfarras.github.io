# Roles

Sumber bacaan ini dapat dilihat pada [https://python.langchain.com/docs/concepts/messages/#role](https://python.langchain.com/docs/concepts/messages/#role)

_Roles_ (oeran) digunakan untuk membedakan tipe-tipe dari pesan saat konversasi menggunakan ChatModel. Selain itu, menggunakan role, dapat membantu Model untuk mengetahui bagaimana harus menanggapi kumpulan pesan yang diberikan. {==ChatModels yang diberikan ke model berisikan daftar pesan minimal yang terdiri dari ChatUser dan ChatModel==}

## Daftar Roles

| Role | Deskripsi |
| :---- | :---- |
|`system`|Digunakan untuk memberikan instruksi ke model bagaimana harus berprilaku.|
|`user`|Representasi dari user yang memberikan perintah ke model|
|`asistant`|Mewakili respon dari model, bisadalam bentuk text atau dalam bentuk permintaan mengakses sebuah _tools_|
|`tool`|Pesan yang digunakan untuk memberikan nilai keluaran dari tools kepada model setelah mendapatkan data dari luar atau proses setelah pengambilan data selesai. Hanya dapat digunakan untuk chat model yang mendukung _tool calling_|