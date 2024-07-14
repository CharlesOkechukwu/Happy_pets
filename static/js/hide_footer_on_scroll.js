let lastScrollTop = 0;
const footer = document.getElementById('footer');

window.addEventListener('scroll', () => {
    let scrollTop = document.documentElement.scrollTop;
    if (scrollTop > lastScrollTop) {
        // Scroll Down
        footer.style.transform = 'translateY(100%)';
    } else {
        // Scroll Up
        footer.style.transform = 'translateY(0)';
    }
    lastScrollTop = scrollTop;
});