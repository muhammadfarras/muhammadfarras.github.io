# How to use `steghide`
`Steghide` dapat menyisipkan/embed sekaligus meng-ekstrak file embed kedalam file cover. Dibawah ini adalah `tree` dari direktori saya yang akan kita gunakan untuk mencoba command `steghide`

```
.
├── embeded
├── image.jpg
└── secret-word.txt
```

`image.jpg` adalah cover file, dan `secret-word.txt` adalah file yang akan kita embed kedalam `image.jpg`. Untuk melakukan proses tersebut kita menggunakan command dibawah ini

```bash
steghide embed -ef secret-word.txt -cf image.jpg -sf embeded/picture-for-you.jpg -p keytoopen
```

| command | Description |
| :------ | :-----------|
| steghide | command untuk menjalankan proses steghanography |
| embed | argumen untuk meng-embed file, `extract` untuk sebaliknya |
| -ef <embed file> | opsi nama file yang akan di embed |
| -cf <cover file> | file cover dari file yang diembed |
| -sf <stego file> | file yang telah berhasil diembed |
| -p <phrase> | frasa yang digunakan untuk meng-ekstrak embeded file |

Setelah menjalankan command diatas maka, file dengan nama `/embeded/picture-for-you.jpg` akan terbentuk

```bash
.
├── embeded
│   └── picture-for-you.jpg
├── image.jpg
└── secret-word.txt
```

## How to extract
Mirip dengan cara diatas, yang berbeda adalah argumen yang diberikan adalah `extract`

```bash
steghide extract -sf picture-for-you.jpg -p keytoopen    
wrote extracted data to "secret-word.txt".
```
Embed file akan terbentuk setelah proses extract selesai dilakukan

```bash
.
├── embeded
│   ├── picture-for-you.jpg
│   └── secret-word.txt
├── image.jpg
└── secret-word.txt
```

```bash
cat secret-word.txt
Hello tania, I'm realy-realy loving you                                      
```


