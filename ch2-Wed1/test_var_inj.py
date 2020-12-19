from variable_injctn  import injection

def test_inject():
    assert injection("Any",True,6) == 'Any,True,6'
    assert injection('December',False,19,20.20) != "December,True,19,20.20"
    assert injection('Vi',5,'ual',5.1,'udi',0,'c',0,'de') != "Visual studio code"
    assert injection(True, 28, 7.900) == "True,28,7.900"