import tkinter as tk
from tkinter import ttk, messagebox
import random

class VerbPracticeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Practica de Verbos Regulares en Ingles")
        self.root.geometry("800x600")
        self.root.configure(bg='lightgray')
        
        # Lista de verbos del PDF
        self.verbs = [
            ("Abandonar", "Abandon", "Abandoned"),
            ("Abolir", "Abolish", "Abolished"),
            ("Abrir", "Open", "Opened"),
            ("Absorber", "Absorb", "Absorbed"),
            ("Abusar", "Abuse", "Abused"),
            ("Acceder", "Accede", "Acceded"),
            ("Acentuar", "Accent", "Accented"),
            ("Acercarse", "Approach", "Approached"),
            ("Aconsejar", "Advice", "Advised"),
            ("Acordar", "Agree", "Agreed"),
            ("Actuar", "Act", "Acted"),
            ("Acusar", "Accuse", "Accused"),
            ("Adivinar", "Guess", "Guessed"),
            ("Administrar", "Manage", "Managed"),
            ("Admirar", "Admire", "Admired"),
            ("Admitir", "Admit", "Admitted"),
            ("Adorar", "Adore", "Adored"),
            ("Adquirir", "Acquire", "Acquired"),
            ("Agradecer", "Thank", "Thanked"),
            ("Anadir", "Add", "Added"),
            ("Anunciar", "Advertise", "Advertised"),
            ("Anunciar", "Announce", "Announced"),
            ("Aparcar", "Park", "Parked"),
            ("Aparecer", "Appear", "Appeared"),
            ("Aprobar", "Pass", "Passed"),
            ("Apurarse", "Hurry", "Hurried"),
            ("Archivar", "File", "Filed"),
            ("Arreglar", "Arrange", "Arranged"),
            ("Arreglar", "Fix", "Fixed"),
            ("Arrestar", "Arrest", "Arrested"),
            ("Asegurar", "Assure", "Assured"),
            ("Asistir", "Assist", "Assisted"),
            ("Atacar", "Attack", "Attacked"),
            ("Atar", "Tie", "Tied"),
            ("Avanzar", "Advance", "Advanced"),
            ("Ayudar", "Help", "Helped"),
            ("Bailar", "Dance", "Danced"),
            ("Bendecir", "Bless", "Blessed"),
            ("Besar", "Kiss", "Kissed"),
            ("Buscar", "Search", "Searched"),
            ("Calentar", "Warm", "Warmed"),
            ("Cambiar", "Change", "Changed"),
            ("Caminar", "Walk", "Walked"),
            ("Cargar", "Charge", "Charged"),
            ("Casarse", "Marry", "Married"),
            ("Castigar", "Punish", "Punished"),
            ("Cepillar", "Brush", "Brushed"),
            ("Cerrar", "Close", "Closed"),
            ("Chocar", "Crash", "Crashed"),
            ("Cobrar", "Cash", "Cashed"),
            ("Cocinar", "Cook", "Cooked"),
            ("Combinar", "Combine", "Combined"),
            ("Comenzar", "Start", "Started"),
            ("Cometer", "Commit", "Committed"),
            ("Comparar", "Compare", "Compared"),
            ("Complacer", "Please", "Pleased"),
            ("Completar", "Complete", "Completed"),
            ("Componer", "Compose", "Composed"),
            ("Comportarse", "Behave", "Behaved"),
            ("Comprobar", "Check", "Checked"),
            ("Comprometer", "Engage", "Engaged"),
            ("Confiar", "Trust", "Trusted"),
            ("Considerar", "Consider", "Considered"),
            ("Consistir", "Consist", "Consisted"),
            ("Contar", "Count", "Counted"),
            ("Contener", "Contain", "Contained"),
            ("Continuar", "Continue", "Continued"),
            ("Copiar", "Copy", "Copied"),
            ("Coronar", "Crown", "Crowned"),
            ("Creer", "Believe", "Believed"),
            ("Cruzar", "Cross", "Crossed"),
            ("Cubrir", "Cover", "Covered"),
            ("Cuidar", "Care", "Cared"),
            ("Culpar", "Blame", "Blamed"),
            ("Declarar", "Declare", "Declared"),
            ("Dedicar", "Devote", "Devoted"),
            ("Dejar caer", "Drop", "Dropped"),
            ("Deletrear", "Spell", "Spelled"),
            ("Demorar", "Delay", "Delayed"),
            ("Denegar", "Deny", "Denied"),
            ("Desear", "Hope", "Hoped"),
            ("Desear", "Wish", "Wished"),
            ("Destruir", "Destroy", "Destroyed"),
            ("Detener", "Stop", "Stopped"),
            ("Dirigirse", "Address", "Addressed"),
            ("Disculparse", "Apologize", "Apologized"),
            ("Disfrutar", "Enjoy", "Enjoyed"),
            ("Disparar", "Fire", "Fired"),
            ("Empujar", "Push", "Pushed"),
            ("Entregar", "Deliver", "Delivered"),
            ("Entrenar", "Train", "Trained"),
            ("Entretener", "Amuse", "Amused"),
            ("Enumerar", "Number", "Numbered"),
            ("Envidiar", "Envy", "Envied"),
            ("Equilibrar", "Balance", "Balanced"),
            ("Escalar", "Climb", "Climbed"),
            ("Esperar", "Wait", "Waited"),
            ("Estudiar", "Study", "Studied"),
            ("Evitar", "Avoid", "Avoided"),
            ("Exclamar", "Exclaim", "Exclaimed"),
            ("Explicar", "Explain", "Explained"),
            ("Expresar", "Express", "Expressed"),
            ("Extranar", "Miss", "Missed"),
            ("Firmar", "Sign", "Signed"),
            ("Fracasar", "Fail", "Failed"),
            ("Freir", "Fry", "Fried"),
            ("Fumar", "Smoke", "Smoked"),
            ("Ganar", "Gain", "Gained"),
            ("Girar", "Turn", "Turned"),
            ("Gustar", "Like", "Liked"),
            ("Hablar", "Talk", "Talked"),
            ("Herir", "Wound", "Wounded"),
            ("Imaginar", "Imagine", "Imagined"),
            ("Intentar", "Attempt", "Attempted"),
            ("Intentar", "Try", "Tried"),
            ("Jugar", "Play", "Played"),
            ("Juzgar", "Judge", "Judged"),
            ("Lavar", "Wash", "Washed"),
            ("Levantar", "Raise", "Raised"),
            ("Limpiar", "Clean", "Cleaned"),
            ("Llamar", "Call", "Called"),
            ("Llegar", "Arrive", "Arrived"),
            ("Llenar", "Fill", "Filled"),
            ("Llevar", "Carry", "Carried"),
            ("Llevar a cabo", "Perform", "Performed"),
            ("Llorar", "Cry", "Cried"),
            ("Llover", "Rain", "Rained"),
            ("Mandar", "Command", "Commanded"),
            ("Mantener", "Maintain", "Maintained"),
            ("Marcar", "Mark", "Marked"),
            ("Masajear", "Massage", "Massaged"),
            ("Matar", "Kill", "Killed"),
            ("Medir", "Measure", "Measured"),
            ("Mirar", "Look", "Looked"),
            ("Molestar", "Annoy", "Annoyed"),
            ("Morir", "Die", "Died"),
            ("Mover", "Move", "Moved"),
            ("Navegar", "Sail", "Sailed"),
            ("Nombrar", "Name", "Named"),
            ("Notar", "Note", "Noted"),
            ("Notificar", "Notice", "Noticed"),
            ("Observar", "Observe", "Observed"),
            ("Observar", "Watch", "Watched"),
            ("Ofrecer", "Offer", "Offered"),
            ("Ordenar", "Order", "Ordered"),
            ("Permanecer", "Stay", "Stayed"),
            ("Permitir", "Allow", "Allowed"),
            ("Pertenecer", "Belong", "Belonged"),
            ("Pesar", "Weigh", "Weighed"),
            ("Pescar", "Fish", "Fished"),
            ("Planificar", "Plan", "Planned"),
            ("Practicar", "Practice", "Practiced"),
            ("Preferir", "Prefer", "Preferred"),
            ("Preguntar", "Ask", "Asked"),
            ("Preocuparse", "Worry", "Worried"),
            ("Preparar", "Prepare", "Prepared"),
            ("Probar", "Taste", "Tasted"),
            ("Prometer", "Promise", "Promised"),
            ("Pronunciar", "Pronounce", "Pronounced"),
            ("Querer", "Want", "Wanted"),
            ("Rechazar", "Refuse", "Refused"),
            ("Recibir", "Receive", "Received"),
            ("Reclamar", "Claim", "Claimed"),
            ("Recoger", "Pick", "Picked"),
            ("Recolectar", "Collect", "Collected"),
            ("Recordar", "Remember", "Remembered"),
            ("Regar", "Water", "Watered"),
            ("Registrar", "Register", "Registered"),
            ("Reir", "Laugh", "Laughed"),
            ("Reparar", "Repair", "Repaired"),
            ("Repetir", "Repeat", "Repeated"),
            ("Reportar", "Report", "Reported"),
            ("Requerir", "Require", "Required"),
            ("Reservar", "Reserve", "Reserved"),
            ("Resolver", "Resolve", "Resolved"),
            ("Respirar", "Breathe", "Breathed"),
            ("Responder", "Answer", "Answered"),
            ("Rezar", "Pray", "Prayed"),
            ("Salvar", "Save", "Saved"),
            ("Secar", "Dry", "Dried"),
            ("Seguir", "Follow", "Followed"),
            ("Servir", "Serve", "Served"),
            ("Silbar", "Whistle", "Whistled"),
            ("Solicitar", "Request", "Requested"),
            ("Sonar", "Sound", "Sounded"),
            ("Sonreir", "Smile", "Smiled"),
            ("Sorprender", "Surprise", "Surprised"),
            ("Suceder", "Happen", "Happened"),
            ("Sufrir", "Suffer", "Suffered"),
            ("Suplicar", "Beg", "Begged"),
            ("Telefonear", "Phone", "Phoned"),
            ("Terminar", "Finish", "Finished"),
            ("Testear", "Test", "Tested"),
            ("Tocar", "Touch", "Touched"),
            ("Trabajar", "Work", "Worked"),
            ("Traducir", "Translate", "Translated"),
            ("Unir", "Unite", "United"),
            ("Usar", "Use", "Used"),
            ("Variar", "Vary", "Varied"),
            ("Vestir", "Dress", "Dressed"),
            ("Viajar", "Travel", "Traveled"),
            ("Visitar", "Visit", "Visited")
        ]
        
        self.current_verb = None
        self.score = 0
        self.total_questions = 0
        
        self.setup_ui()
        self.new_question()
        
    def setup_ui(self):
        # Titulo principal
        title_label = tk.Label(self.root, text="Practica de Verbos Regulares", 
                              font=('Arial', 20, 'bold'), bg='lightgray', fg='darkblue')
        title_label.pack()
        title_label.pack_configure(pady=20)
        
        # Frame principal
        main_frame = tk.Frame(self.root, bg='lightgray')
        main_frame.pack(expand=True, fill='both')
        main_frame.pack_configure(padx=20)
        
        # Marcador de puntuacion
        self.score_label = tk.Label(main_frame, text="Puntuacion: 0/0 (0%)", 
                                   font=('Arial', 14), bg='lightgray', fg='darkgreen')
        self.score_label.pack()
        self.score_label.pack_configure(pady=20)
        
        # Frame para la pregunta
        question_frame = tk.Frame(main_frame, bg='white', relief='raised', bd=2)
        question_frame.pack(fill='x')
        question_frame.pack_configure(pady=20)
        
        # Etiqueta de pregunta
        self.question_label = tk.Label(question_frame, text="", 
                                      font=('Arial', 18, 'bold'), 
                                      bg='white', fg='darkblue')
        self.question_label.pack()
        self.question_label.pack_configure(pady=20)
        
        # Etiqueta del infinitivo
        self.infinitive_label = tk.Label(question_frame, text="", 
                                        font=('Arial', 16), 
                                        bg='white', fg='blue')
        self.infinitive_label.pack()
        self.infinitive_label.pack_configure(pady=20)
        
        # Frame para las opciones
        self.options_frame = tk.Frame(main_frame, bg='lightgray')
        self.options_frame.pack()
        self.options_frame.pack_configure(pady=20, fill='x')
        
        # Variable para la seleccion
        self.selected_option = tk.StringVar()
        self.option_buttons = []
        
        # Frame para botones de control
        control_frame = tk.Frame(main_frame, bg='lightgray')
        control_frame.pack()
        control_frame.pack_configure(pady=20)
        
        # Boton verificar
        self.check_button = tk.Button(control_frame, text="Verificar Respuesta", 
                                     command=self.check_answer, 
                                     font=('Arial', 12, 'bold'),
                                     bg='green', fg='white', 
                                     padx=20, pady=10, cursor='hand2')
        self.check_button.pack(side='left')
        self.check_button.pack_configure(padx=10)
        
        # Boton siguiente
        self.next_button = tk.Button(control_frame, text="Siguiente Pregunta", 
                                    command=self.new_question, 
                                    font=('Arial', 12, 'bold'),
                                    bg='blue', fg='white', 
                                    padx=20, pady=10, cursor='hand2',
                                    state='disabled')
        self.next_button.pack(side='left')
        self.next_button.pack_configure(padx=10)
        
        # Boton reiniciar
        self.reset_button = tk.Button(control_frame, text="Reiniciar", 
                                     command=self.reset_game, 
                                     font=('Arial', 12),
                                     bg='red', fg='white', 
                                     padx=20, pady=10, cursor='hand2')
        self.reset_button.pack(side='left')
        self.reset_button.pack_configure(padx=10)
        
        # Etiqueta de retroalimentacion
        self.feedback_label = tk.Label(main_frame, text="", 
                                      font=('Arial', 14, 'bold'), 
                                      bg='lightgray')
        self.feedback_label.pack()
        self.feedback_label.pack_configure(pady=10)
        
    def new_question(self):
        # Seleccionar verbo aleatorio
        self.current_verb = random.choice(self.verbs)
        spanish, infinitive, past = self.current_verb
        
        # Actualizar interfaz
        self.question_label.config(text="Cual es el pasado de este verbo?")
        self.infinitive_label.config(text=f'"{spanish}" -> {infinitive}')
        
        # Limpiar opciones anteriores
        for button in self.option_buttons:
            button.destroy()
        self.option_buttons = []
        
        # Generar opciones (respuesta correcta + 3 incorrectas)
        correct_answer = past
        wrong_answers = []
        
        # Generar respuestas incorrectas
        while len(wrong_answers) < 3:
            random_verb = random.choice(self.verbs)
            wrong_answer = random_verb[2]  # pasado
            if wrong_answer != correct_answer and wrong_answer not in wrong_answers:
                wrong_answers.append(wrong_answer)
        
        # Combinar y mezclar opciones
        all_options = [correct_answer] + wrong_answers
        random.shuffle(all_options)
        
        # Crear botones de opcion
        self.selected_option.set("")
        
        for i, option in enumerate(all_options):
            btn = tk.Radiobutton(self.options_frame, text=option, 
                               variable=self.selected_option, value=option,
                               font=('Arial', 14), bg='lightgray', 
                               activebackground='lightblue',
                               padx=20, pady=10, cursor='hand2')
            btn.grid(row=i//2, column=i%2, sticky='w', padx=20, pady=5)
            self.option_buttons.append(btn)
        
        # Habilitar boton de verificar, deshabilitar siguiente
        self.check_button.config(state='normal')
        self.next_button.config(state='disabled')
        self.feedback_label.config(text="")
        
    def check_answer(self):
        if not self.selected_option.get():
            messagebox.showwarning("Atencion", "Por favor selecciona una respuesta.")
            return
        
        self.total_questions += 1
        correct_answer = self.current_verb[2]
        
        if self.selected_option.get() == correct_answer:
            self.score += 1
            self.feedback_label.config(text="Correcto!", fg='green')
        else:
            self.feedback_label.config(
                text=f"Incorrecto. La respuesta correcta es: {correct_answer}", 
                fg='red'
            )
        
        # Actualizar marcador
        percentage = (self.score / self.total_questions) * 100 if self.total_questions > 0 else 0
        self.score_label.config(text=f"Puntuacion: {self.score}/{self.total_questions} ({percentage:.1f}%)")
        
        # Deshabilitar verificar, habilitar siguiente
        self.check_button.config(state='disabled')
        self.next_button.config(state='normal')
        
    def reset_game(self):
        self.score = 0
        self.total_questions = 0
        self.score_label.config(text="Puntuacion: 0/0 (0%)")
        self.new_question()


if __name__ == "__main__":
    root = tk.Tk()
    app = VerbPracticeApp(root)
    root.mainloop()