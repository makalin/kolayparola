import random
import string

# Kelime listesi
WORDS = ["Mavi", "Kırmızı", "Yeşil", "Büyük", "Küçük", "Hızlı", "Yavaş", "Güçlü", "Zayıf", "Yüksek", "Derin", "Parlak", "Sessiz", "Canlı", "Mutlu", "Üzgün", "Sert", "Yumuşak", "Keskin", "Donuk", "Açık", "Kapalı", "Uzun", "Kısa", "İnce", "Kalın", "Düz", "Kıvrımlı", "Soğuk", "Sıcak"]

# Word list
# WORDS = ["Blue", "Red", "Green", "Big", "Small", "Fast", "Slow", "Strong", "Weak", "High", "Deep", "Bright", "Silent", "Lively", "Happy", "Sad", "Hard", "Soft", "Sharp", "Dull", "Open", "Closed", "Long", "Short", "Thin", "Thick", "Straight", "Curved", "Cold", "Hot"]


# Rakamlar ve özel karakterler
NUMBERS = "0123456789"
SPECIAL_CHARS = "!@#$%^&*"

def generate_password():
    """Hatırlanması kolay ama güçlü parola üretir."""
    word1 = random.choice(WORDS)
    word2 = random.choice(WORDS)
    number = random.choice(NUMBERS) + random.choice(NUMBERS)
    special = random.choice(SPECIAL_CHARS)
    
    password = f"{word1}{word2}{special}{number}"
    return password

if __name__ == "__main__":
    print("Parola:", generate_password())
