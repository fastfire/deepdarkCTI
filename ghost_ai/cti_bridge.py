#!/usr/bin/env python3
"""
Ghost AI — DeepDarkCTI Bridge
Sentinel Dark OSINT threat intelligence feed integration.
Market intelligence + active/current tracking.
NO wallet integration.
"""
from __future__ import annotations
import json
import os
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path
from typing import Optional


class ThreatCategory(str, Enum):
    CREDENTIAL_EXPOSURE   = "credential_exposure"
    RANSOMWARE            = "ransomware"
    APT                   = "apt"
    SUPPLY_CHAIN          = "supply_chain"
    WEB_EXPLOITATION      = "web_exploitation"
    DARK_WEB_MARKET       = "dark_web_market"
    ZERO_DAY              = "zero_day"
    PHISHING              = "phishing"
    BOTNET                = "botnet"
    FIRMWARE              = "firmware"


class Severity(str, Enum):
    CRITICAL = "critical"
    HIGH     = "high"
    MEDIUM   = "medium"
    LOW      = "low"
    INFO     = "info"


@dataclass
class CTIEntry:
    title: str
    description: str
    severity: Severity
    category: ThreatCategory
    source: str
    tags: list[str] = field(default_factory=list)
    ttps: list[str] = field(default_factory=list)          # MITRE ATT&CK IDs
    affected_systems: list[str] = field(default_factory=list)
    iocs: list[str] = field(default_factory=list)          # Indicators of Compromise
    apt_group: Optional[str] = None
    published_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    is_active: bool = True
    is_current: bool = True  # within last 7 days

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "description": self.description,
            "severity": self.severity.value,
            "category": self.category.value,
            "source": self.source,
            "tags": self.tags,
            "ttps": self.ttps,
            "affected_systems": self.affected_systems,
            "iocs": self.iocs,
            "apt_group": self.apt_group,
            "published_at": self.published_at,
            "is_active": self.is_active,
            "is_current": self.is_current,
        }


# ─── Static seed feed (loaded when live APIs unavailable) ────────────────────

SEED_CTI_FEED: list[CTIEntry] = [
    CTIEntry(
        title="[ACTIVE] Mass GitHub Token Harvesting Campaign",
        description="Automated bots scanning public repos and Pastebin for exposed GitHub tokens. Immediate rotation required.",
        severity=Severity.CRITICAL,
        category=ThreatCategory.CREDENTIAL_EXPOSURE,
        source="Ghost AI / DeepDarkCTI",
        tags=["github", "tokens", "harvesting", "automation"],
        ttps=["T1552.001", "T1530"],
        affected_systems=["GitHub", "CI/CD pipelines"],
        iocs=["api.github.com scan patterns", "pastebin.com mass queries"],
        is_active=True, is_current=True,
    ),
    CTIEntry(
        title="[CURRENT] LockBit 3.0 Targeting Financial Sector",
        description="LockBit affiliates using stolen credentials from dark web markets to pivot into financial institution VPNs.",
        severity=Severity.CRITICAL,
        category=ThreatCategory.RANSOMWARE,
        source="Ghost AI / DeepDarkCTI",
        tags=["lockbit", "ransomware", "finance", "vpn"],
        ttps=["T1486", "T1078", "T1190"],
        affected_systems=["Windows Server", "VMware ESXi", "Citrix"],
        apt_group="LockBit 3.0",
        is_active=True, is_current=True,
    ),
    CTIEntry(
        title="[ACTIVE] PyPI Malware Packages — Infostealer Droppers",
        description="Typosquatted Python packages (requests2, boto4, django-utils2) dropping infostealers on install.",
        severity=Severity.CRITICAL,
        category=ThreatCategory.SUPPLY_CHAIN,
        source="Ghost AI / DeepDarkCTI",
        tags=["pypi", "supply-chain", "infostealer", "typosquatting"],
        ttps=["T1195.001", "T1059.006"],
        affected_systems=["Python environments", "Developer workstations"],
        iocs=["requests2", "boto4", "django-utils2"],
        is_active=True, is_current=True,
    ),
    CTIEntry(
        title="[CURRENT] APT41 Targeting Telecom via Zero-Day",
        description="Chinese state actor APT41 exploiting unpatched CVE in enterprise VPN appliances. Patch immediately.",
        severity=Severity.CRITICAL,
        category=ThreatCategory.APT,
        source="Ghost AI / DeepDarkCTI",
        tags=["apt41", "china", "zero-day", "telecom", "vpn"],
        ttps=["T1190", "T1059", "T1070"],
        affected_systems=["Cisco IOS-XE", "Fortinet FortiGate"],
        apt_group="APT41",
        is_active=True, is_current=True,
    ),
    CTIEntry(
        title="[ACTIVE] Dark Web Market — Stealer Logs Batch Sale",
        description="450K fresh stealer logs on sale on RAMP forum. Includes banking credentials, session cookies, crypto wallets.",
        severity=Severity.HIGH,
        category=ThreatCategory.DARK_WEB_MARKET,
        source="Ghost AI / DeepDarkCTI",
        tags=["dark-web", "stealer-logs", "credentials", "RAMP"],
        ttps=["T1539", "T1552"],
        affected_systems=["Banking apps", "Email accounts"],
        is_active=True, is_current=True,
    ),
    CTIEntry(
        title="[CURRENT] BeEF Hook via Malvertising Chain",
        description="Drive-by campaigns using malvertising to deliver BeEF hooks. Targets Chrome/Firefox on Windows.",
        severity=Severity.HIGH,
        category=ThreatCategory.WEB_EXPLOITATION,
        source="Ghost AI / DeepDarkCTI",
        tags=["beef", "xss", "malvertising", "browser-hook"],
        ttps=["T1189", "T1185"],
        affected_systems=["Chrome 120+", "Firefox 121+"],
        is_active=True, is_current=True,
    ),
    CTIEntry(
        title="[ACTIVE] Firmware Backdoor in IoT Routers",
        description="Undocumented backdoor found in TP-Link and D-Link router firmware. Unblob analysis confirmed C2 staging.",
        severity=Severity.HIGH,
        category=ThreatCategory.FIRMWARE,
        source="Ghost AI / DeepDarkCTI",
        tags=["firmware", "iot", "backdoor", "router", "unblob"],
        ttps=["T1542", "T1601"],
        affected_systems=["TP-Link TL-WR940N", "D-Link DIR-825"],
        is_active=True, is_current=True,
    ),
]


class CTIBridge:
    """Ghost AI Threat Intelligence aggregator and feed manager."""

    def __init__(self) -> None:
        self._feed: list[CTIEntry] = list(SEED_CTI_FEED)

    def get_feed(
        self,
        severity: Optional[str] = None,
        category: Optional[str] = None,
        active_only: bool = False,
        current_only: bool = False,
    ) -> list[dict]:
        entries = self._feed
        if severity and severity != "all":
            entries = [e for e in entries if e.severity.value == severity]
        if category:
            entries = [e for e in entries if e.category.value == category]
        if active_only:
            entries = [e for e in entries if e.is_active]
        if current_only:
            entries = [e for e in entries if e.is_current]
        return [e.to_dict() for e in entries]

    def get_active_count(self) -> dict:
        return {
            "total": len(self._feed),
            "active": sum(1 for e in self._feed if e.is_active),
            "current": sum(1 for e in self._feed if e.is_current),
            "critical": sum(1 for e in self._feed if e.severity == Severity.CRITICAL),
            "by_category": {
                cat.value: sum(1 for e in self._feed if e.category == cat)
                for cat in ThreatCategory
            },
        }

    def search(self, query: str) -> list[dict]:
        q = query.lower()
        results = [
            e for e in self._feed
            if q in e.title.lower()
            or q in e.description.lower()
            or any(q in t for t in e.tags)
            or any(q in t for t in e.ttps)
        ]
        return [e.to_dict() for e in results]

    def ingest_stix2(self, stix_bundle: dict) -> int:
        """Ingest a STIX 2.x bundle and add entries to feed."""
        added = 0
        for obj in stix_bundle.get("objects", []):
            if obj.get("type") == "indicator":
                self._feed.append(CTIEntry(
                    title=obj.get("name", "Unknown Indicator"),
                    description=obj.get("description", ""),
                    severity=Severity.HIGH,
                    category=ThreatCategory.APT,
                    source="STIX2 Import",
                    tags=obj.get("labels", []),
                    ttps=[p["phase_name"] for p in obj.get("kill_chain_phases", [])],
                    published_at=obj.get("created", datetime.now(timezone.utc).isoformat()),
                ))
                added += 1
        return added


if __name__ == "__main__":
    bridge = CTIBridge()
    stats = bridge.get_active_count()
    print(json.dumps(stats, indent=2))
    print(f"\nFeed sample (critical):")
    for entry in bridge.get_feed(severity="critical")[:3]:
        print(f"  [{entry['severity'].upper()}] {entry['title']}")
