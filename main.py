class Query:
    def __init__(self, query):
        self.type = query[0] #Pieskir pirmo elementu 
        self.number = int(query[1]) #parvers 2 elementu par veselu skailti
        if self.type == 'add':
            self.name = query[2] #pieskir treso elementu no vaicajuma "name", ja ir "add"

def read_queries():
    n = int(input()) #izlasa pirmo intigeri no lietotaja, kas reprezentee query skaitu
    return [Query(input().split()) for i in range(n)] #izveido list kas atkartojas n reizes izveidojot Query objektu katram inputam

def write_responses(result): #panem list ar atbildem un izprintee tos uz 1 linijas
    print('\n'.join(result)) #visas atbildes ieliek viena stringa

def process_queries(queries):
    result = [] #tukss saraksts
    contacts = [] #tukss saraksts
    for cur_query in queries:
        if cur_query.type == 'add': #ja kontaktam ar tadu pasu numuru eksiste, kontakta vards tiek atjauninats
            for contact in contacts:
                if contact.number == cur_query.number:
                    contact.name = cur_query.name
                    break
            else:
                contacts.append(cur_query)
        elif cur_query.type == 'del': # query mekle vai ir kontakts ar tadu pasu vardu un ja vards sakrit kontakts tiek izdzests
            for j in range(len(contacts)):
                if contacts[j].number == cur_query.number:
                    contacts.pop(j)
                    break
        else:
            response = 'not found' # ja kontakts nav atrasts izprintee 'not found' un ieliek to result sarakstaa
            for contact in contacts:
                if contact.number == cur_query.number:
                    response = contact.name
                    break
            result.append(response) #ja
    return result #atgriez result sarakstu 

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))



