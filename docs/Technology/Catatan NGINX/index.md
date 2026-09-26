### How to steup web interface into NGX


## Install NGINX

```bash
sudo apt install nginx
```

Gunakan `systemctl` untuk memastikan service NGINX berjalan.

```bash
sudo systemctl status nginx
```

Jika berjalan maka akan muncul informasi seperti dibawah ini
```bash
● nginx.service - A high performance web server and a reverse proxy server
     Loaded: loaded (/usr/lib/systemd/system/nginx.service; enabled; preset: enabled)
     Active: active (running) since Sat 2026-09-26 18:27:19 CST; 24min ago
       Docs: man:nginx(8)
   Main PID: 55540 (nginx)
      Tasks: 3 (limit: 2263)
     Memory: 4.6M (peak: 9.4M)
        CPU: 366ms
```

Lokasi interface ada di `/var/html`

Selanjutnya buatlah folder pada `/var/html` untuk menaruh aplikasi. Gunakan perintah

```bash
mkdir var/html/aplikasi_farras
```

## Compile project (Angular)

Pada catatan ini saya menggunakan membuat aplikasi menggunakan angular. Masuk kedalam folder project root dan jalankan perintah

```bash
ng build --configuration production
```

Hasil aplikasi akan terbentuk pada folder dist

```
dist
└───your_application_name
    └───browser
        └───media

```

Selanjutnya pindahkan semua yg ada dibrowser {==yang berisikan file `index.html`==} pada `var/html/aplikasi_farras`

## Setup ngix ke folder aplikasi_farras

Buatlah sebuah file pada `/etc/nginx/sites-variable` untuk membuat konfigurasi.

```bash
sudo vim /etc/nginx/sites-variabl
```

dan copy paste perintah berikut

```json
server {
    server_name _;

    root /var/www/sjsjb;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }
}
```

Menaktifkan website pada `sites-enabled`, kita symlink

```bash
sudo ln -s /etc/nginx/sites-available/application_farras /etc/nginx/sites-enabled/
```

[Opsina], kita bisa menghapus `defeault` site

```bash
sudo rm /etc/nginx/sites-enabled/default
```

Check syntax dengan perintah `sudo nginx -t`, jika semuanya berjalan lancar maka akan muncul

```
syntax is ok
test is successfull
```

Terakhir, reload aplikasi nginix

```bash
sudo systemctl reload nginx
```

## Setup using HTTPS (jika public dan sudah punya DNS)

Check apakalh firewall jalan

```bash
sudo ufw status
```

jika inactive tidak measalah, artinya 443 dan 80 bisa di akses.

install certbot jika tidak ada

```bash
sudo apt install certbot python3-certbot-nginx -y
certbot --version
```

Rubah server_name pada `/var/www/application_farras`

```json

server {
    listen 80;
    server_name dns_kamu.com; // Tambahkan ini

    root /var/www/sjsjb;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }
}
```

lalu jalankan

```bash
sudo certbot --nginx -d dns_kamu.com
```

Viola aplikasi sudah bisa di akses menggunakan HTTPS