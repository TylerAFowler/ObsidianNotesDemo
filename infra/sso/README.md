# SSO (SAML) service-provider config

- `sp-metadata.test.xml`: register this with the **test** IdP. Prod metadata comes after the pilot.
- The SP signing cert lives in the vault (`sso-sp-signing-test`); it is not in git.
- Clock skew allowed: 2 minutes.
