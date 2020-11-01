play = True
while play:
    x = float (input("\nWhat is your wrist size?\n\n"))
    chest = x*6.5
    hips = chest*0.85
    waist = chest*0.70
    thigh = chest*0.53
    neck = chest*0.37
    upper_arm = chest*0.36
    calves = chest*0.34
    forearms = chest*0.29
    print ("\nChest: " + str(chest) + "")
    print ("\nHips: " + str(hips) + "")
    print ("\nWaist: " + str(waist) + "")
    print ("\nThigh: " + str(thigh) + "")
    print ("\nNeck: " + str(neck) + "")
    print ("\nUpper Arms: " + str(upper_arm) + "")
    print ("\nCalves: " + str(calves) + "")
    print ("\nForearms: " + str(forearms) + "")
    z = str (input("\nDo you want to exit? (yes/no)\n\n"))
    if z == "no": play = True
    if z == "yes": play = False