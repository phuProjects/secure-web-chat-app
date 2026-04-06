# Secure Web Chat

End-to-end encrypted messaging (work in progress). Built in phases: plain chat, auth, RSA directory, AES+RSA messages, integrity, logging, polish.

## Layout

- `server/` — WebSocket server (`server.py`), auth (`auth.py`), storage (`storage.py`)
- `client/` — static UI (`index.html`, `app.js`, `crypto.js`)
- `shared/` — `protocol.py` message types for JSON over WebSocket

## Run (skeleton)

```bash
cd secure-chat
pip install -r requirements.txt
python server/server.py
```

Serve `client/` over HTTP (browsers need a real origin for some crypto later), e.g.:

```bash
cd client
python -m http.server 8080
```

Open `http://127.0.0.1:8080` and point `app.js` `WS_URL` at your server if needed.

## Docs (to fill in Phase 7)

- Architecture diagram
- Encryption design and trust model
- Security decisions and limitations
