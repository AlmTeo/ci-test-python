from script import check_status
from site_pinger import check_status

def test_check_status():
    assert check_status() == "OK"

# Down site example: http://imgbb.com/
# Up site example: https://www.google.com/
def test_check_status_success():
    result = check_status("https://www.google.com/")
    assert result == "UP"