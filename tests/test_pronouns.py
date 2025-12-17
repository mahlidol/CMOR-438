from lanastance.pronouns import pronoun_features


def test_pronoun_features_runs():
    text = "I love you and you love me"

    features = pronoun_features(text)

    assert isinstance(features, dict)
    assert "first_person_rate" in features
    assert "second_person_rate" in features
