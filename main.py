from controllers import menu_controller
from views import menu_view

"""main loop"""

active = True
while active:
    main_loop = menu_controller.MainLoop(menu_view=menu_view.MenuView)
    # menu_controller.MainLoop.run(main_loop)
    main_loop.run()
    