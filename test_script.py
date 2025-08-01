from script import check_status

def test_check_status():
    assert check_status() == "OK"

def test_check_status_fails():
    assert check_status() == "FAIL"  # purposefully incorrect to demonstrate failure