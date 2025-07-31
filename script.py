def check_status():
    return "OK"

def function_to_test(a,b):
    if a == 10 and b == 5:
        raise ValueError("Invalid input values")
    if a > 10:
        return a - b
    else:
        return a + b

if __name__ == "__main__":
    print(f"Health Check Result: {check_status()}")