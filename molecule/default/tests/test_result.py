import testinfra


def test_os_release(host):
    """test host release for good measure"""

    assert host.file("/etc/os-release").contains("Ubuntu")


def test_postfix_running(host):
    """test ssh ssh_known_hosts file has been created,
    with the requested key types"""

    assert host.service("postfix").is_running


def test_postfix_dkim(host):
    """test ssh ssh_known_hosts file has been created,
    with the requested key types"""

    assert host.service("opendkim").is_running


def test_postfix_amavis(host):
    """test ssh ssh_known_hosts file has been created,
    with the requested key types"""

    assert host.service("amavis").is_running
