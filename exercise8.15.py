def model(undesigns, completedmodels):
    """Simulasikan mencetak setiap desain hingga daftar habis."""
    while undesigns:
        design = undesigns.pop()
        print(f"Mencetak model: {design}")
        completedmodels.append(design)
def showcompletedmodels(completed_models):
    """Tampilkan semua model yang telah selesai dicetak."""
    print("\nModel-model berikut telah selesai dicetak:")
    for completed_model in completed_models:
        print(completed_model)