# Incident Response Procedure

**Document ID:** OPS-PROC-005
**Owner:** Site Reliability Engineering
**Applies to:** Production incidents affecting availability, security, or data integrity

## 1. Severity Levels
| Severity | Definition | Response Time |
|----------|------------|----------------|
| SEV-1 | Full outage or data breach affecting all customers | Immediate, 24/7 |
| SEV-2 | Partial outage or major feature degradation | Within 15 minutes |
| SEV-3 | Minor degradation, workaround available | Within 4 business hours |
| SEV-4 | Cosmetic or low-impact issue | Next business day |

## 2. Declaring an Incident
1. Anyone can declare an incident by running `/incident declare` in Slack or
   calling the on-call number listed in PagerDuty.
2. The declarer becomes Incident Commander (IC) until formally handed off.
3. The IC opens a dedicated `#incident-<id>` channel and starts a shared
   incident doc using the provided template.

## 3. Roles
- **Incident Commander (IC):** Coordinates response, makes final calls on
  mitigation actions, communicates status.
- **Ops Lead:** Executes technical mitigation (rollbacks, scaling, failover).
- **Communications Lead (SEV-1/SEV-2 only):** Drafts customer-facing and
  internal status updates every 30 minutes.

## 4. Mitigation Priority
Restore service first; root-cause analysis comes after mitigation, not
before. Acceptable first actions include rollback (see Deployment Runbook,
Section 3), traffic failover, or feature-flag disablement.

## 5. Communication Cadence
- SEV-1: updates every 15 minutes in the incident channel.
- SEV-2: updates every 30 minutes.
- SEV-3/4: update on resolution only.

## 6. Postmortem
A blameless postmortem is required for all SEV-1 and SEV-2 incidents within
5 business days of resolution, using the standard postmortem template
(background, timeline, root cause, action items with owners and due dates).

## 7. Security Incidents
Suspected security incidents (breach, unauthorized access, ransomware)
follow this same declaration process but must additionally page the
Security on-call and follow the Information Security Policy's incident
reporting requirement of notifying security@company.example within 1 hour.
