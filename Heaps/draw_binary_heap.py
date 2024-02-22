# Write and showcase an algorithm for drawing a heap as a binary tree; using graphics interface or simply a 2D grid.

import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants for screen dimensions and colors
width = 800
height = 500
pink = (255, 193, 203)
darker_pink = (255,20,147)
white = (255, 255, 255)

# Function to draw the heap as a binary tree
def draw_heap_tree(screen, heap, level, x, y, spacing, parent_x=None, parent_y=None): # x and y are the position of the current node
    if level < len(heap):
        pygame.draw.circle(screen, white, (x, y), 35)  # Draw circle for the node
        font = pygame.font.Font(None, 45)
        text = font.render(str(heap[level]), True, pink)
        screen.blit(text, (x - 10, y - 10)) # displays value of the node on circle

        # Draw a line to the parent
        if parent_x is not None and parent_y is not None: # if there is a parent node, draw a line to connect the nodes
            pygame.draw.line(screen, darker_pink, (x, y - 35), (parent_x, parent_y + 35), 2)

        # Draw left child
        draw_heap_tree(screen, heap, 2 * level + 1, x - spacing, y + 100, spacing / 2, x, y)

        # Draw right child
        draw_heap_tree(screen, heap, 2 * level + 2, x + spacing, y + 100, spacing / 2, x, y)

# Example usage
heap_example = [6, 3, 92, 1, 3, 13, 23, 12, 12, 3, 12]

# Create Pygame screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Heap as Binary Tree")

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(pink)

    # Draw the heap as a binary tree
    draw_heap_tree(screen, heap_example, 0, width // 2, 50, 200)

    pygame.display.flip()

  
