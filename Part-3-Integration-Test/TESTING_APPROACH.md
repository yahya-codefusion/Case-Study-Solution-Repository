# Part 3 - Testing Approach

Flow:

```text
API create project -> Web UI verify -> Mobile/BrowserStack verify -> Tenant isolation
```

## API
Create the project with `POST /api/v1/projects` and verify ID, name and active status.

## Web
Login to the correct tenant and wait for the project card before validating it.

## Mobile
Run the same UI validation against required iOS/Android devices through BrowserStack. Credentials are supplied through CI secrets.

## Tenant isolation
Login as another tenant and verify the created project is not visible. A stronger implementation should also verify direct unauthorized API/resource access returns the expected denial status.

## Reliability
- Use Playwright auto-waiting assertions.
- Use API timeouts.
- Avoid hard-coded sleeps.
- Use environment variables for secrets.
- Capture reports/screenshots in CI.
