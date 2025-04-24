
class GenerationResult:
    
    def __init__(self):
        # The current indentation level.
        GenerationResult.tabs = 0
        self._raw_text = ""
        self.text = ""
        
        self.set_variable("text")
        self.current_var = "text"
        self.checkpoints_stack = list()
    
    def get_text(self) -> str :
        return self._raw_text
        
    def set_text(self, text:str):
        self._raw_text = text
    
    raw_text = property(get_text, set_text)
    
    def do_print(self, to_print:str) :
        """Concatene the given text to the generated string."""
        tabs = ""
        if self.raw_text.endswith('\n') or self.raw_text == "":
            tabs = '\t' * GenerationResult.tabs
        self.raw_text += tabs + to_print

    def end_section(self) :
        self.raw_text += '\n'
    
    def print_to_console(self) :
        print(self.text)
    
    def set_variable(self, var_name:str):
        setattr(self, var_name, "")
    
    def print(self, new_test:str):
        setattr(self, self.current_var, self.current_var + new_test)

    def stack(self):
        self.checkpoints_stack.append(self.raw_text)
        self.raw_text = ""
    
    def unstack(self) -> str:
        ret = self.raw_text
        self.raw_text = self.checkpoints_stack.pop() + self.raw_text
        return ret
        