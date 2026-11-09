from support_agent import respond


def test_order_status_does_not_invent_tracking_details():
    reply = respond("My package is late, where is it?")

    assert reply.category == "order status"
    assert "can't access live order tracking" in reply.message
    assert "order number" in reply.message


def test_billing_reply_protects_payment_information():
    reply = respond("I was charged twice")

    assert reply.category == "billing"
    assert "full number" in reply.message


def test_human_request_is_flagged_for_handoff():
    reply = respond("I want to speak to a human")

    assert reply.category == "human handoff"
    assert reply.needs_human is True


def test_incomplete_message_gets_clarification():
    reply = respond("help")

    assert reply.category == "clarification"
    assert "which support topic" in reply.message


def test_empty_message_gets_prompt_to_explain():
    reply = respond("  ")

    assert reply.category == "clarification"
    assert "what you need help with" in reply.message


def test_account_reply_never_asks_for_password():
    reply = respond("I can't log in to my account")

    assert reply.category == "account access"
    assert "without sharing your password" in reply.message
