document.addEventListener('DOMContentLoaded', function () {
    const togglePassword = document.getElementById('togglePassword');
    const passwordInput = document.getElementById('password');
    const eyeIcon = document.getElementById('eyeIcon');

    togglePassword.addEventListener('click', function () {
        const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
        passwordInput.setAttribute('type', type);
        eyeIcon.classList.toggle('fa-eye');
        eyeIcon.classList.toggle('fa-eye-slash');
    });

    const loginForm = document.getElementById('loginForm');
    const emailInput = document.getElementById('email');
    const emailError = document.getElementById('emailError');
    const passwordError = document.getElementById('passwordError');

    loginForm.addEventListener('submit', function (e) {
        e.preventDefault();

        let isValid = true;

        emailInput.classList.remove('error');
        emailError.classList.remove('visible');
        passwordInput.classList.remove('error');
        passwordError.classList.remove('visible');

        const email = emailInput.value.trim();
        const password = passwordInput.value.trim();

        if (!email || !isValidEmail(email)) {
            emailInput.classList.add('error');
            emailError.classList.add('visible');
            isValid = false;
        }

        if (!password) {
            passwordInput.classList.add('error');
            passwordError.classList.add('visible');
            isValid = false;
        }

        if (isValid) {
            const btn = document.getElementById('loginBtn');
            btn.innerHTML = '<span>Logging in...</span> <i class="fas fa-spinner fa-spin"></i>';
            btn.disabled = true;
            setTimeout(function () {
                btn.innerHTML = '<span>Login</span> <i class="fas fa-arrow-right"></i>';
                btn.disabled = false;
            }, 2000);
        }
    });

    function isValidEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }

    emailInput.addEventListener('input', function () {
        if (emailInput.classList.contains('error')) {
            emailInput.classList.remove('error');
            emailError.classList.remove('visible');
        }
    });

    passwordInput.addEventListener('input', function () {
        if (passwordInput.classList.contains('error')) {
            passwordInput.classList.remove('error');
            passwordError.classList.remove('visible');
        }
    });
});