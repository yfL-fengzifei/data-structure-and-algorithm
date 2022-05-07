"""
script info:
name: greedy algorithm
"""


def boardcastCover():
    # 需要覆盖的所有州
    states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

    # 广播及其能够覆盖的州
    stations = {}
    stations["kone"] = set(["id", "nv", "ut"])
    stations["ktwo"] = set(["wa", "id", "mt"])
    stations["kthree"] = set(["or", "nv", "ca"])
    stations["kfour"] = set(["nv", "ut"])
    stations["kfive"] = set(["ca", "az"])

    # 最终保留的广播
    final_stations = set()

    while states_needed:
        # 当前最优广播
        best_station = None

        states_covered = set()

        for station, states_for_station in stations.items():
            # 广播能够覆盖的 剩余未覆盖的州中 的 州
            covered = states_needed & states_for_station

            # 找到能够尽可能多的覆盖未涉及州范围最广的广播
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered
        states_needed -= states_covered
        final_stations.add(best_station)

    return final_stations


if __name__ == '__main__':
    print(__doc__)

    print(boardcastCover())
