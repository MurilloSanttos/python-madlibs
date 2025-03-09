import os

# Criar diretório de histórias se não existir
os.makedirs("stories", exist_ok=True)

# História 1: Aventura na Floresta
aventura = """Aventura na Floresta Encantada
Era uma vez, em uma [ADJETIVO] floresta, vivia um [ANIMAL] muito [ADJETIVO].
Todos os dias, ele [VERBO NO PASSADO] pela floresta e [VERBO NO PASSADO] com seus amigos.
Um dia, encontrou uma [SUBSTANTIVO] [ADJETIVO] escondida atrás de uma [SUBSTANTIVO].
"[EXCLAMAÇÃO]!" gritou o [ANIMAL]. "Encontrei um tesouro [ADJETIVO]!"
Ele decidiu levar a [SUBSTANTIVO] para sua [LUGAR] e guardá-la para sempre.
Desde então, o [ANIMAL] se tornou o mais [ADJETIVO] da floresta e viveu [ADVÉRBIO] feliz."""

# História 2: Viagem Espacial
viagem = """Missão no Espaço Sideral
O astronauta [NOME] estava pronto para sua [ADJETIVO] missão no espaço.
Ele embarcou na nave [NOME DE NAVE] com seu fiel [ANIMAL] de estimação.
Durante a decolagem, a nave fez um barulho [ONOMATOPEIA] e [VERBO NO PASSADO] para o céu.
Ao chegar no espaço, [NOME] viu [NÚMERO] [SUBSTANTIVO PLURAL] flutuando ao redor.
"Nossa nave precisa de mais [SUBSTANTIVO]," disse o comandante pelo rádio.
[NOME] respondeu: "Vou [VERBO INFINITIVO] para encontrar [SUBSTANTIVO] suficiente!"
A missão durou [NÚMERO] [UNIDADE DE TEMPO PLURAL] e foi considerada um sucesso [ADJETIVO]."""

# História 3: Receita Maluca
receita = """Receita Secreta do Chef
Para preparar o famoso [SUBSTANTIVO] [ADJETIVO] do Chef [NOME], você vai precisar:
- 2 xícaras de [SUBSTANTIVO PLURAL]
- 3 colheres de [SUBSTANTIVO] [ADJETIVO]
- Um punhado de [SUBSTANTIVO PLURAL] frescos
- [NÚMERO] gotas de extrato de [SUBSTANTIVO]

Primeiro, [VERBO] os [SUBSTANTIVO PLURAL] em uma panela [ADJETIVO].
Depois, adicione o [SUBSTANTIVO] e mexa [ADVÉRBIO] por [NÚMERO] minutos.
Quando a mistura ficar [ADJETIVO], grite "[EXCLAMAÇÃO]!" e adicione os ingredientes restantes.
Sirva [ADJETIVO] com um pouco de [SUBSTANTIVO] por cima.
O Chef [NOME] garante que todos vão [VERBO] de alegria!"""

# História 4: Dia na Praia
praia = """Um Dia Inesquecível na Praia
No último [DIA DA SEMANA], fui à praia com meu [MEMBRO DA FAMÍLIA] e levamos nosso [ADJETIVO] [SUBSTANTIVO].
O tempo estava [ADJETIVO], com o sol [VERBO NO GERÚNDIO] intensamente.
Enquanto eu [VERBO NO PASSADO] na areia, vi um [ANIMAL] [VERBO NO GERÚNDIO] na água.
"[EXCLAMAÇÃO]!" gritei, "[VERBO] rápido para ver isso!"
Meu [MEMBRO DA FAMÍLIA] estava ocupado [VERBO NO GERÚNDIO] um castelo de areia [ADJETIVO].
Decidimos comer nosso lanche: sanduíches de [SUBSTANTIVO] com [SUBSTANTIVO].
Foi o dia mais [ADJETIVO] que já tive em uma praia!"""

# História 5: Fábula Moderna
fabula = """A Fábula do [ANIMAL] e do [ANIMAL]
Em uma [ADJETIVO] cidade, um [ANIMAL] [ADJETIVO] e um [ANIMAL] [ADJETIVO] eram vizinhos.
O [ANIMAL] sempre [VERBO NO PASSADO] muito cedo e [VERBO NO PASSADO] o dia todo.
Já o [ANIMAL] preferia [VERBO INFINITIVO] e só [VERBO NO PASSADO] quando necessário.
Um dia, um [SUBSTANTIVO] [ADJETIVO] apareceu no bairro, causando [SUBSTANTIVO].
O [ANIMAL] disse: "Devemos [VERBO INFINITIVO] imediatamente!"
Mas o [ANIMAL] respondeu: "Prefiro [VERBO INFINITIVO] com [SUBSTANTIVO] primeiro."
No final, eles aprenderam que é melhor [VERBO INFINITIVO] juntos do que [VERBO INFINITIVO] separados.
A moral da história é: "[FRASE DE MORAL]"."""

# Salvar histórias em arquivos
with open("stories/aventura_floresta.txt", "w", encoding="utf-8") as f:
    f.write(aventura)

with open("stories/viagem_espacial.txt", "w", encoding="utf-8") as f:
    f.write(viagem)

with open("stories/receita_maluca.txt", "w", encoding="utf-8") as f:
    f.write(receita)

with open("stories/dia_praia.txt", "w", encoding="utf-8") as f:
    f.write(praia)

with open("stories/fabula_moderna.txt", "w", encoding="utf-8") as f:
    f.write(fabula)

print("Templates de histórias criados com sucesso no diretório 'stories'!")