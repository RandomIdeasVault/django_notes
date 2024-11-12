
const menuBtn = document.querySelector('.menu-btn');
const menu = document.querySelector('.menu');
const menuRight = document.querySelector('.menu-right');
const menuLeft = document.querySelector('.menu-left');
const rightItems = document.querySelectorAll('.menu-right .nav-item');
const leftItems = document.querySelectorAll('.menu-left .nav-item');

let showMenu = false;

menuBtn.addEventListener('click', toggleMenu)

function toggleMenu() {
    if (!showMenu) {
        menuBtn.classList.add('close')
        menu.classList.add('show')
        menuRight.classList.add('show')
        menuLeft.classList.add('show')
        rightItems.forEach(item => item.classList.add('show'));
        leftItems.forEach(item => item.classList.add('show'));

        showMenu = true;
    } else {
        menuBtn.classList.remove('close')
        menu.classList.remove('show')
        menuRight.classList.remove('show')
        menuLeft.classList.remove('show')
        rightItems.forEach(item => item.classList.remove('show'));
        leftItems.forEach(item => item.classList.remove('show'));

        showMenu = false;
    }
}
