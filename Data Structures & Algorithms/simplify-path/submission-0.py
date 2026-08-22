class Solution:
    def simplifyPath(self, path: str) -> str:
        # Loop through the main path, "/" is the delimiter
        # 1. Multiple slashes consecutively -> treat as 1
        # 2. >= 3 dots = a valid file name
        # 3. 1 dots = nothing
        # 4. 2 dots = previous parent directory (retreat 1 folder)
        #     e.g: nghiavu/../happy => /happy
        

        # Stored as a deque [ ]
        # Add to right.
        # Pop to Right if seeing a 2 dots (..)
        # Join them altogether by the end 

        # Usin SPLIT:
        # e.g: path = "/neetcode/practice//...///../courses"
        # ["", "neetcode", "practice", "", "...", "", "", "..", "courses"]
        
        content = path.split("/") 
        order = deque()

        # Start adding into 
        for w in content:
            if w == "." or w == "":
                continue
            
            if w != "..":
                order.append(w)
            else:
                if order:
                    order.pop()
        
        # Start joining them altogether
        return "/" + "/".join(order)
            


        