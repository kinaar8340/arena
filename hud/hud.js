/* Arena HUD. Instrument, not a dashboard. */
(() => {
  const $ = (sel, root = document) => root.querySelector(sel);
  const $$ = (sel, root = document) => [...root.querySelectorAll(sel)];

  const SEED = {
    tick: 0,
    mode: "CORRECTING",
    lamp: "CORRECTING",
    fault: "admissible",
    streak: 0,
    n_persist: 8,
    n_terminal: 12,
    scenario: null,
    reject: null,
    catalog_insufficient: true,
    alignment: { t: 1.0, c: 0.65, leak: 0.18, p: 0.5 },
    a_star: {
      t: 1.0, eps_t: 0.08, c: 0.65, eps_c: 0.10,
      leak_min: 0.08, leak_max: 0.32, p: 0.5, life_slots: 8,
    },
    residual: { dt: 0, dc: 0, dleak: 0, dp: 0 },
    life: [0, 1, 2, 3, 4, 5, 6, 7],
    pointer: [0, 1, 2, 3],
    frozen: false,
    ranks: [
      { id: "R1", name: "lattice-waveguide", owns: "t", t: 1, c: 0.65, leak: 0.18, p: 0.5, pip: "ok", locked: false },
      { id: "R2", name: "energy surfaces", owns: "c", t: 1, c: 0.65, leak: 0.18, p: 0.5, pip: "ok", locked: false },
      { id: "R3", name: "near-field network", owns: "leak", t: 1, c: 0.65, leak: 0.18, p: 0.5, pip: "ok", locked: false },
      { id: "R4", name: "identity shell", owns: "p", t: 1, c: 0.65, leak: 0.18, p: 0.5, pip: "ok", locked: false },
      { id: "R5", name: "boundary-scaffold", owns: "tension", t: 1, c: 0.65, leak: 0.18, p: 0.5, pip: "ok", locked: false },
    ],
    motto: "Without correction, adaptation takes control.",
  };

  const fmt = (x, n = 3) => (Number.isFinite(x) ? Number(x).toFixed(n) : "—");
  const sgn = (x) => `${x >= 0 ? "+" : ""}${fmt(x, 3)}`;

  function yOf(value, lo, hi) {
    const t = (value - lo) / (hi - lo);
    const u = Math.min(1, Math.max(0, t));
    return 92 - u * 80;
  }

  function drawGauge(el, value, lo, hi, band, forbidY) {
    const svg = $("svg", el);
    const y = yOf(value, lo, hi);
    const b0 = yOf(band[0], lo, hi);
    const b1 = yOf(band[1], lo, hi);
    const top = Math.min(b0, b1);
    const h = Math.abs(b1 - b0);
    svg.innerHTML = `
      <line x1="12" y1="12" x2="12" y2="92" stroke="#8a7a55" stroke-width="0.7"/>
      <rect x="9" y="${top}" width="6" height="${Math.max(h, 1)}" fill="#c4a35a" opacity="0.28"/>
      ${forbidY != null ? `<line x1="6" y1="${forbidY}" x2="18" y2="${forbidY}" stroke="#c45c4a" stroke-width="1.2"/>` : ""}
      <polygon points="6,${y} 12,${y - 2.2} 18,${y} 12,${y + 2.2}" fill="#e8d5a3"/>
    `;
    $(".g-val", el).textContent = fmt(value);
  }

  function renderRanks(state) {
    const stack = $("#rank-stack");
    stack.innerHTML = state.ranks.map((r) => `
      <li data-id="${r.id}">
        <div class="rank-head">
          <span class="rank-id">${r.id}</span>
          <span class="rank-name">${r.name}</span>
          <span class="pip ${r.pip}" title="${r.pip}"></span>
        </div>
        <div class="rank-read">
          <span><b>t</b> ${fmt(r.t)}</span>
          <span><b>c</b> ${fmt(r.c)}</span>
          <span><b>ℓ</b> ${fmt(r.leak)}</span>
          <span><b>p</b> ${fmt(r.p)}</span>
        </div>
      </li>
    `).join("");
  }

  function renderVenn(state) {
    const p = state.alignment.p;
    const leak = state.alignment.leak;
    const ring = $("#pointer-ring");
    const r = 8 + p * 14;
    ring.setAttribute("r", String(r));
    const hatch = $("#leak-fill");
    hatch.setAttribute("opacity", String(0.22 + Math.min(0.7, leak * 1.4)));
    const g = $("#catalog-g");
    if (state.mode === "ADAPTING" || state.mode === "TERMINAL") {
      g.setAttribute("transform", "translate(66 36) skewX(-10) rotate(-6) translate(-66 -36)");
    } else {
      g.removeAttribute("transform");
    }
    const line = $("#reject-line");
    line.textContent = state.reject ? `reject  ${state.reject}` : "";
    const panel = $("#venn-panel");
    if (state.reject === "pointer_eq_life" || state.reject === "leak_zero") {
      panel.classList.add("flash");
      setTimeout(() => panel.classList.remove("flash"), 180);
    }
  }

  function renderGauges(state) {
    const a = state.alignment;
    const s = state.a_star;
    drawGauge($('.gauge[data-k="t"]'), a.t, 0.5, 1.8, [s.t - s.eps_t, s.t + s.eps_t], null);
    drawGauge($('.gauge[data-k="c"]'), a.c, 0, 1, [s.c - s.eps_c, s.c + s.eps_c], null);
    drawGauge($('.gauge[data-k="leak"]'), a.leak, 0, 1, [s.leak_min, s.leak_max], yOf(0, 0, 1));
    drawGauge($('.gauge[data-k="p"]'), a.p, 0, 1, [Math.max(0, s.p - 0.15), Math.min(0.99, s.p + 0.15)], yOf(1, 0, 1));
    const r = state.residual;
    $("#res-dt").textContent = `dt ${sgn(r.dt)}`;
    $("#res-dc").textContent = `dc ${sgn(r.dc)}`;
    $("#res-dleak").textContent = `dℓ ${sgn(r.dleak)}`;
    $("#res-dp").textContent = `dp ${sgn(r.dp)}`;
    $("#fault-class").textContent = `fault  ${state.fault}`;
  }

  function render(state) {
    const app = $("#app");
    app.classList.toggle("is-adapting", state.mode === "ADAPTING" || state.mode === "TERMINAL");
    app.classList.toggle("is-terminal", state.mode === "TERMINAL");
    $("#tick-read").textContent = String(state.tick).padStart(4, "0");
    $("#lamp").textContent = state.lamp;
    $("#footer").textContent = state.motto;
    renderRanks(state);
    renderVenn(state);
    renderGauges(state);
  }

  async function post(path, body) {
    const res = await fetch(path, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: body ? JSON.stringify(body) : "{}",
    });
    const data = await res.json();
    render(data);
    return data;
  }

  async function refresh() {
    try {
      const res = await fetch("/state");
      const data = await res.json();
      render(data);
    } catch {
      render(SEED);
    }
  }

  function bind() {
    $$("#controls button[data-act]").forEach((btn) => {
      btn.addEventListener("click", () => post(`/${btn.dataset.act}`));
    });
    $$("#controls button[data-inject]").forEach((btn) => {
      btn.addEventListener("click", () => post("/inject", { scenario: btn.dataset.inject }));
    });
  }

  bind();
  render(SEED);
  refresh();
  setInterval(refresh, 500);
})();
