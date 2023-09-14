from app import change


def test_change():
    assert [{2: '50 centimos'}, {1: '20 centimos'}, {1: '10 centimos'}, {2: '2 centimos'}] == change(1.34)