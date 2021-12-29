import bge

mouse = list(bgelogic.mouse.position)

margin = .05

mouse[0] = min(max(mouse[0], 0 + margin), 1 - margin)
mouse[1] = min(max(mouse[1], 0 + margin), 1 - margin)

bge.logic.mouse.position = tuple(mouse)