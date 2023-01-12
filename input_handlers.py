from typing import Optional

import tcod.event

from actions import Action, EscapeAction, MovementAction

class EventHandler(tcod.event.EventDispatch[Action]):
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None
        key = event.sym

        match key:
            case tcod.event.K_UP:
                action = MovementAction(0, -1)
            case tcod.event.K_DOWN:
                action = MovementAction(0, 1)
            case tcod.event.K_LEFT:
                action = MovementAction(-1, 0)
            case tcod.event.K_RIGHT:
                action = MovementAction(1, 0)
            case tcod.event.K_ESCAPE:
                action = EscapeAction()
            case _:
                pass
        return action