import winshell

def empty_recycle_bin():

    winshell.recycle_bin().empty(
        confirm=False,
        show_progress=False,
        sound=True
    )

    return "Recycle Bin emptied, Boss."