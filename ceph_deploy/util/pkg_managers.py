from ceph_deploy.lib.remoto import process


def apt(conn, package, *a, **kw):
    cmd = [
        'env',
        'DEBIAN_FRONTEND=noninteractive',
        'apt-get',
        '-q',
        'install',
        '--assume-yes',
        package,
    ]
    return process.run(
        conn,
        cmd,
        *a,
        **kw
    )


def apt_update(conn):
    cmd = [
        'apt-get',
        '-q',
        'update',
    ]
    return process.run(
        conn,
        logger,
        cmd,
    )


def yum(conn, package, *a, **kw):
    cmd = [
        'yum',
        '-y',
        '-q',
        'install',
        package,
    ]
    return process.run(
        conn,
        cmd,
        *a,
        **kw
    )


def rpm(conn, rpm_args=None, *a, **kw):
    """
    A minimal front end for ``rpm`. Extra flags can be passed in via
    ``rpm_args`` as an iterable.
    """
    rpm_args = rpm_args or []
    cmd = [
        'rpm',
        '-Uvh',
    ]
    cmd.extend(rpm_args)
    return process.run(
        conn,
        cmd,
        *a,
        **kw
    )
