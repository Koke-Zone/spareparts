/* Al-Bais Motors — site script.
   Settings (phone, WhatsApp, form email) come from window.SITE, set in each page. */
(function () {
  'use strict';

  var SITE = window.SITE || {};
  var STORE_KEY = 'albais-enquiry';

  function $(sel, root) { return (root || document).querySelector(sel); }
  function $all(sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); }

  function waLink(text) {
    return 'https://wa.me/' + SITE.whatsapp + '?text=' + encodeURIComponent(text);
  }

  function icon(name) {
    return '<svg class="icon" aria-hidden="true"><use href="#i-' + name + '"></use></svg>';
  }

  function escapeHtml(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }

  /* ---------- Mobile navigation ---------- */
  var toggle = $('.nav-toggle');
  var nav = $('#site-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = !nav.classList.contains('is-open');
      nav.classList.toggle('is-open', open);
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      toggle.innerHTML = icon(open ? 'close' : 'menu') + '<span class="sr-only">Menu</span>';
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('is-open')) toggle.click();
    });
  }

  /* ---------- Footer year ---------- */
  $all('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* ---------- Enquiry list (saved in the browser) ---------- */
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
      var cats = [{ id: 'all', name: 'All parts' }].concat(window.CATEGORIES);
      tabs.innerHTML = cats.map(function (c) {
        return '<li><button type="button" data-cat="' + c.id + '" aria-pressed="' + (state.cat === c.id) + '">' + escapeHtml(c.name) + '</button></li>';
      }).join('');
      tabs.addEventListener('click', function (e) {
        var b = e.target.closest('button[data-cat]');
        if (!b) return;
        state.cat = b.getAttribute('data-cat');
        $all('button', tabs).forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); });
        render();
      });
    }

    var bikeSelect = $('[data-filter-bike]');
    if (bikeSelect) {
      bikeSelect.innerHTML = '<option value="">All bikes</option>' + window.BIKES.map(function (b) {
        return '<option' + (b === state.bike ? ' selected' : '') + '>' + escapeHtml(b) + '</option>';
      }).join('');
      bikeSelect.addEventListener('change', function () { state.bike = bikeSelect.value; render(); });
    }
    var catSelect = $('[data-filter-cat]');
    if (catSelect) {
      catSelect.innerHTML = '<option value="all">All categories</option>' + window.CATEGORIES.map(function (c) {
        return '<option value="' + c.id + '"' + (c.id === state.cat ? ' selected' : '') + '>' + escapeHtml(c.name) + '</option>';
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

    function catName(id) {
      var c = window.CATEGORIES.filter(function (x) { return x.id === id; })[0];
      return c ? c.name : '';
    }

    function render() {
      var q = state.q.trim().toLowerCase();
      var items = window.PRODUCTS.filter(function (p) {
        if (state.cat !== 'all' && p.cat !== state.cat) return false;
        if (state.bike && p.fits.indexOf(state.bike) === -1 && p.fits.indexOf('All bikes') === -1) return false;
        if (q && (p.name + ' ' + p.desc + ' ' + catName(p.cat) + ' ' + p.fits.join(' ')).toLowerCase().indexOf(q) === -1) return false;
        return true;
      });
      if (limit) items = items.slice(0, limit);

      if (!items.length) {
        grid.innerHTML = '<div class="no-results" style="grid-column:1/-1"><p><strong>We list our most common parts here — we stock many more.</strong></p>' +
          '<p>Send us your bike model and the part you need, and we\'ll confirm price and stock.</p>' +
          '<a class="btn btn--wa" href="' + waLink('Hi Al-Bais Motors, I am looking for: ' + state.q) + '" target="_blank" rel="noopener">' + icon('whatsapp') + 'Ask on WhatsApp</a></div>';
        return;
      }

      grid.innerHTML = items.map(function (p) {
        var msg = 'Hi Al-Bais Motors, please tell me the price and availability of: ' + p.name + '. My bike: ';
        return '<article class="card product">' +
          '<div class="product-media">' + icon(p.icon) + '</div>' +
          '<div class="product-body">' +
            '<span class="product-cat">' + escapeHtml(catName(p.cat)) + '</span>' +
            '<h3>' + escapeHtml(p.name) + '</h3>' +
            '<p>' + escapeHtml(p.desc) + '</p>' +
            '<p class="product-fits"><strong>Fits:</strong> ' + escapeHtml(p.fits.join(', ')) + '</p>' +
            '<div class="product-actions">' +
              '<a class="btn btn--wa" href="' + waLink(msg) + '" target="_blank" rel="noopener">' + icon('whatsapp') + 'Ask price</a>' +
              '<button type="button" class="btn btn--ghost" data-add="' + p.id + '">' + icon('plus') + 'Add to list</button>' +
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
      b.innerHTML = icon('check') + 'Added';
      setTimeout(function () {
        b.classList.remove('is-added');
        b.innerHTML = icon('plus') + 'Add more';
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
        return p ? '- ' + p.name + ' x ' + i.qty : '';
      }).filter(Boolean).join('\n');
    }

    function renderList() {
      var list = readList().filter(function (i) { return findProduct(i.id); });
      if (!list.length) {
        listEl.innerHTML = '<li class="empty-state">Your list is empty. <a href="products.html">Browse parts</a> and tap <strong>Add to list</strong>.</li>';
      } else {
        listEl.innerHTML = list.map(function (i) {
          var p = findProduct(i.id);
          return '<li><div><strong>' + escapeHtml(p.name) + '</strong><small>' + escapeHtml(p.fits.slice(0, 2).join(', ')) + '</small></div>' +
            '<div class="qty"><button type="button" data-dec="' + i.id + '" aria-label="Fewer ' + escapeHtml(p.name) + '">−</button><span>' + i.qty + '</span>' +
            '<button type="button" data-inc="' + i.id + '" aria-label="More ' + escapeHtml(p.name) + '">+</button></div>' +
            '<button type="button" class="remove" data-remove="' + i.id + '" aria-label="Remove ' + escapeHtml(p.name) + '">' + icon('close') + '</button></li>';
        }).join('');
      }
      var text = listText(list);
      if (hidden) hidden.value = text;
      if (waBtn) {
        waBtn.href = waLink('Hi Al-Bais Motors, please send prices and availability for:\n' + (text || '(my parts list)') + '\nMy bike: ');
      }
    }

    listEl.addEventListener('click', function (e) {
      var list = readList();
      var id, item;
      if ((id = (e.target.closest('[data-inc]') || {}).dataset) && id.inc) {
        item = list.filter(function (i) { return i.id === id.inc; })[0]; if (item) item.qty += 1;
      } else if ((id = (e.target.closest('[data-dec]') || {}).dataset) && id.dec) {
        item = list.filter(function (i) { return i.id === id.dec; })[0];
        if (item) { item.qty -= 1; if (item.qty < 1) list = list.filter(function (i) { return i !== item; }); }
      } else if ((id = (e.target.closest('[data-remove]') || {}).dataset) && id.remove) {
        list = list.filter(function (i) { return i.id !== id.remove; });
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
      data._subject = (form.getAttribute('data-subject') || 'Website enquiry') + ' — ' + (data.Name || 'Al-Bais Motors website');
      data._template = 'table';
      data._captcha = 'false';
      data['Sent from page'] = location.href.split('?')[0];
      if (data.Email) data._replyto = data.Email;

      var label = submit ? submit.innerHTML : '';
      if (submit) { submit.disabled = true; submit.textContent = 'Sending…'; }

      fetch(SITE.formEndpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
        body: JSON.stringify(data)
      })
        .then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { return { ok: r.ok, body: j }; }); })
        .then(function (res) {
          if (!res.ok || String(res.body.success) === 'false') throw new Error(res.body.message || 'Send failed');
          if (window.fbq) window.fbq('track', 'Lead', { content_name: form.getAttribute('data-subject') || 'Form' });
          if (window.gtag) window.gtag('event', 'generate_lead', { form_name: form.getAttribute('data-subject') || 'Form' });
          form.reset();
          if (listEl) saveList([]);
          location.href = form.getAttribute('data-thanks') || 'thank-you.html';
        })
        .catch(function () {
          if (status) {
            status.className = 'form-status is-error';
            status.innerHTML = 'Sorry, your message could not be sent right now. ' +
              '<a href="' + waLink((form.getAttribute('data-subject') || 'Enquiry') + '\n' + formToText(data)) + '" target="_blank" rel="noopener"><strong>Send it on WhatsApp instead</strong></a> ' +
              'or call <a href="tel:' + SITE.phoneIntl + '">' + SITE.phoneDisplay + '</a>.';
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
      var done = function () { b.setAttribute('aria-label', 'Link copied'); b.innerHTML = icon('check'); };
      if (navigator.clipboard) navigator.clipboard.writeText(location.href).then(done, function () {});
    });
  });
})();
