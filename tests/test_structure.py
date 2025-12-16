from lanastance.structure import structure_features


def test_structure_features_output():
    text = """hello hello
    this is a test
    hello hello
    this is only a test
    """

    features = structure_features(text)

    assert isinstance(features, dict)

    assert "repetition_rate" in features
    assert "lexical_entropy" in features
    assert "line_end_similarity" in features

    for value in features.values():
        assert isinstance(value, float)

