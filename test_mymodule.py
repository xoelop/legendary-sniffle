from my_module import get_ip


def test_get_ip_type():
    ip = get_ip()
    assert isinstance(ip, str)

def test_get_ip_dots():
    ip = get_ip()
    assert ip.count('.') == 3