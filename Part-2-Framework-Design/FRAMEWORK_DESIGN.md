# Part 2 - Framework Design

## Structure

```text
tests/
  web/
  mobile/
  api/
  integration/
pages/
  login_page.py
  dashboard_page.py
api/
  client.py
data/
  users.json
config/
  config.yaml
reports/
.github/workflows/tests.yml
```

## Design
- Python + pytest + Playwright
- Page Object Model for UI
- Requests/API client for backend testing
- Environment variables for credentials and tokens
- Configurable tenant, environment and browser
- BrowserStack for mobile/cross-platform tests
- GitHub Actions for CI/CD

## Missing requirements to confirm
1. How is test data created and cleaned?
2. How does 2FA work in test environments?
3. Which BrowserStack devices are required?
4. How many tests can run in parallel?
5. Which report format is required?
6. Which tests run on every pull request?
7. What are the Admin, Manager and Employee permissions?
8. What API status codes and error responses are expected?
