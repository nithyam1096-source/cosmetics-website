document.addEventListener('DOMContentLoaded', function() {
    AOS.init({
        duration: 1000,
        once: true,
        offset: 100,
    });

    const heroSwiper = document.querySelector('.hero-swiper');
    if (heroSwiper) {
        new Swiper(heroSwiper, {
            loop: true,
            speed: 800,
            autoplay: {
                delay: 4000,
                disableOnInteraction: false,
                pauseOnMouseEnter: true,
            },
            effect: 'fade',
            fadeEffect: {
                crossFade: true
            },
            navigation: {
                nextEl: '.hero-next',
                prevEl: '.hero-prev',
            },
            pagination: {
                el: '.hero-pagination',
                clickable: true,
                dynamicBullets: true,
            },
        });
    }

    const mobileMenuBtn = document.getElementById('mobileMenuBtn');
    const mobileNav = document.getElementById('mobileNav');
    const closeMobileNav = document.getElementById('closeMobileNav');

    if (mobileMenuBtn && mobileNav) {
        mobileMenuBtn.addEventListener('click', function() {
            mobileNav.classList.add('active');
        });
    }

    if (closeMobileNav && mobileNav) {
        closeMobileNav.addEventListener('click', function() {
            mobileNav.classList.remove('active');
        });
    }

    document.addEventListener('click', function(e) {
        if (mobileNav && mobileNav.classList.contains('active') && 
            !mobileNav.contains(e.target) && 
            e.target !== mobileMenuBtn) {
            mobileNav.classList.remove('active');
        }
    });

    const wishlistBtns = document.querySelectorAll('.wishlist-btn, .btn-wishlist');
    wishlistBtns.forEach(function(btn) {
        btn.addEventListener('click', function() {
            const icon = this.querySelector('i') || this;
            icon.classList.toggle('far');
            icon.classList.toggle('fas');
            icon.classList.toggle('text-danger');
        });
    });

    const cartBtns = document.querySelectorAll('.cart-btn, .btn-add-cart');
    cartBtns.forEach(function(btn) {
        btn.addEventListener('click', function() {
            const badge = document.querySelector('.badge-count');
            if (badge) {
                let count = parseInt(badge.textContent);
                badge.textContent = count + 1;
            }
        });
    });

    const luxurySection = document.getElementById('luxuryAbout');
    if (luxurySection) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('in-view');
                }
            });
        }, {
            threshold: 0.2
        });
        observer.observe(luxurySection);
    }

    const luxuryImages = document.querySelectorAll('.luxury-image-wrapper');
    luxuryImages.forEach(img => {
        img.addEventListener('mouseenter', function() {
            this.style.zIndex = '5';
        });
        img.addEventListener('mouseleave', function() {
            this.style.zIndex = '1';
        });
    });

    const fadeElements = document.querySelectorAll('.fade-in-section');
    if (fadeElements.length) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    observer.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.15,
            rootMargin: '0px 0px -50px 0px',
        });
        fadeElements.forEach((el, i) => {
            el.style.setProperty('--card-index', i);
            observer.observe(el);
        });
    }

    const shopTrigger = document.querySelector('.shop-trigger');
    const navDropdown = document.querySelector('.nav-dropdown');
    if (shopTrigger && navDropdown) {
        shopTrigger.addEventListener('click', function(e) {
            e.preventDefault();
            navDropdown.classList.toggle('open');
        });
        document.addEventListener('click', function(e) {
            if (!navDropdown.contains(e.target)) {
                navDropdown.classList.remove('open');
            }
        });
    }

    const addToCartBtns = document.querySelectorAll('.add-to-cart-btn[data-key]');
    addToCartBtns.forEach(function(btn) {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            var key = this.getAttribute('data-key');
            var originalHtml = this.innerHTML;
            this.disabled = true;
            this.innerHTML = '<i class="fas fa-spinner fa-spin"></i> <span>Adding...</span>';
            fetch('/add-to-cart/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCsrfToken(),
                },
                body: JSON.stringify({key: key, qty: 1}),
            })
            .then(function(r) { return r.json(); })
            .then(function(d) {
                if (d.success) {
                    var badge = document.querySelector('.cart-badge');
                    if (badge) badge.textContent = d.item_count;
                    btn.innerHTML = '<i class="fas fa-check"></i> <span>Added!</span>';
                    btn.classList.add('added');
                    setTimeout(function() {
                        btn.innerHTML = originalHtml;
                        btn.disabled = false;
                        btn.classList.remove('added');
                    }, 2000);
                } else {
                    btn.innerHTML = originalHtml;
                    btn.disabled = false;
                }
            })
            .catch(function() {
                btn.innerHTML = originalHtml;
                btn.disabled = false;
            });
        });
    });

    function getCsrfToken() {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var c = cookies[i].trim();
            if (c.indexOf('csrftoken=') === 0) return c.substring(10);
        }
        return '';
    }
});
