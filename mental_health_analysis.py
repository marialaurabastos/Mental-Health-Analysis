# --- CLASSE PARA REPRESENTAR UM PARTICIPANTE ---
class Participants:
    def __init__(self, 
                 name, age,gender, country, family_history, treatment, 
                 remote_work, benefits, leave, mental_health_interview, 
                 coworkers, supervisor, mental_vs_physical
                ):
        
        self.name = name
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


# --- lista que guarda as informações ---
participants_list = []

# --- MENU ---
option = ""
while option != "C":

    print('''
    MENTAL HEALTH ANALYSIS

    MENU:
    [A] - Inserir dados
    [B] - Visualizar dados e estatísticas
    [C] - Sair
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

            name = input("Nome: ")
            age = int(input("Idade: "))
            gender = input("Gênero: ")
            country = input("País: ")

            print('''
            \nOPÇÕES:
            [1] - Sim
            [2] - Não
            [3] - Não sabe / não informado
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
                name, age,gender, country, family_history, treatment, 
                remote_work, benefits, leave, mental_health_interview, 
                coworkers, supervisor, mental_vs_physical
            )
            
            participants_list.append(participants)

        print("\nCadastros realizados com sucesso!")


    elif option == "B":
        if len(participants_list) == 0:

            print("\nNenhum dado. Cadastre os participantes primeiro.")

        else:
            panel = Analysis(participants_list) #instancia um objeto da classe de analise e guarda na variavel panel

            print("\nESTATÍSTICAS DA PESQUISA")

            print(f"Total de participantes: {len(participants_list)}")
            print(f"Média das idades: {panel.average_age():.1f} anos")
            print(f"Participantes com questões de saúde mental na família: {panel.family_history_amount()} -> {panel.family_history_percentage():.2f}%.")
            print(f"Participantes que buscaram tratamento: {panel.treatment_amount()} -> {panel.treatment_percentage():.2f}%.")
            print(f"Participantes que trabalham remotamente: {panel.remote_amount()} -> {panel.remote_percentage():.2f}%.")
            print(f"Participantes que possuem benefícios de saúde: {panel.benefits_amount()} -> {panel.benefits_percentage():.2f}%.")
            print(f"participantes que têm possibilidade de afastamento médico: {panel.leave_amount()} -> {panel.leave_percentage():.2f}%.")
            print(f"Participantes que notam consequências negativas ao conversar com um superior sobre saúde mental: {panel.mental_health_interview_amount()} -> {panel.mental_health_interview_percentage():.2f}%. ")
            print(f"Participantes que estão dispostos a conversar com colegas: {panel.coworkers_amount()} -> {panel.coworkers_percentage():.2f}%.")
            print(f"Participantes que estão dispostos a conversar com supervisores: {panel.supervisor_amount()} -> {panel.supervisor_percentage():.2f}%.")
            print(f"participantes que acham importante a saúde mental em comparação à corporal: {panel.mental_vs_physical_amount()} -> {panel.mental_vs_physical_percentage():.2f}%")


    

    elif option == "C": break
    

    else:
        print("\nOpção inválida. Por favor, escolha A, B ou C.")

