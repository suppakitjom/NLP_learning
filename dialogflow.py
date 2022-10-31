def detect_intent(text):
    """Returns the result of detect intent with texts as inputs.

    Using the same `session_id` between requests allows continuation
    of the conversation."""
    from google.cloud import dialogflow
    project_id = 'nlp-test-lpgo'
    session_id = '123456789'
    language_code = 'en'
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    # print("Session path: {}\n".format(session))

    text_input = dialogflow.TextInput(text=text, language_code=language_code)

    query_input = dialogflow.QueryInput(text=text_input)

    response = session_client.detect_intent(request={
        "session": session,
        "query_input": query_input
    })

    # print("Query text: {}".format(response.query_result.query_text))
    print("---- Detected intent: {} (confidence: {}) ----".format(
        response.query_result.intent.display_name,
        response.query_result.intent_detection_confidence,
    ))
    feedback = 'Could not detect intent'
    if response.query_result.intent.display_name == "Add":
        n1 = float(response.query_result.parameters['number1'])
        n2 = float(response.query_result.parameters['number2'])
        feedback = ("{} + {} equals to {}".format(n1, n2, n1 + n2))
    elif response.query_result.intent.display_name == "Subtract":
        n1 = float(response.query_result.parameters['number1'])
        n2 = float(response.query_result.parameters['number2'])
        feedback = ("{} - {} equals to {}".format(n1, n2, n1 - n2))
    elif response.query_result.intent.display_name == "Multiply":
        n1 = float(response.query_result.parameters['number1'])
        n2 = float(response.query_result.parameters['number2'])
        feedback = ("{} × {} equals to {}".format(n1, n2, n1 * n2))
    elif response.query_result.intent.display_name == "Divide":
        n1 = float(response.query_result.parameters['number1'])
        n2 = float(response.query_result.parameters['number2'])
        feedback = ("{} ÷ {} equals to {}".format(n1, n2, n1 / n2))

    return feedback


# detect_intent(text='Sum of 5 and 8')
