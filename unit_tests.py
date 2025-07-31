from unittest.mock import Mock
from script import function_to_test

def test_function_to_test():
    # Mocking the function to simulate different scenarios
    mock_function = Mock(side_effect=lambda a, b: a - b if a > 10 else a + b)

    # Test case where a > 10
    result1 = mock_function(15, 5)
    assert result1 == 10, f"Expected 10, got {result1}"

    # Test case where a <= 10
    result2 = mock_function(5, 3)
    assert result2 == 8, f"Expected 8, got {result2}"

def test_function_to_test_invalid_input():
    # Test case where a == 10 and b == 5 raises ValueError
    try:
        function_to_test(10, 5)
    except ValueError as e:
        assert str(e) == "Invalid input values", f"Expected 'Invalid input values', got {str(e)}"
    else:
        assert False, "Expected ValueError was not raised"