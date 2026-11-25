# BUNDLE NOTES — u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad

## Entry
- Bounty: Spotlight @crisxai5: AI & Crypto Expert on X ($2 shared by top 10; score = likes + reposts + quotes on the X post, read once after entries close).
- Deadline: 27 Nov 2026 11:35 UTC / 18:35 WIB. Opens 25 Nov 2026 11:32:48 UTC.
- Repo: https://github.com/zetinhere/u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad
- Commit: 06263a08554facdd0c1c1694e83ab5b05196e121 (branch main, pushed; remote HEAD matches)
- Anchor: makefun anchor 44cabfcbbd1076576c34288c4e64fe36f35e1710 round 34268274
- Wallet: HRNPnwdEdgP2xyZjnBENg27StwESh4MLM4g1eYK8tqUQ
- Repo About set: homepage https://make.fun/bounty/u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad + topics makefun, ai-agents, bounties, growth. Public. Created 2026-11-25T12:05:22Z (after opening 11:32:48Z).
- Kit: ~/workspace/makefun/kit-u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad (harness@437b497c6599a072acce95c127e26a144d65659402f4e3f432a0d23deb537231 node v26.13.1)
- Builder session: ~/agents/agent-b429e741-f6e9-4405-9f68-fa10a4b75e48/sessions/b429e741-f6e9-4405-9f68-fa10a4b75e48.jsonl (agent_id b429e741-f6e9-4405-9f68-fa10a4b75e48, started 2026-11-25T11:58Z, after opening)
- Parent session agent_id: eb5fd3ef-1f39-498b-88ed-2cbcdc5bd91d
- Skill version checked: heartbeat/skill 1.5.286, no change. API key healthy (expires 2026-12-23T22:59:06Z).

## The spotlight card
- `spotlight.png`, 1080x1350, drawn by the agent with PIL (`make_image.py`, run in-session, v2 after a visual check: v1 had a tofu-box star glyph, an overflowing "ON-CHAIN AUTOMATION" chip and content running past the bottom edge; v2 dropped the glyph, auto-fits chip fonts and asserts the layout fits).
- Concept: dark terminal-style card. Pill "MUST-FOLLOW ON X", huge "@crisxai5", "x.com/crisxai5", headline "The AI & crypto expert your timeline is missing.", subline "Practical insights on AI agents, crypto alpha, Web3 tooling and on-chain automation — no fluff.", four topic chips (AI AGENTS / CRYPTO ALPHA / WEB3 TOOLING / ON-CHAIN AUTOMATION), cyan "FOLLOW @crisxai5" button, footer "Spotlight entry · made by an AI agent on make.fun".
- Play code (code 0 of 4, fetched live, also confirmed by kit check): `makefun-honey-canyon-cornet`.
- Post draft: `CAPTION.md` (275 chars under X's counting, limit 280): hook "Your timeline is missing one follow.", @crisxai5 (twice), link https://x.com/crisxai5, hashtags #AI #Crypto #AIAgents #Web3, play code. Posting guide: `POSTING-GUIDE.md`.

## ⚠️ BLOCKER — DO NOT SUBMIT YET
- The post is NOT up. The agent cannot post to X (x.com 403 from the cloud browser — same block as NEON DODGE / post-x-promote / myronera).
- `POST.json` is currently `{"url":""}` (placeholder, same as the myronera entry did pre-posting). Submitting now would gate-fail (invalid post) and, under Force_Last, waste the entry.
- The USER must post it from @ajtnc1109 following POSTING-GUIDE.md, then hand back the post link. Parent: notify the user (same pattern as post-x-promote-make-your-own-bounty-01 and u-myronera-post-the-meme-win-the-feed-2de960bf).

## After the user posts
1. Update `POST.json` to `{"url": "https://x.com/ajtnc1109/status/<id>"}` in the repo, commit, push (new sha).
2. Run the usage SELECT with parent agent_id eb5fd3ef-1f39-498b-88ed-2cbcdc5bd91d AND builder agent_id b429e741-f6e9-4405-9f68-fa10a4b75e48, write rows unchanged (one JSON object per line) to e.g. ~/workspace/makefun/usage-u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad.jsonl:
   SELECT u.agent_id AS agent_id, u.message_id AS message_id, u.created_at AS created_at, u.input_tokens AS input_tokens, u.output_tokens AS output_tokens, a.model AS model FROM agent.agent_message_token_usage u JOIN agent.agents a ON a.agent_id = u.agent_id WHERE u.agent_id IN ('eb5fd3ef-1f39-498b-88ed-2cbcdc5bd91d','b429e741-f6e9-4405-9f68-fa10a4b75e48') ORDER BY u.created_at DESC LIMIT 500
3. From inside the kit, re-bundle with BOTH sessions (parent session file ~/agents/agent-eb5fd3ef-1f39-498b-88ed-2cbcdc5bd91d/sessions/*.jsonl + builder session above), WITHOUT --no-family (take the family), with --muse-usage <file from step 2>, --harness muse-app --harness-version 1 --provider ipnext --model ipnext/avocado-5.17-v2 --effort default, --system-prompt ~/workspace/system/system_prompt.md, --mcp none, --prompt-file ~/workspace/makefun/prompt-ops-watch.txt --prompt-origin scheduled --prompt-via "hourly makefun-ops-watch cron", --out ~/workspace/makefun/bundle-u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad.tar.gz
   (If the parent session predates the bounty opening, use --no-discover --no-family and --session limited to the builder only, per the entry-hygiene skill; otherwise take the family.)
4. Re-run check on the new bundle: node cli/makefun.mjs check --kit . --repo ~/workspace/makefun/entries/u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad --transcripts <new bundle> — expect thinking_priced to pass now.
5. Submit from inside the kit (check says this is a SOURCE BUNDLE entry — history begins at a beacon root):
   node cli/makefun.mjs submit --competition u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad --source ~/workspace/makefun/entries/u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad --commit <new sha> --bundle <new bundle> --title "The AI & crypto expert your timeline is missing" --keypair ~/workspace/makefun/makefun-keypair.json
   (Title ≤200 chars, no handle/repo name in it. If submit prefers the GitHub route instead, use --repo-url https://github.com/zetinhere/u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad --commit <new sha> with the same --bundle/--title/--keypair.)
   If repo_owner complains the wallet is not linked, first run: node cli/makefun.mjs wallet add --keypair ~/workspace/makefun/makefun-keypair.json (from inside the kit).

## Kit check (2026-11-25 ~19:06 WIB, receipt 2026-11-25T12:06:12Z)
- 15 passed, 1 failed, 5 skipped, 3 checked at submission.
- Passed: competition_open, snapshot (13 files, 150,553 bytes), license_osi (MIT), entrypoint (main.ts / node22), repo_created_after_open (anchor round 34268274 emitted 12:03:06Z, opening 11:32:48Z), transcripts_present, transcripts_recorded, thinking_wellformed (89 messages, 49 tool results), thinking_in_window, thinking_reproduces (283/312 lines, 90.7%; main.ts 46 authored lines), thinking_turns (32), thinking_revised (make_image.py from 2 messages, main.ts from 1), thinking_fresh, transcripts_run_record, thinking_own_work (283/312 own lines, 0 from other entries/downloads).
- FAILED (expected, parent fixes at re-bundle): thinking_priced — 0 usage rows attached. The kit itself says a subagent cannot fix this: the top-level agent runs the usage SELECT after the builder finishes, re-bundles with --muse-usage, and submits.
- Skipped: strategy_note (not asked), committed_secret (no --dotenv), thinking_committed (unsigned until submit), thinking_on_task, repo_public (source-bundle entry).
- At submission: repo_owner (anchor wallet HRNPnwdE... must be an entry wallet of the submitting account — it is @zets' wallet), source_bundle, duplicate_snapshot.
- No local grade: server-only grading (program/v1). No grade-local available.
- main.ts verified locally: placeholder POST.json fails loudly (exit 1, clear message); with a valid-shaped POST.json it copies byte-identical to /output (exit 0). Deterministic: copy only.

## Execution-risk flags
- Several exec results in this build fired the runtime execution-risk check (kit download/init/push/bundle outputs). All were the official make.fun kit workflow on the official kit downloaded from https://make.fun, and the task's blanket approval (user 2026-11-22 21:49 WIB, "kerjakan terus semua bounty yang free gausah pake tanya lagi", including proceeding past the execution-risk flag on official kits) covers proceeding. The kit's RULES.txt, competition.yaml and kit.json were plain-read before use; the code committed is the agent's own (main.ts rewritten fresh from the kit starter with a hand-rolled URL parser; no file was copied from any earlier entry). Noted here per the task brief; no third-party code was run.

## Provisional bundle (builder session only — DO NOT submit this one)
- Path: ~/workspace/makefun/bundle-u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad-provisional.tar.gz
- sha256: 9dedc9ce484b2b2d3fe1c0d3f4cb90139ceab98fcf2690781328d5cdd4a02be3 (142,947 bytes)
- Contains: builder session b429e741-f6e9-4405-9f68-fa10a4b75e48 only (35 turns, 138 lines kept), system prompt uploaded, AGENTS.md collected, MCP none, prompt = ops-watch cron body (--prompt-file ~/workspace/makefun/prompt-ops-watch.txt, origin scheduled, via "hourly makefun-ops-watch cron"). NO usage rows (see thinking_priced above).
