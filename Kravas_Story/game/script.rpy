# This defines the character. 
# 'k' is the nickname we use in code. 
# 'Kravas' is the name the player sees.
define k = Character("Kravas", color="#5c8aff") 
define n = Character(None, kind=nvl) # For 'Narrator' text
define v = Character("Vesperine", color="#5c8aff") 
define a = Character("Aquaman", color="#5c8aff")

label start:
    # ... the rest of your story ...
    # This shows a background. 'bg room' is a placeholder in Ren'Py.
    scene kravas_forest2 

    # 'scene' clears the old screen and adds a background
    # scene bg KravasForest2 

    show kravas_head  # This places the character on top of the background
    k "Here I am in the forest!"
    show kravas_frown
    k "Fuck this"
    show kravas_eyesnarrow
    k "this is a load of Ballox"

    # 'show' puts a character on top of the background
    # "show kravas_happy 
    show kravas_feyeroll
    k "Look! I finally have a face and a place to stay."
    hide kravas_feyeroll
    
    scene kravas_forest2 
    show vesp_head1 with dissolve
    v "The screen is dark, but I can hear the hum of a computer."
    hide vesp_head1 with dissolve
    
    show aquaman
    a "Hi there, but what the fuck an I doing here?"

    a "Finally... the folder name is fixed. I can breathe again."
    hide aquaman with dissolve
    show kravas_what
    k "Now, let's see if this fucking GitHub thing actually works."

    k "what the fuck am I to do now?"

    k "another fucking test, what the fuck is this fucking shit?"
    scene kravas_basement
    show kravas_what
    menu:
        "Fuck this":
            jump commit_choice
        "Keep writing?":
            jump writing_choice

label commit_choice:
    k "Smart move. Safety first!"
    

label writing_choice:
    k "I like your style. Let's build a masterpiece."
    

label end_of_story:
    k "The journey ends here."
    k "The story is over."
    
    python:
        if renpy.emscripten:
            import emscripten
            emscripten.run_script("window.parent.postMessage('closeStory', '*')")
        else:
            renpy.log("Not on web: Skipping exit message.")
            
    return