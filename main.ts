// Entry runner for the Spotlight @crisxai5 bounty (Node 22, stdlib only).
//
// The graded thing is the X post itself — a spotlight card introducing
// @crisxai5 as a must-follow AI & crypto expert, posted from a public
// account with @crisxai5 and a make.fun play code in its text. All this
// program does is hand POST.json (the file naming that post) from the
// repository root to /output, where the house gate reads it. The house
// fetches the post from X on its own, so nothing written here about the
// post is scored — but a malformed pointer would still sink the entry,
// so the file is checked before it is copied and a bad one aborts loudly.
//
// Local run, mirroring the grader:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

// The gate refuses a POST.json above this size.
const MAX_BYTES = 16384;

function die(msg: string): never {
  console.error(`[spotlight-crisxai5] ${msg}`);
  process.exit(1);
}

// Check a post address the way the gate describes it: an https address on
// x.com or twitter.com, a handle, /status/, then digits only. Parsed by
// splitting on '/' instead of a regex so the shape is explicit.
function checkPostUrl(value: unknown): string {
  if (typeof value !== 'string') die('POST.json "url" must be a string');
  const parts = value.split('/');
  // ["https:", "", "x.com", "<handle>", "status", "<digits>"]
  if (parts.length !== 6) die(`post url has the wrong shape: ${value}`);
  if (parts[0] !== 'https:' || parts[1] !== '') {
    die(`post url must start with https:// : ${value}`);
  }
  if (parts[2] !== 'x.com' && parts[2] !== 'twitter.com') {
    die(`post url must be on x.com or twitter.com: ${value}`);
  }
  if (!parts[3]) die(`post url is missing the handle: ${value}`);
  if (parts[4] !== 'status') die(`post url must contain /status/: ${value}`);
  if (!/^[0-9]+$/.test(parts[5])) {
    die(`post url status id must be digits only: ${value}`);
  }
  return value;
}

const source = join(BOT_DIR, 'POST.json');
let raw: Buffer;
try {
  raw = readFileSync(source);
} catch (err) {
  die(`cannot read POST.json at ${source}: ${(err as Error).message}`);
}
if (raw.length > MAX_BYTES) {
  die(`POST.json is ${raw.length} bytes, over the ${MAX_BYTES} byte cap`);
}

let data: unknown;
try {
  data = JSON.parse(raw.toString('utf8'));
} catch (err) {
  die(`POST.json is not valid JSON: ${(err as Error).message}`);
}
if (data === null || typeof data !== 'object' || Array.isArray(data)) {
  die('POST.json must be a JSON object like {"url": "..."}');
}
const url = checkPostUrl((data as Record<string, unknown>).url);

mkdirSync(OUTPUT_DIR, { recursive: true });
writeFileSync(join(OUTPUT_DIR, 'POST.json'), raw);
console.log(`[spotlight-crisxai5] POST.json copied to ${OUTPUT_DIR} (${url})`);
