from .models import TaskManager, Prefijo
import tabula

def _testInicio(item):
    data = TaskManager.objects.get(id__exact=item)
    salida = './media/' + str(data.taskFile).split('.')[0] + '.csv'
    
    try:
        tabula.convert_into(data.taskFile, salida, output_format="csv", pages='all')
    except ValueError:
        print(ValueError)

    import csv
    with open(salida, 'r') as file:
        reader = csv.reader(file)
        i = 0
        a = 0
        resol = ""
        name = ""
        cc = ""
        dv = ""
        data = []
        for row in reader:
            for col in range(len(row)):
                if row[col].split(' ')[0] != '30.':
                   if row not in data:
                      data.append(row)

            for j in range(len(row)):
                paso = 0
                lista = row[j].split(' ')
                for k in range(len(lista)):
                    if lista[k] == '4.':
                       if resol == '':
                            if len(row[j].split(' ')) == 5:
                                r = row[j].split(' ')
                                resol = r[len(row[j].split(' ')) - 1]
                            else:
                                resol = row[j + 1]
                    elif lista[k] == '1001.':
                        name = lista[k + 4] + ' ' + lista[k + 5] + ' ' + lista[k + 6] + ' ' + lista[k + 7]
                    elif lista[k] == '1002.':
                        if lista[k + 4] == '1003.':
                            paso = 1
                            for character in row[j + 1].split(' '):
                                cc += character
                    elif lista[k] == '1003.':
                        if paso == 0:
                            for character in range(3, len(lista)):
                                cc += lista[character]
                    elif lista[k] == '1004.':
                        if len(lista) == 2:
                            fila = row[j + 1].split(' ')
                            dv = fila[len(fila) - len(fila)]
                        elif len(lista) == 3:
                            dv = lista[len(lista) - 1]

            i += 1

        log = []
        k = len(data)
        pref = ''
        fecha_ini = ''
        nro_ini = ''
        nro_fin = ''
        res = ''
        vigencia = ''
        for d in range(k):
            if d == 23 or d == 24 or d == 25:
                for f in range(len(data[d])):
                    fecha = data[d][f].split(' ')
                    if fecha[0] == '997.':
                        if len(fecha) == 3:
                            fval = data[d][f + 1].split(' ')
                            for date_ini in range(len(fval)):
                                if date_ini < 8:
                                    fecha_ini += fval[date_ini]
                        else:
                            for date_ini in range(3, len(fecha)):
                                if date_ini < 11:
                                    fecha_ini += fecha[date_ini]

            if d == 34 or d == 36 or d == 39:
                for m in range(len(data[d])):
                    if m == 2 and data[d][m] != '':
                        vigencia = data[d][4].split(' ')[0]
                        res = data[d][m].split(' ') 
                        if len(res) > 3:
                            pref =  res[1]
                            nro_ini = res[2]
                            nro_fin = res[3]

                        elif len(res) > 0 or len(res) < 3:
                            if len(res) == 1:
                                pref =  res[0]
                            else:
                                pref =  res[1]

                        vigencia = vigencia
                        nro_ini = nro_ini.replace(',', '')
                        nro_fin = nro_fin.replace(',', '')

                        if nro_ini != '' or nro_fin != '':
                            if pref not in log:
                                log.append(pref)
                                savePref(item, pref, resol, fecha_ini, vigencia, nro_ini, nro_fin)


                    elif m == 3 and data[d][m] != '':
                        vigencia = data[d][4].split(' ')[0]
                        res = data[d][m].split(' ')
                        if len(res) == 3:
                            pref =  res[0]
                            nro_ini = res[1]
                            nro_fin = res[2]
                        elif len(res) > 3:
                            pref =  res[1]
                            nro_ini = res[2]
                            nro_fin = res[3]
                        elif len(res) > 0 or len(res) < 3:
                            nro_ini = res[0]
                            nro_fin = res[1]

                        vigencia = vigencia
                        nro_ini = nro_ini.replace(',', '')
                        nro_fin = nro_fin.replace(',', '')

                        if pref not in log:
                            log.append(pref)
                            savePref(item, pref, resol, fecha_ini, vigencia, nro_ini, nro_fin)

def savePref(item, prefi, resol, f_ini, vigen, num_ini, num_fin):
    print('id_res:', item)
    print('prefijo:', prefi)
    print('resolucion:', resol)
    print('fecha ini:', f_ini)
    print('vigencia:', vigen)
    print('nro ini:', num_ini)
    print('nro_fin:', num_fin)
    print('----------------------')
    
    prefijo = Prefijo.objects.create(
        id_task = item,
        prefijo = prefi,
        fecha_ini_pref = f_ini,
        vigencia_pref = vigen,
        nro_ini_pref = num_ini,
        nro_fin_pref = num_fin,
        resolucion_pref = resol,
    )


