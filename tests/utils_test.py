import pandas as pd
from app.utils import get_user_data

def test_get_user_data():
    """
    Test the get_user_data function
    """
    age = 35
    sex = "F"
    sick = "hypothyroid"
    tsh = 4.5
    t3 = 2.4
    tt4 = 120
    t4u = 1.2
    fti = 100
    
    expected_data = {"age": age,
                    "sex": sex,
                    "sick": sick,
                    "TSH": tsh,
                    "T3": t3,
                    "TT4": tt4,
                    "T4U": t4u,
                    "FTI": fti
                    }
    expected_features = pd.DataFrame(expected_data, index=[0])
    
    assert get_user_data(age, sex, sick, tsh, t3, tt4, t4u, fti).equals(expected_features)
