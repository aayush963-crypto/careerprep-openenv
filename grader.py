def grade_response(response: str, expected_keywords: list) -> float:
    response_lower = response.lower()
    matches = sum(1 for keyword in expected_keywords if keyword.lower() in response_lower)
    return matches / len(expected_keywords)