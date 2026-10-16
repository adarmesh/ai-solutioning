# VPN Setup Guide

**Document ID:** IT-GUIDE-011
**Owner:** IT Service Desk
**Applies to:** All employees requiring remote access to internal systems

## 1. Overview
The company uses GlobalProtect VPN to provide secure access to internal
systems (internal wikis, staging environments, internal admin tools) for
employees working outside the office network.

## 2. Prerequisites
- Company laptop with MDM profile installed.
- MFA enrolled (see Information Security Policy, Section 2).
- Active directory account in good standing.

## 3. Installation Steps
1. Download the GlobalProtect client from the IT Service Desk portal
   (itportal.company.example/vpn).
2. Install the client using your local admin credentials (Mac) or run as
   the provisioned IT profile (Windows).
3. Open GlobalProtect and enter the portal address: vpn.company.example.
4. Authenticate using your company SSO credentials plus MFA.
5. Once connected, you should see a green "Connected" status in the system
   tray/menu bar.

## 4. Troubleshooting
- **"Certificate error" on connect:** Your device certificate may have
  expired. Re-run the MDM enrollment from Settings > Company Portal.
- **Connects but cannot reach internal sites:** Confirm split-tunneling is
  disabled by checking Settings > Advanced in the GlobalProtect client.
- **Repeated disconnects:** Switch from Wi-Fi to a wired connection to rule
  out network instability, then contact the IT Service Desk with your
  connection logs (Help > Collect Logs).

## 5. Support
Open a ticket with the IT Service Desk (itportal.company.example) or use the
#it-help Slack channel for urgent VPN access issues.
