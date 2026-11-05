# 🗺️ deepdarkCTI — Future Roadmap & Automation Enhancements

This document outlines planned improvements to evolve this CTI repository from a curated markdown list into an automated, machine-readable threat intelligence knowledge base.

---

## ⚡ 1. Automated Link Validation & Liveness Probing
- [ ] **Automated Onion & Clearweb Health Checks**:
  - Deploy a daily scheduled CI/CD workflow (GitHub Actions) using a Tor SOCKS5 proxy to test HTTP responsiveness for all listed `.onion` domains and surface links.
  - Automatically flag dead, seized, or migrated endpoints with visual markdown badges (`🟢 Online`, `🔴 Offline`, `⚠️ Seized`).

---

## 🔄 2. Machine-Readable Data Formats & Feeds
- [ ] **Multi-Format Export Pipeline**:
  - Create an automated parser that converts Markdown tables into structured formats:
    - `JSON` (for programmatic parsing)
    - `CSV` (for analyst spreadsheet triage)
    - `STIX 2.1 / MISP Feed` (for direct ingestion into SIEMs and Threat Intelligence Platforms).
- [ ] **RSS / Webhook Change Alerts**:
  - Automatically generate an RSS/Atom feed notifying subscribers when new threat actor channels or ransomware portals are added.

---

## 🏷️ 3. Threat Classification & Cross-Referencing
- [ ] **MITRE ATT&CK & Threat Group Tagging**:
  - Tag entries with associated threat actors (e.g., LockBit, BlackCat/ALPHV, Play) and suspected nation-state affiliations or cybercrime motives.
- [ ] **Searchable Web Directory**:
  - Build a lightweight Static Site (GitHub Pages) with full-text search, category filtering, and copyable links.

