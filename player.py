def player(x, y, canva, zoom=1.0):
    ####################
    ####### BACK #######
    ####################
    bg1 = canva.create_rectangle(
        x + 15*zoom, y + 5*zoom, x + 35*zoom, y + 65*zoom, fill="black", tags="player")
    bg2 = canva.create_rectangle(
        x + 5*zoom, y + 30*zoom, x + 45*zoom, y + 60*zoom, fill="black", tags="player")

    ####################
    ####### HEAD #######
    ####################
    he1 = canva.create_rectangle(x + 20*zoom, y, x + 30*zoom, y + 5*zoom, fill="white", outline="black", tags="player")
    he2_1 = canva.create_rectangle(x + 15*zoom, y + 5*zoom, x + 20*zoom, y + 10*zoom, fill="white", outline="black", tags="player")
    he2_2 = canva.create_rectangle(x + 30*zoom, y + 5*zoom, x + 35*zoom, y + 10*zoom, fill="white", outline="black", tags="player")
    he3_1 = canva.create_rectangle(x + 10*zoom, y + 10*zoom, x + 15*zoom, y + 20*zoom, fill="white", outline="black", tags="player")
    he3_2 = canva.create_rectangle(x + 35*zoom, y + 10*zoom, x + 40*zoom, y + 20*zoom, fill="white", outline="black", tags="player")
    he4_1 = canva.create_rectangle(x + 15*zoom, y + 20*zoom, x + 20*zoom, y + 25*zoom, fill="white", outline="black", tags="player")
    he4_2 = canva.create_rectangle(x + 30*zoom, y + 20*zoom, x + 35*zoom, y + 25*zoom, fill="white", outline="black", tags="player")

    ####################
    ####### BODY #######
    ####################
    b1_1 = canva.create_rectangle(x + 10*zoom, y + 25*zoom, x + 15*zoom, y + 30*zoom, fill="white", outline="black", tags="player")
    b1_2 = canva.create_rectangle(x + 35*zoom, y + 25*zoom, x + 40*zoom, y + 30*zoom, fill="white", outline="black", tags="player")
    b2_1 = canva.create_rectangle(x + 5*zoom, y + 30*zoom, x + 10*zoom, y + 35*zoom, fill="white", outline="black", tags="player")
    b2_2 = canva.create_rectangle(x + 40*zoom, y + 30*zoom, x + 45*zoom, y + 35*zoom, fill="white", outline="black", tags="player")
    b3_1 = canva.create_rectangle(x, y + 35*zoom, x + 5*zoom, y + 55*zoom, fill="white", outline="black", tags="player")
    b3_2 = canva.create_rectangle(x + 45*zoom, y + 35*zoom, x + 50*zoom, y + 55*zoom, fill="white", outline="black", tags="player")
    b4_1 = canva.create_rectangle(x + 5*zoom, y + 55*zoom, x + 10*zoom, y + 60*zoom, fill="white", outline="black", tags="player")
    b4_2 = canva.create_rectangle(x + 40*zoom, y + 55*zoom, x + 45*zoom, y + 60*zoom, fill="white", outline="black", tags="player")
    b5_1 = canva.create_rectangle(x + 10*zoom, y + 60*zoom, x + 20*zoom, y + 65*zoom, fill="white", outline="black", tags="player")
    b5_2 = canva.create_rectangle(x + 30*zoom, y + 60*zoom, x + 40*zoom, y + 65*zoom, fill="white", outline="black", tags="player")
    b6 = canva.create_rectangle(x + 20*zoom, y + 65*zoom, x + 30*zoom, y + 70*zoom, fill="white", outline="black", tags="player")

    ####################
    ####### FOOT #######
    ####################
    f1_2 = canva.create_rectangle(x + 10*zoom, y + 70*zoom, x + 15*zoom, y + 75*zoom, fill="brown", outline="black", tags=("player", "fl2"))
    f1_1 = canva.create_rectangle(x + 15*zoom, y + 70*zoom, x + 20*zoom, y + 75*zoom, fill="brown", outline="black", tags=("player", "fl1"))
    f2_1 = canva.create_rectangle(x + 30*zoom, y + 70*zoom, x + 35*zoom, y + 75*zoom, fill="brown", outline="black", tags=("player", "fr1"))
    f2_2 = canva.create_rectangle(x + 35*zoom, y + 70*zoom, x + 40*zoom, y + 75*zoom, fill="brown", outline="black", tags=("player", "fr2"))

    ####################
    ####### SYMB #######
    ####################
    col1 = canva.create_rectangle(x + 20*zoom, y + 35*zoom, x + 30*zoom, y + 40*zoom, fill="#9F47DE", tags="player")
    col2 = canva.create_rectangle(x + 15*zoom, y + 40*zoom, x + 25*zoom, y + 45*zoom, fill="#77B5FE", tags="player")
    col3 = canva.create_rectangle(x + 25*zoom, y + 40*zoom, x + 35*zoom, y + 45*zoom, fill="#FFA500", tags="player")
    col4 = canva.create_rectangle(x + 15*zoom, y + 45*zoom, x + 25*zoom, y + 50*zoom, fill="yellow", tags="player")
    col5 = canva.create_rectangle(x + 25*zoom, y + 45*zoom, x + 35*zoom, y + 50*zoom, fill="#6DD100", tags="player")
    col6 = canva.create_rectangle(x + 20*zoom, y + 50*zoom, x + 30*zoom, y + 55*zoom, fill="red", tags="player")

    ######################
    ####### HITBOX #######
    ######################
    hitbox = canva.create_rectangle(x, y + 5*zoom, x + 50*zoom, y + 75*zoom, outline="yellow", tags="player")
