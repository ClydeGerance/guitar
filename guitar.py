from guitarstring import GuitarString
from stdaudio import play_sample
import stdkeys

if __name__ == '__main__':
    # Initialize window for keyboard input
    stdkeys.create_window()

    # Define the keyboard layout and corresponding frequencies
    keyboard = "q2we4r5ty7u8i9op-[=]"
    base_frequency = 220  # Frequency for the 'q' key
    guitar_strings = [GuitarString(base_frequency * (1.059463 ** (i))) for i in range(20)]

    #Maintain a set of plucked strings
    plucked_strings = set()

    n_iters = 0
    while True:
        # it turns out that the bottleneck is in polling for key events
        # for every iteration, so we'll do it less often, say every 
        # 1000 or so iterations
        if n_iters == 1000:
            stdkeys.poll()
            n_iters = 0
        n_iters += 1

        # check if the user has typed a key; if so, process it
        if stdkeys.has_next_key_typed():
            key = stdkeys.next_key_typed()
            if key in keyboard:
                index = keyboard.index(key)
                if 0 <= index < len(guitar_strings):
                    guitar_string = guitar_strings[index]
                    guitar_string.pluck()
                    plucked_strings.add(guitar_string)  # Add to plucked strings set

        # Sample only the plucked strings
        sample = sum(string.sample() for string in plucked_strings)

        # play the sample on standard audio
        play_sample(sample)

        # Advance the simulation of each plucked guitar string by one step
        for string in plucked_strings:  # No need to copy and remove
            string.tick()
