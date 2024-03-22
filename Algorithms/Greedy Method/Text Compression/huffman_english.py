from heapq import heappush, heappop, heapify
from collections import defaultdict

# publically available frequency data for english letters
frequency = {
    'E': 12.02, 'T': 9.10, 'A': 8.12, 'O': 7.68, 'I': 7.31,
    'N': 6.95, 'S': 6.28, 'R': 6.02, 'H': 5.92, 'D': 4.32,
    'L': 3.98, 'U': 2.88, 'C': 2.71, 'M': 2.61, 'F': 2.30,
    'Y': 2.11, 'W': 2.09, 'G': 2.03, 'P': 1.82, 'B': 1.49,
    'V': 1.11, 'K': 0.69, 'X': 0.17, 'Q': 0.11, 'J': 0.10,
    'Z': 0.07
}

# Build tree
def build_huffman_tree(frequency):
    # Create a min-heap with each unique letter as a node along with its frequency
    min_heap = [[weight, [letter, ""]] for letter, weight in frequency.items()]
    heapify(min_heap)
    
    # Iterate through min-heap while theres more than one node
    while len(min_heap) > 1:
        
        # Remove nodes with lowest frequency
        left= heappop(min_heap)
        right= heappop(min_heap)
        
        # Encode letters
        for pair in left[1:]:
            pair[1] = '0' + pair[1]
        for pair in right[1:]:
            pair[1] = '1' + pair[1]
        
        # Add nodes back into minheap with combined encoding
        heappush(min_heap, [left[0] + right[0]] + left[1:] + right[1:])
    
    return sorted(heappop(min_heap)[1:], key=lambda p: (len(p[-1]), p))

sample_text = """Saknarth glanced over at the chronometer. It would be a half hour before the Morning Star rose. There was work to be done; he must prepare the day's horoscope. He laughed to himself. What fools priests and rulers must be to believe that the stars foretold the future. What an upset if they learned how it all originated in the minds of astrologers—no more the guesswork based upon a knowledge of the past. Well, so far, thought Saknarth, my forecasts have been more or less true.

Seating himself at a little desk in the shaded glow of an oil lamp, he proceeded to write his prophecies, taking care to befog them with astrological formulae and mystic bosh.

A half hour passed. Already a dim light glowed deep in the eastern horizon. Now from low in the sky a blue star gleamed, a steady glowing mote of light heralding the dawn. The Morning Star.

Saknarth pushed back his stool from the desk and stood up. He glanced through the open panel at the planet. Then over to the largest telescope in the observatory, a twenty inch reflector. He applied his single round eye to the eyepiece and gazed at great Kurnal, largest of the inner planets.

A crescent of brilliant light, the major part of it dark. It was nearing its closest, Saknarth thought. The sun was behind it and the night side was presented to Mars. The thin crescent glowed brightly. He could see dimly dark shading of landmasses in that area, but the rest was dark, unlit.

Saknarth reflected. Here it was that Kwarit had seen his lights, in the dark of the Earth. But then he was using a bigger instrument; he was using the great fifty inch reflector, largest ever made. That had been removed. The priests had said that it was accursed of the Devil and they had taken it and placed it in the Hall of Evil Things. None were permitted to look through it. Saknarth swore softly to himself. Oh for a glimpse through it, for a single glance—

The day was nearly over. Saknarth had delivered his horoscope to the Emperor and had served his moments at the court; now he was wending his way homeward through the narrow streets of Lucas Phoenicus. He saw before him a great building, the Imperial Museum. Suddenly a thought struck him; he would like to see Kwarit's telescope.

Accordingly he entered the vast institute. Through the long passages he went, past the exhibits of stuffed beasts and catalogued plants, and the many rooms of ancient empires and lost peoples. Through all these he went into the wing where lay the Hall of Evil Things. This was well guarded he thought. Two helmeted and cuirassed soldiers stood before the entrance. Their single eyes gleamed suspiciously at all passers by, their stumpy horns capped by dangerous looking steel spikes, their hands resting upon huge maces at their sides. They halted Saknarth as he sought to enter, but he showed them his credentials as a member of the Imperial Court and was permitted to pass. Down the hall he strode, past cases of forbidden books, evil robes, devil haunted, and mummeries of all kinds to the very end where, behind an iron railing, stood the telescope."""

sample_frequency = defaultdict(int)
for char in sample_text.upper():  # Convert to uppercase to match the frequency table
    if char in frequency or char == ' ':  # Include space in the count
        sample_frequency[char] += 1

# Re-build the Huffman tree with the actual sample frequency data
huffman_tree_sample = build_huffman_tree(sample_frequency)

# Generating Huffman codes from the new tree
huffman_codes_sample = {item[0]: item[1] for item in huffman_tree_sample}

# Calculating the total bits required for the sample text using Huffman coding
total_bits_huffman_sample = sum(sample_frequency[letter] * len(huffman_codes_sample[letter]) for letter in sample_frequency)

# Total characters in the sample text
total_characters_sample = sum(sample_frequency.values())

# Total bits required using 8-bit ASCII coding for the sample
total_bits_ascii_sample = total_characters_sample * 8

print(total_bits_huffman_sample, total_bits_ascii_sample, total_bits_huffman_sample / total_bits_ascii_sample)


