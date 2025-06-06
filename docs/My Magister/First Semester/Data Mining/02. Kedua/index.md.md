
# Linear Regresion (General Linear Model)

[Source](https://www.youtube.com/watch?v=7ArmBVF2dCs)
[Source Two](https://www.youtube.com/watch?v=eYTumjgE2IY)
[Find Least Of Square](https://www.youtube.com/watch?v=PaFPbb66DxQ)

## Main Idea

!!! notes 
    ![alt text](assets/01.%20RegressionLinear.png)


Ada 3 hal yang perlu dipahami deari _Linar Regression_

1. _Least Square_ untuk mencocokan garis pada sebuah data
2. Kalkulasi _R Square_ ($R^2$), tujuan untuk mengetahui seberapa bagus tebakan yang dihasilkan.
3. Terakhir kita mengkalkulasi nilai `p` dari $R^2$

## Least Square

Adalah sebuah metode statistik untuk menemukan garis yang palik cocok dalam bentuk persamaan $y=mx+b$ dari data yang diberikan;

!!! info "Slope"
    $$m = \frac{n\sum_{}{}{xy} - (\sum_{}{}{x} \sum_{}{}{y})}{n\sum_{}{}{x^2}-(\sum_{}{}{}x)^2}$$

!!! info "Intercept"
    $$b = \frac{\sum_{}{}{y} - m \sum_{}{}{y}}{n}$$

| Simbol | Deskripsi |
| :---- | :----- |
| `y` | Guest value of Least Square |
| `m` | Slope atau garis miring |
| `b` | Intercept dari `y` ketika nilai dari `x` adalah 0 (Menghilangkan seluruh absolute error) |

### Tujuan Metode

Tujuannya adalah mengurangi jumlah kuadrat kesalahan (_Mean Square of Error_) hingga sekecil mungkin.

!!! info "Rumus Mean Absoule Error"

    $$MSE = \sum_{}{}\frac{(y-p)^2}{b}$$

### Limitasi

Walapun _Least of Square_ dipertimbangkan menjadi metode yang terbaik untuk menemukan garis yang paling cocok, namun metode tersebut memliki beberapa kekurangan;

1. Metode ini hanya menunjukan hubungan antara dua buah variable. Semua penyebab lainnya dan efeknya tidak dipertimbangkan.
2. Metode tersebut tidak dapat diandalkan untuk data yang tidak terdistribusi.
3. Metode ini sangat rentan dan sensitif terhadap data outliers, data yang sangat signifikan perbedaanya dengan data yang lain.

### R Square, coefficient of determination

$R^2$ atau biasa disebut dengan _R Square_ atau _Coeffecient of Determintaion_ adalah metode statistik yang memliki tujuan untuk prediksi hasil keluaran atau menguji hipotesa pada dasar informasi yang berkaitan tersebut.

{==R2 menentukan sebarapa bagus hasil yang diamation direplikasi oleh sebuah model, berdasarakan proporso dari total varian yang dijelaskan oleh mode.==}

Ada beberapa definisi dari $R^2$ dan terkadang memliki arti yang sama. Pada Linear Regression (yang mengandung intercept `b`), R Square adalah kuandrat dari korelasi koofesien (r), antara hasil yang diobservasi dan nilai keluaran yang diamatin. Jika $R^2$ ditambahkan, maka $R^2$ adalah kuadrat dari koofesien dari beberapa korelasi. Koofensiansi biasanya ditentukan dengan rentang nilai dari 0 hingga 1.

!!! info "Rumus $R^2$"
    $$SS_{res} = \sum_i{(y_i - f_i)^2}$$

    $$SS_{tot} = \sum_i{(y_i - \bar x)^2}$$

    $$R^2 = 1 - \frac{SS_{res}}{SS_{tot}}$$


## Orange 3 Tugas

* [Edit Domain](https://orangedatamining.com/blog/managing-data-with-edit-domain/)

## Using python 

https://www.digitalocean.com/community/tutorials/multiple-linear-regression-python


