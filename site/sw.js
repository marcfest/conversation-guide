/* Conversation Guide — service worker DISABLED during active development.
   This is a self-destruct kill-switch: it claims control, deletes every cache,
   unregisters itself, and reloads open pages so they drop SW control and go
   straight to the network. There is NO fetch handler, so nothing is intercepted
   or cached. Replace with a real caching SW before launch if offline is wanted. */
self.addEventListener('install', function () {
  self.skipWaiting();
});

self.addEventListener('activate', function (e) {
  e.waitUntil(
    caches.keys().then(function (keys) {
      return Promise.all(keys.map(function (k) { return caches.delete(k); }));
    }).then(function () {
      return self.registration.unregister();
    }).then(function () {
      return self.clients.matchAll({ type: 'window' });
    }).then(function (clients) {
      clients.forEach(function (c) { c.navigate(c.url); });
    })
  );
});
