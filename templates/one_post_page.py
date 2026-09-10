one_post_html = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Пост</title>
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

        .btn-summarize {
            color: #1565c0;
            border-color: #90caf9;
            background: #e3f2fd;
        }

        .btn-summarize:hover {
            border-color: #1565c0;
            background: #bbdefb;
            color: #0d47a1;
        }

        .btn-summarize:disabled {
            opacity: 0.6;
            cursor: not-allowed;
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

        .post-detail {
            background: #ffffff;
            padding: 32px 36px;
            border-radius: 8px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.04);
            margin-bottom: 24px;
        }

        .post-title {
            font-size: 26px;
            font-weight: 600;
            color: #1a1a1a;
            margin-bottom: 8px;
            line-height: 1.3;
        }

        .post-meta {
            display: flex;
            gap: 16px;
            font-size: 14px;
            color: #757575;
            margin-bottom: 20px;
            padding-bottom: 16px;
            border-bottom: 1px solid #f0f0f0;
            flex-wrap: wrap;
        }

        .post-meta span {
            display: flex;
            align-items: center;
            gap: 4px;
        }

        .post-content {
            font-size: 16px;
            line-height: 1.7;
            color: #333;
            white-space: pre-wrap;
            word-break: break-word;
        }

        .summarize-section {
            margin-top: 20px;
            padding-top: 20px;
            border-top: 1px solid #eaeaea;
        }

        .summarize-header {
            display: flex;
            align-items: center;
            gap: 12px;
            flex-wrap: wrap;
        }

        .summarize-header h4 {
            font-size: 15px;
            font-weight: 600;
            color: #1a1a1a;
            margin: 0;
        }

        .summarize-content {
            margin-top: 12px;
            padding: 16px 20px;
            background: #f5f7fa;
            border-radius: 6px;
            border-left: 3px solid #1565c0;
            font-size: 15px;
            line-height: 1.6;
            color: #1a1a1a;
            display: none;
        }

        .summarize-content.active {
            display: block;
        }

        .summarize-content .loading-dots {
            display: flex;
            align-items: center;
            gap: 6px;
            padding: 4px 0;
        }

        .summarize-content .loading-dots span {
            width: 10px;
            height: 10px;
            background: #1565c0;
            border-radius: 50%;
            display: inline-block;
            animation: dotBounce 1.4s infinite ease-in-out both;
        }

        .summarize-content .loading-dots span:nth-child(1) {
            animation-delay: -0.32s;
        }

        .summarize-content .loading-dots span:nth-child(2) {
            animation-delay: -0.16s;
        }

        .summarize-content .loading-dots span:nth-child(3) {
            animation-delay: 0;
        }

        @keyframes dotBounce {
            0%, 80%, 100% {
                transform: scale(0);
            }
            40% {
                transform: scale(1);
            }
        }

        .summarize-content .loading-text {
            color: #757575;
            font-size: 14px;
            margin-left: 10px;
        }

        .summarize-content .summary-text {
            white-space: pre-wrap;
            word-break: break-word;
            animation: fadeIn 0.5s ease;
        }

        .summarize-content .summary-error {
            color: #c62828;
            animation: fadeIn 0.5s ease;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .comments-section {
            background: #ffffff;
            padding: 24px 36px;
            border-radius: 8px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.04);
        }

        .comments-section h3 {
            font-size: 18px;
            font-weight: 600;
            margin-bottom: 16px;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .comments-section h3 .count {
            font-weight: 400;
            color: #757575;
            font-size: 14px;
        }

        .comments-list {
            display: flex;
            flex-direction: column;
            gap: 12px;
            margin-bottom: 20px;
            max-height: 400px;
            overflow-y: auto;
        }

        .comment-item {
            padding: 12px 0;
            border-bottom: 1px solid #f0f0f0;
        }

        .comment-item:last-child {
            border-bottom: none;
        }

        .comment-content {
            font-size: 15px;
            color: #1a1a1a;
            line-height: 1.5;
            word-break: break-word;
        }

        .comment-meta {
            font-size: 12px;
            color: #999;
            margin-top: 4px;
        }

        .comment-form {
            display: flex;
            gap: 10px;
            margin-top: 16px;
            padding-top: 16px;
            border-top: 1px solid #f0f0f0;
            flex-wrap: wrap;
        }

        .comment-form .input-group {
            flex: 1;
            display: flex;
            gap: 10px;
            min-width: 200px;
        }

        .comment-form input[type="text"] {
            flex: 1;
            padding: 10px 14px;
            border: 1px solid #d0d0d0;
            border-radius: 4px;
            font-size: 14px;
            font-family: inherit;
            background: #fafafa;
            transition: border 0.2s;
            min-width: 100px;
        }

        .comment-form input[type="text"]:focus {
            outline: none;
            border-color: #1a1a1a;
            background: #ffffff;
        }

        .comment-form .file-upload-wrapper {
            position: relative;
            display: inline-block;
        }

        .comment-form .file-upload-wrapper input[type="file"] {
            position: absolute;
            left: 0;
            top: 0;
            opacity: 0;
            width: 100%;
            height: 100%;
            cursor: pointer;
        }

        .comment-form .btn {
            padding: 10px 20px;
            flex-shrink: 0;
        }

        .file-preview {
            display: none;
            padding: 8px 12px;
            background: #f0f0f0;
            border-radius: 4px;
            font-size: 13px;
            color: #555;
            width: 100%;
            margin-top: 8px;
        }

        .file-preview.active {
            display: block;
        }

        .file-preview .file-name {
            font-weight: 500;
        }

        .file-preview .file-size {
            color: #999;
            margin-left: 8px;
        }

        .file-preview .remove-file {
            cursor: pointer;
            color: #c62828;
            margin-left: 12px;
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

        .ws-status {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            font-size: 12px;
            padding: 2px 10px;
            border-radius: 12px;
            background: #f0f0f0;
            color: #757575;
        }

        .ws-status.connected {
            background: #e8f5e9;
            color: #2e7d32;
        }

        .ws-status .dot {
            width: 6px;
            height: 6px;
            border-radius: 50%;
            display: inline-block;
            background: #bdbdbd;
        }

        .ws-status.connected .dot {
            background: #4caf50;
        }

        .comment-image-wrapper {
            margin: 6px 0;
            max-width: 100%;
        }

        .comment-image {
            max-width: 100%;
            max-height: 400px;
            width: auto;
            height: auto;
            border-radius: 8px;
            margin: 6px 0;
            display: block;
            cursor: pointer;
            border: 1px solid #eaeaea;
            object-fit: contain;
        }

        .comment-image.svg-image {
            background: #f8f9fa;
            padding: 10px;
            min-height: 50px;
            min-width: 50px;
        }

        .comment-image.gif-image {
            max-height: 300px;
        }

        .comment-image:hover {
            opacity: 0.9;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }

        .comment-image-error {
            display: none;
            padding: 12px;
            background: #fbe9e7;
            border-radius: 8px;
            color: #c62828;
            font-size: 13px;
            margin: 6px 0;
        }

        .comment-image-error a {
            color: #1a73e8;
            text-decoration: none;
            margin-top: 4px;
            display: inline-block;
        }

        .comment-image-error a:hover {
            text-decoration: underline;
        }

        .image-modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.85);
            z-index: 1000;
            justify-content: center;
            align-items: center;
            padding: 20px;
            cursor: pointer;
        }

        .image-modal.active {
            display: flex;
        }

        .image-modal img {
            max-width: 90%;
            max-height: 90%;
            border-radius: 6px;
            object-fit: contain;
        }

        .image-modal .close-modal {
            position: absolute;
            top: 20px;
            right: 30px;
            font-size: 36px;
            color: #fff;
            cursor: pointer;
            background: none;
            border: none;
            padding: 10px;
        }

        @media (max-width: 640px) {
            body {
                padding: 16px 12px;
            }

            .post-detail {
                padding: 20px 16px;
            }

            .post-title {
                font-size: 20px;
            }

            .comments-section {
                padding: 16px 16px;
            }

            .comment-form {
                flex-direction: column;
            }

            .comment-form .input-group {
                flex-direction: column;
                width: 100%;
            }

            .comment-form input[type="text"] {
                width: 100%;
            }

            .header {
                flex-wrap: wrap;
                gap: 12px;
            }

            .header-actions {
                justify-content: flex-start;
            }

            .comment-image {
                max-height: 250px;
            }

            .image-modal img {
                max-width: 95%;
                max-height: 80%;
            }

            .summarize-header {
                flex-direction: column;
                align-items: flex-start;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header class="header">
            <div class="header-left">
                <a href="/page/posts/html" class="logo">blog<span>.</span></a>
            </div>
            <div class="header-actions">
                <span class="user-badge" id="userBadge">
                    <span class="dot" id="statusDot"></span>
                    <span id="userEmail">Загрузка...</span>
                </span>
                <span class="ws-status" id="wsStatus">
                    <span class="dot"></span>
                    <span id="wsStatusText">отключен</span>
                </span>
                <button class="btn btn-danger" id="logoutBtn">Выйти</button>
            </div>
        </header>

        <!-- ДОБАВЛЕН ЭЛЕМЕНТ ДЛЯ СООБЩЕНИЙ -->
        <div id="message" class="message"></div>

        <div id="postContainer">
            <div class="loading-state" id="loadingState">
                <div class="spinner"></div>
                <div>Загрузка поста...</div>
            </div>

            <div id="postContent" class="hidden">
                <div class="post-detail">
                    <div class="post-title" id="postTitle"></div>
                    <div class="post-meta">
                        <span>✏️ <strong id="postAuthor">Автор</strong></span>
                        <span>📅 <span id="postDate">—</span></span>
                    </div>
                    <div class="post-content" id="postBody"></div>

                    <div class="summarize-section">
                        <div class="summarize-header">
                            <h4>📝 Выжимка текста</h4>
                            <button class="btn btn-summarize" id="summarizeBtn">Получить выжимку</button>
                        </div>
                        <div class="summarize-content" id="summarizeContent">
                            <div class="loading-dots">
                                <span></span>
                                <span></span>
                                <span></span>
                            </div>
                            <span class="loading-text">Генерация выжимки...</span>
                        </div>
                    </div>
                </div>

                <div class="comments-section" id="commentsSection">
                    <h3>
                        💬 Комментарии
                        <span class="count" id="commentsCount">0</span>
                    </h3>
                    <div class="comments-list" id="commentsList">
                        <div class="loading-state" style="padding:20px 0; font-size:13px; color:#999;">
                            Загрузка комментариев...
                        </div>
                    </div>
                    <div class="comment-form">
                        <div class="input-group">
                            <input type="text" id="commentInput" placeholder="Написать комментарий..." maxlength="500">
                            <div class="file-upload-wrapper">
                                <button class="btn" id="fileBtn">📎 Файл</button>
                                <input type="file" id="fileInput" multiple>
                            </div>
                        </div>
                        <button class="btn btn-primary" id="sendCommentBtn">Отправить</button>
                    </div>
                    <div class="file-preview" id="filePreview">
                        <span class="file-name" id="fileName">file.txt</span>
                        <span class="file-size" id="fileSize">(0 bytes)</span>
                        <span class="remove-file" id="removeFile">✕</span>
                    </div>
                </div>
            </div>

            <div class="empty-state hidden" id="emptyState">
                <div class="icon">📄</div>
                <h3>Пост не найден</h3>
                <p>Возможно, он был удален</p>
            </div>
        </div>
    </div>

    <div class="image-modal" id="imageModal">
        <button class="close-modal" id="closeModal">&times;</button>
        <img id="modalImage" src="" alt="Просмотр фото">
    </div>

    <script>
        const API_URL = window.location.origin;
        const WS_URL = window.location.host;
        const STORAGE_KEYS = {
            ACCESS_TOKEN: 'access_token',
            REFRESH_TOKEN: 'refresh_token',
            USER_EMAIL: 'user_email'
        };

        const postId = window.location.pathname.split('/').pop();

        let ws = null;
        let wsConnected = false;
        let wsReconnectTimeout = null;
        let isConnecting = false;
        let isRefreshing = false;
        let refreshSubscribers = [];
        let selectedFiles = [];
        let reconnectAttempts = 0;
        const MAX_RECONNECT_ATTEMPTS = 3;
        let isRedirecting = false;

        // ========== S3 URL Detection ==========
        function isImageUrl(url) {
            if (!url || typeof url !== 'string') return false;

            if (url.includes('s3.cloud.ru') || url.includes('s3.') || url.includes('amazonaws.com')) {
                return true;
            }

            const extensions = [
                'jpg', 'jpeg', 'png', 'gif', 'webp', 'bmp', 
                'svg', 'ico', 'tiff', 'tif', 'avif', 'heic', 
                'heif', 'raw', 'psd', 'ai', 'eps'
            ];

            const fileName = url.split('/').pop() || '';
            const ext = fileName.split('.').pop()?.toLowerCase() || '';

            if (extensions.includes(ext)) {
                return true;
            }

            const lowerFileName = fileName.toLowerCase();
            for (const ext of extensions) {
                if (lowerFileName.endsWith('.' + ext)) {
                    return true;
                }
            }

            return false;
        }

        function getImageClass(url) {
            if (!url || typeof url !== 'string') return '';

            const lowerUrl = url.toLowerCase();
            if (lowerUrl.includes('.svg') || lowerUrl.endsWith('.svg')) {
                return 'svg-image';
            }
            if (lowerUrl.includes('.gif') || lowerUrl.endsWith('.gif')) {
                return 'gif-image';
            }
            return '';
        }

        // ========== Token Management ==========
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

        document.addEventListener('DOMContentLoaded', () => {
            if (!isAuthenticated()) {
                window.location.href = '/';
                return;
            }
            updateUI();
            loadPost();
            initImageModal();
            initSummarizeButton(); // Обработчик вешается один раз при загрузке
        });

        function initImageModal() {
            const modal = document.getElementById('imageModal');
            const modalImg = document.getElementById('modalImage');
            const closeBtn = document.getElementById('closeModal');

            modal.addEventListener('click', (e) => {
                if (e.target === modal) {
                    modal.classList.remove('active');
                }
            });

            closeBtn.addEventListener('click', () => {
                modal.classList.remove('active');
            });

            document.addEventListener('keydown', (e) => {
                if (e.key === 'Escape') {
                    modal.classList.remove('active');
                }
            });
        }

        function openImageModal(src) {
            const modal = document.getElementById('imageModal');
            const modalImg = document.getElementById('modalImage');
            modalImg.src = src;
            modal.classList.add('active');
        }

        // ИСПРАВЛЕНА ОШИБКА: был token.split('.'), теперь token.split('.')[1]
        function isTokenExpired(token) {
            try {
                const payload = JSON.parse(atob(token.split('.')[1]));
                const exp = payload.exp * 1000;
                return Date.now() >= exp;
            } catch {
                return true;
            }
        }

        function clearTokens() {
            localStorage.removeItem(STORAGE_KEYS.ACCESS_TOKEN);
            localStorage.removeItem(STORAGE_KEYS.REFRESH_TOKEN);
            localStorage.removeItem(STORAGE_KEYS.USER_EMAIL);
        }

        function redirectToLogin(message) {
            if (isRedirecting) return;
            isRedirecting = true;

            if (ws) {
                try { ws.close(1000, 'Token expired'); } catch (err) {}
                ws = null;
                wsConnected = false;
            }
            if (wsReconnectTimeout) {
                clearTimeout(wsReconnectTimeout);
            }

            reconnectAttempts = 0;
            isConnecting = false;

            showMessage(message || '⏰ Сессия истекла. Войдите заново.', 'error');

            setTimeout(() => {
                window.location.href = '/';
            }, 1500);
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
                    let newAccessToken;
                    if (typeof data === 'string') {
                        newAccessToken = data;
                    } else if (data.access_token) {
                        newAccessToken = data.access_token;
                    } else {
                        newAccessToken = data;
                    }

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
            if (!msg) return; // защита на случай отсутствия
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

        function isUrl(text) {
            if (!text) return false;
            try {
                const url = new URL(text);
                return url.protocol === 'http:' || url.protocol === 'https:';
            } catch {
                return false;
            }
        }

        function formatFileSize(bytes) {
            if (bytes === 0) return '0 bytes';
            const k = 1024;
            const sizes = ['bytes', 'KB', 'MB', 'GB'];
            const i = Math.floor(Math.log(bytes) / Math.log(k));
            return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
        }

        // ========== Render Comment ==========
        function renderCommentContent(text) {
            if (!text) return '';

            const trimmed = text.trim();

            if (isUrl(trimmed)) {
                const url = trimmed;

                if (isImageUrl(url)) {
                    const imageClass = getImageClass(url);

                    return `
                        <div class="comment-image-wrapper">
                            <img 
                                src="${escapeHtml(url)}" 
                                alt="Изображение" 
                                class="comment-image ${imageClass}"
                                onclick="openImageModal('${escapeHtml(url)}')"
                                loading="lazy"
                                onerror="this.onerror=null; this.style.display='none'; this.parentElement.querySelector('.comment-image-error').style.display='block';"
                                onload="this.parentElement.querySelector('.comment-image-error').style.display='none'; this.style.display='block';"
                            >
                            <div class="comment-image-error">
                                ⚠️ Не удалось загрузить изображение
                                <br>
                                <a href="${escapeHtml(url)}" target="_blank" rel="noopener noreferrer">
                                    📎 Открыть оригинал
                                </a>
                            </div>
                        </div>
                    `;
                }

                return `<a href="${escapeHtml(url)}" target="_blank" rel="noopener noreferrer" style="color: #1a73e8; text-decoration: none; word-break: break-all;">${escapeHtml(url)}</a>`;
            }

            return escapeHtml(text);
        }

        function renderPost(post) {
            const container = document.getElementById('postContent');
            const loading = document.getElementById('loadingState');
            const empty = document.getElementById('emptyState');

            if (!post) {
                container.classList.add('hidden');
                loading.classList.add('hidden');
                empty.classList.remove('hidden');
                return;
            }

            document.getElementById('postTitle').textContent = post.title || 'Без названия';
            document.getElementById('postAuthor').textContent = post.author || 'Автор';
            document.getElementById('postDate').textContent = post.created_at 
                ? new Date(post.created_at).toLocaleDateString('ru-RU', { 
                    year: 'numeric', month: 'long', day: 'numeric',
                    hour: '2-digit', minute: '2-digit'
                })
                : 'Недавно';
            document.getElementById('postBody').textContent = post.content || '';

            resetSummarizeState();

            container.classList.remove('hidden');
            loading.classList.add('hidden');
            empty.classList.add('hidden');

            if (post.comments && Array.isArray(post.comments)) {
                renderComments(post.comments);
            }

            connectWebSocket();
        }

        function renderComments(comments) {
            const list = document.getElementById('commentsList');
            const count = document.getElementById('commentsCount');

            if (!comments || comments.length === 0) {
                list.innerHTML = `
                    <div style="padding:16px 0; color:#999; font-size:14px; text-align:center;">
                        Пока нет комментариев. Будьте первым!
                    </div>
                `;
                count.textContent = '0';
                return;
            }

            count.textContent = comments.length;
            list.innerHTML = comments.map(comment => {
                const text = comment.comment_content || comment.content || '';
                const renderedContent = renderCommentContent(text);
                return `
                    <div class="comment-item">
                        <div class="comment-content">${renderedContent}</div>
                        <div class="comment-meta">
                            ${comment.author ? `👤 ${escapeHtml(comment.author)}` : ''}
                            ${comment.created_at ? ` · ${new Date(comment.created_at).toLocaleString('ru-RU')}` : ''}
                        </div>
                    </div>
                `;
            }).join('');
        }

        async function loadPost() {
            const container = document.getElementById('postContent');
            const loading = document.getElementById('loadingState');
            const empty = document.getElementById('emptyState');

            container.classList.add('hidden');
            loading.classList.remove('hidden');
            empty.classList.add('hidden');

            try {
                const response = await fetchWithAuth(`${API_URL}/posts/${postId}`);

                if (response.ok) {
                    const data = await response.json();
                    renderPost(data);
                } else if (response.status === 404) {
                    renderPost(null);
                    showMessage('Пост не найден', 'error');
                } else {
                    const error = await response.json();
                    showMessage(error.detail || 'Ошибка загрузки поста', 'error');
                    renderPost(null);
                }
            } catch (err) {
                if (err.message !== 'Session expired') {
                    showMessage('Ошибка соединения с сервером', 'error');
                    renderPost(null);
                }
            }
        }

        // ========== Summarize Function ==========
        function resetSummarizeState() {
            const content = document.getElementById('summarizeContent');
            const btn = document.getElementById('summarizeBtn');
            
            if (content) {
                content.className = 'summarize-content';
                content.innerHTML = `
                    <div class="loading-dots">
                        <span></span>
                        <span></span>
                        <span></span>
                    </div>
                    <span class="loading-text">Генерация выжимки...</span>
                `;
            }
            
            if (btn) {
                btn.disabled = false;
                btn.textContent = 'Получить выжимку';
            }
        }

        function initSummarizeButton() {
            const btn = document.getElementById('summarizeBtn');
            const content = document.getElementById('summarizeContent');
            
            if (!btn || !content) {
                console.error('❌ Элементы выжимки не найдены');
                return;
            }

            // Удаляем старые обработчики, чтобы избежать дублирования
            btn.removeEventListener('click', summarizeHandler);
            btn.addEventListener('click', summarizeHandler);
        }

        async function summarizeHandler() {
            const btn = document.getElementById('summarizeBtn');
            const content = document.getElementById('summarizeContent');
            
            if (btn.disabled) return;
            
            console.log('🔍 Кнопка выжимки нажата!');
            console.log('📤 ID поста:', postId);
            
            content.className = 'summarize-content active';
            content.innerHTML = `
                <div class="loading-dots">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
                <span class="loading-text">Генерация выжимки...</span>
            `;
            
            btn.disabled = true;
            btn.textContent = '⏳ Загрузка...';

            try {
                const url = `/ai/summarize/${postId}/`; // можно изменить на /summarize/ если без префикса
                console.log('📤 Запрос к:', url);
                
                const response = await fetchWithAuth(url, {
                    method: 'GET'
                });

                console.log('📥 Статус:', response.status);

                if (response.ok) {
                    const data = await response.json();
                    console.log('✅ Данные:', data);
                    
                    let summaryText = '';
                    if (typeof data === 'string') {
                        summaryText = data;
                    } else if (data.summary) {
                        summaryText = data.summary;
                    } else if (data.text) {
                        summaryText = data.text;
                    } else if (data.result) {
                        summaryText = data.result;
                    } else {
                        summaryText = JSON.stringify(data, null, 2);
                    }

                    content.className = 'summarize-content active';
                    content.innerHTML = `<div class="summary-text">${escapeHtml(summaryText)}</div>`;
                    showMessage('✅ Выжимка успешно получена', 'success');
                } else {
                    let errorDetail = 'Ошибка получения выжимки';
                    try {
                        const error = await response.json();
                        errorDetail = error.detail || errorDetail;
                    } catch (e) {
                        errorDetail = `HTTP ${response.status}: ${response.statusText}`;
                    }
                    
                    console.error('❌ Ошибка:', errorDetail);
                    content.className = 'summarize-content active';
                    content.innerHTML = `<div class="summary-error">❌ ${escapeHtml(errorDetail)}</div>`;
                    showMessage('Ошибка получения выжимки', 'error');
                }
            } catch (err) {
                console.error('❌ Исключение:', err);
                if (err.message !== 'Session expired') {
                    content.className = 'summarize-content active';
                    content.innerHTML = `<div class="summary-error">❌ Ошибка соединения: ${escapeHtml(err.message)}</div>`;
                    showMessage('Ошибка соединения с сервером', 'error');
                }
            } finally {
                btn.disabled = false;
                btn.textContent = 'Получить выжимку';
            }
        }

        // ========== WebSocket ==========
        function connectWebSocket() {
            if (isConnecting && reconnectAttempts >= MAX_RECONNECT_ATTEMPTS) {
                console.log('Max reconnect attempts reached');
                redirectToLogin('Превышено количество попыток подключения');
                return;
            }

            isConnecting = true;
            reconnectAttempts++;

            const token = localStorage.getItem(STORAGE_KEYS.ACCESS_TOKEN);
            if (!token) {
                updateWsStatus(false);
                isConnecting = false;
                return;
            }

            if (isTokenExpired(token)) {
                console.log('Token expired, refreshing...');
                refreshAccessToken().then(newToken => {
                    if (newToken) {
                        isConnecting = false;
                        connectWebSocket();
                    } else {
                        redirectToLogin('Токен истек');
                    }
                });
                return;
            }

            if (ws) {
                try { ws.close(1000, 'Reconnecting'); } catch (err) {}
                ws = null;
            }

            const wsUrl = `ws://${WS_URL}/posts/ws/${postId}/?access_token=${encodeURIComponent(token)}`;

            try {
                ws = new WebSocket(wsUrl);
                ws.binaryType = 'blob';

                ws.onopen = () => {
                    wsConnected = true;
                    isConnecting = false;
                    reconnectAttempts = 0;
                    updateWsStatus(true);
                    console.log('WebSocket connected');
                };

                ws.onmessage = (event) => {
                    try {
                        console.log('WebSocket message received:', event.data);

                        if (event.data instanceof Blob) {
                            event.data.text().then(text => {
                                if (text && text.trim()) {
                                    addCommentToUI(text);
                                }
                            });
                            return;
                        }

                        if (typeof event.data === 'string') {
                            const text = event.data.trim();
                            if (text) {
                                console.log('Received text message:', text);
                                addCommentToUI(text);
                            }
                        }
                    } catch (err) {
                        console.error('Failed to process WS message:', err);
                    }
                };

                ws.onclose = (event) => {
                    wsConnected = false;
                    isConnecting = false;
                    updateWsStatus(false);

                    console.log(`WebSocket closed: code=${event.code}, reason=${event.reason}`);

                    if (event.code === 1008 || event.reason === 'Token expired') {
                        showMessage('❌ Неверный токен или сессия истекла', 'error');
                        redirectToLogin('Токен истек');
                        return;
                    }

                    if (event.code !== 1000 && reconnectAttempts < MAX_RECONNECT_ATTEMPTS) {
                        if (wsReconnectTimeout) {
                            clearTimeout(wsReconnectTimeout);
                        }
                        wsReconnectTimeout = setTimeout(connectWebSocket, 3000);
                    } else if (reconnectAttempts >= MAX_RECONNECT_ATTEMPTS) {
                        redirectToLogin('Превышено количество попыток подключения');
                    }
                };

                ws.onerror = (err) => {
                    console.error('WebSocket error:', err);
                };

            } catch (err) {
                console.error('WebSocket connection failed:', err);
                updateWsStatus(false);
                isConnecting = false;
                if (reconnectAttempts < MAX_RECONNECT_ATTEMPTS) {
                    wsReconnectTimeout = setTimeout(connectWebSocket, 5000);
                } else {
                    redirectToLogin('Ошибка подключения WebSocket');
                }
            }
        }

        function addCommentToUI(text) {
            const list = document.getElementById('commentsList');
            const count = document.getElementById('commentsCount');

            const renderedContent = renderCommentContent(text);

            const newCommentHtml = `
                <div class="comment-item">
                    <div class="comment-content">${renderedContent}</div>
                    <div class="comment-meta">
                        · ${new Date().toLocaleString('ru-RU')}
                    </div>
                </div>
            `;

            const emptyPlaceholder = list.querySelector('div[style]');
            if (emptyPlaceholder && list.children.length === 1) {
                list.innerHTML = newCommentHtml;
            } else {
                list.insertAdjacentHTML('beforeend', newCommentHtml);
            }

            const allComments = list.querySelectorAll('.comment-item');
            count.textContent = allComments.length;
            list.scrollTop = list.scrollHeight;
        }

        function updateWsStatus(connected) {
            const status = document.getElementById('wsStatus');
            const text = document.getElementById('wsStatusText');
            if (connected) {
                status.className = 'ws-status connected';
                text.textContent = 'подключен';
            } else {
                status.className = 'ws-status';
                text.textContent = 'отключен';
            }
        }

        function sendText(content) {
            if (!ws || ws.readyState !== WebSocket.OPEN) {
                showMessage('Нет соединения с сервером', 'error');
                return false;
            }

            if (!content || content.trim() === '') {
                showMessage('Напишите сообщение', 'error');
                return false;
            }

            try {
                ws.send(content.trim());
                document.getElementById('commentInput').value = '';
                return true;
            } catch (err) {
                console.error('Failed to send:', err);
                showMessage('Ошибка отправки', 'error');
                return false;
            }
        }

        function sendFile(file) {
            if (!ws || ws.readyState !== WebSocket.OPEN) {
                showMessage('Нет соединения с сервером', 'error');
                return;
            }

            try {
                ws.send(file);
                showMessage(`Файл ${file.name} отправлен`, 'success');

                selectedFiles = [];
                document.getElementById('filePreview').classList.remove('active');
                document.getElementById('fileInput').value = '';
            } catch (err) {
                console.error('Failed to send file:', err);
                showMessage('Ошибка отправки файла', 'error');
            }
        }

        function sendComment() {
            const input = document.getElementById('commentInput');
            const text = input.value.trim();

            if (selectedFiles.length > 0) {
                selectedFiles.forEach(file => sendFile(file));
                selectedFiles = [];
                return;
            }

            if (text) {
                sendText(text);
            } else {
                showMessage('Напишите сообщение или выберите файл', 'error');
            }
        }

        // ========== UI Handlers ==========
        document.getElementById('sendCommentBtn').addEventListener('click', sendComment);

        document.getElementById('commentInput').addEventListener('keydown', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                sendComment();
            }
        });

        document.getElementById('fileInput').addEventListener('change', (e) => {
            const files = e.target.files;
            if (files.length > 0) {
                selectedFiles = Array.from(files);

                const preview = document.getElementById('filePreview');
                const name = document.getElementById('fileName');
                const size = document.getElementById('fileSize');

                if (files.length === 1) {
                    name.textContent = files[0].name;
                    size.textContent = `(${formatFileSize(files[0].size)})`;
                } else {
                    name.textContent = `${files.length} файлов`;
                    size.textContent = `(всего ${formatFileSize(Array.from(files).reduce((sum, f) => sum + f.size, 0))})`;
                }

                preview.classList.add('active');
            }
        });

        document.getElementById('removeFile').addEventListener('click', () => {
            selectedFiles = [];
            document.getElementById('filePreview').classList.remove('active');
            document.getElementById('fileInput').value = '';
        });

        document.getElementById('logoutBtn').addEventListener('click', async () => {
            if (confirm('Выйти?')) {
                try {
                    await fetch(`${API_URL}/auth/logout/`, {
                        method: 'POST',
                        headers: getAuthHeaders()
                    });
                } catch (err) {}

                if (ws) {
                    try { ws.close(1000, 'User logout'); } catch (err) {}
                    ws = null;
                    wsConnected = false;
                }

                if (wsReconnectTimeout) {
                    clearTimeout(wsReconnectTimeout);
                }

                reconnectAttempts = 0;
                isConnecting = false;

                clearTokens();
                window.location.href = '/';
            }
        });

        window.addEventListener('beforeunload', () => {
            if (ws) {
                try { ws.close(1000, 'Page unload'); } catch (err) {}
            }
            if (wsReconnectTimeout) {
                clearTimeout(wsReconnectTimeout);
            }
        });

        console.log('🔍 Debug info:');
        console.log('  - Post ID:', postId);
        console.log('  - API URL:', API_URL);
        console.log('  - Summarize endpoint:', `/ai/summarize/${postId}/`);
        console.log('  - Token exists:', !!localStorage.getItem(STORAGE_KEYS.ACCESS_TOKEN));
    </script>
</body>
</html>"""
