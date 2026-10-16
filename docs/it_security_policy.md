# Information Security Policy

**Document ID:** SEC-POL-003
**Effective date:** 2024-09-15
**Owner:** Information Security

## 1. Password Requirements
- Minimum length: 14 characters.
- Must include at least one uppercase letter, one lowercase letter, one
  number, and one special character.
- Passwords must be rotated every 180 days for accounts without multi-factor
  authentication (MFA) enabled; accounts with MFA enabled do not require
  periodic rotation.
- Reuse of the last 10 passwords is prohibited.

## 2. Multi-Factor Authentication (MFA)
- MFA is mandatory for all access to email, VPN, cloud infrastructure
  consoles, and source control.
- Approved MFA methods: authenticator app (preferred), hardware security key.
  SMS-based MFA is disallowed for privileged accounts (admin, infrastructure,
  finance systems).

## 3. Device Security
- Company laptops must have full-disk encryption enabled and a screen lock
  timeout of 5 minutes or less.
- Personal devices ("BYOD") may only access company email and chat through
  the approved Mobile Device Management (MDM) profile.

## 4. Data Classification
| Level | Description | Example |
|-------|-------------|---------|
| Public | No restriction | Marketing materials |
| Internal | Employees only | Internal wikis |
| Confidential | Need-to-know basis | Customer contracts |
| Restricted | Named individuals only | Source code, credentials |

## 5. Incident Reporting
Suspected security incidents (phishing, lost device, unauthorized access)
must be reported to security@company.example within 1 hour of discovery.
See the Incident Response Procedure for the full process.

## 6. Third-Party Access
External vendors requiring system access must sign a Data Processing
Agreement and be provisioned with time-limited accounts not exceeding 90
days without re-approval.
