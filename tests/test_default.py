import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_services_running_and_enabled(Service):
    assert Service('prometheus-node-exporter').is_running
    assert Service('prometheus-node-exporter').is_enabled


def test_node_exporter_metrics(Command):
    out = Command.check_output('curl http://localhost:9100/metrics')
    assert 'process_cpu_seconds_total' in out
