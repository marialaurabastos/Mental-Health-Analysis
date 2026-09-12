# --- CLASSE PARA REPRESENTAR UM PARTICIPANTE ---
class Participants:
    def __init__(self, 
                 age, gender, country, family_history, treatment, 
                 remote_work, benefits, leave, mental_health_interview, 
                 coworkers, supervisor, mental_vs_physical
                ):
        
        self.age = age
        self.gender = gender
        self.country = country
        self.family_history = family_history
        self.treatment = treatment
        self.remote_work = remote_work
        self.benefits = benefits
        self.leave = leave
        self.mental_health_interview = mental_health_interview
        self.coworkers = coworkers
        self.supervisor = supervisor
        self.mental_vs_physical = mental_vs_physical

# --- CLASSE PARA A ANÁLISE DE DADOS ---
class Analysis:
    def __init__(self, participants):
        self.participants = participants

# --- média de idade dos participantes ---
    def average_age(self):
        age_sum = 0

        for participants in self.participants:
            age_sum += participants.age
        return age_sum / len(self.participants) if len(self.participants) > 0 else 0
    
# --- função geral para cálculos posteriores ---
    def count_by_attribute(self, attribute_name, target_value = 1):
        count = 0
        
        for participants in self.participants:
            response_value = getattr(participants, attribute_name)

            if response_value == target_value:
                count += 1
        return count

# --- quantidade de respostas "sim" ---
    def family_history_amount(self):
        return self.count_by_attribute("family_history", 1)

    def treatment_amount(self):
        return self.count_by_attribute("treatment", 1)

    def remote_amount(self):
        return self.count_by_attribute("remote_work", 1)

    def benefits_amount(self):
        return self.count_by_attribute("benefits", 1)

    def mental_health_interview_amount(self):
        return self.count_by_attribute("mental_health_interview", 1)

    def leave_amount(self):
        return self.count_by_attribute("leave", 1)

    def coworkers_amount(self):
        return self.count_by_attribute("coworkers", 1)

    def supervisor_amount(self):
        return self.count_by_attribute("supervisor", 1)

    def mental_vs_physical_amount(self):
        return self.count_by_attribute("mental_vs_physical", 1)


    def remote_leave_treatment(self):
            remote_group = []
            presential_group = []

            for p in self.participants:
                if p.remote_work == 1:
                    remote_group.append(p)
                elif p.remote_work == 2:
                    presential_group.append(p)

            if len(remote_group) == 0 or len(presential_group) == 0:
                return None

            remote_analysis = Analysis(remote_group)
            presential_analysis = Analysis(presential_group)

            results = {
                "total_remote": len(remote_group),
                "total_presential": len(presential_group),
                "treatment_remote": remote_analysis.treatment_percentage(),
                "treatment_presential": presential_analysis.treatment_percentage(),
                "leave_remote": remote_analysis.leave_percentage(),
                "leave_presential": presential_analysis.leave_percentage()
            }
            return results

# --- porcentagem das respostas ---

# --- método geral para calculo da porcentagm ---
    def percentage_by_attribute(self, attribute_name, target_value=1):
        total = len(self.participants)
        count = self.count_by_attribute(attribute_name, target_value)
        return (count / total) * 100 if total > 0 else 0.0
    
# --- métodos para porcentagem de cada dado ---
    def family_history_percentage(self):
        return self.percentage_by_attribute("family_history", 1)

    def treatment_percentage(self):
        return self.percentage_by_attribute("treatment", 1)

    def remote_percentage(self):
        return self.percentage_by_attribute("remote_work", 1)

    def benefits_percentage(self):
        return self.percentage_by_attribute("benefits", 1)

    def mental_health_interview_percentage(self):
        return self.percentage_by_attribute("mental_health_interview", 1)

    def leave_percentage(self):
        return self.percentage_by_attribute("leave", 1)

    def coworkers_percentage(self):
        return self.percentage_by_attribute("coworkers", 1)

    def supervisor_percentage(self):
        return self.percentage_by_attribute("supervisor", 1)

    def mental_vs_physical_percentage(self):
        return self.percentage_by_attribute("mental_vs_physical", 1)


# --- CLASSE PARA OS FILTROS --- 

class DataFilter:

    def __init__(self, participants):
        self.participants = participants

    def filter_age(self, min_age, max_age):
        filtered = []
        for participants in self.participants:
            if min_age <= participants.age <= max_age:
                filtered.append(participants)
        return filtered

    def filter_gender(self, target_gender):
        filtered = []
        for participants in self.participants:
            if participants.gender.lower() == target_gender.lower():
                filtered.append(participants)
        return filtered

    def filter_country(self, target_country):
        filtered = []
        for participants in self.participants:
            if participants.country.lower() == target_country.lower():
                filtered.append(participants)
        return filtered

    def filter_family_history(self, have_history):
        filtered = []
        for participants in self.participants:
            if participants.family_history == have_history:
                filtered.append(participants)
        return filtered

    def filter_treatment(self, search_treatment):
        filtered = []
        for participants in self.participants:
            if participants.treatment == search_treatment:
                filtered.append(participants)
        return filtered

    def filter_remote(self, is_remote):
        filtered = []
        for participants in self.participants:
            if participants.remote_work == is_remote:
                filtered.append(participants)
        return filtered

    def filter_benefits(self, have_benefits):
        filtered = []
        for participants in self.participants:
            if participants.benefits == have_benefits:
                filtered.append(participants)
        return filtered
    
# --- lista que guarda as informações ---
participants_list = []

# --- MENU ---
running = True

while running:

    print('''
    MENTAL HEALTH ANALYSIS

    MENU:
    [A] - Inserir dados
    [B] - Visualizar dados e estatísticas
    [C] - Análise de participantes que trabalham remotamente, têm possibilidade de afastamento médico e buscaram tratamento
    [D] - Sair
    ''')

    option = input("Escolha uma opção: ").upper() #.upper() para aceitar tanto "A" quando "a"

    if option == "A":

        data_amount = 0
        people_amount = int(input("Quantos participantes serão analisados? " ))

        while data_amount < people_amount:
            data_amount += 1

# --- INSERÇÃO DE DADOS ---
# onde tem int o será: 1 para sim, 2 para não e 3 para não sei / não informado
            print('''
            \nCADASTRO DE PARTICIPANTES  
            ''')

            age = int(input("Idade: "))
            gender = input("Gênero (M/F/Outro): ")
            country = input("País (Sigla): ")

            print('''
            \nOPÇÕES:
            [1] - Sim
            [2] - Não
            [3] - Não sabe / Não informado
            ''')

            family_history = int(input("O participante tem questões de saúde mental na família? "))
            treatment = int(input("O participante buscou tratamento? "))
            remote_work = int(input("O participante trabalha remotamente? "))
            benefits = int(input("O participante tem benefícios de saúde mental? "))
            leave = int(input("O participante tem possibilidade de afastamento médico? "))
            mental_health_interview = int(input("O participante nota consequências negativas ao conversar com um superior sobre saúde mental? "))
            coworkers = int(input("O participante está disposto a conversar com colegas? "))
            supervisor = int(input("O participante está disposto a conversar com supervisores? "))
            mental_vs_physical = int(input("O participante acha importante a saúde mental em comparação à corporal? "))

            participants = Participants(
                age, gender, country, family_history, treatment, 
                remote_work, benefits, leave, mental_health_interview, 
                coworkers, supervisor, mental_vs_physical
            )
                
            participants_list.append(participants)

            print("\nCadastros realizados com sucesso!")

    elif option == "B":
        if len(participants_list) == 0:

            print("\nNenhum dado. Cadastre os participantes primeiro.")

        else:
            submenu_running = True
            
            while submenu_running:
                print('''
                \nOPÇÕES:
                [A] - Ver todos os dados e estatísticas
                [B] - Filtrar dados
                [C] - Voltar
                ''')
                sub_option = input("\nEscolha uma opção: ").upper()

                analysis_list = []

                if sub_option == "A":

                    analysis_list = participants_list
                
                    panel_data = Analysis(participants_list) #instancia um objeto da classe de analise e guarda na variavel panel_data

                    #cabecalho
                    print("\nESTATÍSTICAS DA PESQUISA")
                    print("=" * 137)
                    print(f"TOTAL DE PARTICIPANTES: {len(participants_list)}")
                    print(f"Média das idades: {panel_data.average_age():.1f} anos")
                    print("=" * 137)
                    print(f"| {'Métrica / Pergunta':<95} | {'Qnt (Sim)':^15} | {'% (Sim)':^17} |")
                    print("|" + "-" * 97 + "|" + "-" * 17 + "|" + "-" * 19 + "|")
                    #corpo da tabela
                    metrics = [
                        ("Participantes com questões de saúde mental na família", panel_data.family_history_amount(), f"{panel_data.family_history_percentage():.1f}%"),
                        ("Participantes que buscaram tratamento", panel_data.treatment_amount(), f"{panel_data.treatment_percentage():.1f}%"),
                        ("Participantes que trabalham remotamente", panel_data.remote_amount(), f"{panel_data.remote_percentage():.1f}%"),
                        ("Participantes que possuem benefícios de saúde", panel_data.benefits_amount(), f"{panel_data.benefits_percentage():.1f}%"),
                        ("Participantes que têm possibilidade de afastamento médico", panel_data.leave_amount(), f"{panel_data.leave_percentage():.1f}%"),
                        ("Participantes que notam consequências negativas ao conversar com um superior sobre saúde mental", panel_data.mental_health_interview_amount(), f"{panel_data.mental_health_interview_percentage():.1f}%"),
                        ("Participantes que estão dispostos a conversar com colegas", panel_data.coworkers_amount(), f"{panel_data.coworkers_percentage():.1f}%"),
                        ("Participantes que estão dispostos a conversar com supervisores", panel_data.supervisor_amount(), f"{panel_data.supervisor_percentage():.1f}%"),
                        ("Participantes que acham importante a saúde mental em comparação à corporal", panel_data.mental_vs_physical_amount(), f"{panel_data.mental_vs_physical_percentage():.1f}%")
                    ]

                    for description, amount, percentage in metrics:
                        print(f"| {description:<95} | {amount:^15} | {percentage:^17} |")
                    print("-" * 137)

                    input("\nPressione ENTER para continuar...")

                elif sub_option == "B":

                    chosen_filter = DataFilter(participants_list)
                    filtered_result = []

                    print('''
                    FILTRAR POR:
                    [1] Faixa etária
                    [2] Gênero
                    [3] País
                    [4] Histórico familiar
                    [5] Busca por tratamento
                    [6] Trabalho remoto
                    [7] Existência de benefícios
                    ''')

                    selected_filter = input("Escolha o filtro: ")

                    if selected_filter == "1":
                        min_age = int(input("Idade mínima: "))
                        max_age = int(input("Idade máxima: "))
                        filtered_result = chosen_filter.filter_age(min_age, max_age)

                    elif selected_filter == "2":
                        target_gender = input("Gênero: ")
                        filtered_result = chosen_filter.filter_gender(target_gender)

                    elif selected_filter == "3":
                        target_country = input("País: ")
                        filtered_result = chosen_filter.filter_country(target_country)

                    elif selected_filter == "4":
                        have_history = int(input("Histórico familiar \n(1 - Sim) \n(2 - Não) "))
                        filtered_result = chosen_filter.filter_family_history(have_history)

                    elif selected_filter == "5":
                        search_treatment = int(input("Tratamento \n(1 - Sim) \n(2 - Não) "))
                        filtered_result = chosen_filter.filter_treatment(search_treatment)

                    elif selected_filter == "6":
                        is_remote = int(input("Trabalha remotamente \n(1 - Sim) \n(2 - Não) "))
                        filtered_result = chosen_filter.filter_remote(is_remote)

                    elif selected_filter == "7":
                        have_benefits = int(input("Benefícios de saúde mental \n(1 - Sim) \n(2 - Não) "))
                        filtered_result = chosen_filter.filter_benefits(have_benefits)

                    else:
                        print("Opção inválida.")

                    if not filtered_result:
                        print("\nNenhum participante encontrado com esse critério.")
                    else:
                        filtered_panel = Analysis(filtered_result)

                        print("\n" + "=" * 137)
                        print(f"ESTATÍSTICAS DO GRUPO FILTRADO ({len(filtered_result)} participante(s))")
                        print("=" * 137)
                        print(f"| {'Métrica / Pergunta':<95} | {'Qnt (Sim)':^15} | {'% (Sim)':^17} |")
                        print("|" + "-" * 97 + "|" + "-" * 17 + "|" + "-" * 19 + "|")

                        metrics = [
                            ("Participantes com questões de saúde mental na família", filtered_panel.family_history_amount(), f"{filtered_panel.family_history_percentage():.1f}%"),
                            ("Participantes que buscaram tratamento", filtered_panel.treatment_amount(), f"{filtered_panel.treatment_percentage():.1f}%"),
                            ("Participantes que trabalham remotamente", filtered_panel.remote_amount(), f"{filtered_panel.remote_percentage():.1f}%"),
                            ("Participantes que possuem benefícios de saúde", filtered_panel.benefits_amount(), f"{filtered_panel.benefits_percentage():.1f}%"),
                            ("Pacientes que têm possibilidade de afastamento médico", filtered_panel.leave_amount(), f"{filtered_panel.leave_percentage():.1f}%"),
                            ("Pacientes que notam consequências negativas ao conversar com superior", filtered_panel.mental_health_interview_amount(), f"{filtered_panel.mental_health_interview_percentage():.1f}%"),
                            ("Participantes que estão dispostos a conversar com colegas", filtered_panel.coworkers_amount(), f"{filtered_panel.coworkers_percentage():.1f}%"),
                            ("Participantes que estão dispostos a conversar com supervisores", filtered_panel.supervisor_amount(), f"{filtered_panel.supervisor_percentage():.1f}%"),
                            ("Participantes que acham importante a saúde mental em comparação à corporal", filtered_panel.mental_vs_physical_amount(), f"{filtered_panel.mental_vs_physical_percentage():.1f}%")
                        ]

                        for description, amount, percentage in metrics:
                            print(f"| {description:<95} | {amount:^15} | {percentage:^17} |")
                        print("-" * 137)

                    input("\nPressione ENTER para continuar...")

                elif sub_option == "C":
                    print("\nVoltando ao menu principal...")
                    submenu_running = False

                else:
                    print("\nOpção inválida. Escolha A, B ou C.")
    
    elif option == "C":
        if len(participants_list) == 0:
            print("Não há dados para serem analisados. Por favor cadastre os participantes.")

        else:
            data_cross = Analysis(participants_list)
            calculated_data = data_cross.remote_leave_treatment()

            if calculated_data is None:
                print("Cadastre os participantes primeiro.")

            else:
                print("\nCRUZAMENTO: IMPACTO DO FORMATO DE TRABALHO")
                print(f"Total Remoto: {calculated_data['total_remote']} | Total Presencial: {calculated_data['total_presential']}")
                
                print("\n--- Busca por Tratamento ---")
                print(f"Trabalhadores Remotos: {calculated_data['treatment_remote']:.1f}%")
                print(f"Trabalhadores Presenciais: {calculated_data['treatment_presential']:.1f}%")
                
                print("\n--- Possibilidade de Afastamento Médico ---")
                print(f"Trabalhadores Remotos: {calculated_data['leave_remote']:.1f}%")
                print(f"Trabalhadores Presenciais: {calculated_data['leave_presential']:.1f}%")

            input("\nPressione ENTER para continuar...")
            

    elif option == "D":
        print("\nSaindo do sistema... até logo!")
        running = False
    
    else:
        print("\nOpção inválida. Por favor, escolha A, B, C ou D.")