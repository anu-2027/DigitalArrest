/* DigitalArmour — Service Worker v1
 * Network-first strategy: always try the network, fall back to cache.
 * API routes (/analyze, /analytics, /test-cases, /explain) are never
 * intercepted — they always go directly to the Flask server.
 */

const CACHE = 'digitalarmour-v1';
const PRECACHE = ['/', '/static/manifest.json', '/static/icon.svg'];

// API paths that must never be served from cache
const API_PATHS = ['/analyze', '/analytics', '/test-cases', '/explain'];

// ── Install: pre-cache the app shell ──────────────────────────────
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE)
      .then(cache => cache.addAll(PRECACHE))
      .then(() => self.skipWaiting())
  );
});

// ── Activate: purge old cache versions ────────────────────────────
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys()
      .then(keys => Promise.all(
        keys.filter(k => k !== CACHE).map(k => caches.delete(k))
      ))
      .then(() => self.clients.claim())
  );
});

// ── Fetch: network-first, fall back to cache ──────────────────────
self.addEventListener('fetch', event => {
  const url = new URL(event.request.url);

  // Never intercept API calls — always hit the live server
  if (API_PATHS.some(p => url.pathname.startsWith(p))) return;
  if (event.request.method !== 'GET') return;

  event.respondWith(
    fetch(event.request)
      .then(response => {
        if (response && response.ok) {
          const clone = response.clone();
          caches.open(CACHE).then(cache => cache.put(event.request, clone));
        }
        return response;
      })
      .catch(() =>
        caches.match(event.request)
          .then(cached => cached || caches.match('/'))
      )
  );
});
