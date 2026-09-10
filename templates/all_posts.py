posts_html = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Посты</title>
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
            padding: 32px 24px;
            color: #1a1a1a;
        }

        .container {
            max-width: 780px;
            margin: 0 auto;
        }

        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 16px 0;
            margin-bottom: 32px;
            border-bottom: 1px solid #eaeaea;
        }

        .header-left {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .header-left .logo {
            font-size: 20px;
            font-weight: 600;
            color: #1a1a1a;
            text-decoration: none;
            letter-spacing: -0.3px;
        }

        .header-left .logo span {
            color: #999;
        }

        .header-actions {
            display: flex;
            gap: 8px;
            align-items: center;
            flex-wrap: wrap;
        }

        .btn {
            padding: 6px 14px;
            background: none;
            border: 1px solid #d0d0d0;
            border-radius: 4px;
            font-size: 13px;
            cursor: pointer;
            transition: all 0.2s;
            color: #555;
            text-decoration: none;
            display: inline-block;
            font-weight: 450;
        }

        .btn:hover {
            border-color: #1a1a1a;
            color: #1a1a1a;
            background: #fafafa;
        }

        .btn-primary {
            background: #1a1a1a;
            color: #ffffff;
            border-color: #1a1a1a;
        }

        .btn-primary:hover {
            background: #000000;
            border-color: #000000;
            color: #ffffff;
        }

        .btn-danger {
            color: #c62828;
            border-color: #d0d0d0;
        }

        .btn-danger:hover {
            border-color: #c62828;
            color: #c62828;
        }

        .user-badge {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 13px;
            color: #757575;
            padding: 4px 12px;
            background: #f0f0f0;
            border-radius: 16px;
        }

        .user-badge .dot {
            width: 6px;
            height: 6px;
            border-radius: 50%;
            background: #4caf50;
            display: inline-block;
        }

        .user-badge .dot.offline {
            background: #bdbdbd;
        }

        .posts-list {
            display: flex;
            flex-direction: column;
            gap: 16px;
        }

        .post-card {
            background: #ffffff;
            padding: 24px 28px;
            border-radius: 8px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.04);
            transition: all 0.2s;
            cursor: pointer;
            border: 1px solid transparent;
        }

        .post-card:hover {
            box-shadow: 0 4px 12px rgba(0,0,0,0.06);
            border-color: #eaeaea;
            transform: translateY(-1px);
        }

        .post-card.no-id {
            cursor: default;
            opacity: 0.7;
        }

        .post-title {
            font-size: 18px;
            font-weight: 600;
            color: #1a1a1a;
            margin-bottom: 6px;
        }

        .post-author {
            font-size: 14px;
            color: #757575;
        }

        .post-author strong {
            color: #333;
        }

        .post-meta {
            display: flex;
            gap: 16px;
            margin-top: 8px;
            font-size: 13px;
            color: #999;
        }

        .post-meta span {
            display: flex;
            align-items: center;
            gap: 4px;
        }

        .empty-state {
            text-align: center;
            padding: 80px 20px;
            background: #ffffff;
            border-radius: 8px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.04);
        }

        .empty-state .icon {
            font-size: 48px;
            margin-bottom: 16px;
        }

        .empty-state h3 {
            font-size: 18px;
            color: #1a1a1a;
            margin-bottom: 8px;
        }

        .empty-state p {
            color: #757575;
            font-size: 14px;
        }

        .loading-state {
            text-align: center;
            padding: 80px 20px;
            color: #999;
            font-size: 14px;
        }

        .loading-state .spinner {
            display: inline-block;
            width: 28px;
            height: 28px;
            border: 2px solid #e0e0e0;
            border-radius: 50%;
            border-top-color: #1a1a1a;
            animation: spin 0.8s linear infinite;
            margin-bottom: 16px;
        }

        @keyframes spin {
            to { transform: rotate(360deg); }
        }

        .message {
            padding: 14px 20px;
            border-radius: 4px;
            font-size: 14px;
            line-height: 1.5;
            margin-bottom: 20px;
            display: none;
        }

        .message.error {
            display: block;
            background: #fbe9e7;
            color: #c62828;
            border-left: 3px solid #c62828;
        }

        .message.success {
            display: block;
            background: #e8f5e9;
            color: #2e7d32;
            border-left: 3px solid #2e7d32;
        }

        .message.info {
            display: block;
            background: #f0f0f0;
            color: #555;
            border-left: 3px solid #999;
        }

        .hidden {
            display: none !important;
        }

        .modal-overlay {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(0,0,0,0.4);
            z-index: 1000;
            justify-content: center;
            align-items: center;
        }

        .modal-overlay.active {
            display: flex;
        }

        .modal {
            background: #ffffff;
            padding: 32px 36px;
            border-radius: 8px;
            max-width: 500px;
            width: 90%;
            box-shadow: 0 8px 32px rgba(0,0,0,0.15);
        }

        .modal h2 {
            font-size: 20px;
            font-weight: 600;
            margin-bottom: 20px;
        }

        .modal .form-group {
            margin-bottom: 16px;
        }

        .modal .form-group label {
            display: block;
            font-size: 14px;
            font-weight: 500;
            margin-bottom: 4px;
            color: #333;
        }

        .modal .form-group input,
        .modal .form-group textarea {
            width: 100%;
            padding: 10px 14px;
            border: 1px solid #d0d0d0;
            border-radius: 4px;
            font-size: 14px;
            font-family: inherit;
        }

        .modal .form-group textarea {
            min-height: 120px;
            resize: vertical;
        }

        .modal .form-group input:focus,
        .modal .form-group textarea:focus {
            outline: none;
            border-color: #1a1a1a;
        }

        .modal-actions {
            display: flex;
            gap: 8px;
            justify-content: flex-end;
            margin-top: 20px;
        }

        @media (max-width: 640px) {
            body {
                padding: 16px 12px;
            }

            .header {
                flex-wrap: wrap;
                gap: 12px;
            }

            .header-actions {
                justify-content: flex-start;
            }

            .post-card {
                padding: 16px 20px;
            }

            .post-title {
                font-size: 16px;
            }

            .modal {
                padding: 24px 20px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header class="header">
            <div class="header-left">
                <a href="/" class="logo">blog<span>.</span></a>
            </div>
            <div class="header-actions">
                <span class="user-badge" id="userBadge">
                    <span class="dot" id="statusDot"></span>
                    <span id="userEmail">Загрузка...</span>
                </span>
                <button class="btn btn-primary" id="createPostBtn">+ Создать</button>
                <button class="btn btn-danger" id="logoutBtn">Выйти</button>
            </div>
        </header>

        <div id="message" class="message"></div>

        <div id="postsContainer">
            <div class="loading-state" id="loadingState">
                <div class="spinner"></div>
                <div>Загрузка постов...</div>
            </div>

            <div class="posts-list hidden" id="postsList"></div>

            <div class="empty-state hidden" id="emptyState">
                <div class="icon">📭</div>
                <h3>Нет постов</h3>
                <p>Создайте первый пост</p>
            </div>
        </div>
    </div>

    <div class="modal-overlay" id="createModal">
        <div class="modal">
            <h2>✏️ Создать пост</h2>
            <form id="createPostForm">
                <div class="form-group">
                    <label for="postTitle">Заголовок</label>
                    <input type="text" id="postTitle" placeholder="Введите заголовок">
                </div>
                <div class="form-group">
                    <label for="postContent">Содержание</label>
                    <textarea id="postContent" placeholder="Введите содержание"></textarea>
                </div>
                <div class="modal-actions">
                    <button type="button" class="btn" onclick="closeModal()">Отмена</button>
                    <button type="submit" class="btn btn-primary">Опубликовать</button>
                </div>
            </form>
        </div>
    </div>

    <script>
        const API_URL = window.location.origin;
        const STORAGE_KEYS = {
            ACCESS_TOKEN: 'access_token',
            REFRESH_TOKEN: 'refresh_token',
            USER_EMAIL: 'user_email'
        };

        let isRefreshing = false;
        let refreshSubscribers = [];
        let isRedirecting = false;

        function isAuthenticated() {
            return !!localStorage.getItem(STORAGE_KEYS.ACCESS_TOKEN);
        }

        function getAuthHeaders() {
            const token = localStorage.getItem(STORAGE_KEYS.ACCESS_TOKEN);
            return {
                'Content-Type': 'application/json',
                'Authorization': token ? `Bearer ${token}` : ''
            };
        }

        function isTokenExpired(token) {
            try {
                const payload = JSON.parse(atob(token.split('.')[1]));
                const exp = payload.exp * 1000;
                return Date.now() >= exp;
            } catch {
                return true;
            }
        }

        document.addEventListener('DOMContentLoaded', () => {
            if (!isAuthenticated()) {
                window.location.href = '/';
                return;
            }
            updateUI();
            loadPosts();
        });

        function clearTokens() {
            localStorage.removeItem(STORAGE_KEYS.ACCESS_TOKEN);
            localStorage.removeItem(STORAGE_KEYS.REFRESH_TOKEN);
            localStorage.removeItem(STORAGE_KEYS.USER_EMAIL);
        }

        async function refreshAccessToken() {
            if (isRefreshing) {
                return new Promise((resolve) => {
                    refreshSubscribers.push(resolve);
                });
            }

            isRefreshing = true;
            const refreshToken = localStorage.getItem(STORAGE_KEYS.REFRESH_TOKEN);

            if (!refreshToken) {
                isRefreshing = false;
                clearTokens();
                redirectToLogin('Отсутствует refresh токен');
                return null;
            }

            try {
                const response = await fetch(`${API_URL}/auth/refresh_token/`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ refresh_token: refreshToken })
                });

                if (response.ok) {
                    const data = await response.json();
                    const newAccessToken = data.access_token || data;
                    if (newAccessToken) {
                        localStorage.setItem(STORAGE_KEYS.ACCESS_TOKEN, newAccessToken);
                        refreshSubscribers.forEach(cb => cb(newAccessToken));
                        refreshSubscribers = [];
                        return newAccessToken;
                    }
                }

                clearTokens();
                redirectToLogin('Сессия истекла');
                return null;
            } catch (err) {
                console.error('Refresh token error:', err);
                clearTokens();
                redirectToLogin('Ошибка обновления токена');
                return null;
            } finally {
                isRefreshing = false;
            }
        }

        function redirectToLogin(message) {
            if (isRedirecting) return;
            isRedirecting = true;

            showMessage(message || '⏰ Сессия истекла. Войдите заново.', 'error');

            setTimeout(() => {
                window.location.href = '/';
            }, 1500);
        }

        async function fetchWithAuth(url, options = {}) {
            let accessToken = localStorage.getItem(STORAGE_KEYS.ACCESS_TOKEN);

            let response = await fetch(url, {
                ...options,
                headers: {
                    'Content-Type': 'application/json',
                    ...(accessToken ? { 'Authorization': `Bearer ${accessToken}` } : {}),
                    ...options.headers
                }
            });

            if (response.status === 401) {
                const newAccessToken = await refreshAccessToken();
                if (newAccessToken) {
                    response = await fetch(url, {
                        ...options,
                        headers: {
                            'Content-Type': 'application/json',
                            'Authorization': `Bearer ${newAccessToken}`,
                            ...options.headers
                        }
                    });
                } else {
                    redirectToLogin('Не удалось обновить сессию');
                    throw new Error('Session expired');
                }
            }
            return response;
        }

        function updateUI() {
            const userEmail = document.getElementById('userEmail');
            const statusDot = document.getElementById('statusDot');
            const email = localStorage.getItem(STORAGE_KEYS.USER_EMAIL);

            if (isAuthenticated()) {
                userEmail.textContent = email || 'Пользователь';
                statusDot.className = 'dot';
            } else {
                userEmail.textContent = 'Гость';
                statusDot.className = 'dot offline';
            }
        }

        function showMessage(text, type = 'info') {
            const msg = document.getElementById('message');
            msg.textContent = text;
            msg.className = `message ${type}`;
            clearTimeout(window.messageTimeout);
            window.messageTimeout = setTimeout(() => {
                msg.className = 'message';
                msg.textContent = '';
            }, 5000);
        }

        function escapeHtml(text) {
            if (!text) return '';
            const div = document.createElement('div');
            div.textContent = text;
            return div.innerHTML;
        }

        // ========== НОРМАЛИЗАЦИЯ ОТВЕТА ==========
        // Приводит любой формат ответа к массиву объектов { id, title, author, created_at }
        // Поддерживает:
        //   1) { title: [...], id: [...] }  — ResponseManyPostsSchema
        //   2) [ { id, title, ... }, ... ] — массив объектов
        //   3) [ "title1", "title2" ]      — массив строк (без id → некликабельно)
        function normalizePosts(data) {
            if (!data) return [];

            // Формат ResponseManyPostsSchema: параллельные массивы title и id
            if (data && Array.isArray(data.title)) {
                const titles = data.title;
                const ids = Array.isArray(data.id) ? data.id : [];

                // Если длины не совпадают — предупреждаем (это и есть источник сдвига на бэке)
                if (ids.length !== titles.length) {
                    console.warn(
                        `⚠️ Несовпадение длин: title=${titles.length}, id=${ids.length}. ` +
                        `Посты без id будут некликабельны.`
                    );
                }

                return titles.map((title, i) => ({
                    // id берём строго по тому же индексу i, что и title
                    id: (i < ids.length && ids[i] != null) ? ids[i] : null,
                    title: title,
                    author: null,
                    created_at: null
                }));
            }

            // Формат: массив объектов
            if (Array.isArray(data)) {
                return data.map((item) => {
                    if (typeof item === 'string') {
                        return { id: null, title: item, author: null, created_at: null };
                    }
                    if (item && typeof item === 'object') {
                        return {
                            id: item.id != null ? item.id : null,
                            title: item.title || item.name || 'Без названия',
                            author: item.author || null,
                            created_at: item.created_at || null
                        };
                    }
                    return { id: null, title: String(item), author: null, created_at: null };
                });
            }

            return [];
        }

        function renderPosts(data) {
            const list = document.getElementById('postsList');
            const loading = document.getElementById('loadingState');
            const empty = document.getElementById('emptyState');

            const posts = normalizePosts(data);

            if (!posts || posts.length === 0) {
                list.classList.add('hidden');
                loading.classList.add('hidden');
                empty.classList.remove('hidden');
                return;
            }

            list.innerHTML = posts.map((post) => {
                const title = post.title || 'Без названия';
                const postId = post.id;
                const hasId = postId !== null && postId !== undefined;

                // Если id нет — не делаем карточку кликабельной
                const clickAttr = hasId ? `onclick="openPost('${postId}')"` : '';
                const noIdClass = hasId ? '' : 'no-id';

                return `
                    <div class="post-card ${noIdClass}" ${clickAttr}>
                        <div class="post-title">${escapeHtml(title)}</div>
                        <div class="post-author">
                            <strong>${escapeHtml(post.author || 'Автор')}</strong>
                        </div>
                        <div class="post-meta">
                            <span>📅 ${post.created_at ? new Date(post.created_at).toLocaleDateString('ru-RU') : 'Недавно'}</span>
                        </div>
                    </div>
                `;
            }).join('');

            list.classList.remove('hidden');
            loading.classList.add('hidden');
            empty.classList.add('hidden');
        }

        async function loadPosts() {
            const list = document.getElementById('postsList');
            const loading = document.getElementById('loadingState');
            const empty = document.getElementById('emptyState');

            list.classList.add('hidden');
            loading.classList.remove('hidden');
            empty.classList.add('hidden');

            try {
                const response = await fetchWithAuth(`${API_URL}/posts`);

                if (response.ok) {
                    const data = await response.json();
                    console.log('📥 /posts response:', data);
                    renderPosts(data);
                } else {
                    const error = await response.json().catch(() => ({}));
                    showMessage(error.detail || 'Ошибка загрузки постов', 'error');
                    renderPosts([]);
                }
            } catch (err) {
                if (err.message !== 'Session expired') {
                    showMessage('Ошибка соединения с сервером', 'error');
                    renderPosts([]);
                }
            }
        }

        async function createPost(postData) {
            try {
                const response = await fetchWithAuth(`${API_URL}/posts`, {
                    method: 'POST',
                    body: JSON.stringify(postData)
                });

                if (response.ok) {
                    showMessage('✅ Пост создан!', 'success');
                    loadPosts();
                    return true;
                } else {
                    const error = await response.json();
                    showMessage(error.detail || 'Ошибка создания поста', 'error');
                    return false;
                }
            } catch (err) {
                if (err.message !== 'Session expired') {
                    showMessage('Ошибка соединения', 'error');
                }
                return false;
            }
        }

        function openPost(postId) {
            if (postId !== null && postId !== undefined && postId !== '') {
                window.location.href = `/page/posts/${postId}`;
            }
        }

        function openModal() {
            if (!isAuthenticated()) {
                showMessage('Войдите, чтобы создать пост', 'error');
                return;
            }
            document.getElementById('createModal').classList.add('active');
            document.getElementById('postTitle').value = '';
            document.getElementById('postContent').value = '';
        }

        function closeModal() {
            document.getElementById('createModal').classList.remove('active');
        }

        document.getElementById('createPostBtn').addEventListener('click', openModal);

        document.getElementById('logoutBtn').addEventListener('click', async () => {
            if (confirm('Выйти?')) {
                try {
                    await fetch(`${API_URL}/auth/logout/`, {
                        method: 'POST',
                        headers: getAuthHeaders()
                    });
                } catch (err) {}

                clearTokens();
                window.location.href = '/';
            }
        });

        document.getElementById('createPostForm').addEventListener('submit', async (e) => {
            e.preventDefault();

            const title = document.getElementById('postTitle').value.trim();
            const content = document.getElementById('postContent').value.trim();

            if (!title || !content) {
                showMessage('Заполните все поля', 'error');
                return;
            }

            const success = await createPost({ title, content });
            if (success) {
                closeModal();
            }
        });

        document.getElementById('createModal').addEventListener('click', (e) => {
            if (e.target === e.currentTarget) {
                closeModal();
            }
        });

        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                closeModal();
            }
        });
    </script>
</body>
</html>"""
