from IPython.display import Javascript

def copy_to_clipboard(text):
    # Escape single and double quotes in the text
    escaped_text = text.replace("'", "\\'").replace('"', '\\"')
    
    # Execute JavaScript to copy the escaped text to the clipboard
    display(Javascript(f'''
        const el = document.createElement('textarea');
        el.value = `{escaped_text}`;
        document.body.appendChild(el);
        el.select();
        document.execCommand('copy');
        document.body.removeChild(el);
    '''))
    
    print(f'Copied to clipboard:\n{text}')


def node_valuation():
    
    while True:
        try: 
            nod_l = input('Longitudinal measure: ')
            nod_ap = input('Antero-posterior measure: ')
            nod_t = input('Transversal measure: ')
            if nod_l and nod_ap and nod_t:
                nod_l = float(nod_l.replace(',','.'))
                nod_ap = float(nod_ap.replace(',','.'))
                nod_t = float(nod_t.replace(',','.'))
                node_vol = nod_l * nod_ap * nod_t * 0.52
                node_measure = f'{nod_l} x {nod_ap} x {nod_t} cm, com volume nodular de {node_vol:.2f} ml'
                break
            elif nod_l and nod_ap and not nod_t:
                node_measure = f'{nod_l} x {nod_ap} cm'
                break
            elif nod_l and nod_t and not nod_ap: 
                node_measure = f'{nod_l} x {nod_t} cm'
                break
            elif nod_ap and nod_t and not nod_l:    
                node_measure = f'{nod_ap} x {nod_t} cm'
                break
        except:
            print('Digite pelo menos 2 medidas')
            
    while True:
        try:
            side = int(input('Topography: 1. LTD, 2. LTE, 3. istmo (type the number according to your selection): '))
            if side == 1:
                side = 'lobo direito'
                break
            elif side == 2:
                side = 'lobo esquerdo'
                break
            elif side == 3:
                side = 'istmo'
                break
        except: 
            print('Type a valid number')
        
    while True:
        try: 
            position = int(input('Position: 1. Superior third, 2. Medial third, 3. Inferior third'))
            if position == 1:
                position = 'terço superior'
                break
            elif position == 2:
                position = 'terço médio'
                break
            elif position == 3:
                position = 'terço inferior'
                break
        except: 
            print('Type a valid number')
   
    while True:
        try: 
            aspect = int(input('Aspect: 1. Solid, 2. Solid-Cystic, 3. Cystic bigger than solid, 4. Spongiform, 5. Cystic: '))
            if aspect == 1:
                aspect = 'sólido'
                aspect_pt = 2
                break
            elif aspect == 2: 
                aspect = 'sólido-cístico'
                aspect_pt = 1
                break
            elif aspect == 3: 
                aspect = 'componente cístico maior do que sólido'
                aspect_pt = 0
                break
            elif aspect == 4:
                aspect = 'espongiforme'
                aspect_pt = 0
                break
            elif aspect == 5:
                aspect = 'cístico'
                aspect_pt = 0
                break
        except: 
            print('Type a valid number')
    
    while True:
        try: 
            echo = int(input('Echogenicity: 1. Hipo, 2. Iso, 3. Hiper, 4. Very hipo, 5. Ane: '))
            if echo == 1:
                echo = 'hipoecogênico'
                echo_pt = 2
                break
            elif echo == 2:
                echo = 'isoecogênico'
                echo_pt = 1
                break
            elif echo == 3: 
                echo = 'hiperecogênico'
                echo_pt = 1
                break
            elif echo == 4: 
                echo = 'muito hipoecogênico'
                echo_pt = 3
                break
            elif echo == 5: 
                echo = 'anecóico'
                echo_pt = 0
                break
        except: 
            print('Type a valid number')
        
    while True:
        try: 
            shape = int(input('Shape: 1. Wider than tall, 2. Taller than wide: '))
            if shape == 1:
                shape = 'eixo horizontal maior que o vertical'
                shape_pt = 0
                break
            elif shape == 2: 
                shape = 'eixo vertical maior que o horizontal'
                shape_pt = 3
                break
        except: 
            print('Type a valid number')
        
    while True: 
        try: 
            margin = int(input('Margin: 1. Smooth, 2. Ill defined, 3. Lobulated, 4. Irregular, 5. Extra-thyroidal extention: '))
            if margin == 1: 
                margin = 'de contornos bem delimitados'
                margin_pt = 0
                break
            elif margin == 2:
                margin = 'de contornos pouco nítidos'
                margin_pt = 0
                break
            elif margin == 3: 
                margin = 'de contornos lobulados'
                margin_pt = 2
                break
            elif margin == 4:
                margin = 'de contornos irregulares'
                margin_pt = 2
                break
            elif margin == 5: 
                margin = 'com extensão extra-tireodiana'
                margin_pt = 3
                break
        except: 
            print('Type a valid number')
    
    while True:
        try: 
            echogenic_foci = int(input('Echogenic foci: 1. None, 2. Comet tail artifact, 3. macrocalcification, 4. Complete peripheral calcification, 5. Incomplete peripheral calcification, 6. Microcalcification: '))
            if echogenic_foci == 1: 
                echogenic_foci = 'sem focos ecogênicos'
                echogenic_foci_pt = 0
                break 
            elif echogenic_foci == 2: 
                echogenic_foci = 'com artefatos ecogênicos em cauda de cometa'
                echogenic_foci_pt = 0
                break
            elif echogenic_foci == 3: 
                echogenic_foci = 'com a presença de macrocalcificações'
                echogenic_foci_pt = 1
                break
            elif echogenic_foci == 4: 
                echogenic_foci = 'com calcificação periférica completa'
                echogenic_foci_pt = 0
                break
            elif echogenic_foci == 5: 
                echogenic_foci = 'com calcificação periférica incompleta'
                echogenic_foci_pt = 2
                break
            elif echogenic_foci == 6:
                echogenic_foci = 'com a presença de microcalcificações'
                echogenic_foci_pt = 3
                break
        except: 
            print('Type a valid number')
    
    tirads = aspect_pt + echo_pt + shape_pt + margin_pt + echogenic_foci_pt
    if tirads <= 1: 
        acr_tirads = 1
    elif tirads == 2: 
        acr_tirads = 2
    elif tirads == 3:
        acr_tirads = 3
    elif tirads >= 4 and tirads <= 6: 
        acr_tirads = 4
    elif tirads >= 7: 
        acr_tirads = 5
    
    while True:
        try: 
            doppler = input('Doppler: 1. Ausência de fluxo, 2. Exclusivamente periférico, 3. Predominantemente periférico, 4. Predominantemente central, 5. Central exuberante: ')
            if doppler == '':
                doppler = ''
                break
            else:
                doppler = int(doppler)
                if doppler == 1: 
                    doppler = 'Ausência de fluxo ao Doppler (Chammas I).'
                    break
                else:
                    ir = input('Type the resistance index: ')
                    if ir:
                        ir = f'IR {ir}'
                    if doppler == 2:
                        doppler = f'Vascularização exclusivamente periférica ao Doppler (Chammas II). {ir}'
                        break
                    elif doppler == 3:
                        doppler = f'Vascularização predominantemente periférica ao Doppler (Chammas III). {ir}'
                        break
                    elif doppler == 4:
                        doppler = f'Vascularização predominantemente central ao Doppler (Chammas IV). {ir}'
                        break
                    elif doppler == 5:
                        doppler = f'Vascularização central exuberante ao Doppler (Chammas V). {ir}'
                        break
                    else:
                        print('Digite um número válido')
        except:
            print('Digite um número válido')
        
    node = f'Localizado no {side}, {position}, medindo {node_measure}, de aspecto {aspect}, {echo}, com {shape}, {margin}, {echogenic_foci}. ACR-TIRADS {acr_tirads}. {doppler}'
    return node, doppler
    

while True: 
    try:
        aspecto_glandular = int(input('Qual ecogenicidade glandular: 1. Homogênea, 2. Heterogênea: '))
        if aspecto_glandular == 1: 
            aspecto_glandular = 'homogênea'
            break
        elif aspecto_glandular == 2: 
            aspecto_glandular = 'heterogênea'
            break
    except: 
        print('Digite um número válido')

while True:
    try:
        contorno_glandular = int(input('Contorno glandular: 1. Regular, 2. Lobulado, 3. Irregular: '))
        if contorno_glandular == 1: 
            contorno_glandular = 'regulares'
            break
        elif contorno_glandular == 2: 
            contorno_glandular = 'lobulados'
            break
        elif contorno_glandular == 3:
            contorno_glandular = 'irregulares'
    except: 
        print('Digite um número válido')

while True:
    try:
        ltd_l = input('LTD_l: ')
        ltd_ap = input('LTD_ap: ')
        ltd_t = input('LTD_t: ')
        lte_l = input('LTE_l: ')
        lte_ap = input('LTE_ap: ')
        lte_t = input('LTE_t: ')

        if ltd_l and ltd_ap and ltd_t and lte_l and lte_ap and lte_t: 
            ltd_l = float(ltd_l.replace(',','.'))
            ltd_ap = float(ltd_ap.replace(',','.'))
            ltd_t = float(ltd_t.replace(',','.'))
            lte_l = float(lte_l.replace(',','.'))
            lte_ap = float(lte_ap.replace(',','.'))
            lte_t = float(lte_t.replace(',','.'))
            volume_ltd = ltd_l * ltd_ap * ltd_t *0.52
            volume_ltd = round(volume_ltd,2)
            volume_lte = lte_l * lte_ap * lte_t *0.52
            volume_lte = round(volume_lte,2)
            volume_total = volume_ltd + volume_lte        
            
            if volume_total > 15:
                volume_glandular = 'aumentado'
            elif volume_total > 5 and volume_total <= 15:
                volume_glandular = 'normal'
            elif volume_total <=5:
                volume_glandular = 'reduzido'

            break
    except:
        print('Digite as medidas corretamente')

while True:
    istmo_ap = input('Istmo(digite f se filiforme): ').lower()
    try: 
        if istmo_ap == 'f':
            istmo_ap = 'filiforme'
            break
        else: 
            istmo_ap = float(istmo_ap.replace(',','.'))
            istmo_ap = str(istmo_ap) + ' ml'
            break
    except: 
        print('Digite novamente a atribuição ao istmo. f se filiforme ou a medida antero-posterior')        
        
while True: 
    try:
        node_presence = int(input('Há formações nodulares: 1. Sim, 2. Não: '))
        if node_presence == 1: 
            node_presence = ', com a presença das formações nodulares descritas abaixo.'
            while True:
                try: 
                    node_numbers = int(input('Quantos nódulos estão presentes: '))
                    break
                except:
                    print('Digite um número válido')

            nodes = []    
            for i in range(node_numbers):
                i += 1
                node = f'- N{i}: {node_valuation()[0]}\n'
                nodes.append(node)
            if node_numbers == 1:
                node_conclusion = '- Presença de formação nodular descrita acima.'
            elif node_numbers > 1:
                node_conclusion = '- Presença de formações nodulares descrita acima.'    
            break
        elif node_presence == 2:
            node_presence = '.'
            node_conclusion = ''
            break
    except:
        print('Digite um número válido')

        

if node_valuation()[1] == '':
    doppler_title = ''
elif node_valuation()[1] != '':
    doppler_title = 'COM DOPPLER COLORIDO DE TIREOIDE'


if aspecto_glandular == 2 and volume_total > 15:
    gland_conclusion = f'''
CONCLUSÃO:
    
- Glândula com ecotextura heterogênea e volume aumentado compatível com tireoidite.\n'''
elif aspecto_glandular == 'heterogênea' and volume_total < 5:
    gland_conclusion = f'''
CONCLUSÃO:
    
- Glândula com ecotextura heterogênea e volume diminuído compatível com tireoidite crônica.\n'''
elif aspecto_glandular == 'heterogênea' and volume_total >= 5 and volume_total <= 15: 
    gland_conclusion = f'''
CONCLUSÃO:
    
- Glândula com ecotextura heterogênea compatível com tireoidite.\n'''
elif aspecto_glandular == 'homogênea' and volume_total >= 5 and volume_total <= 15:
    gland_conclusion = f'''
CONCLUSÃO:
    
- Glândula com ecotextura e volume normais.\n'''
elif aspecto_glandular == 'homogênea' and volume_total < 5: 
    gland_conclusion = f'''
CONCLUSÃO:
    
- Glândula com volume reduzido.\n'''
elif aspecto_glandular == 'homogênea' and volume_total > 15:
    gland_conclusion = f'''
CONCLUSÃO:
    
- Glândula com volume aumentado.\n'''
else:
    gland_conclusion = f'''
CONCLUSÃO:

'''

#avaliar se ainda falta continuar as possibilidades (melhor opção) ou colocar else: gland_conclusion = '''CONCLUSÃO:
#'''


laudo = f'''
                                ULTRASSONOGRAFIA DE TIREOIDE {doppler_title}
            

TÉCNICA:

Exame realizado com transdutor linear de alta frequência. 


RELATÓRIO:

Tireoide tópica, de volume {volume_glandular}, ecotextura {aspecto_glandular} e de contornos {contorno_glandular}{node_presence}


BIOMETRIA: 

Lobo direito: {ltd_l} x {ltd_ap} x {ltd_t} cm, com volume de {volume_ltd} ml
Lobo esquerdo: {ltd_l} x {ltd_ap} x {ltd_t} cm, com volume de {volume_lte} ml
Istmo: {istmo_ap}
Volume total: {volume_total:.2f} ml

'''

try: 
    for i in nodes:
        laudo += i
except: 
    pass


laudo = laudo + gland_conclusion 
laudo += node_conclusion 

copy_to_clipboard(laudo)

# reavaliar na descricao quanto apenas 1 nodulo descrever como formacao nodular descrita abaixo e nao no plural    
