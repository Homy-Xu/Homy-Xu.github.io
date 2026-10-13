(() => {
  'use strict';
  const root = document.documentElement;
  const languageButton = document.querySelector('.language-button');
  const dialog = document.querySelector('.figure-dialog');
  let activeFigure = null;

  function setLanguage(language) {
    const chinese = language === 'zh';
    root.lang = chinese ? 'zh-CN' : 'en';
    languageButton.querySelector('span').textContent = chinese ? 'EN' : '中文';
    languageButton.setAttribute('aria-label', chinese ? 'Switch to English' : '切换到中文');
    document.querySelector('.dialog-close').setAttribute('aria-label', chinese ? '关闭图片' : 'Close figure');
    document.querySelectorAll('[data-preview]').forEach(link => {
      link.setAttribute('aria-label', `${chinese ? '放大图片' : 'Enlarge figure'}: ${link.dataset.title}`);
    });
    if (activeFigure) updateCaption();
    try { localStorage.setItem('homepage-language', chinese ? 'zh' : 'en'); } catch (_) { /* Storage may be disabled. */ }
  }

  function updateCaption() {
    const chinese = root.lang === 'zh-CN';
    dialog.querySelector('.dialog-caption').textContent = chinese ? activeFigure.dataset.captionZh : activeFigure.dataset.captionEn;
  }

  languageButton.hidden = false;
  let savedLanguage = 'en';
  try { savedLanguage = localStorage.getItem('homepage-language') || 'en'; } catch (_) { /* English remains the default. */ }
  setLanguage(savedLanguage);
  languageButton.addEventListener('click', () => setLanguage(root.lang === 'en' ? 'zh' : 'en'));

  if (typeof dialog.showModal === 'function') {
    document.querySelectorAll('[data-preview]').forEach(link => {
      link.addEventListener('click', event => {
        if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey || event.button !== 0) return;
        event.preventDefault();
        activeFigure = link;
        const image = dialog.querySelector('.dialog-image');
        image.src = link.href;
        image.alt = link.querySelector('img').alt;
        dialog.querySelector('#figure-dialog-title').textContent = link.dataset.title;
        dialog.querySelector('.dialog-paper-link').href = link.dataset.paper;
        updateCaption();
        dialog.showModal();
        document.body.classList.add('modal-open');
        dialog.querySelector('.dialog-close').focus();
      });
    });
    dialog.querySelector('.dialog-close').addEventListener('click', () => dialog.close());
    dialog.addEventListener('click', event => {
      const rect = dialog.getBoundingClientRect();
      if (event.target === dialog && (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom)) dialog.close();
    });
    dialog.addEventListener('close', () => {
      document.body.classList.remove('modal-open');
      activeFigure?.focus({preventScroll: true});
    });
  }

  const navigation = [...document.querySelectorAll('.navigation a')];
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(entries => {
      for (const entry of entries) {
        if (!entry.isIntersecting) continue;
        for (const link of navigation) {
          const current = link.hash === `#${entry.target.id}`;
          link.classList.toggle('active', current);
          if (current) link.setAttribute('aria-current', 'location');
          else link.removeAttribute('aria-current');
        }
      }
    }, {rootMargin: '-5% 0px -70% 0px', threshold: 0});
    navigation.forEach(link => observer.observe(document.querySelector(link.hash)));
  }
})();
