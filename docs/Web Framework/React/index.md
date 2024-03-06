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
                <>
                    <h1>Selamat Sore</h1>
                    <h2>Kertas Pena React</h2>
                    <small><i>Ini menggunakan fragment</i></small>
                <>
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

    === "Standard function"

        ```js
        function call(x){
            console.log(x**2)
        }

        call(2) // Return : 2
        ```

    === "Arrow function"

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

Dibawa ini adalah prop life cycle

![prop life cycle](./aset/prop%20life%20cycle.png)

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

### State

Dibawah ini adalah state life cycle

![prop life cycle](./aset/state%20life%20cycle.png)

Berbeda dengan Props, nilai dari **State** dapat diperbarui didalam component. **State** dibuat menggunakan _hook function_. Fungsi tersebut membutuhkan satu argumen yaitu nilai awal dari state. Fungsi yang digunakan adalah `#!js useState`, dimana mengembalikan sebuah array dengan dua element. 

* **Element pertama** berisikan nama dari state, 
* dan **element kedua** adalah fungsi yang digunakan untuk memperbarui nilai dari state

```{.js title="syntax"}
const [state, setState] = React.useState(intialValue);

// atau
import React, { useState } from 'react';
const [state, setState] = useState(intialValue);
```

Selain itu, hook function hanya bisa digunakan didaalam function component, jika anda mendefinisikannya pada top level maka interpreter akan mengeluarkan error.

Dibawah ini adalah snippet kode penggunaan state serta penggantian nilai dari variable tersebut menggunakan function kembalian dari `useState`.

!!! quote "Code"

    === "PropsAndState/LearnState.js"

        ```{.js linenums="1" hl_lines="6 17"}
        import { Accordion,AccordionDetails,AccordionSummary,Typography, Button } from '@mui/material';
        import React, { useState } from 'react';

        function RootAccordian(props){

            const [waktuState, setWaktuState] = useState("pagi") //(1)
            
            return (
                <Accordion>
                <AccordionSummary
                aria-controls="panel1a-content"
                id="panel1a-header">
                    <Typography><b>{props.title}</b></Typography>
                </AccordionSummary>
                <AccordionDetails>
                    
                    <Button variant="outlined" onClick = {(e)=> setWaktuState("Sore")}> //(2)
                        Change Waktu
                    </Button>

                    <Typography>
                        <ParentComponent waktu={waktuState} />
                    </Typography>
                </AccordionDetails>
            </Accordion>
            )
        }
        function ParentComponent(props){

            

            return(
                <>
                    Selama {props.waktu}
                </>
            )
        }

        export default RootAccordian
        ```

        1. Create state
        2. Change sate using function hook


#### Define state with objects
Kita juga dapat mendefinisikan state dengan nilai object.

```js
const [name, setName] = useState({
    firstName: 'Muhammad Farras',
    lastName: 'Ma\'ruf'
});
```


!!! quote "Code"

    === "ropsAndState/LearnStateValueObject.js"

        ```js
        import { Accordion,AccordionDetails,AccordionSummary,Typography, Button } from '@mui/material';
        import React, { useState } from 'react';

        function RootAccordian(props){

            const namaLengkap = {
                namaDepan : "Muhammad Farras",
                namaBelakang : "Ma'ruf"
            }
            const [nama, setNama] = useState(namaLengkap)
            
            return (
                <Accordion>
                <AccordionSummary
                aria-controls="panel1a-content"
                id="panel1a-header">
                <Typography><b>{props.title}</b></Typography>
                </AccordionSummary>
                <AccordionDetails>
                    
                    <Button variant="outlined" onClick = {(e)=> 
                        setNama({"namaDepan" : "Faris","namaBelakang" : "Ma'ruf"})}>
                        Change Name
                    </Button>

                    <Typography>
                        <ChildComponent nama={nama} />
                    </Typography>
                </AccordionDetails>
            </Accordion>
            )
        }
        function ChildComponent(props){

            return(
                <>
                    Nama saya : {props.nama.namaDepan} {props.nama.namaBelakang}
                </>
            )
        }

        export default RootAccordian
        ```


#### update partial object
Jika anda ingin melakukan perubahan sebagian, kita dapat menggunakan spread operator. Contoh dibawah ini menyalin `name` state objeckt dan memperbarui `firstName` dengan Jim.
```js
setName({ ...name, firstName: 'Jim' })
```

### Stateless Component

**React stateless** compenent adalah murni fungsi javascript yang mengambil nilai _props_ sebagai argument dan mengambalikanna dalam bentuk element react.


!!! quote "Code"

    === "Contoh"

        ```js
        function HeaderText(props) {
        return (
            <h1>
                {props.text}
            </h1>
            )
        }
        export default HeaderText;
        ```

Contoh `HeaderText` component diatas adalah _pure component_. Sebuah component dikatakan _pure_ (murni) jika nilai kembaliannya secara konsisten sama dengan nilai masukannya. React menyediakan `#!js React.memo()` yang mana memberikan optimasi performa dari pure function components. Dibawah ini kita akan bungkus fungsi pure tersebut dengan `memo`.

!!! quote "Code"

    === "Contoh"

        ```js
        import React, { memo } from 'react';

        function HeaderText(props) {
        return (
            <h1>
                {props.text}
            </h1>
            )
        }
        export default memo(HeaderText);
        ```

Sekarang komponen terender dan akan dihafal. Render selanjutnya, react akan me-render memoizednya jika `props` tidak berubah. Fungsi `#!js React.memo()` memiliki argumen kedua yang mana kita dapat mengkostumasi kondisi render, `#!js arePropsEqual()`.


### Conditional Rendering
Kita dapat menggunakan **conditional statement** untuk merender UI yang berbeda tergantung kondisi tertentu. Sebagai contohh, jika user terautentikasi maka munculkan komponen `#!react <Logout/>` dan `#!react <Logit/>` sebaliknya.

!!! quote "Code"

    === "Traditional if statement"

        ```js
        function MyComponent(props) {
            const isLoggedin = props.isLoggedin;
            if (isLoggedin) {
                return (
                    <Logout />
                )
            }
            return (
                <Login />
            )
        }
        ```

    === "Logical Operator"

        ```js
        function MyComponent(props) {
            const isLoggedin = props.isLoggedin;
                return (
                <div>
                    { isLoggedin ? <Logout /> : <Login /> }
                </div>
            );
        }
        ```


## React Hooks
There are certain important rules for using hooks in React. You should always call hooks
at the top level in your React function component. You shouldn't call hooks inside loops,
conditional statements, or nested functions.

Ada beberapa aturan penting saat menggunakan hooks in React. 

1. Kita harus sellalu memanggil hooks pada tole level pada function component.
2. Kita tidak dapat menggail hooks didalam perulangan
3. Kita tidak dapat memanggil hooks pada conditional statements
4. Atau pada nested function

### Usestate
Kita telah familiar dengan useState dimana telah ada pada catatan [state](#state).

!!! quote "Code"

    === "PropsAndState/LearnStateLearnReactHookUseStateBatching.js"

        ```{.js numlines="1" hl_lines="7-8 10-13 15-19 30-32"}
        import { Accordion,AccordionDetails,AccordionSummary,Typography, Button } from '@mui/material';
        import React, { useState, useEffect } from 'react';

        function RootAccordian(props){

            const [countSatu, setCountSatu] = useState(0)
            const [countDua, setCountDua] = useState(0)

            const countIncreament = () => {
                setCountSatu(countSatu + 1)
                setCountDua(countDua -1 )
            }

            // Called after every render
            useEffect(() => {
                console.log('Hello from useEffect')
                // Membuktikan bahwa useState menggunakan batching
            })
            
            return (
                <Accordion>
                <AccordionSummary
                aria-controls="panel1a-content"
                id="panel1a-header">
                <Typography><b>{props.title}</b></Typography>
                </AccordionSummary>
                <AccordionDetails>
                    
                    <Button variant="outlined" onClick={countIncreament} >
                        Change
                    </Button>

                    <Typography variant="subtitle1" gutterBottom>
                        {countSatu}
                    </Typography>
                    <Typography variant="subtitle1" gutterBottom>
                        {countDua}
                    </Typography>
                </AccordionDetails>
            </Accordion>
            )
        }

        export default RootAccordian
        ```

Component diatas, ketika kita meng-click button `Change` maka react akan melakukan render. {==Under the hood, react akan me-render ketika terjadi perubahan pada **state**==}


!!! info
    There is also a hook function called that is useReducer recommended to use when you have a complex state

Dimulai dari react versi 18, semua peribahan state akan di kumpulkan terlebih dahulu sebelum dirender, disebut dengan **bactched**. Jika kita tidak ingin batch updates pada kasus tertentu, kita dapat menggunakan pustaka `react-dom` API `#!js flushSync`.

!!! quote "Code"

    === "ropsAndState/LearnReactHookUseStateFlashSync.js"

        ```js
        const countIncreament = () => {

            flushSync( () => {
                setCountSatu(countSatu + 1) // Langsung dirender
            })
            setCountDua(countDua -1 ) // Render bersamaan dengan batch
        }
        ```

### useEfect
`useEffect` Hook function dapat digunakan untuk melakukan side-effects pada React Function component.

```js
useEffect(callback, [dependencies])
```

`callback` function terdiri dari side-effect logic dan `dependencies` adalah opsional array yang berisikan dependencies.

callback function pada `useEffect` akan terpanggil setiap render dilakukan. Sebagaimana yang telah kita lihat pada snipped code pada [Usestate](#Usestate) yang mana akan menampilkan pesan kedalam console log.

Pada kode tersebut, setiap terjadi perubahan pada state `countSatu` dan `countDua`. Namun jika argument kedua diisi dengan state tertentu, maka `useEffect` hanya akan berjalan jika kumpulan state pada argumen kedua berubah.

!!! quote "Code"

    === "ropsAndState/LearnReactHookUseStateFlashSync.js"

        ```js
        // Called every render and change state countSatu
        useEffect(() => {
            console.log('Render flashSync')
        },[countSatu])
        ```

        Jika argument opsional diisi dengan array kosong maka callback `useEffect` hanya akan jalan saat render pertama kali.

`useEffect function` juga dapat mengembalikan sebuah function yg mana function tersebut akan berjalan sebelum setiap effect berjalan.

!!! quote "Code"

    === "ropsAndState/LearnReactHookUseStateFlashSync.js"

        ```js
        // Called every render and change state countSatu
        useEffect(() => {
            console.log('Render flashSync')

            return () => {
                console.log("This will run berfore effect")
            }
        },[countSatu])
        ```

### useRef
Hook `useRef` mengamblikan mutable object yang dapat digunakan. Syntax inisiasi sebagai berikut

```js
const ref = useRef(initialValue)
```

Nilai kembalian ref memliki nilai _current property_ yang dinisiasi dengan nilai yg diberikan pada argument `initialValue`. Namun pada contoh setelah ini, saya tidak langsung menaruh initial valuenya, akan tetapi pertama kita berikan nilai `#!js null` lalu menggunakan JSX element ref property dan memberikan nilari ref tersebut ke useRef. Setelah itu maka input reff akan berisi Input Element dan kita gunakan untuk mengeksekusi focus function pada input tersebut.

!!! quote "Code"

    === "ropsAndState/LearnReactHookUseRef.js"

        ```js
        import React, {useRef} from "react"
        import { Accordion,AccordionDetails,AccordionSummary,Typography, Button, Input } from '@mui/material';

        function RootAccordian(props){

            const inputRef = useRef(null)

            const callBackuseRef = (e) => {
                console.log(inputRef.current)
                inputRef.current.focus()
            }
            
            return (
                <Accordion>
                <AccordionSummary
                aria-controls="panel1a-content"
                id="panel1a-header">
                <Typography><b>{props.title}</b></Typography>
                </AccordionSummary>
                <AccordionDetails>
                    
                    
                    <Button variant="outlined" onClick={callBackuseRef} >
                        Change
                    </Button>

                    <Input inputRef={inputRef} id="outlined-basic" label="Outlined" variant="outlined" />
                    
                </AccordionDetails>
            </Accordion>
            )
        }

        export default RootAccordian
        ```

!!! note
    Pada buku yg digunakan pada catatan ini menggunakan component `#!js <Input/>` dari React, sedangkan pada catatan ini menggunakan Materail UI _v.5.14.20_ (pada saat catatan ini dibuat). Maka dari itu ada perbedaan saat meng-assign `useRef`. Pada MUI menggunakan attribute `#!js inputRef` sendangkan pada buku menggunakan `#!js ref`.



## Context API
Membagi data menggunakan Props dapat sangat merepotkan jika komponen kita sangat dalam dan kompleks. Kita harus mengopar data melalui semua komponen hingga ke yg paling dalam. **Context API** datang sebagai penolong, dan fitur tersebut sangat dianjurkan untuk menggunakan data yang global dan dibutuhkan oleh banyak komponen, sebagai contoh adalah {==autentikasi dari user ==}

Context dibuat menggunakan method dan method tersebut membutuhkan satu argumen yang mendifinisikan nilai default-nya. Kita dapat membuat file terpisah khusus untuk context.

!!! quote "Code"

    === "PropsAndState/Contexts/AuthContext.js"

        ```js
        import React from "react"

        const AuthContext = React.createContext('')

        export { AuthContext }
        ```

Selanjutnya kita akan menggunakan context provider component untuk membuat context kita dapat diakses oleh component lain. Context provider component memiliki nilai `prop` yang akan dioper agar dapat dikonsumsi oleh component-component.

!!! quote "Code"

    === "PropsAndState/LearnUsingContextAPI.js"

        ```js
        import React, {useRef} from "react"
        import { Accordion,AccordionDetails,AccordionSummary,Typography, Button, Input } from '@mui/material'
        import { AuthContext } from "./Contexts/AuthContext"

        const myVariables = {nama:"Farras",skill:"Spring boot and react",hobby:"Hiking"}

        function RootAccordian(props){
            const myContext = React.useContext(AuthContext)

            return (
                <AuthContext.Provider value = {myVariables}>

                    <Accordion>
                        <AccordionSummary
                        aria-controls="panel1a-content"
                        id="panel1a-header">
                        <Typography><b>{props.title}</b></Typography>
                        </AccordionSummary>
                        <AccordionDetails>
                            
                            <ParentComponent/>

                        </AccordionDetails>
                    </Accordion>

                </AuthContext.Provider>
            )
        }

        // .. cutted, isinya adalah comonent <ParentComponent/> dan child-nya
        export default RootAccordian
        ```

Contoh diatas kita membungkus komponen `#!js <ParentComponent/>` didalam `#!js <AuthContext.Provider/>` menggunakan context provider component, sehingga object yang ditampung oleh `#!js myVariables` dapat diakses oleh semua komponen termasuk child dari component `#!js <ParentComponent/>`


Sekarag kita dapat mengakses nilai yang disediakan pada semua component anakan tersebut menggunakan syntax berikut. `#!js const namaContext = React.useContext(AuthContext);`


!!! quote "Code"

    === "PropsAndState/LearnUsingContextAPI.js"

        ```js
        // ... lanjutan
        function ParentComponent(){
            // We dont need any prop argument here
            // Need to get Context
            const myContext = React.useContext(AuthContext)
            return (
                <>
                    <Typography>
                        My name is {myContext.nama} (from parent)
                    </Typography>
                    <ChildComponent/>
                </>
            )
        }

        function ChildComponent(){
            // We dont need any prop argument here
            // Need to get Context
            const myContext = React.useContext(AuthContext)
            return (
                <>
                    <Typography>
                        My Skill {myContext.skill} (From child 1)
                    </Typography>
                    <ChildComponent2/>
                </>
            )
        }

        function ChildComponent2(){
            // We dont need any prop argument here
            // Need to get Context
            const myContext = React.useContext(AuthContext)
            return (
                <>
                    <Typography>
                        My Hobby {myContext.hobby} (From child 2)
                    </Typography>
                </>
            )
        }

        export default RootAccordian
        ```

## Handling list with react
JavaScript memiliki method `#!js map()` yang mana setara degan method pada java `#!java stream.map()` yang mana mengamblikan nilai baru atas efek dari function pada argumen map.

!!! note
    The best way to craete object

    ```js
    function createData(namaLengkap, namaPanggilan, tanggalLahir, umur){
        return {namaLengkap, namaPanggilan, tanggalLahir, umur}
    }
    ```

    Snipped kode diatas akan menghasilkan object dengan keu nama dari return value.


!!! quote "Code"

    === "HandlingList/HandlingListWithReact.js"

        ```js
        import React from "react"
        import { Accordion,AccordionDetails,AccordionSummary,Typography,
            TableContainer,Table, TableHead, TableRow, TableCell, Paper, TableBody } from '@mui/material'


        function createData(namaLengkap, namaPanggilan, tanggalLahir, umur){
            return {namaLengkap, namaPanggilan, tanggalLahir, umur}
        }

        const myFamilyData = [
            createData ("Muhammad Farras Ma'ruf","Farras","27 Desember 1995", 28),
            createData ("Tania Dwi Haryanti","Tania","11 Juli 1998", 25),
            createData ("Muhammad Faris Ma'ruf","Farras","05 Juli 2020", 3),
            createData ("Nu'man Noah Ma'ruf","Farras","13 Oktober 2021", 2),
            createData ("Rumaysha Hilyah Ma'ruf","Farras","12 Desember 2023", 0),
        ]

        function RootAccordian(props){
            
            return (
                <Accordion>
                    <AccordionSummary
                    aria-controls="panel1a-content"
                    id="panel1a-header">
                    <Typography><b>{props.title}</b></Typography>
                    </AccordionSummary>
                    <AccordionDetails>
                        <CustomizedTables/>
                    </AccordionDetails>
                </Accordion>
            )
        }

        function CustomizedTables() {   
            return (
                <TableContainer component={Paper}>
                    <Table sx={{ minWidth: 700 }} aria-label="customized table">
                        <TableHead>
                            <TableRow>
                                <TableCell>Nama Lengkap</TableCell>
                                <TableCell align="left">Nama Panggilan</TableCell>
                                <TableCell align="left">Tanggal Lahir</TableCell>
                                <TableCell align="left">Umur</TableCell>
                            </TableRow>
                        </TableHead>
                        <TableBody>
                        {myFamilyData.map((row,index) => (
                            <TableRow key={index}>
                                <TableCell component="th" scope="row">
                                    {row.namaLengkap}
                                </TableCell>
                                <TableCell align="left">{row.namaPanggilan}</TableCell>
                                <TableCell align="left">{row.tanggalLahir}</TableCell>
                                <TableCell align="left">{row.umur}</TableCell>
                            </TableRow>
                        ))}
                        </TableBody>
                    </Table>
                </TableContainer>
            );
        }

        export default RootAccordian
        ```

## Handling Event React
Event handling di React mirip dengan handlin DOM element events. Bedanya dengan HTML handling adalah event naming menggunakan camlecase pada react.

!!! quote "Code"

    === "HandlingEventWithReact/LearnHandlingEvent.js"

        ```js
        import React, {useState} from "react"
        import { Accordion,AccordionDetails,AccordionSummary,Typography, Snackbar,Button } from '@mui/material';

        function RootAccordian(props){

            const [openSb, setOpenSb] = useState(false)

            const toastDisplay = (event) => {

                // Event prevent default
                event.preventDefault()

                // Rubah state
                setOpenSb (true)
            }

            const handleClose = (event, reason) => {

                console.log("Ints handel close, must set open sb to false")
                setOpenSb(false);
            };
            
            return (
                <Accordion>
                <AccordionSummary
                aria-controls="panel1a-content"
                id="panel1a-header">
                <Typography><b>{props.title}</b></Typography>
                </AccordionSummary>
                <AccordionDetails>
                    
                    
                    <Button variant="outlined" onClick={toastDisplay} >
                        Change
                    </Button>

                    <Snackbar
                        open={openSb}
                        autoHideDuration={6000}
                        onClose={handleClose}
                        message="Toast here"
                    />
                </AccordionDetails>
            </Accordion>
            )
        }

        export default RootAccordian
        ```

## Handling React Form

!!! quote "Code"

    === "HandlingFormWithReact/LearnHandlingForm.js"

        ```js
        import React, {useState} from "react"
        import { Accordion,AccordionDetails,AccordionSummary,Typography, Snackbar,Button,
            TableContainer,Table, TableHead, TableRow, TableCell, Paper, TableBody,FormControl,TextField, Box, Stack, Grid  } from '@mui/material';



        // Fucntion to create data
        function createData(namaLengkap, namaPanggilan, tanggalLahir, umur){
            return {namaLengkap, namaPanggilan, tanggalLahir, umur}
        }

        function RootAccordian(props){ 
            
            // State menampung array data
            const [myFamilyData, setMyFamilyData]= useState([])

            // State untuk menampilkan SnackBar
            const [openSb, setOpenSb] = useState(false)

            // State untuk menamping inputan user
            const [user,setUser] = useState({
                namaLengkap : '',
                namaPanggilan : '',
                tanggalLahir : '',
                umur : ''
            })


            // Function to handle changeson input user
            const inputChange = (event) => {
                setUser({...user,[event.target.name]:event.target.value})
            }

            // Function to handle submit event
            const handleSubmit = (event) => {

                // Event prevent default
                event.preventDefault()

                // Push myFamily data
                myFamilyData.push(createData(user.namaLengkap,user.namaPanggilan,user.tanggalLahir,user.umur))
                
                // set to reder
                setMyFamilyData (myFamilyData)

                // Clearn input
                setUser(createData('','','',''))
                console.log(user)

                // Rubah state
                setOpenSb (true)
            }

            // State to handle close SB
            const handleClose = (event, reason) => {
                setOpenSb(false);
            };
            
            return (
                <Accordion>
                <AccordionSummary
                aria-controls="panel1a-content"
                id="panel1a-header">
                <Typography><b>{props.title}</b></Typography>
                </AccordionSummary>
                <AccordionDetails>
                    
                    <Box
                    component="form"
                    onSubmit={handleSubmit}
                    sx={{
                        display: 'flex',
                        alignItems: 'center',
                        '& > :not(style)': { m: 1 },
                    }}>

                        <TextField
                            onChange={inputChange}
                            value={user.namaLengkap} // to store value from state
                            name="namaLengkap"
                            id="outlined-multiline-flexible"
                            label="Nama Lengkap"
                            />
                        <TextField
                            onChange={inputChange}
                            value={user.namaPanggilanp} // to store value from state
                            name="namaPanggilan"
                            id="outlined-multiline-flexible"
                            label="Nama Panggilan"
                            />
                        <TextField
                            onChange={inputChange}
                            value={user.tanggalLahir} // to store value from state
                            name="tanggalLahir"
                            id="outlined-multiline-flexible"
                            label="Tanggal Lahir"
                            />
                        <TextField
                        name="umur"
                            value={user.umur} // to store value from state
                            onChange={inputChange}
                            id="outlined-multiline-flexible"
                            label="Umur"
                        />



                        <Button type="submit"  variant="outlined">
                        Change
                        </Button>

                    </Box>

                    <TableContainer component={Paper}>
                    <Table sx={{ minWidth: 700 }} aria-label="customized table">
                        <TableHead>
                            <TableRow>
                                <TableCell>Nama Lengkap</TableCell>
                                <TableCell align="left">Nama Panggilan</TableCell>
                                <TableCell align="left">Tanggal Lahir</TableCell>
                                <TableCell align="left">Umur</TableCell>
                            </TableRow>
                        </TableHead>
                        <TableBody>
                        {myFamilyData.map((row,index) => (
                            <TableRow key={index}>
                                <TableCell component="th" scope="row">
                                    {row.namaLengkap}
                                </TableCell>
                                <TableCell align="left">{row.namaPanggilan}</TableCell>
                                <TableCell align="left">{row.tanggalLahir}</TableCell>
                                <TableCell align="left">{row.umur}</TableCell>
                            </TableRow>
                        ))}
                        </TableBody>
                    </Table>
                </TableContainer>



                    

                    <Snackbar
                        open={openSb}
                        autoHideDuration={6000}
                        onClose={handleClose}
                        message="The data added"
                    />
                </AccordionDetails>
            </Accordion>
            )
        }

        export default RootAccordian
        ```

## Callback Handlers in JSX

!!! info
    **The Road to React** hal 61

![call back handlers](./aset/Call%20back%20handlrs.png)

Informasi hanya dapat dikirim dari komponen tertinggi ke komponen bawahnya menggunakan prop. Namun menggunakan state dan call back handlers kita dapat membuat component atas dan bawah saling berkomunikasi bertukar informasi via prop.

!!! quote "Code"

    === "ComunicateChildToParent/AppTest.js"

        ```js
        import { useState } from "react"

        function AppTest() {

            const propDate = (event) => {
                console.log("this is in parent")
                if (event != undefined){
                    console.log(event.target.value)
                    setValueFromChild (event.target.value)
                }
                return "kosong"
                
            }

            const [valueFromChild, setValueFromChild] = useState (propDate())

            return (
                <>
                    <h1>Judul</h1>
                    <p>Search for (Parent Component): {valueFromChild}</p>
                    <Search data={propDate}/>

                    
                </>
            )
                
        }

        const Search = (prop) => {
            console.log('Ini dari anakan '+prop.data())

            const [searchText, setSearchText] = useState('')

            const changeEvent = (event) => {

                setSearchText(event.target.value)

                prop.data(event)
            }

            return (
                <>
                    <label>Search</label>
                    <input type="text" id="input" onChange={changeEvent} value={searchText}></input>
                    <p>Search for (Child Component): {searchText}</p>
                    <hr></hr>
                </>
            )
        }
        export default AppTest
        ```

Kode diatas menggunakan prop dan usestate sebagai cara berkomunukasi ke atas dari child ke parent component.

![data](./aset/using%20call%20back%20handlers.png)

