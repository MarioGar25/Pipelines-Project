import random
def wild_pokemon(pokemon, team):
    
    wild_pokemon = random.choice(pokemon["Name"])
    my_pokemon = team[0]
    
    
    
    print(f"Oh vaya! Un {wild_pokemon} salvaje apareció.")
    print(f"Adelante {my_pokemon}!!")
    
    
    
    
    w_p_s = pokemon[pokemon["Name"] == wild_pokemon]
    m_p = pokemon[pokemon["Name"] == my_pokemon]
    
    ax = m_p.plot(kind="bar")
    ax1 = w_p_s.plot(kind="bar")
    ax.legend(loc="center left", bbox_to_anchor=(1, 0.5))

    first_choice = input("Quieres continuar o escapar: ")
    m_p.equal(w_p_s)
    if first_choice.lower() == "escapar":
        return "Escapaste sin problemas!!"
    elif first_choice == "continuar":
        if w_p_s["Speed"] > m_p["Speed"]:
            m_p["HP"] - (w_p_s["Attack"] - (m_p["Defense"]/2))
            if m_p["HP"] <= 0:
                return "Corre al medicooo!!"
            else: 
                w_p_s["HP"] - (m_p["Attack"] - (w_p_s["Defense"]/2))
                if w_p_s["HP"] <= 0:
                    return "Mala suerte, el Pokemon se ha debilitado"
                else:
                    second_choice = input(f"Quieres capturar a {wild_pokemon}[Y/N]: ")
                    if second_choice.lower() == "n":
                        return "Escapaste sin problemas"
                    else:
                        print(f"Lanzas una pokeball")
                        x = random.randint(11, 1)
                        if x > 3:
                            team.append(wild_pokemon)
                            return  f"Felicidades {wild_pokemon} atrapado!! Se unirá a tu equipo"
                        else:
                            return f"Vaya! {wild_pokemon} ha espacadoo y ha huido!!"
        elif w_p_s["Speed"] <= m_p["Speed"]:
            w_p_s["HP"] - (m_p["Attack"]) - (w_p_s["Defense"]/2)
            if w_p_s["HP"] <= 0:
                    return "Mala suerte, el Pokemon se ha debilitado"
            else:
                thrid_choice = input(f"Quieres capturar a {wild_pokemon}[Y/N]: ")
                if third_choice.lower() == "n":
                    return "Escapaste sin problemas"
                else:
                    print(f"Lanzas una pokeball")
                    x = random.randint(11, 1)
                    if x > 3:
                        team.append(wild_pokemon)
                        return  f"Felicidades {wild_pokemon} atrapado!! Se unirá a tu equipo"
                    else:
                        return f"Vaya! {wild_pokemon} ha espacadoo y ha huido!!"

