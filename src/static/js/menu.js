const menu=document.querySelector('#menu');
const desplegable=document.querySelector('#desplegable');

menu.addEventListener('mouseenter',function(){
    desplegable.classList.remove('oculto');
});

menu.addEventListener('mouseleave',function(){
    setTimeout(function() {
        desplegable.setAttribute('class','oculto');
        }
      , 10000);

});