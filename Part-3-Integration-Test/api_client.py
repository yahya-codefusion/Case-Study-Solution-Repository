import requests


class APIClient:
    def __init__(self, base_url, token, tenant_id):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {token}",
            "X-Tenant-ID": tenant_id,
        })

    def create_project(self, name, description, team_members=None):
        response = self.session.post(
            f"{self.base_url}/api/v1/projects",
            json={
                "name": name,
                "description": description,
                "team_members": team_members or [],
            },
            timeout=30,
        )
        response.raise_for_status()
        return response.json()
