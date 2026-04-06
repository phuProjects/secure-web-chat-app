/**
 * Web Crypto API: RSA-OAEP, AES-GCM, SHA-256.
 * Phase 3+: key generation and export.
 * Phase 4+: encrypt/decrypt hybrid payloads.
 */

// Re-export or implement in later phases.
async function cryptoReady() {
  if (!globalThis.crypto?.subtle) {
    throw new Error("Web Crypto API not available");
  }
}
