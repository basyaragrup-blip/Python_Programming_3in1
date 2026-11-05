rivers = {
    'nil': 'egypt',
    'amazon': 'brazil',
    'kapuas': 'indonesia',
}
for river, country in rivers.items():
    print(f"Sungai {river.title()} mengalir melewati negara {country.title()}.")
print("\nDaftar nama sungai:")
for river in rivers.keys():
    print(f"- {river.title()}")
print("\nDaftar nama negara:")
for country in rivers.values():
    print(f"- {country.title()}")