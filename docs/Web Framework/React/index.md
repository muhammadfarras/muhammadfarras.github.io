## Getting Started With React
Untuk membuat react app gunakan command dibawah ini

```shell
npx create-react-app kertas_pena_react #(1)!
```

1. Folder name (appliaction name)

Setelah membuat project folder react, masuk ke folder tersebut

### How to create React Component
**React** adalah pustaka javascript untuk membuat _user interfaces_. React adalah **Component-based**, component bersifat independen dan dapat digunakan secara berulang. Component adalah balok bangunan dasar dari React. 

Ketika awal kita ingin membangun UI menggunakan react, sangat disaranakan untuk memulai dengan membuat _mock interfaces_. Karena dengan demikian akan memudahkan kita dalam mengidentifikasi jenis komponen apa yang harus dibuat dan bagaimana mereka saling berinteraksi.


![basic mock up](./aset/basic%20mock%20up.png)


Gambar diatas adalah mock UI, kita dapat melihat bagaimana UI dapat dipecah menjadi komponen-komponen yang terpisah. Dalam kasus ini, akan ada **application root component**, **search bar component**, **table component** dan **table row component**.

Komponen-komponen dapat digambarkan dengan hierarki pohon, sebagaimana gambar yg ada dibawah ini. **root component** memliki dua komponen anak, **serach komponen** dan **table component**. Sedangkan table component memiliki satu komponen anak, **row component**. {==Penting untuk dipahami didalam react arus data memliki alur dari parent component menuju ke child component==}. InsyaAllah akan ada catatan juga yang membahas tentang bagaimana kita mengirim data dari parent component ke child component menggunakan`#!javascript pros`.

![tree hierarcy.png](./aset/tree%20hierarcy.png )


> React uses the virtual Document Object Model (VDOM) for selective re-rendering of the UI, which makes it more cost-effective. The VDOM is a lightweight copy of the DOM, and manipulation of the VDOM is much faster than it is with the real DOM. Afte the VDOM is updated, React compares it to a snapshot that was taken from the VDOM before updates were run. After the comparison, React will know which parts have been changed, and only these parts will be updated to the real DOM


Komponen react dapat didefinisikan menggunakan Fungsi javascript atau ES6 JavaScript class

!!! quote "Code"

    === "**Function Component**"

        ```js
        function App(){
            return <h1>Judul</h1>
        }
        ```

    === "**Class Component** ES6 JavaScript class"

        ```js
        class App extends React.component{
            render(){
                return <h1>Judl</h1>
            }
        }
        ```

        Komponen yang diimplementasi menggunakan class membutuhkan fungsi `#!js render()` untuk menampilkan dan memperbarui hasil render dari komponen. 

!!! info
    Jika kita lihat perbandingan App function dan class component, kita dapat lihat bahwa fungi `#!js render()` tidak diperlukan didalam function component. Namun, sebelum React _version 16.8_, kita harus menggunakan class component jika ingin menggunakan _states_. Namun sekaramg kita dapat menggunakan **hooks** untuk membuat states pada function component.

### Lets modified App.js

Sekarang mari kita buat component `App` yang memiliki dua buah element `<h1>` dan `<h2>`. Jika komponen kita mengambalikan lebih daru satu elemen kita harus membungkusnya kedalam satu buah element parent seperti tag `<div>`. Namun semenjak **react 16.2** kita juga dapat menggunakan fragments.


!!! quote "Code"

    === "Using `div`"

        ```js
        function App() {
            return (
                <div>
                    <h1>Selamat Sore</h1>
                    <h2>Kertas Pena React</h2>
                </div>
            );
        }

        export default App;
        ```

    === "Using `React.Fragments`"

        ```js
        import React from "react";

        function App() {
            return (
                <React.Fragment>
                    <h1>Selamat Sore</h1>
                    <h2>Kertas Pena React</h2>
                    <small><i>Ini menggunakan fragment</i></small>
                </React.Fragment>
            );
        }

        export default App;
        ```
    
    === "Using shortcut `<>`"

        ```js
        import React from "react";

        function App() {
            return (
                <React.Fragment>
                    <h1>Selamat Sore</h1>
                    <h2>Kertas Pena React</h2>
                    <small><i>Ini menggunakan fragment</i></small>
                </React.Fragment>
            );
        }

        export default App;
        ```

Pada akhir baris code, ada statement `#!js export` yang meng-ekspor komponen tersebut serta dapat diakses oleh komponen lain menggunakan `#!js import` statement. {==Hanya ada satu buah defailt export statement setiap file, namun dapat memiliki multiple named export statement==}.

```js
export default React // Default export
export { name } // Named export
```

### Inspect index.js


!!! quote "Code"

    === "index.js"

        ```js
        import React from 'react';
        import ReactDOM from 'react-dom/client';
        import './index.css';
        import App from './App';
        import reportWebVitals from './reportWebVitals';

        const root = ReactDOM.createRoot(document.getElementById('root'));
        root.render(
        <React.StrictMode>
            <App />
        </React.StrictMode>
        );

        // If you want to start measuring performance in your app, pass a function
        // to log results (for example: reportWebVitals(console.log))
        // or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
        reportWebVitals();
        ```
    
Pada awal baris kode diatas, terdapat `#!js import` statements yang menge-load komponen komponen dan asssets untuk file tersebut. Misalkan, pada baris ke dua meng- `#!js import react-dom-package` dari folder node_modules, dan pada baris ke 4 meng- `#!js import` **App** component (App.js yang ada pada dirktori `src`). Package `#!js react-dom` memberikan kita method-method **DOM-specific. Untuk me-render komponen react ke Data Obect Model (DOM), kita dapat menggunakan render method dari package `#!js react-dom`. `#!js React.StrictMode` digunakan untuk menemukan potensi masalah didalam React App dan akan mencetaknya pada browser console.

## Usefull ES6 Feature
ES6 dirilis pada tahun 2015 degnan mengenalkan banyak fitur. EXMAScripts adalah standarisasi _scripting langauge_, dna JavaScript dalah salah satu yang mengimplementasinya. Pada bagian catatan ini insyaAllah kita akan membahas fitur-fitur penting.

### Constants and variabels
`Constants` adalah _immutable variables, artinya setelah terdefinisi nilai tersebut tidak dapat berubah. Selain itu const adalah **block-scoped** yang mana const variable hanya dapat digunakan didalam block saat dimana terdefinisi.

Namun, jika const mengandung object array, konten dalamnya tetap dapat diganti

```js
const myObj = {foo: 3};
myObj.foo = 5; // This is ok
```

### Arrow functions

!!! quote "Code"

    === "Arrow function"

        ```js
        function(x) {
            return x * 2;
        }

        // Equal dengan

        const calc = x => x * 2
        ```

Penggunaan arrow function dan pemanggilan serta cara JavaScript-nya

!!! quote "Code"

    === "arrow function"

        ```js
        function call(x){
            console.log(x**2)
        }

        call(2) // Return : 2
        ```

    === "Standard function"

        ```js
        arrCal = x => x ** 2

        arrCal(2) // Return : 2
        ```

Jika function body adalah sebuah ekspression, maka kita tidak peru menggunakan return statement (seperti contoh diatas). Karena expression selalu implisit mengembalikan niai. Akan tetapi, jika kita memiliki beberapa baris kode pada function body, maka kita harus menggunakan curl bracket `{}` dan mengambalikan nilainya menggunakan return statement.

```js
const calcSum = (x, y) => {
    console.log('Calculating sum');
    return x + y;
}
```

### Template literals
Cara tradisional untuk menggabungkan kalimat menggunakan operator `+`.

```js
let person = {firstName: 'John', lastName: 'Johnson'};
let greeting = "Hello " + ${person.firstName} + " " + ${person.lastName};
```

Syntax template literals adalah sebagai berikut. Kita harus menggunakan single quote `' '`

```js
let person = {firstName: 'John', lastName: 'Johnson'};
let greeting = 'Hello ${person.firstName}
${person.lastName}';
```

### Clasess and Inheritance
Class definition in ES6 is similar to other object-oriented (OO) languages, such as Java using `class`.
A class can have fields, constructors, and
class methods.

!!! quote "Code"

    === "Person class"

        ```js
        class Person {
            constructor(firstName, lastName) {//(1)! 
            this.firstName = firstName //(2)1
            this.lastName = lastName
            }

            print_name(){ // (3)!
                console.log('Hai '+${this.firstName})
            }
        }
        ```

        1. Constructor
        2. Field
        3. Method

!!! quote "Code"

    === "`Employee` class menurunkan class `Person`"

        ```js
        class Employee extends Person {
            constructor(firstName, lastName, title, salary) {
                super(firstName, lastName);
                this.title = title;
                this.salary = salary;
            }
        }
        ```


### JSX and Styling
**JSX** adalah syntax extension untuk JavaScript. Tidak wajib, namun memberikan banyak manfaat, misalkan mencegah injection (XSS) karena semua nilai diescape kedalam JSX sebelum di render. Dan yg paling pentingkan ada fitur yang membuat kita dapat menyisipkan JavaScript expression didalam pembungkins JSX `{}`.


!!! quote "Code"

    === "we can access the component props when using JSX."

        ```js
        function App() {
            return <h1>Hello World {props.user}</h1>;
        }
        ```


!!! quote "Code"

    === "You can also pass a JavaScript expression as props, as"

        ```js
        <Hello count={2+2} />
        ```


!!! quote "Code"

    === "You can use both internal and external styling with React JSX elements. Here are two
examples of inline styling"

        ```js
        <div style={{ height: 20, width: 200 }}>
            Hello
        </div>

        // Atau

        const divStyle = { color: 'red', height: 30 };
        const MyComponent = () => (
            <div style={divStyle}>Hello</div>
        );
        ```

## Props and State
Kita telah melihat sedikit tentang `props` dan `states` saat membahas hierarki dari komponen pada react.

### Props
**Props** adalah nilai masukan untuk components dan mereka adlah sebuah mekanisme untuk mengoper data dari parent component ke child component. Props berbentu objek JavaScript, artinya mereka dapat terdiri dari beberapa pasangan key dan value. Selain itu Props _immutable_, nilai tidak didalamnya tidak dapat diubah.

!!! quote "Code"

    === "Pass props from parent to child"

        ```{.js title="PropsAndState/SatuProps.js" linenums="1" hl_lines="1 12-13"}
        function SapaParentComponent(props){
            return (
                <>
                <Accordion>
                    <AccordionSummary
                    aria-controls="panel1a-content"
                    id="panel1a-header">
                    <Typography><b>Accordion 1</b></Typography>
                    </AccordionSummary>
                    <AccordionDetails>
                        <Typography>
                            Selamat {props.waktu}
                            <NamaComponent name={props.name}/>
                        </Typography>
                    </AccordionDetails>

                    
                </Accordion>
                    
                </>
            )
        }

        function NamaComponent(props){
            return (
                <>
                    dan selamat datang {props.name}
                </>
            )
        }

        ```

        **App.js sebagai parent class**

        ```{.js title="./App.js"}
        import SatuProps from './PropsAndState/SatuProps'

        function App() {
            return (
                <>
                    <Container maxWidth="sm">


                        <h2>Kertas Pena React</h2>
                        <small><i>Ini menggunakan fragment using only tag</i></small>

                        <hr></hr>
                        
                        <SatuProps name='Muhammad Farras Maruf' waktu='Pagi'/>
                    </Container>
                </>
            );
        }
        ```
        


---

sample

!!! quote "Code"

    === "Example.java"

        ```js

        ```

        ```{.js title="Output"}
        
        ```

!!! quote "Code"

    === "Example.java"

        ```js

        ```

        ```{.java title="Output"}
        ```

    === "Example.java"

        ```js

        ```

        ```{.java title="Output"}

        ```

!!! quote "Code"

    ```java title=""

    ```

    === "Example 1"

        ```js

        ```

        ```{.java title="Output"}

        ```

    === "Example 2"

        ```js

        ```

        ```{.java title="Output"}

        ```