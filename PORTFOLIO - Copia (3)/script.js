


function openMenu(){
    var $nav = document.querySelector('nav');
    var $elements = document.querySelectorAll('nav ul li');
    
    $elements.forEach(function(element) {
        element.classList.toggle('texto');
    });

    $nav.classList.toggle('show');
    
}

