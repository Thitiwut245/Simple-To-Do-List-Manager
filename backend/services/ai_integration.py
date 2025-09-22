# simple rule-based categorizer (fast to integrate for demo)
KEYWORDS = {
    "shopping": ["buy","purchase","shop","order"],
    "work": ["email","report","meeting","deadline","office"],
    "study": ["read","study","homework","assignment","research","paper"],
}

def categorize_text(text: str) -> str:
    t = (text or "").lower()
    for cat, kws in KEYWORDS.items():
        for kw in kws:
            if kw in t:
                return cat
    return "general"
