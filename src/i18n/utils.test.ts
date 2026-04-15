import { describe, it } from 'node:test';
import assert from 'node:assert/strict';
import { getLangFromUrl } from './utils';

describe('getLangFromUrl', () => {
    it('should extract a valid language from the root path', () => {
        const url = new URL('http://localhost/es/');
        assert.equal(getLangFromUrl(url), 'es');
    });

    it('should extract a valid language from a nested path', () => {
        const url = new URL('http://localhost/ro/about');
        assert.equal(getLangFromUrl(url), 'ro');
    });

    it('should fall back to the default language if the path starts with an invalid language', () => {
        const url = new URL('http://localhost/fr/');
        assert.equal(getLangFromUrl(url), 'en');
    });

    it('should fall back to the default language if there is no language prefix', () => {
        const url = new URL('http://localhost/');
        assert.equal(getLangFromUrl(url), 'en');
    });

    it('should handle paths with query parameters correctly', () => {
        const url = new URL('http://localhost/ro/about?q=hello');
        assert.equal(getLangFromUrl(url), 'ro');
    });

    it('should handle paths with hashes correctly', () => {
        const url = new URL('http://localhost/es/#team');
        assert.equal(getLangFromUrl(url), 'es');
    });

    it('should fall back to the default language for invalid language and extra paths', () => {
        const url = new URL('http://localhost/fr/contact');
        assert.equal(getLangFromUrl(url), 'en');
    });
});
