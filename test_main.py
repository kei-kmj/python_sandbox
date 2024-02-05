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

    @pytest.mark.parametrize("capacity", ["Few left", "Limited availability", "Available"])
    def test_check_capacity_available(self, capacity):
        self.mock_get_status.return_value = {"capacity": capacity}
        assert self.client.check_capacity() == "Capacity available"

    def test_check_capacity_failed(self):
        self.mock_get_status.return_value = {"capacity": "Unknown"}
        assert self.client.check_capacity() == "Status check failed"
