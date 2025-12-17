from lanastance.pronouns import pronoun_features


def test_pronoun_features_basic_counts():
    text = "I love you but you love me"

    features = pronoun_features(text)

    assert isinstance(features, dict)
    assert features["first_person_rate"] >= 0
    assert features["second_person_rate"] >= 0
    assert features["third_person_rate"] >= 0

