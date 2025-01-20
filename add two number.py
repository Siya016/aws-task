def lambda_handler(event, context=None):
    """
    Function to add two numbers.
    Simulates AWS Lambda's `event` and `context` structure.
    """
    try:
        # Retrieve numbers from the event
        num1 = event.get('num1', 0)
        num2 = event.get('num2', 0)

        # Validate that inputs are numbers
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            return {
                "statusCode": 400,
                "message": "Both 'num1' and 'num2' must be numbers."
            }

        # Add the numbers
        result = num1 + num2

        # Return the result
        return {
            "statusCode": 200,
            "message": "Success",
            "result": result
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "message": f"An error occurred: {str(e)}"
        }

# Test the function locally
if __name__ == "__main__":
    # Simulate an event with numbers
    event = {"num1": 5, "num2": 7}
    response = lambda_handler(event)
    print(response)
