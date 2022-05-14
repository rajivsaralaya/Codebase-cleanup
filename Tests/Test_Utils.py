#tests/test_utils.py file

#def test_answer():
    #assert inc(3) == 5
    
from app.utils import to_usd
    
    
    
    def test_to_usd():
        # rounding to 2 decimals and have dollar sighn
        assert to_usd(0.45555) == "$0.46"
        
        #large numbers should have comma as separator
        assert to_usd(123456789.98) == "$123,456,789.98"