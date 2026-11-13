/* Al-Bais Motors — site script.
   Settings come from window.SITE and the page's language strings from
   window.I18N (both written into each page by build.py). */
(function () {
  'use strict';

  var SITE = window.SITE || {};
  var T = window.I18N || {};
  var LANG = document.documentElement.lang || 'en';
  var STORE_KEY = 'albais-enquiry';

  function $(sel, root) { return (root || document).querySelector(sel); }
  function $all(sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); }

  // Pick the current language from a { sd, ur, en } object
  function loc(v) { return v && typeof v === 'object' ? (v[LANG] || v.en) : v; }

  function waLink(text) {
    return 'https://wa.me/' + SITE.whatsapp + '?text=' + encodeURIComponent(text);
  }

  function icon(name) {
    return '<svg class="icon' + (name === 'arrow' ? ' icon--dir' : '') + '" aria-hidden="true"><use href="#i-' + name + '"></use></svg>';
  }

  function escapeHtml(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }

  function fitsText(fits) {
    return fits.map(function (f) { return f === 'ALL' ? T.allBikes : f; }).join(LANG === 'en' ? ', ' : '، ');
  }

  /* ---------- Mobile navigation ---------- */
  var toggle = $('.nav-toggle');
  var nav = $('#site-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = !nav.classList.contains('is-open');
      nav.classList.toggle('is-open', open);
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      toggle.innerHTML = icon(open ? 'close' : 'menu') + '<span class="sr-only">' + escapeHtml(T.menu || 'Menu') + '</span>';
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('is-open')) toggle.click();
    });
  }

  /* ---------- Footer year ---------- */
  $all('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* ---------- Enquiry list (saved in the browser, shared by all languages) ---------- */
  function readList() {
    try { return JSON.parse(localStorage.getItem(STORE_KEY)) || []; } catch (e) { return []; }
  }
  function saveList(list) {
    try { localStorage.setItem(STORE_KEY, JSON.stringify(list)); } catch (e) { /* storage blocked */ }
    updateCount();
  }
  function findProduct(id) {
    return (window.PRODUCTS || []).filter(function (p) { return p.id === id; })[0];
  }
  function updateCount() {
    var total = readList().reduce(function (n, item) { return n + item.qty; }, 0);
    $all('[data-enquiry-count]').forEach(function (el) {
      el.textContent = total;
      el.hidden = total === 0;
    });
  }
  function addToList(id) {
    var list = readList();
    var item = list.filter(function (i) { return i.id === id; })[0];
    if (item) item.qty += 1; else list.push({ id: id, qty: 1 });
    saveList(list);
  }
  updateCount();

  /* ---------- Product catalogue ---------- */
  var grid = $('[data-products]');
  if (grid && window.PRODUCTS) {
    var limit = parseInt(grid.getAttribute('data-limit'), 10) || 0;
    var params = new URLSearchParams(location.search);
    var state = { cat: params.get('cat') || 'all', bike: params.get('bike') || '', q: params.get('q') || '' };

    var tabs = $('[data-cat-tabs]');
    if (tabs) {
      var cats = [{ id: 'all', name: T.allParts }].concat(window.CATEGORIES);
      tabs.innerHTML = cats.map(function (c) {
        return '<li><button type="button" data-cat="' + c.id + '" aria-pressed="' + (state.cat === c.id) + '">' + escapeHtml(loc(c.name)) + '</button></li>';
      }).join('');
      tabs.addEventListener('click', function (e) {
        var b = e.target.closest('button[data-cat]');
        if (!b) return;
        state.cat = b.getAttribute('data-cat');
        $all('button', tabs).forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); });
        if (catSelect) catSelect.value = state.cat;
        render();
      });
    }

    var bikeSelect = $('[data-filter-bike]');
    if (bikeSelect) {
      bikeSelect.innerHTML = '<option value="">' + escapeHtml(T.allBikes) + '</option>' + window.BIKES.map(function (b) {
        return '<option' + (b === state.bike ? ' selected' : '') + '>' + escapeHtml(b) + '</option>';
      }).join('');
      bikeSelect.addEventListener('change', function () { state.bike = bikeSelect.value; render(); });
    }
    var catSelect = $('[data-filter-cat]');
    if (catSelect) {
      catSelect.innerHTML = '<option value="all">' + escapeHtml(T.allCategories) + '</option>' + window.CATEGORIES.map(function (c) {
        return '<option value="' + c.id + '"' + (c.id === state.cat ? ' selected' : '') + '>' + escapeHtml(loc(c.name)) + '</option>';
      }).join('');
      catSelect.addEventListener('change', function () {
        state.cat = catSelect.value;
        if (tabs) $all('button', tabs).forEach(function (x) { x.setAttribute('aria-pressed', String(x.getAttribute('data-cat') === state.cat)); });
        render();
      });
    }
    var search = $('[data-filter-search]');
    if (search) {
      search.value = state.q;
      search.addEventListener('input', function () { state.q = search.value; render(); });
    }

    function catOf(id) { return window.CATEGORIES.filter(function (x) { return x.id === id; })[0]; }
    function allText(v) { return v && typeof v === 'object' ? v.sd + ' ' + v.ur + ' ' + v.en : (v || ''); }

    function render() {
      var q = state.q.trim().toLowerCase();
      var items = window.PRODUCTS.filter(function (p) {
        if (state.cat !== 'all' && p.cat !== state.cat) return false;
        if (state.bike && p.fits.indexOf(state.bike) === -1 && p.fits.indexOf('ALL') === -1) return false;
        // Search matches the part in any of the three languages
        if (q && (allText(p.name) + ' ' + allText(p.desc) + ' ' + allText((catOf(p.cat) || {}).name) + ' ' + p.fits.join(' ')).toLowerCase().indexOf(q) === -1) return false;
        return true;
      });
      if (limit) items = items.slice(0, limit);

      if (!items.length) {
        grid.innerHTML = '<div class="no-results" style="grid-column:1/-1"><p><strong>' + escapeHtml(T.noResultsTitle) + '</strong></p>' +
          '<p>' + escapeHtml(T.noResultsText) + '</p>' +
          '<a class="btn btn--wa" href="' + waLink(T.msgLookingFor + state.q) + '" target="_blank" rel="noopener">' + icon('whatsapp') + escapeHtml(T.askOnWa) + '</a></div>';
        return;
      }

      grid.innerHTML = items.map(function (p) {
        var name = loc(p.name);
        var msg = T.msgPrice + name + '\n' + T.msgMyBike;
        return '<article class="card product">' +
          '<div class="product-media">' + icon(p.icon) + '</div>' +
          '<div class="product-body">' +
            '<span class="product-cat">' + escapeHtml(loc((catOf(p.cat) || {}).name)) + '</span>' +
            '<h3>' + escapeHtml(name) + '</h3>' +
            '<p>' + escapeHtml(loc(p.desc)) + '</p>' +
            '<p class="product-fits"><strong>' + escapeHtml(T.fits) + '</strong> <bdi>' + escapeHtml(fitsText(p.fits)) + '</bdi></p>' +
            '<div class="product-actions">' +
              '<a class="btn btn--wa" href="' + waLink(msg) + '" target="_blank" rel="noopener">' + icon('whatsapp') + escapeHtml(T.askPrice) + '</a>' +
              '<button type="button" class="btn btn--ghost" data-add="' + p.id + '">' + icon('plus') + escapeHtml(T.addToList) + '</button>' +
            '</div>' +
          '</div>' +
        '</article>';
      }).join('');

      // Keep the URL shareable, e.g. products.html?cat=brakes
      if (!limit && history.replaceState) {
        var p2 = new URLSearchParams();
        if (state.cat !== 'all') p2.set('cat', state.cat);
        if (state.bike) p2.set('bike', state.bike);
        if (state.q) p2.set('q', state.q);
        var qs = p2.toString();
        history.replaceState(null, '', location.pathname + (qs ? '?' + qs : ''));
      }
    }

    grid.addEventListener('click', function (e) {
      var b = e.target.closest('[data-add]');
      if (!b) return;
      addToList(b.getAttribute('data-add'));
      b.classList.add('is-added');
      b.innerHTML = icon('check') + escapeHtml(T.added);
      setTimeout(function () {
        b.classList.remove('is-added');
        b.innerHTML = icon('plus') + escapeHtml(T.addMore);
      }, 1400);
    });

    render();
  }

  /* ---------- Enquiry page ---------- */
  var listEl = $('[data-enquiry-list]');
  if (listEl) {
    var waBtn = $('[data-enquiry-wa]');
    var hidden = $('[data-enquiry-field]');

    function listText(list) {
      return list.map(function (i) {
        var p = findProduct(i.id);
        return p ? '- ' + loc(p.name) + ' x ' + i.qty : '';
      }).filter(Boolean).join('\n');
    }

    function renderList() {
      var list = readList().filter(function (i) { return findProduct(i.id); });
      if (!list.length) {
        listEl.innerHTML = '<li class="empty-state">' + T.emptyList + '</li>';
      } else {
        listEl.innerHTML = list.map(function (i) {
          var p = findProduct(i.id);
          var name = escapeHtml(loc(p.name));
          return '<li><div><strong>' + name + '</strong><small><bdi>' + escapeHtml(fitsText(p.fits.slice(0, 2))) + '</bdi></small></div>' +
            '<div class="qty"><button type="button" data-dec="' + i.id + '" aria-label="' + escapeHtml(T.fewer) + ': ' + name + '">−</button><span>' + i.qty + '</span>' +
            '<button type="button" data-inc="' + i.id + '" aria-label="' + escapeHtml(T.more) + ': ' + name + '">+</button></div>' +
            '<button type="button" class="remove" data-remove="' + i.id + '" aria-label="' + escapeHtml(T.remove) + ': ' + name + '">' + icon('close') + '</button></li>';
        }).join('');
      }
      var text = listText(list);
      if (hidden) hidden.value = text;
      if (waBtn) waBtn.href = waLink(T.msgListIntro + '\n' + (text || T.myPartsList) + '\n' + T.msgMyBike);
    }

    listEl.addEventListener('click', function (e) {
      var list = readList();
      var inc = e.target.closest('[data-inc]');
      var dec = e.target.closest('[data-dec]');
      var rem = e.target.closest('[data-remove]');
      var item;
      if (inc) {
        item = list.filter(function (i) { return i.id === inc.dataset.inc; })[0];
        if (item) item.qty += 1;
      } else if (dec) {
        item = list.filter(function (i) { return i.id === dec.dataset.dec; })[0];
        if (item) { item.qty -= 1; if (item.qty < 1) list = list.filter(function (i) { return i !== item; }); }
      } else if (rem) {
        list = list.filter(function (i) { return i.id !== rem.dataset.remove; });
      } else {
        return;
      }
      saveList(list);
      renderList();
    });

    renderList();
  }

  /* ---------- Forms → email (FormSubmit), with WhatsApp fallback ---------- */
  function formToText(data) {
    return Object.keys(data).filter(function (k) { return k.charAt(0) !== '_' && data[k]; })
      .map(function (k) { return k + ': ' + data[k]; }).join('\n');
  }

  $all('form[data-form]').forEach(function (form) {
    var status = $('.form-status', form);
    var submit = $('button[type="submit"]', form);

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (status) { status.className = 'form-status'; status.textContent = ''; }

      // Built-in validation messages, plus a red border on bad fields
      var firstBad = null;
      $all('input, select, textarea', form).forEach(function (f) {
        var bad = !f.checkValidity();
        f.setAttribute('aria-invalid', bad ? 'true' : 'false');
        if (bad && !firstBad) firstBad = f;
      });
      if (firstBad) { firstBad.reportValidity(); firstBad.focus(); return; }

      var fd = new FormData(form);
      if (fd.get('_honey')) return; // spam bot

      var data = {};
      fd.forEach(function (v, k) { data[k] = data[k] ? data[k] + ', ' + v : v; });
      delete data._honey;
      var nameField = $('[autocomplete="name"]', form);
      var emailField = $('input[type="email"]', form);
      var subject = form.getAttribute('data-subject') || T.websiteEnquiry;
      data._subject = subject + ' — ' + ((nameField && nameField.value) || 'Al-Bais Motors') + ' [' + LANG.toUpperCase() + ']';
      data._template = 'table';
      data._captcha = 'false';
      data[T.fLanguage] = T.langName;
      data[T.fSentFrom] = location.href.split('?')[0];
      if (emailField && emailField.value) data._replyto = emailField.value;

      var label = submit ? submit.innerHTML : '';
      if (submit) { submit.disabled = true; submit.textContent = T.sending; }

      fetch(SITE.formEndpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
        body: JSON.stringify(data)
      })
        .then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { return { ok: r.ok, body: j }; }); })
        .then(function (res) {
          if (!res.ok || String(res.body.success) === 'false') throw new Error(res.body.message || 'Send failed');
          if (window.fbq) window.fbq('track', 'Lead', { content_name: subject });
          if (window.gtag) window.gtag('event', 'generate_lead', { form_name: subject });
          form.reset();
          if (listEl) saveList([]);
          location.href = form.getAttribute('data-thanks') || 'thank-you.html';
        })
        .catch(function () {
          if (status) {
            status.className = 'form-status is-error';
            status.innerHTML = escapeHtml(T.sendError) + ' ' +
              '<a href="' + waLink(subject + '\n' + formToText(data)) + '" target="_blank" rel="noopener"><strong>' + escapeHtml(T.sendOnWa) + '</strong></a> ' +
              escapeHtml(T.orCall) + ' <a href="tel:' + SITE.phoneIntl + '" dir="ltr">' + SITE.phoneDisplay + '</a>.';
          }
        })
        .then(function () {
          if (submit) { submit.disabled = false; submit.innerHTML = label; }
        });
    });
  });

  /* ---------- Share buttons ---------- */
  $all('[data-share-native]').forEach(function (b) {
    if (!navigator.share) { b.hidden = true; return; }
    b.addEventListener('click', function () {
      navigator.share({ title: document.title, url: location.href }).catch(function () {});
    });
  });
  $all('[data-share-copy]').forEach(function (b) {
    b.addEventListener('click', function () {
      var done = function () { b.setAttribute('aria-label', T.linkCopied); b.innerHTML = icon('check'); };
      if (navigator.clipboard) navigator.clipboard.writeText(location.href).then(done, function () {});
    });
  });
})();
