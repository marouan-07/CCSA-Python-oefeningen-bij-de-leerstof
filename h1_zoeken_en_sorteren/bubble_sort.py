def bubble_sort(a):
    n = len(a)
    aantal = 0  # Teller om bij te houden hoe vaak het if-statement wordt uitgevoerd
    
    # Buitenste lus van i = 0 tot n-2
    for i in range(n - 1):
        # Binnenste lus van j = n-1 afstappen tot i+1 (achterwaarts)
        for j in range(n - 1, i, -1):
            aantal += 1  # Tel elke uitvoering van de controle
            if a[j - 1] > a[j]:
                # Wissel de elementen a[j-1] en a[j]
                a[j - 1], a[j] = a[j], a[j - 1]
        
        # Druk de rij af na elke iteratie van de buitenste lus
        print(a)
        
    # Druk het totaal aantal uitvoeringen van het if-statement af
    print(f"Voor een rij van lengte {n} werd het if-statement {aantal} keer uitgevoerd")


# Hoe je de invoer inleest en de functie aanroept volgens de opgave:
if __name__ == "__main__":
    a = [int(_) for _ in input().split()]
    bubble_sort(a)

