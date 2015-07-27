class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        width = min(G,C)-max(E,A)
        width = 0 if width<0 else width
        height = min(D,H)-max(B,F)
        height = 0 if height<0 else height
        overlap = height*width
        
        return (D-B)*(C-A)+(G-E)*(H-F)-overlap