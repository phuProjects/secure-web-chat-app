/**
 * WebSocket client and UI.
 * Phase 1: connect, send/receive plain chat.
 * Phases 2–4: auth, key upload, secure payloads (see crypto.js).
 */

const WS_URL = "ws://127.0.0.1:8765";

const logEl = document.getElementById("log");
const statusEl = document.getElementById("status");
const inputEl = document.getElementById("msg");
const sendBtn = document.getElementById("send");

function appendLine(text) {
  const line = document.createElement("div");
  line.textContent = text;
  logEl.appendChild(line);
  logEl.scrollTop = logEl.scrollHeight;
}

function setConnected(connected) {
  statusEl.textContent = connected ? "Connected" : "Disconnected";
  sendBtn.disabled = !connected;
}

let socket = null;

function connect() {
  socket = new WebSocket(WS_URL);
  socket.addEventListener("open", () => setConnected(true));
  socket.addEventListener("close", () => setConnected(false));
  socket.addEventListener("error", () => appendLine("[error] connection failed"));
  socket.addEventListener("message", (ev) => {
    try {
      const data = JSON.parse(ev.data);
      if (data.type === "chat" && data.text != null) {
        appendLine(data.text);
        return;
      }
    } catch {
      /* fall through */
    }
    appendLine(String(ev.data));
  });
}

function sendChat() {
  const text = inputEl.value.trim();
  if (!text || !socket || socket.readyState !== WebSocket.OPEN) return;
  // Phase 1: plain JSON; align keys with shared/protocol.py
  socket.send(JSON.stringify({ type: "chat", text }));
  inputEl.value = "";
}

sendBtn.addEventListener("click", sendChat);
inputEl.addEventListener("keydown", (e) => {
  if (e.key === "Enter") sendChat();
});

connect();
