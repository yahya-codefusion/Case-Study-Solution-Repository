# QA Automation Case Study

## Part 1 - Debugging Flaky Tests
- Identified timing, dynamic loading, 2FA, tenant loading and CI/browser issues.
- Replaced immediate assertions with Playwright `expect()` waits.
- Added project-count validation to avoid false positives.

## Part 2 - Framework Design
Designed a simple pytest + Playwright framework for:
- Web: Chrome, Firefox and Safari/WebKit
- Mobile: BrowserStack
- API testing
- Multiple tenants and user roles
- CI/CD with GitHub Actions

## Part 3 - API + UI Integration
Test flow:
1. Create project using API.
2. Verify project in web UI.
3. Validate mobile access through BrowserStack concept.
4. Verify tenant isolation.

## Setup

```bash
pip install -r requirements.txt
playwright install
```

Set credentials through environment variables. Never commit real passwords or tokens.

## Run

```bash
pytest
pytest --html=reports/test-report.html --self-contained-html
```

See `Part-1-Flaky-Test`, `Part-2-Framework-Design`, and `Part-3-Integration-Test` for the complete solution.
