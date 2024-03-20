import random

def nicknames(ism):
    a1 = f"꧁☆ {ism} ☆꧂"
    
    a2 = f"❄️|•|💫 {ism} •|•|•|•"
    
    a3 = f"🚀🪐 {ism} 🌪️🌿☄️"
    
    a4 = f"❄️彡 {ism} 彡❄️"
    
    a5 = f"⚜️🔱 {ism} 🔱⚜️"
    
    a6 = f"🧲💸 {ism} 💸🧲"
    
    lst = [a1, a2, a3, a4, a5, a6]
    
    b = random.choice(lst)
    return b
    

print(nicknames("Diyorbek"))