"""
Gerenciamento de histórias para MadLibs - Lógica de substituição de texto principal
"""
import os
import re
from pathlib import Path

class Story:
    """Representa uma história do MadLibs com placeholders."""
    
    def __init__(self, title, content):
        """Inicialize uma história com seu título e conteúdo.

        Args:
            title (str): O título da história
            content (str): O conteúdo da história com placeholders
        """
        self.title = title
        self.content = content
        self.placeholders = self._extract_placeholders()
    
    def _extract_placeholders(self):
        """Extraia todos os placeholders exclusivos do conteúdo da história.

        Retorna:
            list: Uma lista de placeholders exclusivos (sem duplicatas)
        """
        # Procura por padrões como [SUBSTANTIVO], [VERBO], etc.
        # Usa expressão regular para encontrar texto entre colchetes
        placeholders = re.findall(r'\[([^\]]+)\]', self.content)
        
        # Remove duplicatas preservando a ordem de aparição
        unique_placeholders = []
        for placeholder in placeholders:
            if placeholder not in unique_placeholders:
                unique_placeholders.append(placeholder)
                
        return unique_placeholders
    
    def get_placeholders(self):
        """Retorne a lista de espaços reservados na história.
        
        Returns:
            list: A lista de marcadores de posição
        """
        return self.placeholders
    
    def fill_placeholders(self, words):
        """Preencha os espaços reservados com as palavras fornecidas.
        
        Esta é a lógica central de substituição de texto do MadLibs.
        
        Args:
            words (dict): Mapeamento de espaços reservados para palavras no dicionário
                          (e.g., {'SUBSTANTIVO': 'cachorro', 'VERBO': 'correr'})
        
        Returns:
            str: A história com todos os placeholders substituídos por palavras
        """
        filled_content = self.content
        
        # Substitui cada placeholder pela palavra correspondente
        for placeholder, word in words.items():
            # Substitui todos os casos de [PLACEHOLDER] por word
            filled_content = filled_content.replace(f"[{placeholder}]", word)
            
        return filled_content


class StoryManager:
    """Gerencia o carregamento, salvamento e processamento de histórias."""
    
    def __init__(self, stories_dir="stories", saved_dir="saved"):
        """Inicialize o gerenciador de histórias.
        
        Args:
            stories_dir (str): Diretório contendo modelos de história
            saved_dir (str): Diretório para salvar histórias concluídas
        """
        self.stories_dir = Path(stories_dir)
        self.saved_dir = Path(saved_dir)
        
        # Garantir que os diretórios existam
        self.stories_dir.mkdir(exist_ok=True)
        self.saved_dir.mkdir(exist_ok=True)
    
    def get_available_stories(self):
        """Obtenha uma lista de arquivos de histórias disponíveis.
        
        Returns:
            list: Lista de nomes de arquivos de história
        """
        return [f.name for f in self.stories_dir.glob("*.txt")]
    
    def load_story(self, filename):
        """Carregar uma história do arquivo.
        
        Args:
            filename (str): Nome do arquivo da história
            
        Returns:
            Story: Um objeto Story com título e conteúdo
            
        Raises:
            FileNotFoundError: Se o arquivo da história não existir
        """
        file_path = self.stories_dir / filename
        
        with open(file_path, 'r', encoding='utf-8') as file:
            # A primeira linha é o título
            title = file.readline().strip()
            # O resto é o conteúdo
            content = file.read().strip()
            
        return Story(title, content)
    
    def create_sample_story(self):
        """Crie um arquivo de história de amostra para fins de teste."""
        sample_story = """Viagem à Montanha
                        No último fim de semana, fui acampar nas [LUGAR]. Acordei cedo e coloquei minha [SUBSTANTIVO] na mochila.
                        Durante a trilha, vi um [ANIMAL] [VERBO NO GERÚNDIO] alegremente.
                        O tempo estava muito [ADJETIVO], o que tornou a caminhada ainda mais [ADJETIVO].
                        Quando cheguei ao topo, gritei "[EXCLAMAÇÃO]!" pela vista incrível.
                        """
        sample_path = self.stories_dir / "viagem.txt"
        
        with open(sample_path, 'w', encoding='utf-8') as file:
            file.write(sample_story)
        
        return "viagem.txt"
    
    def save_story(self, name, content):
        """Salvar uma história concluída.
        
        Args:
            name (str): Nome para a história salva
            content (str): Conteúdo da história concluída
            
        Returns:
            str: O nome do arquivo da história salva
        """
        # Sanitizar o nome do arquivo (remover caracteres especiais)
        safe_name = "".join(c if c.isalnum() else "_" for c in name)
        file_path = self.saved_dir / f"{safe_name}.txt"
        
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
            
        return file_path.name
    
    def get_saved_stories(self):
        """Obtenha uma lista de arquivos de histórias salvos.
        
        Returns:
            list: Lista de nomes de arquivos de histórias salvas
        """
        return [f.name for f in self.saved_dir.glob("*.txt")]
    
    def load_saved_story(self, filename):
        """Carregar uma história salva.
        
        Args:
            filename (str): Nome do arquivo de história salvo
            
        Returns:
            str: Conteúdo da história salva
            
        Raises:
            FileNotFoundError: Se a história salva não existir
        """
        file_path = self.saved_dir / filename
        
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
