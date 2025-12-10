import requests
from requests.auth import HTTPBasicAuth

class TestRailClient:
    def __init__(self, base_url, username, api_key, run_id, case_ids=None):
        self.base_url = base_url.rstrip("/")
        self.username = username
        self.api_key = api_key
        self.run_id = run_id
        self.case_ids = case_ids or {}

    def add_result_for_case(self, test_name, status_id, comment):
        case_id = self.case_ids.get(test_name)
        if not case_id:
            raise ValueError(f"No case_id found for test: {test_name}")

        url = f"{self.base_url}/index.php?/api/v2/add_result_for_case/{self.run_id}/{case_id}"
        payload = {"status_id": status_id, "comment": comment}

        response = requests.post(url, json=payload, auth=HTTPBasicAuth(self.username, self.api_key))
        response.raise_for_status()
        return response.json()

