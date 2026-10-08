from mth5.mth5 import MTH5

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
    with MTH5() as mth5_object:
        mth5_object.open_mth5(r"tesis_geofisica_test.h5", "a")

    #survey_group = mth5_object.add_survey("example")
    #
    #station_group = mth5_object.add_station("mt001", survey="example")
    #station_group = survey_group.stations_group.add_station("mt002")
    #station_group.metadata.location.latitude = "40:05:01"
    #station_group.metadata.location.longitude = -122.3432
    #station_group.metadata.location.elevation = 403.1
    #station_group.metadata.acquired_by.author = "me"
    #station_group.metadata.orientation.reference_frame = "geomagnetic"
    #
    #station_group.write_metadata()
    #
    #run_01 = mth5_object.add_run("mt002", "001", survey="example")
    #run_02 = station_group.add_run("002")
    #
    #ex = mth5_object.add_channel("mt002", "001", "ex", "electric", None, survey="example")
    #hy = run_01.add_channel("hy", "magnetic", None)
    #tf = station_group.transfer_functions_group.add_transfer_function("tf01")
    #fcs = station_group.fourier_coefficients_group.add_fc_group("fc01")
    #
    #print(mth5_object)

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
    else:
        print('not order')

