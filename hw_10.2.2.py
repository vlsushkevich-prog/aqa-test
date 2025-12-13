class Logger:
    def log(self, message):
        print(f"[Log] {message}")

class Service(Logger):
    def process(self):
        self.log("Начал обработку")
        print("Обрабатываю")
        self.log("Закончил обработку")

s = Service()
s.process()