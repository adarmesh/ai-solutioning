# Data Retention and Deletion Policy

**Document ID:** SEC-POL-009
**Owner:** Information Security / Legal

## 1. Purpose
Defines how long different categories of company and customer data are
retained before deletion or anonymization, in line with regulatory and
contractual obligations.

## 2. Retention Schedule
| Data category | Retention period | Action after period |
|----------------|------------------|----------------------|
| Customer support tickets | 3 years | Anonymize |
| Application logs (non-security) | 90 days | Delete |
| Security audit logs | 7 years | Archive to cold storage |
| Employee HR records | 7 years after termination | Archive |
| Financial transaction records | 10 years | Archive |
| Marketing email lists | Until opt-out or 2 years of inactivity | Delete |
| Product analytics (aggregated) | Indefinite | N/a (anonymized at collection) |

## 3. Deletion Requests
Customer data deletion requests (e.g., GDPR "right to erasure") are handled
by the Legal team within 30 days of a verified request, per the process in
the (separate) Privacy Request Handling procedure, which is not included in
this corpus.

## 4. Backup Retention
Database backups are retained for 35 days on a rolling basis regardless of
the underlying data's retention schedule, to support disaster recovery.
Backups older than 35 days are automatically purged.

## 5. Legal Holds
Data subject to a legal hold is exempt from standard deletion schedules
until the hold is lifted by Legal.
