# Logistic Regression

Bismillah, sumber catatan ini ada beberapa diantaranya

1. [Data Camp : Logistic Regression](https://www.datacamp.com/tutorial/understanding-logistic-regression-python)
2. Practical Statistics for Data Scientists, Peter Brauce, Andrew Brauce, dan Peter Gedeck

## Pengertian

Tujuan dalam menganalisa menggunakan model _Logistic Regression_ mirip dengan model regresi statistik yang lainya, yaitu {==menemukan garis yang paling cocok==}, sehingga dengan demikian model tersebut dapat mendeskripsikan hubungan antara dependent variable atau response dan independent variabel atau bisa disebu sebagai prediktor.

Lalu yang membedakan antara logistic regression dengan linear regression adalah hasil keluaran dari variabel _logistic regression_ yang mana dalam bentuk _binary_ (0 atau 1, iya atau tidak, bagus atau buruk). Selain dari hasil keluaran, perbedaan model tersebut terlihat dari belum model dan asumsinya. Linear Regression mencari kecocokan dengan _least Square_ dan kualitas model tersebut diukur dengan RMSE, MAE dan $R^2$. Sedangkan pada Logistic Regresion menggunakan MLE (_Maximum Likelihood Estimation_).

![alt text](../assets/02.%20Linear%20vs%20Log%20Reg.png)

## Uji performa

### Receiver Operator Characteristic (ROC)

Kurva ROC dibangun dengan memploting _true posirive rate **TPR**_ dengan _False Positive Rate **FPR**_. `TPR` adalah proporsi dari observasi yang diprediksi _true positive_ berdasarkan seluruh observasi positif $TP/(TP+FN)$. Sedangkan `FPR` adalah proporsi dari obeservasi yang diprediksi _false positive_ berdasarkan seluruh observasi, $FP/(TP+FN)$.

Contoh, pada pengujian medis, _true positive rate_ adalah tingkat nilai true positive yang mana pasien secara benar teridentifikasi berdasarkan hasil uji coba dinyatakan postive pada penyakit ditanyakan tersebut.


A discrete classifier that returns only the predicted class gives a single point on the ROC space. But for probabilistic classifiers, which give a probability or score that reflects the degree to which an instance belongs to one class rather than another, we can create a curve by varying the threshold for the score. Note that many discrete classifiers can be converted to a scoring classifier by ‘looking inside’ their instance statistics. For example, a decision tree determines the class of a leaf node from the proportion of instances at the node.


[source](https://www.displayr.com/what-is-a-roc-curve-how-to-interpret-it/)

[source : Quest Stat](https://www.youtube.com/watch?v=4jRBRDbJemM)

[Source : More Explained](https://www.youtube.com/watch?v=ExJCi6aj1cM)

[Why TPR, FPR dan Tresshold differeint with the data given](https://stackoverflow.com/questions/63734949/how-does-roc-curve-function-calculates-fpr-tpr-values-behind-the-scene-in-my)

[Logistic Regression : Data Tab Youtube](https://www.youtube.com/watch?v=T5AoqxQFkzY)

[Logistic Regression : Data Tab Note](https://datatab.net/tutorial/logistic-regression)
