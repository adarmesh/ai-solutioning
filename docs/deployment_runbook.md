# Production Deployment Runbook

**Document ID:** ENG-DOC-114
**Owner:** Platform Engineering
**Applies to:** All services deployed to the production Kubernetes cluster

## 1. Deployment Windows
- Standard deployments are allowed Monday-Thursday, 09:00-16:00 in the
  primary engineering timezone.
- No deployments on Fridays, weekends, or during the last 3 business days
  of any fiscal quarter ("quarter-close freeze"), except emergency
  hotfixes approved by an Engineering Director.

## 2. Standard Deployment Steps
1. Ensure CI pipeline is green on the target commit (all unit, integration,
   and security scan stages passed).
2. Open a deployment ticket in the `#deploys` Slack channel using the
   `/deploy` slash command, tagging the on-call engineer.
3. Deploy to the `staging` namespace first and run the smoke test suite
   (`make smoke-test ENV=staging`).
4. If smoke tests pass, promote the same image tag to `production` using
   `kubectl argo rollouts promote <service-name>`.
5. Monitor the rollout dashboard for 15 minutes post-deploy for error-rate
   or latency regressions.
6. Close the deployment ticket with a status update.

## 3. Rollback Procedure
- If error rate exceeds 2% above baseline or p99 latency exceeds 2x
  baseline within the 15-minute monitoring window, roll back immediately:
  `kubectl argo rollouts undo <service-name>`.
- Notify the `#incidents` channel if a rollback is triggered.

## 4. Canary Releases
Services with more than 10,000 requests/minute must use a canary rollout:
5% traffic for 10 minutes, then 25%, 50%, 100%, each gated on error-rate and
latency thresholds defined above.

## 5. Emergency Hotfixes
Emergency hotfixes bypass the staging smoke-test requirement but still
require sign-off from the on-call Engineering Director and must be
followed by a retroactive incident review within 2 business days.
