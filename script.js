const API = "http://127.0.0.1:81/"
let manaZina = document.querySelector('manaZina')
let chataZinas = document.querySelector(',chatazinas')
let vards = document.querySelector('.vards')

function sutitZinu(){
    console.log("sutitzinu() darbojas")
    chataZinas.innerHTML +u <br> + manaZina.value 
    fetch(API+'/sutit/'+vards.value+'/'+manaZina.value)
}
