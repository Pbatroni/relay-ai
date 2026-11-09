"""Grounded, deterministic response rules for the Relay AI demo."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Reply:
    message: str
    category: str
    needs_human: bool = False


def respond(message: str) -> Reply:
    """Return a safe next step without claiming access to customer accounts."""
    text = " ".join(message.lower().split())
    if not text:
        return Reply(
            "Tell me a little about what you need help with, and I'll guide you.",
            "clarification",
        )

    if any(phrase in text for phrase in ("human", "person", "agent", "representative")):
        return Reply(
            "I can flag this for a support teammate. Please share a short description "
            "of the issue. Don't include passwords or full payment-card details.",
            "human handoff",
            needs_human=True,
        )

    if any(word in text for word in ("charged", "charge", "payment", "billing", "invoice")):
        return Reply(
            "I can help route a billing issue, but I can't view your account or verify "
            "a charge here. Please describe the charge and its date, and include only "
            "the last four digits of a card if needed—never the full number.",
            "billing",
        )

    if any(word in text for word in ("return", "refund", "exchange")):
        return Reply(
            "I can help with a return or refund request, but I can't confirm eligibility "
            "without the order details and the applicable policy. Share the item and "
            "approximate purchase date; omit payment details.",
            "returns",
        )

    if any(word in text for word in ("order", "delivery", "shipment", "tracking", "package")):
        return Reply(
            "I can't access live order tracking in this demo. Please check the tracking "
            "link in your order confirmation, or share your order number (not payment "
            "details) so a support teammate can look into it.",
            "order status",
        )

    if any(word in text for word in ("password", "login", "sign in", "locked", "account")):
        return Reply(
            "For account access, use the password-reset link on the official sign-in "
            "page. I can't reset accounts here; if that doesn't work, tell me the "
            "error message without sharing your password or verification code.",
            "account access",
        )

    if any(word in text for word in ("broken", "error", "not working", "issue", "problem")):
        return Reply(
            "I'm sorry that isn't working. What were you trying to do, and what "
            "happened instead? Please leave out passwords, verification codes, and "
            "payment details.",
            "troubleshooting",
        )

    return Reply(
        "I'm not sure which support topic this is about. Is it an order, billing, "
        "return, account-access, or product issue? Please don’t share sensitive "
        "account or payment information.",
        "clarification",
    )
