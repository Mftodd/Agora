

// welcome
let getWallet = document.querySelector("#get-wallet")


getWallet.addEventListener("click", function() {
    ethereum.request({ method: 'eth_requestAccounts' });
})

let slideshow = document.querySelector('#slideshow')
let slides = slideshow.getElementsByTagName('li')


// featured items carousel

let slideIndex=1;
showSlides(slideIndex);


function changeSlide(n) {
    showSlides(slideIndex += n)
}

function currentSlide(n) {
    showSlides(slideIndex = n)
}

function showSlides(n) {

    if(n > slides.length) {slideIndex=1}
    if(n < 1) {slideIndex = slides.length}

    for (let i = 0; i < slides.length; i++){
        slides[i].style.display='none';
    }
    
    slides[slideIndex-1].style.display='block';
};
