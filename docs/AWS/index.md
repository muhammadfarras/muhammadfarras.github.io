## Problem saat mengakses tomcat server menggunakan dns public AWS
Kondisi nya ketika kita baru menginstall apache tomcat server secara bawaan kita menggunakan port 8080. Maka dari itu kita harus menambahkan inbound rule baru pada VPC.

1. Kunjungin [EC2 instance](https://console.aws.amazon.com/ec2/)  dan pilih Security Groups pada bagian Network & Security.
2. Kita dapat membuat security group baru atau menambahkan rule dari security group yang telah di assign pada instance.