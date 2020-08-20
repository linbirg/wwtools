# 获取当前主机对外的链接情况

import psutil as pu


def ll_pids():
    return pu.pids()


def pp_pid(pid):
    return pu.Process(pid)


def find_by_name(name, pids=None):
    if pids is None:
        pids = ll_pids()

    trgs = []

    for pid in pids:
        pinfo = pp_pid(pid)
        # print(pinfo.name)
        if not pinfo.name() == name:
            continue

        trgs.append(pinfo)

    return trgs


def ll_all_established_conns(process):
    conns = process.connections()
    if not conns or len(conns) <= 0:
        return []

    est_conns = []
    for c in conns:
        status = c.status
        if not status == 'ESTABLISHED':
            continue

        est_conns.append(c)

    return est_conns


def ll_est_tcps_by_name(name, pids=None):
    processes = find_by_name(name, pids)

    est_conns = []

    for p in processes:
        est_conn = ll_all_established_conns(p)
        if est_conn:
            est_conns += est_conn

    return est_conns


if __name__ == '__main__':
    est_conns = ll_est_tcps_by_name('QQMusic.exe')
    print("len of est_conns:", len(est_conns))
    print(est_conns)
