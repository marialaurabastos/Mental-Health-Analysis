# --- PROJETO 2 ---

import time
import pandas as pd

survey_db = pd.read_csv('survey.csv', sep = ';')

treat_data = {
    'state': 'Not specified',
    'self_employed': 'Not specified',
    'work_interfere': 'Not specified',
    'comments': 'No comment'
}

survey_db.fillna(value = treat_data, inplace=True)

#--- tratamento 'Age' ---

survey_db['Age'] = pd.to_numeric(survey_db['Age'], errors = 'coerce')

invalid_age = ~survey_db['Age'].between(18, 100)

median_age = survey_db.loc[survey_db['Age'].between(18, 100), 'Age'].median()

survey_db.loc[invalid_age, 'Age'] = median_age

#--- tratamento 'Gender' ---

treat_gender = {
    'Female': 'Female',
    'female': 'Female',
    'Cis Female': 'Female',
    'F': 'Female',
    'Woman': 'Female',
    'f': 'Female',
    'Femake': 'Female',
    'woman': 'Female',
    'Female ': 'Female',
    'cis-female/femme': 'Female',
    'Female (cis)': 'Female',
    'femail': 'Female',

    'M': 'Male',
    'Male': 'Male',
    'male': 'Male',
    'm': 'Male',
    'Male-ish': 'Male',
    'maile': 'Male',
    'something kinda male?': 'Male',
    'Cis Male': 'Male',
    'Mal': 'Male',
    'Male (CIS)': 'Male',
    'Make': 'Male',
    'Guy (-ish) ^_^': 'Male',
    'male leaning androgynous': 'Male',
    'Male ': 'Male',
    'Man': 'Male',
    'msle': 'Male',
    'Mail': 'Male',
    'cis male': 'Male',
    'Malr': 'Male',
    'Cis Man': 'Male',
    'ostensibly male, unsure what that really means': 'Male',

    'Trans-female': 'Other',
    'queer/she/they': 'Other',
    'non-binary': 'Other',
    'Nah': 'Other',
    'All': 'Other',
    'Enby': 'Other',
    'fluid': 'Other',
    'Genderqueer': 'Other',
    'Androgyne': 'Other',
    'Agender': 'Other',
    'Trans woman': 'Other',
    'Neuter': 'Other',
    'Female (trans)': 'Other',
    'queer': 'Other',
    'A little about you': 'Other',
    'p': 'Other'
}

survey_db['Gender'] = survey_db['Gender'].replace(treat_gender)

#--- padronização 'Country' e 'state' ---

survey_db['Country'] = survey_db['Country'].str.strip().str.title()

survey_db['state'] = survey_db['state'].str.strip().str.upper()

#--- tratamento 'no_employees' ---

treat_no_employees = {
    '01/mai': '1-5',
    'jun/25': '6-25'
}

survey_db['no_employees'] = survey_db['no_employees'].replace(treat_no_employees)

#--- validação dos campos ---

columns_yes_no = ['family_history', 'treatment', 'remote_work', 'self_employed', 'tech_company', 'obs_consequence'] 
columns_yes_no_maybe = ['mental_health_consequence', 'phys_health_consequence', 'mental_health_interview', 'phys_health_interview']
columns_yes_no_dontknow = ['benefits', 'wellness_program', 'seek_help', 'anonymity', 'mental_vs_physical']
columns_yes_no_some = ['coworkers', 'supervisor']

valid_options_work_interfere = ['Often', 'Rarely', 'Never', 'Sometimes', 'Not specified']
valid_options_employees = ['1-5', '6-25', '26-100', '100-500', '500-1000', 'More than 1000']
valid_options_leave = ["Somewhat easy", "Don't know", "Somewhat difficult", "Very difficult", "Very easy"]
valid_options_care = ['Yes', 'No', 'Not sure']
valid_options_yes_no = ['Yes', 'No', 'Not specified']
valid_options_yes_no_maybe = ['Yes', 'No', 'Maybe']
valid_options_yes_no_dontknow = ['Yes', 'No', "Don't know"]
valid_options_yes_no_some = ['Yes', 'No', 'Some of them']
valid_options_gender = ['Female', 'Male', 'Other']

error_yes_no = (~survey_db[columns_yes_no].isin(valid_options_yes_no)).any(axis = 1)
error_yes_no_maybe = (~survey_db[columns_yes_no_maybe].isin(valid_options_yes_no_maybe)).any(axis = 1)
error_yes_no_dontknow = (~survey_db[columns_yes_no_dontknow].isin(valid_options_yes_no_dontknow)).any(axis = 1)
error_yes_no_some = (~survey_db[columns_yes_no_some].isin(valid_options_yes_no_some)).any(axis = 1)
error_work_interfere = ~survey_db['work_interfere'].isin(valid_options_work_interfere)
error_employees = ~survey_db['no_employees'].isin(valid_options_employees)
error_leave = ~survey_db['leave'].isin(valid_options_leave)
error_care = ~survey_db['care_options'].isin(valid_options_care)
error_gender = ~survey_db['Gender'].isin(valid_options_gender)

#--- contagem de linhas inválidas ---

all_invalid_lines = (error_yes_no | error_yes_no_maybe | error_yes_no_dontknow | error_yes_no_some | error_work_interfere | error_employees | error_leave | error_care | error_gender) 


total_read = len(survey_db)
total_invalid = all_invalid_lines.sum()
total_valid = total_read - total_invalid

average_age = survey_db['Age'].mean()

amount_ans_by_country = survey_db['Country'].value_counts()
amount_ans_by_gender = survey_db['Gender'].value_counts()
amount_ans_by_org_type = survey_db['tech_company'].value_counts()
amount_ans_by_org_size = survey_db['no_employees'].value_counts()
amount_ans_by_treatement = survey_db['treatment'].value_counts()
amount_ans_by_history = survey_db['family_history'].value_counts()
amount_ans_by_remote = survey_db['remote_work'].value_counts()
amount_ans_by_benefits = survey_db['benefits'].value_counts()
amount_ans_by_obs_consequence = survey_db['obs_consequence'].value_counts()

visible_columns = ['Age', 'Gender', 'Country', 'treatment', 'tech_company']

running_main = True

def filter_exibition(column_name, search_term):
    results = survey_db[survey_db[column_name] == search_term]

    if results.empty:
        print(f"\nNenhum registro encontrado para '{search_term}'.")

    else:
        print(results[visible_columns].to_string(index=False))
        print("-" * 50)

def search_exibition(column_name, search_term):

    # .astype(str) garante a busca em texto
    # .str.contains() procura "partes" da palavra, case=False ignora maiúsculas e minúsculas
    mask = survey_db[column_name].astype(str).str.contains(search_term, case=False, na=False)
    results = survey_db[mask]

    if results.empty:
        print(f"\nNenhum registro encontrado contendo '{search_term}'.")
    else:
        print(f"\nForam encontrados {len(results)} registros.")
        print(results[visible_columns].head(50).to_string(index=False))
        print("-" * 50)


while running_main:

    print('''
        MENTAL HEALTH ANALYSIS
    
        MENU:
        [A] - Visualizar dados e estatísticas
        [B] - Pesquisar
        [C] - Gerar relatório
        [0] - Sair
        ''')

    option = input('Escolha uma opção: ').upper()

    if option == 'A':

        print('--- VALIDAÇÃO ---')
        print(f'Quantidade de registros lidos: {total_read}')
        print(f'Quantidade de registros válidos: {total_valid}')
        print(f'Quantidade de registros inválidos: {total_invalid}')

        print('--- ANÁLISES ---')
        print(f'Média das idades: {average_age:.1f} anos\n')

        print('Distribuição por País:')

        print(amount_ans_by_country.head(10).to_string(header=False)) 
        print('-' * 30)

        print('Distribuição por Gênero:')
        print(amount_ans_by_gender.to_string(header=False))
        print('-' * 30)

        print('Distribuição por Tipo de Organização:')
        print(amount_ans_by_org_type.to_string(header=False))
        print('-' * 30)

        print('Distribuição por Tamanho da Organização:')
        print(amount_ans_by_org_size.to_string(header=False))
        print('-' * 30)

        print('Procuraram Tratamento (Visão Geral):')
        print(amount_ans_by_treatement.to_string(header=False))
        print('-' * 30)

        print('Histórico Familiar (Visão Geral):')
        print(amount_ans_by_history.to_string(header=False))
        print('-' * 30)

        print('Trabalham Remotamente (Visão Geral):')
        print(amount_ans_by_remote.to_string(header=False))
        print('-' * 30)

        print('Possuem benefício de saúde (Visão Geral):')
        print(amount_ans_by_benefits.to_string(header=False))
        print('-' * 30)

        print('Notam consequências negativas ao conversar com um superior (Visão Geral):')
        print(amount_ans_by_obs_consequence.to_string(header=False))
        print('-' * 30)

    elif option == 'B':

        running_search = True
        while running_search:

            print('''
            MENTAL HEALTH ANALYSIS
        
            MENU:
            [A] - Pesquisar
            [B] - Filtrar respostas
            [C] - Ordenar respostas
            [0] - Voltar
            ''')

            option = input('Escolha uma opção: ').upper()

            if option == 'A':

                running_search_by = True
                while running_search_by:

                    print('''
                    BUSCAR POR:
                            
                    MENU:
                    [A] - País
                    [B] - Estado
                    [C] - Gênero
                    [D] - Faixa etária
                    [E] - Resposta sobre tratamento;
                    [F] - Resposta sobre benefícios;
                    [G] - Resposta sobre anonimato;
                    [0] - Voltar
                    ''')

                    option = input('Escolha uma opção: ').upper()

                    if option == 'A':
                        country_name = input('Qual país você deseja analisar? ').strip().title()

                        print(f'\nExibindo resultados para {country_name}: ')

                        search_exibition('Country', country_name)

                    elif option == 'B':
                        state_name = input('Qual estado você deseja analisar? ').strip().upper()

                        print(f'Exibindo resultados para {state_name}: ')

                        search_exibition('state', state_name)

                    elif option == 'C':
                        chosen_gender = input('Qual gênero você deseja analisar (Female / Male / Other)? ').strip().title()

                        print(f'Exibindo resultados para {chosen_gender}: ')

                        search_exibition('Gender', chosen_gender)

                    elif option == 'D':
                        min_age = int(input('Qual a idade mínima? '))
                        max_age = int(input('Qual a idade máxima? '))

                        print(f'Exibindo resultados para a faixa etária de {min_age} a {max_age} anos: ')

                        results = survey_db[survey_db['Age'].between(min_age, max_age)]
                        
                        if results.empty:
                            print(f"\nNenhum registro encontrado para esta faixa etária.")
                        else:
                            print(results[visible_columns].to_string(index=False))
                            print("-" * 50)

                    elif option == 'E':

                        running_filter_results = True
                        treatment_labels = {
                            '1': 'Buscaram tratamento',
                            '2': 'Não buscaram tratamento'
                        }
                        while running_filter_results:

                            chosen_treatment = input('''
                            Qual grupo você deseja analisar?
                            [1] - Buscaram tratamento
                            [2] - Não buscaram tratamento
                            [3] - Voltar
                            ''')

                            if chosen_treatment == '1':
                                display_text = treatment_labels[chosen_treatment]
                                print(f'Exibindo resultados para {display_text}: ')

                                search_exibition('treatment', 'Yes')

                            elif chosen_treatment == '2':
                                display_text = treatment_labels[chosen_treatment]
                                print(f'Exibindo resultados para {display_text}: ')

                                search_exibition('treatment', 'No')

                            else:
                                print('Voltando...')
                                time.sleep(1)
                                running_filter_results = False
                                
                    elif option == 'F':

                        running_filter_results = True
                        benefits_labels = {
                            '1': 'Possuem benefício de saúde',
                            '2': 'Não possuem benefício de saúde'
                        }
                        while running_filter_results:

                            chosen_benefits = input('''
                            Qual grupo você deseja analisar?
                            [1] - Possuem benefício de saúde
                            [2] - Não possuem benefício de saúde
                            [3] - Voltar
                            ''')

                            if chosen_benefits == '1':
                                display_text = benefits_labels[chosen_benefits]
                                print(f'Exibindo resultados para {display_text}: ')

                                search_exibition('benefits', 'Yes')

                            elif chosen_benefits == '2':
                                display_text = benefits_labels[chosen_benefits]
                                print(f'Exibindo resultados para {display_text}: ')

                                search_exibition('benefits', 'No')

                            else:
                                print('Voltando...')
                                time.sleep(1)
                                running_filter_results = False

                    elif option == 'G':

                        running_filter_results = True
                        anonymity_labels = {
                            '1': 'Acreditam que o anonimato está protegido',
                            '2': 'Não acreditam que o anonimato está protegido',
                            '3': 'Não sabem dizer'
                        }
                        while running_filter_results:

                            chosen_anonimity = input('''
                            Qual percepção sobre o anonimato você deseja analisar?
                            [1] - Acreditam que o anonimato está protegido
                            [2] - Não acreditam que o anonimato está protegido
                            [3] - Não sabem dizer
                            [0] - Voltar
                            ''')

                            if chosen_anonimity == '1':
                                display_text = anonymity_labels[chosen_anonimity]
                                print(f'Exibindo resultados para {display_text}: ')
                                search_exibition('anonymity', 'Yes')
                                
                            elif chosen_anonimity == '2':
                                display_text = anonymity_labels[chosen_anonimity]
                                print(f'Exibindo resultados para {display_text}: ')
                                search_exibition('anonymity', 'No')

                            elif chosen_anonimity == '3':
                                display_text = anonymity_labels[chosen_anonimity]
                                print(f'Exibindo resultados para {display_text}: ')
                                search_exibition('anonymity', "Don't know")
                                
                            else:
                                print('Voltando...')
                                time.sleep(1)
                                running_filter_results = False
                                
                    else:
                        print('Voltando...')
                        time.sleep(1)
                        running_search_by = False
            
            elif option == 'B':
                
                running_filter = True
                while running_filter:
                    
                    print('''
                    FILTRAR POR:
                            
                    MENU:
                    [A] - País
                    [B] - Estado
                    [C] - Faixa etária
                    [D] - Gênero
                    [E] - Trabalho autônomo
                    [F] - Histórico familiar
                    [G] - Busca por tratamento
                    [H] - Trabalho remoto
                    [I] - Empresa de tecnologia
                    [J] - Tamanho da organização
                    [K] - Existência de benefícios
                    [L] - Facilidade de afastamento
                    [0] - Voltar
                    ''')
                    
                    option = input('Escolha uma opção: ').upper()
                    
                    if option == 'A':
                        country_name = input('Qual país você deseja filtrar? ').strip().title()
                        print(f'\nFiltrando resultados para {country_name}: ')
                        filter_exibition('Country', country_name)

                    elif option == 'B':
                        state_name = input('Qual estado você deseja filtrar? ').strip().upper()
                        print(f'\nFiltrando resultados para {state_name}: ')
                        filter_exibition('state', state_name)

                    elif option == 'C':
                        min_age = int(input('Qual a idade mínima? '))
                        max_age = int(input('Qual a idade máxima? '))
                        print(f'\nFiltrando resultados para a faixa etária de {min_age} a {max_age} anos: ')
                        results = survey_db[survey_db['Age'].between(min_age, max_age)]
                        
                        if results.empty:
                            print(f"\nNenhum registro encontrado para esta faixa etária.")
                        else:
                            print(results[visible_columns].to_string(index=False))
                            print("-" * 50)

                    elif option == 'D':
                        chosen_gender = input('Qual gênero você deseja filtrar (Female / Male / Other)? ').strip().title()
                        print(f'\nFiltrando resultados para {chosen_gender}: ')
                        filter_exibition('Gender', chosen_gender)

                    elif option == 'E':
                        running_filter_results = True
                        labels = {'1': 'Trabalha como autônomo', '2': 'Não trabalha como autônomo'}
                        while running_filter_results:
                            chosen_option = input('''
                            Qual grupo você deseja filtrar?
                            [1] - Trabalha como autônomo
                            [2] - Não trabalha como autônomo
                            [0] - Voltar
                            ''')
                            
                            if chosen_option == '1':
                                print(f"\nFiltrando resultados para: {labels[chosen_option]}")
                                filter_exibition('self_employed', 'Yes')
                            elif chosen_option == '2':
                                print(f"\nFiltrando resultados para: {labels[chosen_option]}")
                                filter_exibition('self_employed', 'No')
                            elif chosen_option == '0':
                                print('Voltando...')
                                time.sleep(1)
                                running_filter_results = False
                            else:
                                print('Opção inválida!')
                                time.sleep(1)

                    elif option == 'F':
                        running_filter_results = True
                        labels = {'1': 'Possui histórico familiar', '2': 'Não possui histórico familiar'}
                        while running_filter_results:
                            chosen_option = input('''
                            Qual grupo você deseja filtrar?
                            [1] - Possui histórico familiar
                            [2] - Não possui histórico familiar
                            [0] - Voltar
                            ''')
                            
                            if chosen_option == '1':
                                print(f"\nFiltrando resultados para: {labels[chosen_option]}")
                                filter_exibition('family_history', 'Yes')
                            elif chosen_option == '2':
                                print(f"\nFiltrando resultados para: {labels[chosen_option]}")
                                filter_exibition('family_history', 'No')
                            elif chosen_option == '0':
                                print('Voltando...')
                                time.sleep(1)
                                running_filter_results = False
                            else:
                                print('Opção inválida!')
                                time.sleep(1)

                    elif option == 'G':
                        running_filter_results = True
                        labels = {'1': 'Buscaram tratamento', '2': 'Não buscaram tratamento'}
                        while running_filter_results:
                            chosen_option = input('''
                            Qual grupo você deseja filtrar?
                            [1] - Buscaram tratamento
                            [2] - Não buscaram tratamento
                            [0] - Voltar
                            ''')
                            
                            if chosen_option == '1':
                                print(f"\nFiltrando resultados para: {labels[chosen_option]}")
                                filter_exibition('treatment', 'Yes')
                            elif chosen_option == '2':
                                print(f"\nFiltrando resultados para: {labels[chosen_option]}")
                                filter_exibition('treatment', 'No')
                            elif chosen_option == '0':
                                print('Voltando...')
                                time.sleep(1)
                                running_filter_results = False
                            else:
                                print('Opção inválida!')
                                time.sleep(1)

                    elif option == 'H':
                        running_filter_results = True
                        labels = {'1': 'Trabalham remotamente', '2': 'Não trabalham remotamente'}
                        while running_filter_results:
                            chosen_option = input('''
                            Qual grupo você deseja filtrar?
                            [1] - Trabalham remotamente
                            [2] - Não trabalham remotamente
                            [0] - Voltar
                            ''')
                            
                            if chosen_option == '1':
                                print(f"\nFiltrando resultados para: {labels[chosen_option]}")
                                filter_exibition('remote_work', 'Yes')
                            elif chosen_option == '2':
                                print(f"\nFiltrando resultados para: {labels[chosen_option]}")
                                filter_exibition('remote_work', 'No')
                            elif chosen_option == '0':
                                print('Voltando...')
                                time.sleep(1)
                                running_filter_results = False
                            else:
                                print('Opção inválida!')
                                time.sleep(1)

                    elif option == 'I':
                        running_filter_results = True
                        labels = {'1': 'É empresa de tecnologia', '2': 'Não é empresa de tecnologia'}
                        while running_filter_results:
                            chosen_option = input('''
                            Qual grupo você deseja filtrar?
                            [1] - É empresa de tecnologia
                            [2] - Não é empresa de tecnologia
                            [0] - Voltar
                            ''')
                            
                            if chosen_option == '1':
                                print(f"\nFiltrando resultados para: {labels[chosen_option]}")
                                filter_exibition('tech_company', 'Yes')
                            elif chosen_option == '2':
                                print(f"\nFiltrando resultados para: {labels[chosen_option]}")
                                filter_exibition('tech_company', 'No')
                            elif chosen_option == '0':
                                print('Voltando...')
                                time.sleep(1)
                                running_filter_results = False
                            else:
                                print('Opção inválida!')
                                time.sleep(1)

                    elif option == 'J':
                        running_filter_results = True
                        labels = {
                            '1': '1-5', '2': '6-25', '3': '26-100', 
                            '4': '100-500', '5': '500-1000', '6': 'More than 1000'
                        }
                        while running_filter_results:
                            chosen_option = input('''
                            Qual o tamanho da organização que deseja filtrar?
                            [1] - 1-5
                            [2] - 6-25
                            [3] - 26-100
                            [4] - 100-500
                            [5] - 500-1000
                            [6] - More than 1000
                            [0] - Voltar
                            ''')
                            
                            if chosen_option in labels:
                                print(f"\nFiltrando resultados para tamanho: {labels[chosen_option]}")
                                filter_exibition('no_employees', labels[chosen_option])
                            elif chosen_option == '0':
                                print('Voltando...')
                                time.sleep(1)
                                running_filter_results = False
                            else:
                                print('Opção inválida!')
                                time.sleep(1)

                    elif option == 'K':
                        running_filter_results = True
                        benefits_labels = {
                            '1': 'Possuem benefício de saúde',
                            '2': 'Não possuem benefício de saúde',
                            '3': 'Não sabem dizer'
                        }
                        while running_filter_results:
                            
                            chosen_benefits = input('''
                            Qual grupo você deseja filtrar?
                            [1] - Possuem benefício de saúde
                            [2] - Não possuem benefício de saúde
                            [3] - Não sabem dizer
                            [0] - Voltar
                            ''')
                            
                            if chosen_benefits == '1':
                                display_text = benefits_labels[chosen_benefits]
                                print(f'\nFiltrando resultados para {display_text}: ')
                                filter_exibition('benefits', 'Yes')
                                
                            elif chosen_benefits == '2':
                                display_text = benefits_labels[chosen_benefits]
                                print(f'\nFiltrando resultados para {display_text}: ')
                                filter_exibition('benefits', 'No')
                                
                            elif chosen_benefits == '3':
                                display_text = benefits_labels[chosen_benefits]
                                print(f'\nFiltrando resultados para {display_text}: ')
                                filter_exibition('benefits', "Don't know")
                                
                            elif chosen_benefits == '0':
                                print('Voltando...')
                                time.sleep(1)
                                running_filter_results = False
                                
                            else:
                                print('Opção inválida!')
                                time.sleep(1)

                    elif option == 'L':
                        running_filter_results = True
                        labels = {
                            '1': 'Very easy', '2': 'Somewhat easy', 
                            '3': "Don't know", '4': 'Somewhat difficult', '5': 'Very difficult'
                        }
                        while running_filter_results:
                            chosen_option = input('''
                            Qual o nível de facilidade de afastamento?
                            [1] - Very easy (Muito fácil)
                            [2] - Somewhat easy (Razoavelmente fácil)
                            [3] - Don't know (Não sabe)
                            [4] - Somewhat difficult (Razoavelmente difícil)
                            [5] - Very difficult (Muito difícil)
                            [0] - Voltar
                            ''')
                            
                            if chosen_option in labels:
                                print(f"\nFiltrando resultados para: {labels[chosen_option]}")
                                filter_exibition('leave', labels[chosen_option])
                            elif chosen_option == '0':
                                print('Voltando...')
                                time.sleep(1)
                                running_filter_results = False
                            else:
                                print('Opção inválida!')
                                time.sleep(1)

                    elif option == '0':
                        print('Voltando...')
                        time.sleep(1)
                        running_filter = False
            
            elif option == 'C':
                
                running_sort = True
                while running_sort:
                    
                    print('''
                    ORDENAR RESPOSTAS POR:
                            
                    MENU:
                    [1] - Idade e Gênero
                    [2] - Gênero e Idade
                    [0] - Voltar
                    ''')
                    
                    sort_option = input('Escolha uma opção: ')
                    
                    if sort_option == '1':
                        print('\nOrdenando por Idade e Gênero...')
                        
                        sorted_results = survey_db.sort_values(by=['Age', 'Gender'])
                        
                        print(sorted_results[visible_columns].head(50).to_string(index=False))
                        print("-" * 50)
                        
                    elif sort_option == '2':
                        print('\nOrdenando por Gênero e Idade...')
                        
                        sorted_results = survey_db.sort_values(by=['Gender', 'Age'])
                        
                        print(sorted_results[visible_columns].head(50).to_string(index=False))
                        print("-" * 50)
                        
                    elif sort_option == '0':
                        print('Voltando...')
                        time.sleep(3)
                        running_sort = False
                        
                    else:
                        print('Opção inválida!')
                        time.sleep(3)
            
            elif option == '0':
                print('Voltando...')
                time.sleep(1)
                running_search = False
                
            else:
                print('Opção inválida!')
                time.sleep(1)

    elif option == 'C':
        print('Gerando relatório em texto...')
        time.sleep(1)

        report_content = f'''==================================================
        RELATÓRIO: MENTAL HEALTH IN TECH SURVEY      
        ==================================================

        --- VALIDAÇÃO E LEITURA ---
        Quantidade de registros lidos originais: {total_read}
        Quantidade de registros válidos processados: {total_valid}
        Quantidade de registros inválidos (tratados): {total_invalid}

        --- ESTATÍSTICAS GERAIS ---
        Média de idade dos participantes: {average_age:.1f} anos

        --- DISTRIBUIÇÃO POR PAÍS (Top 10) ---
        {amount_ans_by_country.head(10).to_string()}

        --- DISTRIBUIÇÃO POR GÊNERO ---
        {amount_ans_by_gender.to_string()}

        --- TAMANHO DA ORGANIZAÇÃO ---
        {amount_ans_by_org_size.to_string()}

        --- CONSULTAS ESPECIAIS (Visão Geral) ---

        > Busca por Tratamento:
        {amount_ans_by_treatement.to_string()}

        > Histórico Familiar:
        {amount_ans_by_history.to_string()}

        > Trabalho Remoto:
        {amount_ans_by_remote.to_string()}

        > Possuem Benefícios de Saúde:
        {amount_ans_by_benefits.to_string()}

        > Notam consequências negativas ao conversar com supervisor:
        {amount_ans_by_obs_consequence.to_string()}

        =================================================='''

        with open('mental_health_report.txt', 'w', encoding='utf-8') as file:
            file.write(report_content)

            print('Relatório gerado com sucesso!')

    elif option == '0':
        print('\nSaindo do sistema... até logo!')
        running_main = False
        
    else:
        print('Opção inválida!')
        time.sleep(1)