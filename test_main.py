import pytest
from main import APIClient


class TestAPIClient:

    @pytest.fixture(autouse=True)
    def setup(self, mocker):
        self.client = APIClient("http://test")
        self.mock_get_status = mocker.patch.object(
            self.client, "get_status", autospec=True
        )

    def test_check_capacity_full(self):
        self.mock_get_status.return_value = {"capacity": "Full"}
        assert self.client.check_capacity() == "No capacity"

    def test_check_capacity_available(self):
        self.mock_get_status.return_value = {"capacity": "Available"}
        assert self.client.check_capacity() == "Capacity available"

    def test_check_capacity_failed(self):
        self.mock_get_status.return_value = {"capacity": "Unknown"}
        assert self.client.check_capacity() == "Status check failed"
