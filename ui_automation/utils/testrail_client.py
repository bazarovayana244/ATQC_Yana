import requests
from requests.auth import HTTPBasicAuth

class TestRailClient:
    def __init__(self, base_url, username, api_key, run_id):
        self.base_url = base_url
        self.username = username
        self.api_key = api_key
        self.run_id = run_id
        self.case_ids = {}

    def fetch_run_tests(self):
        url = f"{self.base_url}/index.php?/api/v2/get_tests/{self.run_id}"

        response = requests.get(url, auth=HTTPBasicAuth(self.username, self.api_key))
        response.raise_for_status()

        data = response.json()

        if "tests" not in data:
            raise ValueError(f"Unexpected response from TestRail: {data}")

        tests = data["tests"]

        self.case_ids = {
            test["title"].replace(" ", "_").lower(): test["case_id"]
            for test in tests
        }

    def add_result_for_case(self, test_name, status_id, comment):
        if not self.case_ids:
            raise RuntimeError("Case ID mapping is empty. Call fetch_run_tests() first.")

        key = test_name.lower().strip()

        case_id = self.case_ids.get(key)
        if not case_id:
            raise ValueError(f"No matching TestRail case for test: {test_name}")

        url = f"{self.base_url}/index.php?/api/v2/add_result_for_case/{self.run_id}/{case_id}"
        payload = {"status_id": status_id, "comment": comment}

        response = requests.post(url, json=payload, auth=HTTPBasicAuth(self.username, self.api_key))
        response.raise_for_status()

        return response.json()
