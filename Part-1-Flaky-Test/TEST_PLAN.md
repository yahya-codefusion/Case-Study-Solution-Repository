# Part 1 - Test Plan

| ID | Scenario | Expected Result |
|---|---|---|
| TC-01 | Valid Company1 login | Dashboard opens |
| TC-02 | Invalid password | Login error appears |
| TC-03 | Company2 login | Dashboard opens |
| TC-04 | Company2 projects | Only Company2 data appears |
| TC-05 | Dynamic loading | Elements are waited for |
| TC-06 | Tenant isolation | Company1 data is not visible to Company2 |

## Main risks
- Dynamic dashboard loading
- Slow CI/network
- 2FA
- Different browsers/viewports
- Empty project list causing false positives
