# Highway Data Services: shared code

Fictional demo monorepo for the Obsidian notes showcase.

| Folder | What |
| ------ | ---- |
| `crash-dashboard/etl` | Loads the yearly crash extract into staging and validates it |
| `crash-dashboard/app` | Public crash dashboard (Flask) |
| `crash-dashboard/reports` | Recurring extracts (FHWA monthly, fatality quarterly) |
| `roadview/backend` | RoadView field-video API: uploads, clips, retention |
| `roadview/frontend` | RoadView web viewer |
| `roadview/inference` | Sign / guardrail detection on uploaded video |
| `infra/terraform` | Cloud tenancy: network, buckets, compute |
| `infra/sso` | SAML service-provider config for the SSO migration |
