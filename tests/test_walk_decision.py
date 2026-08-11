from models.walk_decision import WalkDecision

def test_walk_decision():
    decision = WalkDecision(
        recommendation="SHORT_WALK",
        duration_minutes=15,
        reasons=[
            "Air quality is acceptable",
            "No precipitation",
        ],
        risks=[
            "High humidity",
        ]
    )

    assert decision.recommendation == "SHORT_WALK"
    assert decision.duration_minutes == 15
    assert len(decision.reasons) == 2
    assert len(decision.risks) == 1