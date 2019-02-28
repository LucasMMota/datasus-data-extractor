def build_file_path(system, type, date, state):
    filename = type + state + date + '.dbc'
    # todo verificar os paths dos sistemas
    path = '/dissemin/publicos/'+system+'/200801_/Dados/'

    return path, filename
