from mth5.mth5 import MTH5

from scripts import modem

import sys

def create():
    m = MTH5()
    h5_path = "tesis_geofisica_test.h5"
    m.open_mth5(h5_path, mode="w")
    survey_group = m.add_survey("campana_test_2026")
    station_group = m.add_station("MT001", survey="campana_test_2026")
    run_group = m.add_run("MT001", "001", survey="campana_test_2026")

    m.close_mth5()

    print(f"¡Listo! Archivo MTH5 creado con éxito en: {h5_path}")

def read():
    with MTH5() as m:
        m.open_mth5(r"tesis_geofisica_test.h5", "a")
        survey1 = m.get_survey("campana_test_2026")
        print(survey1)
        print(survey1.groups_list)

        m.close_mth5()
        

def download_data():
    import pandas as pd
    from mth5.clients import FDSN
    
    from obspy.clients.fdsn import Client
    client = Client("IRIS")
    inventory = client.get_stations(
        network="US",
        station="*",
        level="channel"
    )
    info = ""
    MT_CHANNELS = ["LFE", "LFN", "LFH", "LQE", "LQN", "LQH"]
    SEISMIC_CHANNELS = ["BHE", "BHN", "BHH"]
    for network in inventory:
        for station in network:
            for channel in station:
                if channel.code in MT_CHANNELS:
                    print(
                        "channel code: ", channel.code,
                        "inicio:", channel.start_date,
                        "fin:", channel.end_date
                    )
                elif channel.code in SEISMIC_CHANNELS:
                    print(
                        "station code: ", station.code,
                        "\nchannel code: ", channel.code,
                        "inicio:", channel.start_date,
                        "fin:", channel.end_date
                    )

    #request = pd.DataFrame({
    #    "network": ["US"],
    #    "station": ["BLA"],
    #    "location": [""],
    #    "channel": ["BHE"],
    #    "start": ["1995-05-08T00:00:00.000000Z"],
    #    "end": ["1996-07-10T00:00:00.000000Z"],
    #})

    #client = FDSN(
    #    mth5_filename="tesis_geofisica_test.h5",
    #    client="IRIS"
    #)

    #client.make_mth5_from_fdsn_client(request)
    #print("download completed")

def data():
    pass

def target():
    pass

if len(sys.argv) > 1:
    do = sys.argv[1]
    if do == 'create':
        create()
    elif do == 'read':
        read()
    elif do == 'data':
        data()
    elif do == 'target':
        target()
    elif do == 'down':
        download_data()
    elif do == 'modem':
        modem.start()
    else:
        print('not order')

