# POST.json — READ THIS FIRST

`POST.json` currently holds a placeholder:

```json
{"url":""}
```

That is **not** a real post address, and the gate refuses it — on purpose.
The post does not exist yet.

## What has to happen, in order

1. The user posts the spotlight card to X from the public account
   **@ajtnc1109**:
   - image: `spotlight.png` in this repository
   - caption: the exact text in `CAPTION.md` (mention `@crisxai5`, link
     `https://x.com/crisxai5`, hashtags, and play code
     `makefun-honey-canyon-cornet`)
   - before the deadline: **Friday 2026-11-27 18:35 WIB**
2. Copy the post's address as X shows it:
   `https://x.com/ajtnc1109/status/<id>`
3. Replace the empty placeholder in `POST.json` with that address:
   ```json
   {"url": "https://x.com/ajtnc1109/status/<id>"}
   ```
4. Commit and push, then submit the entry (parent runs the submit)
   before the deadline.

Do **not** invent a post URL. Do **not** submit with the placeholder —
the gate reads the post from X and refuses an entry whose post cannot
be read.
