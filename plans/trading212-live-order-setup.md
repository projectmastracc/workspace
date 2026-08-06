# Plan: Trading 212 Live Order Setup (Grok CLI)

Temporary ops plan for wiring live Trading 212 API access so Grok can place **explicit, user-approved** live orders. Unrelated to the research repo; safe to delete later.

## Goal

Enable authenticated live Trading 212 API access from this environment with:

- Read access for account, portfolio, and orders
- Write access for market / limit / stop / stop-limit equity orders
- Hard rule: **no live order without an explicit, complete user instruction**

## Standing safety rules

1. Never place a live order unless the user names: **ticker (T212 format), side, size, order type**, and account is **live**.
2. Always **pre-check** cash/position, show the exact payload, wait for **go**, then submit.
3. Prefer env vars over pasting secrets into chat.
4. Prefer a dedicated orders-enabled key; use a separate read-only key for dashboards if possible.
5. If credentials leak (chat, git, logs): **revoke key immediately** in T212 Settings → API and rotate.
6. First live path validation: tiny size order after successful smoke tests.

## Account prerequisites

| Item | Requirement |
|------|-------------|
| Account type | General Invest and/or Stocks & Shares ISA |
| Not supported | SIPP (public API not available) |
| Mode | **Live** (practice keys are separate and will not hit real money) |
| Docs | https://docs.trading212.com/api |
| Help centre | https://helpcentre.trading212.com/hc/en-us/articles/14584770928157-Trading-212-API-key |

## Phase 1 — Generate live API key

On [app.trading212.com](https://app.trading212.com/):

1. Ensure **live** mode (not Practice).
2. **Settings → API (Beta)**.
3. Accept risk warning if prompted.
4. Generate API key named e.g. `grok-cli-live`.
5. Enable permissions:
   - Account data
   - Portfolio
   - Orders (**required** for place/cancel)
   - History (verification / reconciliation)
6. IP access:
   - Prefer **restrict to trusted IPs** if egress IP is stable
   - Use unrestricted only if IP churn makes restriction impractical
7. Save **API Key** + **API Secret** (secret shown once).

Notes from T212:

- Live market, limit, stop, and stop-limit orders are supported via API.
- Key pairs differ between real and demo accounts.

## Phase 2 — Inject credentials into the environment

**Preferred: shell env (no chat paste)**

```bash
export T212_API_KEY='...'
export T212_API_SECRET='...'
export T212_BASE_URL='https://live.trading212.com/api/v0'
```

Optional Basic Auth header:

```bash
export T212_AUTH_HEADER="Basic $(printf '%s:%s' "$T212_API_KEY" "$T212_API_SECRET" | base64 -w0)"
```

**Alt: sourced file (chmod 600)**

```bash
# e.g. ~/.config/t212.env
export T212_API_KEY=...
export T212_API_SECRET=...
export T212_BASE_URL=https://live.trading212.com/api/v0
source ~/.config/t212.env
```

Hard requirements:

- Never commit secrets to git
- Never write keys into this plan file or any tracked path

## Phase 3 — Smoke test (no trades)

After env is set, Grok runs read-only checks:

| Step | Check | Success criteria |
|------|--------|------------------|
| 3.1 | Auth / account summary | 200; cash + total value present |
| 3.2 | Portfolio positions | 200; list (may be empty) |
| 3.3 | Open + recent orders | 200; orders scope valid |
| 3.4 | Instrument metadata / ticker resolve | Confirms T212 symbol form (e.g. `AAPL_US_EQ`) |

On failure: stop. Fix scopes, live vs practice base URL, or IP allowlist before any order path.

Auth model: HTTP Basic — API Key as username, API Secret as password.

Base URLs:

| Environment | Base |
|-------------|------|
| Live | `https://live.trading212.com/api/v0` |
| Practice | practice host (separate key; not used for this plan) |

## Phase 4 — Live order protocol

User instruction template:

> Live: [BUY\|SELL] [qty] of [TICKER_T212] as [MARKET\|LIMIT\|STOP\|STOP_LIMIT] [price fields if needed]. Confirm first.

Grok loop per trade:

1. Parse and restate: ticker, side, quantity, order type, live account
2. Pre-check free cash / position / open orders
3. Show exact request (URL + JSON payload)
4. Wait for explicit **go**
5. Submit order
6. Return order id/status; re-read portfolio and open orders

Quantity convention (equity API): **positive = buy**, **negative = sell**.

Order types to support:

- Market — `POST .../equity/orders/market` (typical path)
- Limit / Stop / Stop-limit — corresponding equity order endpoints per current docs

Currency note: account free cash currency matters (e.g. EUR cash may block USD-denominated buys depending on account setup).

## Phase 5 — Optional tooling

If useful after smoke test:

- Small local CLI (`t212.py` or similar) with subcommands:
  - `portfolio`
  - `orders`
  - `order market|limit ...` (still requires intentional invocation)
- Keep credentials only in env; script never hardcodes secrets

## Phase 6 — Teardown / hygiene

- `unset T212_API_KEY T212_API_SECRET T212_AUTH_HEADER`
- Or end session
- Delete API key in T212 when no longer needed
- Delete this plan file from the repo when finished

## User handoff checklist

- [ ] Live key created with **orders** permission
- [ ] Env vars exported in the shell Grok uses
- [ ] User replies: `env is set — smoke test only`
- [ ] Grok reports account + portfolio snapshot
- [ ] User issues first explicit order (tiny size recommended)
- [ ] Confirm payload → go → fill/status

## Out of scope

- Unsolicited trading, rebalancing, or “run the strategy”
- SIPP
- CFD product surface unless later confirmed in API
- Relying on deprecated Pie endpoints long-term
- Storing secrets in the research monorepo

## Reference links

- API docs: https://docs.trading212.com/api
- API key help: https://helpcentre.trading212.com/hc/en-us/articles/14584770928157-Trading-212-API-key
- API terms: https://www.trading212.com/legal-documentation/API-Terms_EN.pdf
- Community updates (market/live order notes): https://community.trading212.com/t/trading-212-api-update/87988
