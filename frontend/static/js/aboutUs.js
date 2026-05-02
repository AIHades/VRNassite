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


// FAQ
const questionElement = document.querySelectorAll('.aboutUs-FAQ__question')
const itemElement = document.querySelectorAll('.aboutUs-FAQ__item')

questionElement.forEach((question) => {
    question.addEventListener('click', function() {
        const item = this.closest('.aboutUs-FAQ__item');
        const isActive = item.classList.contains('active');

        itemElement.forEach((el) => {
            el.classList.remove('active');
        });

        if (!isActive) {
            item.classList.add('active');
        }
    });
});

