import os
import re

from playwright.sync_api import Page, expect

BASE_URL = os.getenv("BASE_URL", "https://app.workflowpro.com")


def login(page: Page, email: str, password: str):
    page.goto(f"{BASE_URL}/login", wait_until="domcontentloaded")
    page.get_by_label("Email").fill(email)
    page.get_by_label("Password").fill(password)
    page.get_by_role("button", name="Login").click()

    # Wait for the real application state instead of using sleep().
    expect(page).to_have_url(re.compile(r".*/dashboard/?"), timeout=20000)
    expect(page.locator(".welcome-message")).to_be_visible(timeout=20000)


def test_user_login(page: Page):
    email = os.getenv("COMPANY1_EMAIL", "admin@company1.com")
    password = os.getenv("COMPANY1_PASSWORD")
    assert password, "COMPANY1_PASSWORD is not configured"

    login(page, email, password)
    expect(page.locator(".welcome-message")).to_be_visible()


def test_multi_tenant_access(page: Page):
    email = os.getenv("COMPANY2_EMAIL", "user@company2.com")
    password = os.getenv("COMPANY2_PASSWORD")
    assert password, "COMPANY2_PASSWORD is not configured"

    login(page, email, password)

    projects = page.locator(".project-card")
    expect(projects.first).to_be_visible(timeout=30000)

    count = projects.count()
    assert count > 0, "Expected at least one Company2 project"

    for index in range(count):
        project = projects.nth(index)
        expect(project).to_be_visible()
        assert "Company2" in project.inner_text(), (
            f"Unauthorized tenant data found: {project.inner_text()}"
        )
