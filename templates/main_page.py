html_main_page = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Вход</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #f7f7f8;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 24px;
        }

        .container {
            background: #ffffff;
            padding: 48px 56px;
            width: 100%;
            max-width: 400px;
            border-radius: 8px;
            box-shadow: 0 1px 4px rgba(0,0,0,0.06);
        }

        .logo {
            text-align: center;
            font-size: 32px;
            margin-bottom: 4px;
        }

        h1 {
            text-align: center;
            font-size: 22px;
            font-weight: 600;
            color: #1a1a1a;
            margin-bottom: 28px;
            letter-spacing: -0.3px;
        }

        .status {
            text-align: center;
            font-size: 13px;
            color: #757575;
            padding: 8px 0;
            margin-bottom: 20px;
            border-top: 1px solid #eaeaea;
            border-bottom: 1px solid #eaeaea;
        }

        .status.logged-in {
            color: #2e7d32;
            border-color: #a5d6a7;
        }

        .tabs {
            display: flex;
            gap: 0;
            margin-bottom: 28px;
            border-bottom: 1px solid #e0e0e0;
        }

        .tabs button {
            flex: 1;
            padding: 12px 0;
            background: none;
            border: none;
            font-size: 15px;
            font-weight: 500;
            cursor: pointer;
            color: #757575;
            transition: all 0.2s;
            border-bottom: 2px solid transparent;
        }

        .tabs button.active {
            color: #1a1a1a;
            border-bottom-color: #1a1a1a;
        }

        .tabs button:hover:not(.active) {
            color: #1a1a1a;
        }

        .form {
            display: none;
        }

        .form.active {
            display: block;
        }

        .form-group {
            margin-bottom: 20px;
        }

        label {
            display: block;
            font-size: 14px;
            font-weight: 500;
            color: #333;
            margin-bottom: 6px;
        }

        input {
            width: 100%;
            padding: 12px 16px;
            border: 1px solid #d0d0d0;
            border-radius: 4px;
            font-size: 15px;
            transition: border 0.2s;
            background: #fafafa;
        }

        input:focus {
            outline: none;
            border-color: #1a1a1a;
            background: #ffffff;
        }

        .btn-submit {
            width: 100%;
            padding: 14px;
            background: #1a1a1a;
            color: #ffffff;
            border: none;
            border-radius: 4px;
            font-size: 15px;
            font-weight: 500;
            cursor: pointer;
            transition: background 0.2s;
            margin-top: 8px;
        }

        .btn-submit:hover {
            background: #000000;
        }

        .btn-submit:disabled {
            opacity: 0.5;
            cursor: not-allowed;
        }

        .message {
            margin-top: 20px;
            padding: 12px 16px;
            border-radius: 4px;
            display: none;
            font-size: 14px;
            line-height: 1.5;
        }

        .message.success {
            display: block;
            background: #e8f5e9;
            color: #2e7d32;
            border-left: 3px solid #2e7d32;
        }

        .message.error {
            display: block;
            background: #fbe9e7;
            color: #c62828;
            border-left: 3px solid #c62828;
        }

        .message.info {
            display: block;
            background: #f0f0f0;
            color: #555;
            border-left: 3px solid #999;
        }

        .loading {
            display: inline-block;
            width: 18px;
            height: 18px;
            border: 2px solid #ffffff;
            border-radius: 50%;
            border-top-color: transparent;
            animation: spin 0.6s linear infinite;
            margin-right: 8px;
            vertical-align: middle;
        }

        @keyframes spin {
            to { transform: rotate(360deg); }
        }

        .hidden {
            display: none !important;
        }

        @media (max-width: 480px) {
            .container {
                padding: 32px 24px;
            }

            h1 {
                font-size: 20px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo">◆</div>
        <h1>Вход</h1>

        <div id="authStatus" class="status">● не авторизован</div>

        <div class="tabs" id="tabsContainer">
            <button class="active" onclick="switchTab('login')">Вход</button>
            <button onclick="switchTab('register')">Регистрация</button>
        </div>

        <!-- Форма входа -->
        <div id="loginForm" class="form active">
            <form onsubmit="handleLogin(event)">
                <div class="form-group">
                    <label>Email</label>
                    <input type="email" id="loginEmail" placeholder="email@example.com">
                </div>
                <div class="form-group">
                    <label>Пароль</label>
                    <input type="password" id="loginPassword" placeholder="••••••••">
                </div>
                <button type="submit" class="btn-submit" id="loginBtn">Войти</button>
            </form>
        </div>

        <!-- Форма регистрации -->
        <div id="registerForm" class="form">
            <form onsubmit="handleRegister(event)">
                <div class="form-group">
                    <label>Имя пользователя</label>
                    <input type="text" id="regUsername" placeholder="username">
                </div>
                <div class="form-group">
                    <label>Email</label>
                    <input type="email" id="regEmail" placeholder="email@example.com">
                </div>
                <div class="form-group">
                    <label>Пароль</label>
                    <input type="password" id="regPassword" placeholder="••••••••">
                </div>
                <div class="form-group">
                    <label>Подтверждение</label>
                    <input type="password" id="regConfirmPassword" placeholder="••••••••">
                </div>
                <button type="submit" class="btn-submit" id="registerBtn">Создать аккаунт</button>
            </form>
        </div>

        <div id="message" class="message"></div>
    </div>

    <script>
        const API_URL = window.location.origin;
        const STORAGE_KEYS = {
            ACCESS_TOKEN: 'access_token',
            REFRESH_TOKEN: 'refresh_token',
            USER_EMAIL: 'user_email'
        };

        function saveTokens(accessToken, refreshToken, email) {
            if (accessToken) localStorage.setItem(STORAGE_KEYS.ACCESS_TOKEN, accessToken);
            if (refreshToken) localStorage.setItem(STORAGE_KEYS.REFRESH_TOKEN, refreshToken);
            if (email) localStorage.setItem(STORAGE_KEYS.USER_EMAIL, email);
            window.location.href = '/page/posts/html';
        }

        function isAuthenticated() {
            return !!localStorage.getItem(STORAGE_KEYS.ACCESS_TOKEN);
        }

        function updateUI() {
            const status = document.getElementById('authStatus');
            const tabs = document.getElementById('tabsContainer');
            const loginForm = document.getElementById('loginForm');
            const registerForm = document.getElementById('registerForm');

            if (isAuthenticated()) {
                status.className = 'status logged-in';
                status.textContent = '● уже авторизован';
                tabs.style.display = 'none';
                loginForm.classList.remove('active');
                registerForm.classList.remove('active');
                setTimeout(() => {
                    window.location.href = '/page/posts/html';
                }, 1000);
            } else {
                status.className = 'status';
                status.textContent = '● не авторизован';
                tabs.style.display = 'flex';
                loginForm.classList.add('active');
                registerForm.classList.remove('active');
                document.querySelectorAll('.tabs button').forEach(b => b.classList.remove('active'));
                document.querySelector('.tabs button:first-child').classList.add('active');
            }
        }

        function switchTab(tab) {
            if (isAuthenticated()) return;

            const loginForm = document.getElementById('loginForm');
            const registerForm = document.getElementById('registerForm');
            const tabs = document.querySelectorAll('.tabs button');

            if (tab === 'login') {
                loginForm.classList.add('active');
                registerForm.classList.remove('active');
                tabs[0].classList.add('active');
                tabs[1].classList.remove('active');
            } else {
                registerForm.classList.add('active');
                loginForm.classList.remove('active');
                tabs[1].classList.add('active');
                tabs[0].classList.remove('active');
            }
            hideMessage();
        }

        function showMessage(text, type = 'info') {
            const msg = document.getElementById('message');
            msg.textContent = text;
            msg.className = `message ${type}`;
            clearTimeout(window.messageTimeout);
            window.messageTimeout = setTimeout(hideMessage, 5000);
        }

        function hideMessage() {
            const msg = document.getElementById('message');
            msg.className = 'message';
            msg.textContent = '';
        }

        function setLoading(buttonId, loading) {
            const btn = document.getElementById(buttonId);
            if (loading) {
                btn.disabled = true;
                btn.innerHTML = '<span class="loading"></span> Загрузка...';
            } else {
                btn.disabled = false;
                btn.textContent = btn.id === 'loginBtn' ? 'Войти' : 'Создать аккаунт';
            }
        }

        async function handleLogin(e) {
            e.preventDefault();
            if (isAuthenticated()) return;

            hideMessage();

            const email = document.getElementById('loginEmail').value.trim();
            const password = document.getElementById('loginPassword').value;

            if (!email || !password) {
                showMessage('Заполните все поля', 'error');
                return;
            }

            setLoading('loginBtn', true);

            try {
                const response = await fetch(`${API_URL}/auth/tokens/`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ email, password })
                });

                if (response.ok) {
                    const data = await response.json();
                    saveTokens(data.access_token, data.refresh_token, email);
                } else {
                    const error = await response.json();
                    showMessage(error.detail || 'Ошибка входа', 'error');
                    setLoading('loginBtn', false);
                }
            } catch (err) {
                showMessage('Ошибка соединения с сервером', 'error');
                setLoading('loginBtn', false);
            }
        }

        async function handleRegister(e) {
            e.preventDefault();
            if (isAuthenticated()) return;

            hideMessage();

            const username = document.getElementById('regUsername').value.trim();
            const email = document.getElementById('regEmail').value.trim();
            const password = document.getElementById('regPassword').value;
            const confirmPassword = document.getElementById('regConfirmPassword').value;

            if (!username || !email || !password || !confirmPassword) {
                showMessage('Заполните все поля', 'error');
                return;
            }

            if (password !== confirmPassword) {
                showMessage('Пароли не совпадают', 'error');
                return;
            }

            setLoading('registerBtn', true);

            try {
                const response = await fetch(`${API_URL}/auth/register/`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ 
                        username: username,
                        email: email, 
                        password: password, 
                        confirm_password: confirmPassword 
                    })
                });

                if (response.ok) {
                    const data = await response.json();
                    showMessage('✅ Аккаунт создан! Вход...', 'success');
                    setTimeout(() => {
                        saveTokens(data.access_token, data.refresh_token, email);
                    }, 1000);
                } else {
                    const error = await response.json();
                    let msg = error.detail || 'Ошибка регистрации';
                    if (Array.isArray(error.detail)) {
                        msg = error.detail.map(e => e.msg).join(', ');
                    }
                    showMessage(msg, 'error');
                    setLoading('registerBtn', false);
                }
            } catch (err) {
                showMessage('Ошибка соединения с сервером', 'error');
                setLoading('registerBtn', false);
            }
        }

        document.addEventListener('DOMContentLoaded', () => {
            if (isAuthenticated()) {
                window.location.href = '/page/posts/html';
                return;
            }
            updateUI();
        });
    </script>
</body>
</html>"""
