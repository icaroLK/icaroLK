


function openMenu(){
    var $nav = document.querySelector('nav');
    var $elements = document.querySelectorAll('nav ul li');
    var $head = document.querySelector('header');
    
    $elements.forEach(function(element) {
        element.classList.toggle('texto');
    });

    $nav.classList.toggle('show');
    
    
}


function dark_light(){
    document.body.classList.toggle("dark_light");
}