import tkinter as tk
from tkinter import messagebox
import random

# Player class to store each player's information
class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.score = 0

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, dmg):
        self.hp = max(0, self.hp - dmg)

# Quiz battle app class
class QuizBattleApp:
    def __init__(self, master):
        self.master = master
        self.master.title("🔥 Quiz Battle Arena")
        self.master.geometry("700x500")
        self.master.configure(bg="#222")

        # Harder question list
        self.questions = [
            ("What is the output of: print(2 ** 3 ** 2)?", "512"),
            ("Capital of Australia?", "Canberra"),
            ("Binary of 13?", "1101"),
            ("Which sorting algorithm has worst-case O(n^2)?", "Bubble sort"),
            ("Who developed Python?", "Guido van Rossum"),
            ("What is 15 % 4?", "3"),
            ("Name of the fastest sorting algorithm?", "Merge sort"),
            ("Which data structure uses FIFO?", "Queue"),
        ]

        self.p1 = Player("Player 1")
        self.p2 = Player("Player 2")
        self.turn = 0
        self.current_question = None

        self.build_gui()

    def build_gui(self):
        self.title = tk.Label(self.master, text="⚔️ Quiz Battle Arena ⚔️", font=("Arial", 24, "bold"), fg="#00ffcc", bg="#222")
        self.title.pack(pady=20)

        self.hp_label = tk.Label(self.master, text="", font=("Arial", 14), fg="white", bg="#222")
        self.hp_label.pack()

        self.q_label = tk.Label(self.master, text="Press START to begin!", font=("Arial", 16), fg="yellow", bg="#222", wraplength=600, justify="center")
        self.q_label.pack(pady=30)

        self.answer_entry = tk.Entry(self.master, font=("Arial", 14), width=40)
        self.answer_entry.pack()

        self.submit_btn = tk.Button(self.master, text="Submit Answer", command=self.check_answer, font=("Arial", 14), bg="#444", fg="white")
        self.submit_btn.pack(pady=10)

        self.start_btn = tk.Button(self.master, text="Start Game", command=self.next_turn, font=("Arial", 14, "bold"), bg="green", fg="white")
        self.start_btn.pack(pady=10)

    def update_ui(self):
        self.hp_label.config(
            text=f"🧍 {self.p1.name} - HP: {self.p1.hp} | Score: {self.p1.score}      ⚔️     {self.p2.name} - HP: {self.p2.hp} | Score: {self.p2.score}"
        )

    def next_turn(self):
        if not self.p1.is_alive() or not self.p2.is_alive():
            winner = self.p1.name if self.p1.hp > 0 else self.p2.name
            messagebox.showinfo("🏆 Game Over!", f"{winner} wins the battle!")
            self.master.destroy()
            return

        self.current_player = self.p1 if self.turn % 2 == 0 else self.p2
        self.opponent = self.p2 if self.current_player == self.p1 else self.p1

        self.current_question, self.current_answer = random.choice(self.questions)
        self.q_label.config(text=f"{self.current_player.name}, your question:\n{self.current_question}")
        self.answer_entry.delete(0, tk.END)
        self.update_ui()

    def check_answer(self):
        user_answer = self.answer_entry.get().strip().lower()
        correct_answer = self.current_answer.lower()
        
        if user_answer == correct_answer:
            dmg = random.randint(10, 30)
            self.opponent.take_damage(dmg)
            self.current_player.score += 1
            self.q_label.config(text=f"✅ Correct! You hit {self.opponent.name} for {dmg} HP.")
        else:
            self.q_label.config(
                text=f"❌ Wrong Answer!\nYour Answer: {user_answer}\nCorrect Answer: {self.current_answer}"
            )

        self.turn += 1
        self.master.after(3000, self.next_turn)

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizBattleApp(root)
    root.mainloop()

