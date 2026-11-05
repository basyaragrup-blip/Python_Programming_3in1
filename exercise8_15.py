def print_models(undesigns, completedmodels):  
    """Simulasikan mencetak setiap desain hingga daftar habis."""
    while undesigns:
        design = undesigns.pop()
        print(f"Mencetak model: {design}")
        completedmodels.append(design)
def show_completed_models(completedmodels): 
    """Tampilkan semua model yang telah selesai dicetak."""
    print("\nModel-model berikut telah selesai dicetak:")
    for completedmodel in completedmodels:
        print(completedmodel)