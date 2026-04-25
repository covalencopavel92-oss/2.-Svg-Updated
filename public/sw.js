const CACHE_NAME = "scale-automata-v1";
const ASSETS_TO_CACHE = ["/Logogif.webm", "/Logogif.mp4"];

self.addEventListener("install", (event) => {
	event.waitUntil(
		caches.open(CACHE_NAME).then((cache) => {
			return cache.addAll(ASSETS_TO_CACHE);
		}),
	);
	self.skipWaiting();
});

self.addEventListener("activate", (event) => {
	event.waitUntil(
		caches.keys().then((cacheNames) => {
			return Promise.all(
				cacheNames.map((cache) => {
					if (cache !== CACHE_NAME) {
						return caches.delete(cache);
					}
					return Promise.resolve();
				}),
			);
		}),
	);
	self.clients.claim();
});

self.addEventListener("fetch", (event) => {
	const url = new URL(event.request.url);

	// Only cache GET requests
	if (event.request.method !== "GET") return;

	// Cache strategy: Stale-While-Revalidate for astro assets and specific public assets
	if (
		url.pathname.startsWith("/_astro/") ||
		ASSETS_TO_CACHE.includes(url.pathname)
	) {
		event.respondWith(
			caches.match(event.request).then((cachedResponse) => {
				const fetchPromise = fetch(event.request)
					.then((networkResponse) => {
						if (
							networkResponse &&
							networkResponse.status === 200 &&
							networkResponse.type === "basic"
						) {
							const responseToCache = networkResponse.clone();
							caches.open(CACHE_NAME).then((cache) => {
								cache.put(event.request, responseToCache);
							});
						}
						return networkResponse;
					})
					.catch(() => {
						// If network fails, just return cached response
					});

				return cachedResponse || fetchPromise;
			}),
		);
	}
});
