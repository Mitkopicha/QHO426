def crossed_bridge(steps):
    # Display each step
    for step in range(steps):
        print("Crossed step.")

    # Display message
    if (steps > 5):
        print("The bridge is collapsing!")
    else:
        print("We must keep going!")

crossed_bridge(3)
crossed_bridge(6)