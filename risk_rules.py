def analyze_risks(clauses):
    results = []
    total_score = 0
    max_score = len(clauses) * 3

    for clause in clauses:
        clause_lower = clause.lower()

        if "terminate" in clause_lower or "termination" in clause_lower:
            level = "HIGH"
            score = 3
            reason = "Unilateral or sudden termination risk"

        elif "penalty" in clause_lower or "fine" in clause_lower:
            level = "HIGH"
            score = 3
            reason = "Financial penalty clause"

        elif "liability" in clause_lower or "indemnify" in clause_lower:
            level = "MEDIUM"
            score = 2
            reason = "Legal liability exposure"

        elif "confidential" in clause_lower:
            level = "LOW"
            score = 1
            reason = "Confidentiality obligation"

        else:
            continue

        total_score += score

        results.append({
            "clause": clause,
            "level": level,
            "reason": reason
        })

    return results, total_score, max_score
