"""
Teste a lógica de substituição de texto principal do MadLibs
"""
from madlibs.story_manager import Story

def test_simple_substitution():
    """Teste uma substituição de texto simples."""
    title = "História de teste"
    content = "O [ANIMAL] [VERBO] rapidamente pelo [LUGAR]."
    
    story = Story(title, content)
    
    # Verifique se os placeholders foram extraídos corretamente
    placeholders = story.get_placeholders()
    print(f"Placeholders encontrados: {placeholders}")
    assert placeholders == ["ANIMAL", "VERBO", "LUGAR"]
    
    # Teste a substituição
    words = {
        "ANIMAL": "gato",
        "VERBO": "correu",
        "LUGAR": "jardim"
    }
    
    filled_story = story.fill_placeholders(words)
    print(f"História original: {content}")
    print(f"História preenchida: {filled_story}")
    assert filled_story == "O gato correu rapidamente pelo jardim."
    
    print("Teste simples de substituição: PASSOU")

def test_repeated_placeholders():
    """Substituição de teste com placeholders repetidos."""
    title = "Teste com repetição"
    content = "O [ANIMAL] viu outro [ANIMAL] e ambos [VERBO] juntos."
    
    story = Story(title, content)
    
    # Verifique se os placeholders duplicados são tratados corretamente
    placeholders = story.get_placeholders()
    print(f"Placeholders encontrados (sem duplicatas): {placeholders}")
    assert placeholders == ["ANIMAL", "VERBO"]
    
    # Teste a substituição com placeholders repetidos
    words = {
        "ANIMAL": "cachorro",
        "VERBO": "brincaram"
    }
    
    filled_story = story.fill_placeholders(words)
    print(f"História original: {content}")
    print(f"História preenchida: {filled_story}")
    assert filled_story == "O cachorro viu outro cachorro e ambos brincaram juntos."
    
    print("Teste com placeholders repetidos: PASSOU")

def test_missing_placeholders():
    """Teste o que acontece quando nem todos os espaços reservados são fornecidos."""
    title = "Teste com palavras ausentes"
    content = "O [ANIMAL] [VERBO] pelo [LUGAR]."
    
    story = Story(title, content)
    
    # Teste a substituição com palavras faltando
    words = {
        "ANIMAL": "elefante",
        # VERBO está faltando
        "LUGAR": "zoológico"
    }
    
    filled_story = story.fill_placeholders(words)
    print(f"História original: {content}")
    print(f"História preenchida (com placeholder faltando): {filled_story}")
    assert "[VERBO]" in filled_story
    
    print("Teste com palavras faltando: PASSOU")

if __name__ == "__main__":
    print("Testando a lógica fundamental de substituição do MadLibs...\n")
    test_simple_substitution()
    print("\n" + "-"*50 + "\n")
    test_repeated_placeholders()
    print("\n" + "-"*50 + "\n")
    test_missing_placeholders()
    print("\nTodos os testes passaram!")