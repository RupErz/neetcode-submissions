class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = [] # Result list
        # Current words in a line
        curLine = []
        # Current length at a line
        curLength = 0
        # Index to move 
        idx = 0
        while idx < len(words):
            # Check if we can add this word to the line
            # curLength + newWord + spaces req with new words
            if curLength + len(words[idx]) + len(curLine) > maxWidth:

                # Time to add this line to result since we are full!

                # The minimal space required for n - 1 space slot
                spaces = (maxWidth - curLength) // max(1, (len(curLine) - 1))

                # The greedy space in case it is UNEVEN
                greedySpaces = (maxWidth - curLength) % max(1, (len(curLine) - 1))

                # Now we separate this greedyS from Left to Right alter
                for j in range(max(1, len(curLine) - 1)):
                    curLine[j] += (" " * spaces)
                    if greedySpaces > 0:
                        curLine[j] += " "
                        greedySpaces -= 1
                
                # Adding new line into the list 
                result.append("".join(curLine))

                # Reset the line !
                curLine = []
                curLength = 0
            
            curLine.append(words[idx])
            curLength += len(words[idx])
            idx += 1
        
        # Either finish perfectly by last word or having trailing spcs
        last_line = " ".join(curLine) # Only spaces between words
        trailing = maxWidth - len(last_line)
        last_line += " " * trailing

        result.append(last_line)
        return result

            

