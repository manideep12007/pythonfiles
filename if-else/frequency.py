'''Exercise: The letter a is said to be the most frequent letter in the English language.
Count and print how many times this letter appears in the poem below:'''

poem = '''
John Knox was a man of wondrous might,
And his words ran high and shrill,
For bold and stout was his spirit bright,
And strong was his stalwart will.

Kings sought in vain his mind to chain,
And that giant brain to control,
But naught on plain or stormy main
Could daunt that mighty soul.

John would sit and sigh till morning cold
Its shining lamps put out,
For thoughts untold on his mind lay hold,
And brought but pain and doubt.

But light at last on his soul was cast,
Away sank pain and sorrow,
His soul is gay, in a fair to-day,
And looks for a bright to-morrow.
'''

counter = 0
for letter in poem:
    if letter == 'a':
        counter = counter + 1

print(f'The letter a appears {counter} times in the poem.')
