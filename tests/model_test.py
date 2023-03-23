import joblib

def test_model():
    """
    Test the model
    """
    model = joblib.load("/workspaces/euthyroid_diagnostic_support_app/models/RandomForestClassifier.sav")
    sick= [[45, 0, 0, 1.9, 1.0,	82.0,	0.73,	112.0]]
    not_sick = [[49, 0, 0, 0.8,	2.4,123.0,	0.99,	124.0]]
    assert model.predict(sick)[0] == 1
    assert model.predict(not_sick)[0] == 0