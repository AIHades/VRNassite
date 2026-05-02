// Изменение header при прокрутку
document.addEventListener('DOMContentLoaded', () => {
    const header = document.querySelector('.header');
    
    const scroll = () => {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    }

    window.addEventListener('scroll', scroll);
});

// drop-down lists
const questionElement = document.querySelectorAll('.main-whyChooseUs__question')
const itemElement = document.querySelectorAll('.main-whyChooseUs__item')

questionElement.forEach(function(question) {
    question.addEventListener('click', function() {
        const item = this.closest('.main-whyChooseUs__item');
        const isActive = item.classList.contains('active');

        itemElement.forEach(function(el) {
            el.classList.remove('active');
        });

        if (!isActive) {
            item.classList.add('active');
        }
    });
});