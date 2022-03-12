//footer//
const createFooter = () => {
    let footer = document.querySelectorAll('footer');
    footer.innerHTML='';
    
}
createFooter();

//product//
const productImages = document.querySelectorAll(".product-images img");
const productImageSlide = document.querySelector(".image-slider");
let activeImageSlide = 0;
productImages.forEach((item, i) => {
    item.addEventListener('click', () =>{
        productImages[activeImageSlide].classList.remove('active');
        item.classList.add('active');
        productImageSlide.getElementsByClassName.backgroundImage = "url(${item.src})";
        activeImageSlide = i;
    })
})
//toggle size buttons
const sizeBtns = document.querySelectorAll('.size-radio-btn');
let checkedBtn = 0;
sizeBtns.forEach((item, i) => {
item.addEventListener('click',() => {
sizeBtns[checkedBtn].classList.remove('check');
item.classList.add('check');
checkedBtn = i;
})
})

//signip form 
const loader = document.querySelector('.loader');
//select inputs
const submitBtn = document.querySelector('.submit-btn');
const name = document.querySelector('#name');
const email = document.querySelector('#email');
const password = document.querySelector('#password');
const number = document.querySelector('#number');
const tac = document.querySelector('#terms-and-cond');
const notification= document.querySelector("#notification");

submitBtn.addEventListener('click', () =>{
    if(Name.value.lenght < 3){
        showAlert('name must be 3 letters long ')
    } else if(!email.value.length){
        showAlert('enter your email');
    } else if(password.value.length < 8){
        showAlert('password should be 8 letters long');
    } else if(!number.value.length){
        showAlert('enter your phone number');
    } else if (!Number(number.value) || number.value.lenght < 10){
        showAlert('invalid number, please enter valid one');
    } else if(!tac.checked){
        showAlert('you must agree to our terms and condition');
    } else{
        //submit form
        loader.style.display='block';
    }
})

//alert function
const showAlert = (msg) => {
    let alertBox = document.querySelector('.alert-box');
    let alertMsg = document.querySelector('.alert-msg');
    alertMsg.innerHTML = msg;
    alertBox.classList.add('show');
    setTimeout(() => {
        alertBox.classList.remove('show');
    }, 3000);
}