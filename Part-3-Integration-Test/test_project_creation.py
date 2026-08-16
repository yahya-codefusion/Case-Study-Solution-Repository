import os
import re

from playwright.sync_api import Page, expect

from api_client import APIClient


def test_project_creation_flow(page: Page):
    """API -> Web UI -> mobile concept -> tenant isolation.

    BrowserStack mobile execution uses the same assertions in a mobile
    project/device configuration; credentials are never stored in code.
    """
    api = APIClient(
        os.environ["API_BASE_URL"],
        os.environ["API_TOKEN"],
        os.environ["COMPANY1_TENANT_ID"],
    )

    project = api.create_project(
        name="QA Automation Project",
        description="Created by integration test",
    )

    assert project["name"] == "QA Automation Project"
    assert project["status"] == "active"
    project_name = project["name"]

    # Web UI verification.
    page.goto(
        f"{os.environ['WEB_BASE_URL']}/login",
        wait_until="domcontentloaded",
    )
    page.get_by_label("Email").fill(os.environ["COMPANY1_EMAIL"])
    page.get_by_label("Password").fill(os.environ["COMPANY1_PASSWORD"])
    page.get_by_role("button", name="Login").click()

    expect(page).to_have_url(
        re.compile(r".*/dashboard/?"), timeout=20000
    )

    project_card = page.locator(".project-card").filter(
        has_text=project_name
    )
    expect(project_card).to_be_visible(timeout=30000)

    # Mobile validation is configured as a BrowserStack project/device.
    # The same project assertion should be executed there.


def test_company2_cannot_see_company1_project(page: Page):
    """Validate tenant isolation at the UI layer."""
    project_name = "QA Automation Project"

    page.goto(
        f"{os.environ['WEB_BASE_URL']}/login",
        wait_until="domcontentloaded",
    )
    page.get_by_label("Email").fill(os.environ["COMPANY2_EMAIL"])
    page.get_by_label("Password").fill(os.environ["COMPANY2_PASSWORD"])
    page.get_by_role("button", name="Login").click()

    expect(page).to_have_url(
        re.compile(r".*/dashboard/?"), timeout=20000
    )

    project_card = page.locator(".project-card").filter(
        has_text=project_name
    )
    expect(project_card).to_have_count(0)
