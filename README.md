# Relay AI

A small, local customer-support assistant demo built with Streamlit. The assistant
uses deterministic response rules and does not connect to customer accounts,
payments, tracking systems, or external AI services.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Streamlit prints a local URL, usually <http://localhost:8501>.

Run the tests with:

```bash
pytest -q
```

## Customer-message review

The initial test set highlighted three improvement areas:

1. **Grounding:** the assistant must not claim to have checked an order or account
   when it has no system connection.
2. **Clarification:** broad or incomplete messages need a useful follow-up instead
   of a generic or guessed answer.
3. **Privacy and escalation:** account/payment issues need safe information
   boundaries, and a request for a person should be recognized.

The implemented improvement addresses these issues with intent-specific replies,
explicit limitations, safe information requests, clarification, and a handoff flag
for human requests. The tests cover new customer messages for these paths.

This is a demo, not a production support service: it does not create tickets or
perform a real human handoff.
